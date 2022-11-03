from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from customers_cleanup.config.ConfigStore import *
from customers_cleanup.udfs.UDFs import *

def bronze_customers_0(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"lakehouse.bronze_customers")
