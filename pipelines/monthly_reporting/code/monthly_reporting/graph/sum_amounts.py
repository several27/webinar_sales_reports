from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from monthly_reporting.config.ConfigStore import *
from monthly_reporting.udfs.UDFs import *

def sum_amounts(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("CustomerKey"), month(col("OrderDate")).alias("Month"))

    return df1.agg(sum(col("OrderTotalPrice")).alias("Amounts"))
