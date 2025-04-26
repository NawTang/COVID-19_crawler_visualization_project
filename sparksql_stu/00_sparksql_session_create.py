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
    # df.printSchema()
    df.show()

    df.createTempView('add_list')

    # SQL风格
    spark.sql('''
        SELECT * FROM add_list WHERE province='山西'
    ''').show()

    # DSL风格
    df.where("province='上海'").show()
