from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from monthly_reporting.config.ConfigStore import *
from monthly_reporting.udfs.UDFs import *

def silver_sales_customers_0(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"lakehouse.silver_sales_customers")
