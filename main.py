import pyspark as spark
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession\
        .builder\
        .appName('teste')\
        .config("spark.master", "local")\
        .getOrCreate()


def criar_dataframe(path):
    df = spark.read.option("inferSchema","true").json(path)
    return df

if __name__ == "__main__":
    print("TESTE")
