from typing import Callable, Any, Optional, Iterable

import pandas
from pyspark import SparkContext


class SparkParquetIO:
    def _load_parquet(self, path: str, additional_value_extractor: Callable[[str], dict[str, Any]]):
        additional_values = additional_value_extractor(path)
        df = pandas.read_parquet(path, partitioning=None)
        for c, v in additional_values.items():
            df[c] = v
        return df

    def _load_all_parquets(self,
                           paths: Iterable[str],
                           additional_value_extractor: Optional[Callable[[str], dict[str, Any]]] = None):
        result_df = pandas.concat([self._load_parquet(path, additional_value_extractor) for path in paths], axis=0)
        return self._convert_pandas_dataframe_to_spark_records(result_df)

    def spj_load_parquet(self, additional_value_extractor: Optional[Callable[[str], dict[str, Any]]] = None):
        def run(paths: Iterable[str]):
            return self._load_all_parquets(paths, additional_value_extractor)

        return run

    @classmethod
    def _convert_pandas_dataframe_to_spark_records(cls, df):
        return df.to_dict(orient='records')

    def load_spark_dfs_from_paths(self, sc: SparkContext,
                                  paths: list[str],
                                  additional_value_extractor: Optional[Callable[[str], dict[str, Any]]] = None):
        if additional_value_extractor is None:
            additional_value_extractor = lambda p: {}

        paths_batch = sc.parallelize(paths, len(paths))

        return paths_batch.mapPartitions(self.spj_load_parquet(additional_value_extractor)).toDF()
