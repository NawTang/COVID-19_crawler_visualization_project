import pandas as pd
from sqlalchemy import create_engine
from pyspark.sql import SparkSession
import os
os.environ['PYSPARK_PYTHON'] = "D:\\Anaconda\\envs\\pyspark\\python.exe"
os.environ['JAVA_HOME'] = 'D:\\dev\\Java\\jdk1.8.0_202'


# engine = create_engine('mysql+pymysql://root:Naw897@localhost:3306/COVID19_data')
# df = pd.read_csv('../data/cities_data_0420.csv')
# df.to_sql('cities_data_0420', engine, index=False)
# 构建SparkSession执行环境入口对象
spark = SparkSession.builder.\
    appName('test').\
    master('local[*]').\
    getOrCreate()


def store_to_cities_data(dlist):
    pdf = pd.DataFrame(dlist)
    # df.to_sql('cities_data', engine, index=False)
    df = spark.createDataFrame(pdf)
    df.write.mode('overwrite'). \
        format('jdbc'). \
        option('url', 'jdbc:mysql://localhost:3306/covid19_data?useSSL=false&useUnicode=true'). \
        option('dbtable', 'cities_data'). \
        option('user', 'root'). \
        option('password', 'Naw897'). \
        save()


def store_to_day_add_data(dlist):
    pdf = pd.DataFrame(dlist)
    # df.to_sql('day_add_data', engine, index=False)
    df = spark.createDataFrame(pdf)
    df.write.mode('overwrite'). \
        format('jdbc'). \
        option('url', 'jdbc:mysql://localhost:3306/covid19_data?useSSL=false&useUnicode=true'). \
        option('dbtable', 'day_add_data'). \
        option('user', 'root'). \
        option('password', 'Naw897'). \
        save()


def store_to_day_all_data(dlist):
    pdf = pd.DataFrame(dlist)
    # df.to_sql('day_all_data', engine, index=False)
    df = spark.createDataFrame(pdf)
    df.write.mode('overwrite'). \
        format('jdbc'). \
        option('url', 'jdbc:mysql://localhost:3306/covid19_data?useSSL=false&useUnicode=true'). \
        option('dbtable', 'day_all_data'). \
        option('user', 'root'). \
        option('password', 'Naw897'). \
        save()


def store_to_provinces_data(dlist):
    pdf = pd.DataFrame(dlist)
    # df.to_sql('provinces_data', engine, index=False)
    df = spark.createDataFrame(pdf)
    df.write.mode('overwrite'). \
        format('jdbc'). \
        option('url', 'jdbc:mysql://localhost:3306/covid19_data?useSSL=false&useUnicode=true'). \
        option('dbtable', 'provinces_data'). \
        option('user', 'root'). \
        option('password', 'Naw897'). \
        save()


def store_to_world_data(dlist):
    pdf = pd.DataFrame(dlist)
    # df.to_sql('world_data', engine, index=False)
    df = spark.createDataFrame(pdf)
    df.write.mode('overwrite'). \
        format('jdbc'). \
        option('url', 'jdbc:mysql://localhost:3306/covid19_data?useSSL=false&useUnicode=true'). \
        option('dbtable', 'world_data'). \
        option('user', 'root'). \
        option('password', 'Naw897'). \
        save()
