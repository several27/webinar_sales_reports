from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from monthly_reporting.config.ConfigStore import *
from monthly_reporting.udfs.UDFs import *

def final_gold_report(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("lakehouse.final_gold_report")
