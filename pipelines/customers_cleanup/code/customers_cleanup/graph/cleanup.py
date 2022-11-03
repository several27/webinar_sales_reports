from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from customers_cleanup.config.ConfigStore import *
from customers_cleanup.udfs.UDFs import *

def cleanup(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("c_custkey").alias("CustomerKey"), 
        col("c_name").alias("CustomerName"), 
        col("c_address").alias("CustomerAddress"), 
        col("c_nationkey").alias("CustomerNationKey"), 
        col("c_phone").alias("CustomerPhone"), 
        floor(col("c_acctbal")).alias("CustomerAccountBalance"), 
        col("c_mktsegment").alias("CustomerMarketingSegment"), 
        col("c_comment").alias("CustomerComment")
    )
