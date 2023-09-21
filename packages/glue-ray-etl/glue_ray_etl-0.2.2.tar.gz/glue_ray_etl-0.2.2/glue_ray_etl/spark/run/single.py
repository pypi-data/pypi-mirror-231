from typing import Any, Optional, Iterable, Callable

import pandas
from pandas import DataFrame as PandasDataFrame
from pyspark.pandas.typedef import spark_type_to_pandas_dtype
from pyspark.sql import DataFrame as PySparkDataFrame
from pyspark.sql import Row
from pyspark.sql.types import StructType


def cvt_pandas_dt(df: pandas.DataFrame):
    for c, t in df.dtypes.items():
        if t == '<M8[ns]':
            df[c] = pandas.Series(df[c].dt.to_pydatetime(), index=df.index, dtype='object')
        if t == '<m8[ns]':
            df[c] = pandas.Series(df[c].dt.to_pytimedelta(), index=df.index, dtype='object')
    return df


def to_pandas_schema(spark_schema: StructType):
    col_names = spark_schema.names
    pandas_schema = {
        cname: spark_type_to_pandas_dtype(spark_schema[cname].dataType) for cname in col_names
    }
    return pandas_schema


def fill_missing_columns(df: PandasDataFrame, pandas_schema: dict[str, Any]):
    for c, dtype in pandas_schema.items():
        if c not in df.columns:
            df[c] = pandas.Series(name=c, dtype=dtype)
    return df


def pandas_map_partition(spdf: PySparkDataFrame, f, schema: Optional[StructType] = None, **kwargs):
    spark_schema = spdf.schema
    pandas_schema = to_pandas_schema(spark_schema)

    def wrapper_function(spark_records: Iterable[Row]):
        records = [spark_record.asDict() for spark_record in spark_records]
        df = pandas.DataFrame.from_records(records)
        df = fill_missing_columns(df, pandas_schema)
        result_df = f(df, **kwargs)
        result_df = cvt_pandas_dt(result_df)
        return result_df.to_dict(orient='records')

    return spdf.rdd.mapPartitions(wrapper_function).toDF(schema=schema)


def in_pandas_map_partition(spdf: PySparkDataFrame, f: Callable[[PandasDataFrame, ...], PandasDataFrame],
                            schema: Optional[StructType] = None, **kwargs):
    if schema is None:
        schema = pandas_map_partition(spdf, f, schema=None, **kwargs).schema

    def f_iter(pdfs):
        return [f(pdf, **kwargs) for pdf in pdfs]

    return spdf.mapInPandas(f_iter, schema=schema)
