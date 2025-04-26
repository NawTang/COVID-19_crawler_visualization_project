# coding:utf8

# SparkSession对象的导包，来自于pyspark.sql包中
from pyspark.sql import SparkSession
import pandas as pd
import os
os.environ['PYSPARK_PYTHON'] = "D:\\Anaconda\\envs\\pyspark\\python.exe"
os.environ['JAVA_HOME'] = 'D:\\dev\\Java\\jdk1.8.0_202'


if __name__ == '__main__':
    # 构建SparkSession执行环境入口对象
    spark = SparkSession.builder.\
        appName('test').\
        master('local[*]').\
        getOrCreate()
    pdf = pd.read_csv('../data/cities_data_0426.csv')
    df = spark.createDataFrame(pdf)

    df.write.mode('overwrite').\
        format('jdbc').\
        option('url', 'jdbc:mysql://localhost:3306/covid19_data?useSSL=false&useUnicode=true').\
        option('dbtable', 'cities_data').\
        option('user', 'root').\
        option('password', 'Naw897').\
        save()
    print('更新完成')


