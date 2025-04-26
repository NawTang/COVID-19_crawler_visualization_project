# coding:utf8

# SparkSession对象的导包，来自于pyspark.sql包中
from pyspark.sql import SparkSession
import pandas as pd


if __name__ == '__main__':
    # 构建SparkSession执行环境入口对象
    spark = SparkSession.builder.\
        appName('test').\
        master('local[*]').\
        getOrCreate()

    # 通过SparkSession对象获取SparkContext对象
    sc = spark.sparkContext

    # SparkSQL的HelloWorld
    df = spark.read.csv('../data/cities_data_0426.csv', header=True)
    df1 = pd.read_csv('../data/cities_data_0426.csv')
    df2 = spark.createDataFrame(df1)
    df2.printSchema()
    df.printSchema()
    # df.show()

