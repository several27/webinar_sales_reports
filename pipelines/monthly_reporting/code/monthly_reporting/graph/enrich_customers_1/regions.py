from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from monthly_reporting.config.ConfigStore import *
from monthly_reporting.udfs.UDFs import *

def regions(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/databricks-datasets/tpch/delta-001/region/")
