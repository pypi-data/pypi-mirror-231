from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

default_context_conf = {
    u'spark.rdd.compress': u'True',
    u'spark.serializer': u'org.apache.spark.serializer.KryoSerializer',
    u'spark,kryo.referenceTracking': u'False'
}


def init_context(app_name='GlueRayEtlSparkApp', context_conf: dict[str, str] = None):
    if context_conf is None:
        context_conf = default_context_conf

    spark_conf = SparkConf()

    for k, v in context_conf.items():
        spark_conf.set(k, v)
    sc = SparkContext(appName=app_name,
                      conf=spark_conf)
    return sc


def init_session(envvars: dict[str, str] = None):
    if envvars is None:
        envvars = {}
    spark = SparkSession.builder \
        .appName("Hive Partition Read") \
        .enableHiveSupport() \
        .getOrCreate()
    for k, v in envvars:
        spark = spark.config(f"spark.executorEnv.{k}", v)
    return spark
