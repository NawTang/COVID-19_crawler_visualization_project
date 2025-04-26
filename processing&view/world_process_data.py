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
    option('dbtable', 'world_data'). \
    option('user', 'root'). \
    option('password', 'Naw897'). \
    load()


def get_confirmAdd(num):
    result_df = df.sort('confirmAdd', ascending=False).select('continent', 'name', 'confirmAdd').limit(num).toPandas()
    # result_df.printSchema()
    # print(type(result))
    return result_df


def get_confirm(num):
    result_df = df.sort('confirm', ascending=False).select('continent', 'name', 'confirm').limit(num).toPandas()
    return result_df


def get_nowConfirm(num):
    result_df = df.sort('nowConfirm', ascending=False).select('continent', 'name', 'nowConfirm').limit(num).toPandas()
    return result_df


def get_deadCompare(num):
    result_df = df.sort('deadCompare', ascending=False).select('continent', 'name', 'deadCompare').limit(num).toPandas()
    return result_df


def get_healCompare(num):
    result_df = df.sort('healCompare', ascending=False).select('continent', 'name', 'healCompare').limit(num).toPandas()
    return result_df
