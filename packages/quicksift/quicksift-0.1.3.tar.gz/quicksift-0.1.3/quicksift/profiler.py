from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from itertools import combinations
from typing import List, Optional

import numpy as np
import pandas as pd
import polars as pl


class Profiler:
    def __init__(
        self, dataset, groups: Optional[List[str]] = None, sequential: bool = False
    ):
        self.analysis_time_utc = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(dataset, pd.DataFrame):
            self.dataset = pl.DataFrame(dataset).lazy()
        elif isinstance(dataset, pl.DataFrame):
            self.dataset = dataset.lazy()
        else:
            raise NotImplementedError(
                f"dataframe of type={type(dataset)} not supported"
            )
        self.groups = groups
        self.grouped_datasets = []
        self.numeric_columns = [
            col
            for col, dtype in zip(self.dataset.columns, self.dataset.dtypes)
            if dtype in [pl.Int64, pl.Float64]
        ]
        self.numeric_pairs = combinations(self.numeric_columns, 2)
        self.categorical_columns = [
            col
            for col, dtype in zip(self.dataset.columns, self.dataset.dtypes)
            if dtype == pl.Utf8
        ]
        self.sequential = sequential

    def summarize_column(self, col):
        return (
            self.dataset.select(
                [
                    pl.col(col).is_null().sum().alias("observations missing"),
                    pl.col(col).count().alias("total observations"),
                    (pl.col(col).is_null().sum() / pl.col(col).count()).alias(
                        "proportion missing"
                    ),
                    (pl.col(col) > 0).sum().alias("total positive values"),
                    (pl.col(col) == 0).sum().alias("total zero values"),
                    (pl.col(col) < 0).sum().alias("total negative values"),
                    (pl.col(col) > 0).mean().alias("proportion positive values"),
                    (pl.col(col) == 0).mean().alias("proportion zero values"),
                    (pl.col(col) < 0).mean().alias("proportion negative values"),
                    pl.col(col).min().alias("minimum"),
                    pl.col(col).quantile(0.01).alias("quantile=0.01"),
                    pl.col(col).quantile(0.05).alias("quantile=0.05"),
                    pl.col(col).quantile(0.1).alias("quantile=0.1"),
                    pl.col(col).quantile(0.25).alias("quantile=0.25"),
                    pl.col(col).quantile(0.5).alias("median"),
                    pl.col(col).mean().alias("mean"),
                    pl.col(col).mode().alias("mode"),
                    pl.col(col).quantile(0.75).alias("quantile=0.75"),
                    pl.col(col).quantile(0.9).alias("quantile=0.90"),
                    pl.col(col).quantile(0.95).alias("quantile=0.95"),
                    pl.col(col).quantile(0.99).alias("quantile=0.99"),
                    (pl.col(col).quantile(0.75) - pl.col(col).quantile(0.25)).alias(
                        "interquartile range"
                    ),
                    pl.col(col).max().alias("maximum"),
                    pl.col(col).var().alias("variance"),
                    pl.col(col).std().alias("standard deviation"),
                    pl.col(col).kurtosis().alias("kurtosis"),
                    pl.col(col).skew().alias("skew"),
                ]
            )
            .collect()
            .to_dicts()[0]
        )

    def summarize_dataframe(self):
        return dict(
            zip(["number rows", "number columns"], self.dataset.collect().shape)
        )

    def correlate_columns(self, col1, col2):
        return self.dataset.select(pl.corr(col2, col1)).collect()[col2][0]

    def cross_correlate_columns(self, col1, col2):
        np_series1 = self.dataset.select(col1).collect().to_numpy()
        np_series2 = self.dataset.select(col2).collect().to_numpy()

        return np.correlate(np_series1, np_series2, mode="full")

    def profile(self):
        with ThreadPoolExecutor() as executor:
            df_summary = executor.submit(self.summarize_dataframe)
            column_summary = {}
            # correlation_summary = {key1: {key2: {} for key2 in profiler.numeric_columns} for key1 in profiler.numeric_columns}
            correlation_summary = {}

            for col_name in self.numeric_columns:
                column_summary[col_name] = executor.submit(
                    self.summarize_column, col_name
                )

            if self.sequential:
                cross_correlation_summary = {
                    key1: {key2: {} for key2 in profiler.numeric_columns}
                    for key1 in profiler.numeric_columns
                }

            for combo in combinations(self.numeric_columns, 2):
                key1, key2 = combo
                if key1 not in correlation_summary:
                    correlation_summary[key1] = {}
                correlation_summary[key1][key2] = executor.submit(
                    self.correlate_columns, key1, key2
                ).result()

                if self.sequential:
                    if key1 not in cross_correlation_summary:
                        cross_correlation_summary[key1] = {}
                    cross_correlation_summary[key1][key2] = executor.submit(
                        self.cross_correlate_columns, key1, key2
                    ).result()

        col_stats = {k: v.result() for k, v in column_summary.items()}
        for col, summary in correlation_summary.items():
            if col not in col_stats:
                col_stats[col] = {}
            col_stats[col]["correlations"] = summary

        return col_stats
