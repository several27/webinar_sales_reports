from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from orders_cleanup.config.ConfigStore import *
from orders_cleanup.udfs.UDFs import *

def cleanup(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("o_orderkey").alias("OrderKey"), 
        col("o_custkey").alias("OrderCustomerKey"), 
        col("o_orderstatus").alias("OrderStatus"), 
        col("o_totalprice").alias("OrderTotalPrice"), 
        col("o_orderdate").alias("OrderDate"), 
        col("o_orderpriority").alias("OrderPriority"), 
        col("o_clerk").alias("OrderClerk"), 
        col("o_shippriority").alias("OrderShipPriority"), 
        col("o_comment").alias("OrderComment")
    )
