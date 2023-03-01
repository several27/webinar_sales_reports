from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *
from prophecy.utils import *
from mrr_reporting.graph import *

def pipeline(spark: SparkSession) -> None:
    df_silver_sales_customers_0 = silver_sales_customers_0(spark)
    df_silver_sales_orders_1 = silver_sales_orders_1(spark)
    df_by_customer_key = by_customer_key(spark, df_silver_sales_customers_0, df_silver_sales_orders_1)
    df_sum_amounts = sum_amounts(spark, df_by_customer_key)
    df_sum_amounts = df_sum_amounts.cache()
    df_enrich_customers = enrich_customers(spark, df_sum_amounts)
    final_report(spark, df_enrich_customers)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/mrr_reporting")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/mrr_reporting")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
