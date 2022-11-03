from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from orders_cleanup.config.ConfigStore import *
from orders_cleanup.udfs.UDFs import *

def bronze_orders_0(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"lakehouse.bronze_orders")
