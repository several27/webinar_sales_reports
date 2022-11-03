from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from customers_cleanup.config.ConfigStore import *
from customers_cleanup.udfs.UDFs import *

def silver_sales_customers(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("lakehouse.silver_sales_customers")
