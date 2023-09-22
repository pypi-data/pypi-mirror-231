from typing import Callable, Any, Optional, Iterable

import pandas
from pyspark import SparkContext

from glue_ray_etl.spark.run.single import cvt_pandas_dt


class SparkParquetIO:
    def _load_parquet(self, path: str, additional_value_extractor: Callable[[str], dict[str, Any]],
                      ignore_error: bool = False):
        additional_values = additional_value_extractor(path)
        try:
            df = pandas.read_parquet(path, partitioning=None)
        except Exception as e:
            if ignore_error:
                return pandas.DataFrame()
            raise e
        for c, v in additional_values.items():
            df[c] = v
        return df

    def _load_all_parquets(self,
                           paths: Iterable[str],
                           additional_value_extractor: Optional[Callable[[str], dict[str, Any]]] = None,
                           ignore_error: bool = False):
        result_df = pandas.concat([self._load_parquet(path, additional_value_extractor, ignore_error)
                                   for path in paths], axis=0)
        result_df = cvt_pandas_dt(result_df)
        return self._convert_pandas_dataframe_to_spark_records(result_df)

    def spj_load_parquet(self, additional_value_extractor: Optional[Callable[[str], dict[str, Any]]] = None,
                         ignore_error: bool = False):
        def run(paths: Iterable[str]):
            return self._load_all_parquets(paths, additional_value_extractor, ignore_error)

        return run

    @classmethod
    def _convert_pandas_dataframe_to_spark_records(cls, df):
        return df.to_dict(orient='records')

    def load_spark_dfs_from_paths(self, sc: SparkContext,
                                  paths: list[str],
                                  additional_value_extractor: Optional[Callable[[str], dict[str, Any]]] = None,
                                  ignore_error: bool = False):
        if additional_value_extractor is None:
            additional_value_extractor = lambda p: {}

        paths_batch = sc.parallelize(paths, len(paths))

        return paths_batch.mapPartitions(self.spj_load_parquet(additional_value_extractor, ignore_error)).toDF()
