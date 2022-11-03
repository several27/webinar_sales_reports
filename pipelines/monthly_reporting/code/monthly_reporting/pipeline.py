from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from monthly_reporting.config.ConfigStore import *
from monthly_reporting.udfs.UDFs import *
from prophecy.utils import *
from monthly_reporting.graph import *

def pipeline(spark: SparkSession) -> None:
    df_silver_sales_customers_0 = silver_sales_customers_0(spark)
    df_silver_orders_sales_2 = silver_orders_sales_2(spark)
    df_by_customer_key = by_customer_key(spark, df_silver_sales_customers_0, df_silver_orders_sales_2)
    df_sum_amounts = sum_amounts(spark, df_by_customer_key)
    df_enrich_customers_1 = enrich_customers_1(spark, df_sum_amounts)
    final_gold_report(spark, df_enrich_customers_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/monthly_reporting")
    
    MetricsCollector.start(
        spark = spark,
        pipelineId = spark.conf.get("prophecy.project.id") + "/" + "pipelines/monthly_reporting"
    )
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
