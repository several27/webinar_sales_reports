from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *

def with_nations_regions(
        spark: SparkSession,
        in0: DataFrame,
        in1: DataFrame,
        in2: DataFrame, 
        in3: DataFrame
) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.CustomerKey") == col("in1.c_custkey")), "inner")\
        .join(in2.alias("in2"), (col("in2.n_nationkey") == col("in1.c_nationkey")), "inner")\
        .join(in3.alias("in3"), (col("in3.r_regionkey") == col("in2.n_regionkey")), "inner")\
        .select(col("in0.CustomerKey").alias("CustomerKey"), col("in1.c_name").alias("CustomerName"), col("in3.r_name").alias("RegionName"), col("in0.Amounts").alias("Amounts"), col("in0.Month").alias("Month"))
