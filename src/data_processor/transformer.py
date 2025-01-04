from pyspark.sql import SparkSession
from pyspark.sql import functions as F

class DataTransformer:
    def __init__(self, spark: SparkSession):
        self.spark = spark

    def process_sales_data(self, df):
        """
        Process sales data by:
        1. Removing null values
        2. Calculating total revenue
        3. Aggregating by product category
        """
        return (df
                .dropna(subset=['price', 'quantity'])
                .withColumn('total_revenue', F.col('price') * F.col('quantity'))
                .groupBy('category')
                .agg(
                    F.sum('total_revenue').alias('total_revenue'),
                    F.count('*').alias('number_of_sales')
                )
                .orderBy('total_revenue', ascending=False))