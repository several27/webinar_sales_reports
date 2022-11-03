from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from customers_cleanup.config.ConfigStore import *
from customers_cleanup.udfs.UDFs import *
from prophecy.utils import *
from customers_cleanup.graph import *

def pipeline(spark: SparkSession) -> None:
    df_bronze_customers_0 = bronze_customers_0(spark)
    df_cleanup = cleanup(spark, df_bronze_customers_0)
    silver_sales_customers(spark, df_cleanup)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/customers_cleanup")
    
    MetricsCollector.start(
        spark = spark,
        pipelineId = spark.conf.get("prophecy.project.id") + "/" + "pipelines/customers_cleanup"
    )
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
