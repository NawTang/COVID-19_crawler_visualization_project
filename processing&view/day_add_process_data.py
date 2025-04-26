# coding:utf8
import pandas as pd
import tools
from pyspark.sql import SparkSession
import os

os.environ['PYSPARK_PYTHON'] = "D:\\Anaconda\\envs\\pyspark\\python.exe"
os.environ['JAVA_HOME'] = 'D:\\dev\\Java\\jdk1.8.0_202'

spark = SparkSession.builder. \
    appName('test'). \
    master('local[*]'). \
    getOrCreate()

df = spark.read.format('jdbc'). \
    option('url', 'jdbc:mysql://localhost:3306/covid19_data?useSSL=false&useUnicode=true'). \
    option('dbtable', 'day_add_data'). \
    option('user', 'root'). \
    option('password', 'Naw897'). \
    load()


def get_day():
    re_df = df.sort('日期').select('日期').toPandas()
    return re_df


def get_local_confirm_add():
    re_df = df.sort('日期').select('本土新增确诊').toPandas()
    return re_df


def get_confirm_add():
    re_df = df.sort('日期').select('新增确诊').toPandas()
    return re_df


def get_wzz_add():
    re_df = df.sort('日期').select('新增无症状感染者').toPandas()
    return re_df


def get_local_wzz_add():
    re_df = df.sort('日期').select('本土新增无症状感染者').toPandas()
    return re_df


def get_dead_add():
    re_df = df.sort('日期').select('新增死亡').toPandas()
    return re_df


def get_heal_add():
    re_df = df.sort('日期').select('新增治愈').toPandas()
    return re_df


def get_dead_rate():
    re_df = df.sort('日期').select('当日死亡率').toPandas()
    return re_df


def get_heal_rate():
    re_df = df.sort('日期').select('当日治愈率').toPandas()
    return re_df



