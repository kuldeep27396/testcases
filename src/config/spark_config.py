from pyspark.sql import SparkSession

def get_spark_session(app_name: str = "test_session") -> SparkSession:
    return (SparkSession.builder
            .appName(app_name)
            .master("local[*]")
            .config("spark.sql.shuffle.partitions", "2")
            .config("spark.default.parallelism", "4")
            .config("spark.sql.execution.arrow.pyspark.enabled", "true")
            .getOrCreate())
