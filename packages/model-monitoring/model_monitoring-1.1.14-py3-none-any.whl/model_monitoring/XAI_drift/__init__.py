import pandas as pd
import numpy as np
import warnings

from model_monitoring.utils import check_features_sets

standard_threshold = {"relative_red": 0.4, "relative_yellow": 0.2, "absolute_tol": 0.1}


class XAIDrift:
    """XAI Drift Class."""

    def __init__(self, xai_curr, xai_stor, feat_to_check=None, config_threshold=None):
        """XAI Drift Class.

        Args:
            xai_curr (dict): current xai dictionary.
            xai_stor (dict): historical xai dictionary.
            feat_to_check (list, optional): list of features to be checked. Deafualts to None.
            config_threshold (dict, optional): dictionary containing relative and absolute tolerances threshold settings. Defaults to None.
        """
        # Set configuration for relative and asbolute tolerance threshold for alerting
        if config_threshold is None:
            config_threshold = standard_threshold
        self.config_theshold = config_threshold

        # Check if the scores are assigned to the same set of features
        check_features_sets(
            features_1=list(xai_curr["feat_importance"].keys()), features_2=list(xai_stor["feat_importance"].keys())
        )

        if feat_to_check is not None:
            self.xai_curr = {
                "type": xai_curr["type"],
                "feat_importance": {x: xai_curr["feat_importance"][x] for x in feat_to_check},
            }
            self.xai_stor = {
                "type": xai_stor["type"],
                "feat_importance": {x: xai_stor["feat_importance"][x] for x in feat_to_check},
            }
        else:
            self.xai_curr = xai_curr
            self.xai_stor = xai_stor

        self.feat_to_check = feat_to_check

        # Check if the type of feature importance of historical and current xai model is the same
        if self.xai_curr["type"] != self.xai_stor["type"]:
            if (self.xai_curr["type"] == "coef") or (self.xai_stor["type"] == "coef"):
                raise ValueError(
                    f"'{self.xai_curr['type']}' type of feature importance in current xai model is not compatible with '{xai_stor['type']}' typ in historical xai model"
                )
            else:
                warnings.warn(
                    "the type of feature importance in current and historical xai model are not the same but they are compatible"
                )

        # Initialize the report
        xai_drift_report = (
            pd.DataFrame.from_dict(self.xai_curr["feat_importance"], "index", columns=["curr_score"])
            .reset_index()
            .rename(columns={"index": "feature"})
        )
        xai_stor_report = (
            pd.DataFrame.from_dict(self.xai_stor["feat_importance"], "index", columns=["stor_score"])
            .reset_index()
            .rename(columns={"index": "feature"})
        )
        # Save features not in common in both xai model dictionaries
        self.feat_only_cur = list(set(xai_drift_report.feature.unique()) - set(xai_stor_report.feature.unique()))
        self.feat_only_stor = list(set(xai_stor_report.feature.unique()) - set(xai_drift_report.feature.unique()))

        xai_drift_report = xai_drift_report.merge(xai_stor_report, how="outer", on="feature").fillna(0)

        self.xai_drift_report = xai_drift_report

    def get_drift(self):
        """Load on the report the feature importance drift and relative alert from current and historical XAI model."""
        self.relative_red = self.config_theshold["relative_red"]
        self.relative_yellow = self.config_theshold["relative_yellow"]
        self.absolute_tol = self.config_theshold["absolute_tol"]

        # Generation Drift
        for a in self.xai_drift_report.feature.values:
            stor_score = self.xai_drift_report.loc[self.xai_drift_report.feature == a, "stor_score"].values[0]
            curr_score = self.xai_drift_report.loc[self.xai_drift_report.feature == a, "curr_score"].values[0]
            self.xai_drift_report.loc[self.xai_drift_report.feature == a, "drift_perc"] = (
                (curr_score - stor_score) / stor_score * 100 if stor_score != 0 else 0
            )

        # Generation Alert
        for a in self.xai_drift_report.feature.values:
            stor_score = self.xai_drift_report.loc[self.xai_drift_report.feature == a, "stor_score"].values[0]
            curr_score = self.xai_drift_report.loc[self.xai_drift_report.feature == a, "curr_score"].values[0]
            if a in self.feat_only_cur:
                self.xai_drift_report.loc[
                    self.xai_drift_report.feature == a, "relative_warning"
                ] = "Feature not used in historical model"
            elif a in self.feat_only_stor:
                self.xai_drift_report.loc[
                    self.xai_drift_report.feature == a, "relative_warning"
                ] = "Feature not used in current model"
            else:
                if abs(curr_score - stor_score) >= self.absolute_tol:
                    drift_xai = self.xai_drift_report.loc[self.xai_drift_report.feature == a, "drift_perc"].values[0]
                    if abs(drift_xai) > self.relative_red * 100:
                        self.xai_drift_report.loc[self.xai_drift_report.feature == a, "relative_warning"] = "Red Alert"
                    else:
                        if (abs(drift_xai) < self.relative_red * 100) and (abs(drift_xai) > self.relative_yellow * 100):
                            self.xai_drift_report.loc[
                                self.xai_drift_report.feature == a, "relative_warning"
                            ] = "Yellow Alert"
                        else:
                            self.xai_drift_report.loc[self.xai_drift_report.feature == a, "relative_warning"] = np.nan
                else:
                    self.xai_drift_report.loc[self.xai_drift_report.feature == a, "relative_warning"] = np.nan

    def get_report(self):
        """Return the xai drift report.

        Returns:
            pd.DataFrame: report of the class.
        """
        return self.xai_drift_report.sort_values("stor_score", key=abs)

    def plot(self):
        """Plot the report on features importance drift."""
        self.xai_drift_report.sort_values("stor_score", key=abs).plot(
            x="feature", y=["curr_score", "stor_score"], kind="barh", title="Features Importance Drift"
        )
