from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from orders_cleanup.config.ConfigStore import *
from orders_cleanup.udfs.UDFs import *

def silver_sales_orders(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("lakehouse.silver_sales_orders")
