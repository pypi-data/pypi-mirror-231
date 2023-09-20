import inspect
import os
import sys
import warnings
from datetime import timedelta
from statistics import mean

import numpy as np
import pandas as pd
from ConfigSpace import Configuration, ConfigurationSpace
from matplotlib import pyplot as plt
from sklearn.exceptions import NotFittedError
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    make_scorer,
    precision_score,
    recall_score,
)
from sklearn.model_selection import cross_validate
from tqdm.auto import tqdm

from sam_ml.config import (
    get_avg,
    get_n_jobs,
    get_pos_label,
    get_scoring,
    get_secondary_scoring,
    get_strength,
    setup_logger,
)

from .main_model import Model
from .scorer import l_scoring, s_scoring

SMAC_INSTALLED: bool
try:
    from smac import HyperparameterOptimizationFacade, Scenario
    SMAC_INSTALLED = True
except:
    SMAC_INSTALLED = False

logger = setup_logger(__name__)

if not sys.warnoptions:
    warnings.simplefilter("ignore")
    os.environ["PYTHONWARNINGS"] = "ignore" # Also affects subprocesses


class Classifier(Model):
    """ Classifier parent class """

    def __init__(self, model_object = None, model_name: str = "classifier", model_type: str = "Classifier", grid: ConfigurationSpace = ConfigurationSpace()):
        """
        @params:
            model_object: model with 'fit', 'predict', 'set_params', and 'get_params' method (see sklearn API)
            model_name: name of the model
            model_type: kind of estimator (e.g. 'RFC' for RandomForestClassifier)
            grid: hyperparameter grid for the model
        """
        super().__init__(model_object, model_name, model_type)
        self._grid = grid
        self.cv_scores: dict[str, float] = {}
        self.rCVsearch_results: pd.DataFrame|None = None

    def __repr__(self) -> str:
        params: str = ""
        param_dict = self._changed_parameters()
        for key in param_dict:
            if type(param_dict[key]) == str:
                params+= key+"='"+str(param_dict[key])+"', "
            else:
                params+= key+"="+str(param_dict[key])+", "
        params += f"model_name='{self.model_name}'"

        return f"{self.model_type}({params})"
    
    def _changed_parameters(self):
        params = self.get_params(deep=False)
        init_params = inspect.signature(self.__init__).parameters
        init_params = {name: param.default for name, param in init_params.items()}

        init_params_estimator = inspect.signature(self.model.__init__).parameters
        init_params_estimator = {name: param.default for name, param in init_params_estimator.items()}

        def has_changed(k, v):
            if k not in init_params:  # happens if k is part of a **kwargs
                if k not in init_params_estimator: # happens if k is part of a **kwargs
                    return True
                else:
                    if v != init_params_estimator[k]:
                        return True
                    else:
                        return False

            if init_params[k] == inspect._empty:  # k has no default value
                return True
            elif init_params[k] != v:
                return True
            
            return False

        return {k: v for k, v in params.items() if has_changed(k, v)}

    @property
    def grid(self):
        """
        @return:
            hyperparameter tuning grid of the model
        """
        return self._grid
    
    def get_random_config(self):
        """
        @return;
            set of random parameter from grid
        """
        return dict(self.grid.sample_configuration(1))
    
    def get_random_configs(self, n_trails: int) -> list:
        """
        @return;
            n_trails elements in list with sets of random parameterd from grid

        NOTE: filter out duplicates -> could be less than n_trails
        """
        if n_trails<1:
            raise ValueError(f"n_trails has to be greater 0, but {n_trails}<1")
        
        configs = [self._grid.get_default_configuration()]
        if n_trails == 2:
            configs += [self._grid.sample_configuration(n_trails-1)]
        else:
            configs += self._grid.sample_configuration(n_trails-1)
        # remove duplicates
        configs = list(dict.fromkeys(configs))
        return configs

    def replace_grid(self, new_grid: ConfigurationSpace):
        """
        function to replace self.grid 

        e.g.:
            ConfigurationSpace(
                seed=42,
                space={
                    "solver": Categorical("solver", ["lsqr", "eigen", "svd"]),
                    "shrinkage": Float("shrinkage", (0, 1)),
                })
        """
        self._grid = new_grid

    def train(
        self,
        x_train: pd.DataFrame,
        y_train: pd.Series, 
        scoring: str = get_scoring(),
        avg: str = get_avg(),
        pos_label: int | str = get_pos_label(),
        secondary_scoring: str = get_secondary_scoring(),
        strength: int = get_strength(),
        console_out: bool = True
    ) -> tuple[float, str]:
        """
        @return:
            tuple of train score and train time
        """
        return super().train(x_train, y_train, console_out, scoring=scoring, avg=avg, pos_label=pos_label, secondary_scoring=secondary_scoring, strength=strength)
    
    def train_warm_start(
        self,
        x_train: pd.DataFrame,
        y_train: pd.Series, 
        scoring: str = get_scoring(),
        avg: str = get_avg(),
        pos_label: int | str = get_pos_label(),
        secondary_scoring: str = get_secondary_scoring(),
        strength: int = get_strength(),
        console_out: bool = True
    ) -> tuple[float, str]:
        """
        @return:
            tuple of train score and train time
        """
        return super().train_warm_start(x_train, y_train, console_out, scoring=scoring, avg=avg, pos_label=pos_label, secondary_scoring=secondary_scoring, strength=strength)

    def evaluate(
        self,
        x_test: pd.DataFrame,
        y_test: pd.Series,
        avg: str = get_avg(),
        pos_label: int | str = get_pos_label(),
        console_out: bool = True,
        secondary_scoring: str = get_secondary_scoring(),
        strength: int = get_strength(),
    ) -> dict[str, float]:
        """
        @param:
            x_test, y_test: Data to evaluate model

            avg: average to use for precision and recall score (e.g. "micro", None, "weighted", "binary")
            pos_label: if avg="binary", pos_label says which class to score. pos_label is used by s_score/l_score

            console_out: shall the result be printed into the console

            secondary_scoring: weights the scoring (only for 's_score'/'l_score')
            strength: higher strength means a higher weight for the preferred secondary_scoring/pos_label (only for 's_score'/'l_score')

        @return: dictionary with keys with scores: 'accuracy', 'precision', 'recall', 's_score', 'l_score'
        """
        pred = self.predict(x_test)

        # Calculate Accuracy, Precision and Recall Metrics
        accuracy = accuracy_score(y_test, pred)
        precision = precision_score(y_test, pred, average=avg, pos_label=pos_label)
        recall = recall_score(y_test, pred, average=avg, pos_label=pos_label)
        s_score = s_scoring(y_test, pred, strength=strength, scoring=secondary_scoring, pos_label=pos_label)
        l_score = l_scoring(y_test, pred, strength=strength, scoring=secondary_scoring, pos_label=pos_label)

        if console_out:
            print("accuracy: ", accuracy)
            print("precision: ", precision)
            print("recall: ", recall)
            print("s_score: ", s_score)
            print("l_score: ", l_score)
            print()
            print("classification report: ")
            print(classification_report(y_test, pred))

        scores = {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "s_score": s_score,
            "l_score": l_score,
        }

        return scores
    
    def evaluate_score(
        self,
        x_test: pd.DataFrame,
        y_test: pd.Series,
        scoring: str = get_scoring(),
        avg: str = get_avg(),
        pos_label: int | str = get_pos_label(),
        secondary_scoring: str = get_secondary_scoring(),
        strength: int = get_strength(),
    ) -> float:
        """
        @param:
            x_test, y_test: Data to evaluate model
            scoring: metrics to evaluate the models ("accuracy", "precision", "recall", "s_score", "l_score")

            avg: average to use for precision and recall score (e.g. "micro", None, "weighted", "binary")
            pos_label: if avg="binary", pos_label says which class to score. pos_label is used by s_score/l_score
            secondary_scoring: weights the scoring (only for 's_score'/'l_score')
            strength: higher strength means a higher weight for the preferred secondary_scoring/pos_label (only for 's_score'/'l_score')

        @return: score as float
        """
        pred = self.predict(x_test)

        # Calculate score
        if scoring == "accuracy":
            score = accuracy_score(y_test, pred)
        elif scoring == "precision":
            score = precision_score(y_test, pred, average=avg, pos_label=pos_label)
        elif scoring == "recall":
            score = recall_score(y_test, pred, average=avg, pos_label=pos_label)
        elif scoring == "s_score":
            score = s_scoring(y_test, pred, strength=strength, scoring=secondary_scoring, pos_label=pos_label)
        elif scoring == "l_score":
            score = l_scoring(y_test, pred, strength=strength, scoring=secondary_scoring, pos_label=pos_label)
        else:
            raise ValueError(f"scoring='{scoring}' is not supported -> only  'accuracy', 'precision', 'recall', 's_score', or 'l_score' ")

        return score

    def cross_validation(
        self,
        X: pd.DataFrame,
        y: pd.Series,
        cv_num: int = 10,
        avg: str = get_avg(),
        pos_label: int | str = get_pos_label(),
        console_out: bool = True,
        secondary_scoring: str = get_secondary_scoring(),
        strength: int = get_strength(),
    ) -> dict[str, float]:
        """
        @param:
            X, y: data to cross validate on
            cv_num: number of different splits

            avg: average to use for precision and recall score (e.g. "micro", "weighted", "binary")
            pos_label: if avg="binary", pos_label says which class to score. pos_label is used by s_score/l_score

            console_out: shall the result be printed into the console

            secondary_scoring: weights the scoring (only for 's_score'/'l_score')
            strength: higher strength means a higher weight for the preferred secondary_scoring/pos_label (only for 's_score'/'l_score')

        @return:
            dictionary with "accuracy", "precision", "recall", "s_score", "l_score", train_score", "train_time"
        """
        logger.debug(f"cross validation {self.model_name} - started")

        precision_scorer = make_scorer(precision_score, average=avg, pos_label=pos_label)
        recall_scorer = make_scorer(recall_score, average=avg, pos_label=pos_label)
        s_scorer = make_scorer(s_scoring, strength=strength, scoring=secondary_scoring, pos_label=pos_label)
        l_scorer = make_scorer(l_scoring, strength=strength, scoring=secondary_scoring, pos_label=pos_label)

        if avg == "binary":
            scorer = {
                f"precision ({avg}, label={pos_label})": precision_scorer,
                f"recall ({avg}, label={pos_label})": recall_scorer,
                "accuracy": "accuracy",
                "s_score": s_scorer,
                "l_score": l_scorer,
            }
        else:
            scorer = {
                f"precision ({avg})": precision_scorer,
                f"recall ({avg})": recall_scorer,
                "accuracy": "accuracy",
                "s_score": s_scorer,
                "l_score": l_scorer,
            }

        cv_scores = cross_validate(
            self,
            X,
            y,
            scoring=scorer,
            cv=cv_num,
            return_train_score=True,
            n_jobs=get_n_jobs(),
        )

        pd_scores = pd.DataFrame(cv_scores).transpose()
        pd_scores["average"] = pd_scores.mean(numeric_only=True, axis=1)

        score = pd_scores["average"]
        self.cv_scores = {
            "accuracy": score[list(score.keys())[6]],
            "precision": score[list(score.keys())[2]],
            "recall": score[list(score.keys())[4]],
            "s_score": score[list(score.keys())[8]],
            "l_score": score[list(score.keys())[10]],
            "train_score": score[list(score.keys())[7]],
            "train_time": str(timedelta(seconds = round(score[list(score.keys())[0]]))),
        }

        logger.debug(f"cross validation {self.model_name} - finished")

        if console_out:
            print()
            print(pd_scores)

        return self.cv_scores

    def cross_validation_small_data(
        self,
        X: pd.DataFrame,
        y: pd.Series,
        avg: str = get_avg(),
        pos_label: int | str = get_pos_label(),
        leave_loadbar: bool = True,
        console_out: bool = True,
        secondary_scoring: str = get_secondary_scoring(),
        strength: int = get_strength(),
    ) -> dict[str, float]:
        """
        Cross validation for small datasets (recommended for datasets with less than 150 datapoints)

        @param:
            X, y: data to cross validate on

            avg: average to use for precision and recall score (e.g. "micro", "weighted", "binary")
            pos_label: if avg="binary", pos_label says which class to score. pos_label is used by s_score/l_score

            leave_loadbar: shall the loading bar of the training be visible after training (True - load bar will still be visible)
            console_out: shall the result be printed into the console

            secondary_scoring: weights the scoring (only for 's_score'/'l_score')
            strength: higher strength means a higher weight for the preferred secondary_scoring/pos_label (only for 's_score'/'l_score')

        @return:
            dictionary with "accuracy", "precision", "recall", "s_score", "l_score", train_score", "train_time"
        """
        logger.debug(f"cross validation {self.model_name} - started")

        predictions = []
        true_values = []
        t_scores = []
        t_times = []
        
        for idx in tqdm(X.index, desc=self.model_name, leave=leave_loadbar):
            x_train = X.drop(idx)
            y_train = y.drop(idx)
            x_test = X.loc[[idx]]
            y_test = y.loc[idx]

            train_score, train_time = self.train(x_train, y_train, console_out=False)
            prediction = self.predict(x_test)

            predictions.append(prediction)
            true_values.append(y_test)
            t_scores.append(train_score)
            t_times.append(train_time)

        accuracy = accuracy_score(true_values, predictions)
        precision = precision_score(true_values, predictions, average=avg, pos_label=pos_label)
        recall = recall_score(true_values, predictions, average=avg, pos_label=pos_label)
        s_score = s_scoring(true_values, predictions, strength=strength, scoring=secondary_scoring, pos_label=pos_label)
        l_score = l_scoring(true_values, predictions, strength=strength, scoring=secondary_scoring, pos_label=pos_label)
        avg_train_score = mean(t_scores)
        avg_train_time = str(timedelta(seconds=round(sum(map(lambda f: int(f[0])*3600 + int(f[1])*60 + int(f[2]), map(lambda f: f.split(':'), t_times)))/len(t_times))))

        self.cv_scores = {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "s_score": s_score,
            "l_score": l_score,
            "train_score": avg_train_score,
            "train_time": avg_train_time,
        }

        logger.debug(f"cross validation {self.model_name} - finished")

        if console_out:
            print()
            print("classification report:")
            print(classification_report(true_values, predictions))

        return self.cv_scores

    def feature_importance(self) -> plt.show:
        """
        feature_importance() generates a matplotlib plot of the feature importance from self.model
        """
        if not self.feature_names:
            raise NotFittedError("You have to first train the classifier before getting the feature importance (with train-method)")

        if self.model_type == "MLPC":
            importances = [np.mean(i) for i in self.model.coefs_[0]]  # MLP Classifier
        elif self.model_type in ("DTC", "RFC", "GBM", "CBC", "ABC", "ETC", "XGBC"):
            importances = self.model.feature_importances_
        elif self.model_type in ("KNC", "GNB", "BNB", "GPC", "QDA", "BC"):
            logger.warning(f"{self.model_type} does not have a feature importance")
            return
        else:
            importances = self.model.coef_[0]  # "normal"

        feature_importances = pd.Series(importances, index=self.feature_names)

        fig, ax = plt.subplots()
        if self.model_type in ("RFC", "GBM", "ETC"):
            if self.model_type in ("RFC", "ETC"):
                std = np.std(
                    [tree.feature_importances_ for tree in self.model.estimators_], axis=0,
                )
            elif self.model_type == "GBM":
                std = np.std(
                    [tree[0].feature_importances_ for tree in self.model.estimators_], axis=0,
                )
            feature_importances.plot.bar(yerr=std, ax=ax)
        else:
            feature_importances.plot.bar(ax=ax)
        ax.set_title("Feature importances of " + str(self.model_name))
        ax.set_ylabel("use of coefficients as importance scores")
        fig.tight_layout()
        plt.show()
    
    def smac_search(
        self,
        x_train: pd.DataFrame, 
        y_train: pd.Series,
        n_trails: int = 50,
        cv_num: int = 5,
        scoring: str = get_scoring(),
        avg: str = get_avg(),
        pos_label: int | str = get_pos_label(),
        secondary_scoring: str = get_secondary_scoring(),
        strength: int = get_strength(),
        small_data_eval: bool = False,
        walltime_limit: float = 600,
        log_level: int = 20,
    ) -> Configuration:
        """
        @params:
            x_train: DataFrame with train features
            y_train: Series with labels

            n_trails: max number of parameter sets to test
            cv_num: number of different splits per crossvalidation (only used when small_data_eval=False)

            scoring: metrics to evaluate the models ("accuracy", "precision", "recall", "s_score", "l_score")
            avg: average to use for precision and recall score (e.g. "micro", "weighted", "binary")
            pos_label: if avg="binary", pos_label says which class to score. Else pos_label is ignored (except scoring='s_score'/'l_score')
            secondary_scoring: weights the scoring (only for scoring='s_score'/'l_score')
            strength: higher strength means a higher weight for the preferred secondary_scoring/pos_label (only for scoring='s_score'/'l_score')

            small_data_eval: if True: trains model on all datapoints except one and does this for all datapoints (recommended for datasets with less than 150 datapoints)
            
            walltime_limit: the maximum time in seconds that SMAC is allowed to run

            log_level: 10 - DEBUG, 20 - INFO, 30 - WARNING, 40 - ERROR, 50 - CRITICAL (SMAC3 library log levels)

        @return: ConfigSpace.Configuration with best hyperparameters (can be used like dict)
        """
        if not SMAC_INSTALLED:
            raise ImportError("SMAC3 library is not installed -> follow instructions in Repo to install SMAC3 (https://github.com/Priapos1004/SAM_ML)")

        logger.debug("starting smac_search")
        # NormalInteger in grid is not supported (using workaround for now) (04/07/2023)
        if self.model_type in ("RFC", "ETC", "GBM", "XGBC"):
            grid = self.smac_grid
        else:
            grid = self.grid

        scenario = Scenario(
            grid,
            n_trials=n_trails,
            deterministic=True,
            walltime_limit=walltime_limit,
        )

        initial_design = HyperparameterOptimizationFacade.get_initial_design(scenario, n_configs=5)
        logger.debug(f"initial_design: {initial_design.select_configurations()}")

        # define target function
        def grid_train(config: Configuration, seed: int) -> float:
            logger.debug(f"config: {config}")
            model = self.get_deepcopy()
            model.set_params(**config)
            if small_data_eval:
                score = model.cross_validation_small_data(x_train, y_train, console_out=False, leave_loadbar=False, avg=avg, pos_label=pos_label, secondary_scoring=secondary_scoring, strength=strength)
            else:
                score = model.cross_validation(x_train, y_train, console_out=False, cv_num=cv_num, avg=avg, pos_label=pos_label, secondary_scoring=secondary_scoring, strength=strength)
            return 1 - score[scoring]  # SMAC always minimizes (the smaller the better)

        # use SMAC to find the best hyperparameters
        smac = HyperparameterOptimizationFacade(
            scenario,
            grid_train,
            initial_design=initial_design,
            overwrite=True,  # If the run exists, we overwrite it; alternatively, we can continue from last state
            logging_level=log_level,
        )

        incumbent = smac.optimize()
        logger.debug("finished smac_search")
        return incumbent

    def randomCVsearch(
        self,
        x_train: pd.DataFrame,
        y_train: pd.Series,
        n_trails: int = 10,
        cv_num: int = 5,
        scoring: str = get_scoring(),
        avg: str = get_avg(),
        pos_label: int | str = get_pos_label(),
        secondary_scoring: str = get_secondary_scoring(),
        strength: int = get_strength(),
        small_data_eval: bool = False,
        leave_loadbar: bool = True,
    ) -> tuple[dict, float]:
        """
        @params:
            x_train: DataFrame with train features
            y_train: Series with labels

            n_trails: number of parameter sets to test

            scoring: metrics to evaluate the models ("accuracy", "precision", "recall", "s_score", "l_score")
            avg: average to use for precision and recall score (e.g. "micro", "weighted", "binary")
            pos_label: if avg="binary", pos_label says which class to score. Else pos_label is ignored (except scoring='s_score'/'l_score')
            secondary_scoring: weights the scoring (only for scoring='s_score'/'l_score')
            strength: higher strength means a higher weight for the preferred secondary_scoring/pos_label (only for scoring='s_score'/'l_score')

            small_data_eval: if True: trains model on all datapoints except one and does this for all datapoints (recommended for datasets with less than 150 datapoints)

            cv_num: number of different splits per crossvalidation (only used when small_data_eval=False)

            leave_loadbar: shall the loading bar of the different parameter sets be visible after training (True - load bar will still be visible)

        @return: dictionary with best hyperparameters and float of best_score
        """
        logger.debug("starting randomCVsearch")
        results = []
        configs = self.get_random_configs(n_trails)
        at_least_one_run: bool = False
        try:
            for config in tqdm(configs, desc=f"randomCVsearch ({self.model_name})", leave=leave_loadbar):
                logger.debug(f"config: {config}")
                model = self.get_deepcopy()
                model.set_params(**config)
                if small_data_eval:
                    score = model.cross_validation_small_data(x_train, y_train, console_out=False, leave_loadbar=False, avg=avg, pos_label=pos_label, secondary_scoring=secondary_scoring, strength=strength)
                else:
                    score = model.cross_validation(x_train, y_train, cv_num=cv_num, console_out=False, avg=avg, pos_label=pos_label, secondary_scoring=secondary_scoring, strength=strength)
                config_dict = dict(config)
                config_dict[scoring] = score[scoring]
                results.append(config_dict)
                at_least_one_run = True
        except KeyboardInterrupt:
            logger.info("KeyboardInterrupt - output interim result")
            if not at_least_one_run:
                return {}, -1
            

        self.rCVsearch_results = pd.DataFrame(results, dtype=object).sort_values(by=scoring, ascending=False)

        # for-loop to keep dtypes of columns
        best_hyperparameters = {} 
        for col in self.rCVsearch_results.columns:
            value = self.rCVsearch_results[col].iloc[0]
            if str(value) != "nan":
                best_hyperparameters[col] = value

        best_score = best_hyperparameters[scoring]
        best_hyperparameters.pop(scoring)

        logger.debug("finished randomCVsearch")
        
        return best_hyperparameters, best_score
