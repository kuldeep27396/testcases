import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
    IntegerType,
    LongType  # Added this import
)
from chispa.dataframe_comparer import assert_df_equality
from data_processor.transformer import DataTransformer


@pytest.fixture(scope="session")
def spark():
    spark = (SparkSession.builder
             .master("local[*]")
             .appName("unit-tests")
             .getOrCreate())
    yield spark
    spark.stop()


@pytest.fixture
def sample_schema():
    return StructType([
        StructField("product_id", StringType(), True),
        StructField("category", StringType(), True),
        StructField("price", DoubleType(), True),
        StructField("quantity", IntegerType(), True)
    ])


@pytest.fixture
def sample_data(spark, sample_schema):
    data = [
        ("P1", "Electronics", 100.0, 2),
        ("P2", "Electronics", 200.0, 1),
        ("P3", "Clothing", 50.0, 3),
        ("P4", "Clothing", None, 1),  # Null price for testing
    ]

    return spark.createDataFrame(data, sample_schema)


def test_process_sales_data(spark, sample_data):
    # Arrange
    transformer = DataTransformer(spark)

    # Act
    result_df = transformer.process_sales_data(sample_data)

    # Assert
    expected_data = [
        ("Electronics", 400.0, 2),
        ("Clothing", 150.0, 1)
    ]
    expected_schema = StructType([
        StructField("category", StringType(), True),
        StructField("total_revenue", DoubleType(), True),
        StructField("number_of_sales", LongType(), False)
    ])
    expected_df = spark.createDataFrame(expected_data, expected_schema)

    assert_df_equality(result_df, expected_df)


def test_process_sales_data_empty(spark, sample_schema):
    # Arrange
    transformer = DataTransformer(spark)
    empty_df = spark.createDataFrame([], sample_schema)

    # Act
    result_df = transformer.process_sales_data(empty_df)

    # Assert
    assert result_df.count() == 0