from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from orders_cleanup.config.ConfigStore import *
from orders_cleanup.udfs.UDFs import *
from prophecy.utils import *
from orders_cleanup.graph import *

def pipeline(spark: SparkSession) -> None:
    df_bronze_orders_0 = bronze_orders_0(spark)
    df_cleanup = cleanup(spark, df_bronze_orders_0)
    silver_sales_orders(spark, df_cleanup)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/orders_cleanup")
    
    MetricsCollector.start(
        spark = spark,
        pipelineId = spark.conf.get("prophecy.project.id") + "/" + "pipelines/orders_cleanup"
    )
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
