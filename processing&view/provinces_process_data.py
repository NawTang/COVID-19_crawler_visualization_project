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
    option('dbtable', 'provinces_data'). \
    option('user', 'root'). \
    option('password', 'Naw897'). \
    load()


def get_all():
    result_df = df.select('name', 'confirmAdd', 'confirm', 'nowConfirm', 'wzz_add').toPandas()
    return result_df


def get_confirmAdd(num):
    result_df = df.sort('confirmAdd', ascending=False).select('name', 'confirmAdd').limit(num).toPandas()
    return result_df


def get_confirm(num):
    result_df = df.sort('confirm', ascending=False).select('name', 'confirm').limit(num).toPandas()
    return result_df


def get_nowConfirm(num):
    result_df = df.sort('nowConfirm', ascending=False).select('name', 'nowConfirm').limit(num).toPandas()
    return result_df


def get_wzz_add(num):
    result_df = df.sort('wzz_add', ascending=False).select('name', 'wzz_add').limit(num).toPandas()
    return result_df


# 中风险地区总和
def sum_mediumRiskAreaNum():
    result_df = df.agg({'mediumRiskAreaNum': 'sum'}).toPandas()
    return result_df
    # 返回值：
    # +----------------------+
    # | sum(mediumRiskAreaNum) |
    # +----------------------+
    # | 107 |
    # +----------------------+


# 各省中风险地区数量
def get_mediumRiskAreaNum():
    result_df = df.select('name', 'mediumRiskAreaNum').where('mediumRiskAreaNum != 0').toPandas()
    return result_df


# 高风险地区总和
def sum_highRiskAreaNum():
    result_df = df.agg({'highRiskAreaNum': 'sum'}).toPandas()
    return result_df
    # 返回值：
    # +----------------------+
    # | sum(mediumRiskAreaNum) |
    # +----------------------+
    # | 107 |
    # +----------------------+


# 各省高风险地区数
def get_highRiskAreaNum():
    result_df = df.select('name', 'highRiskAreaNum').where('highRiskAreaNum != 0').toPandas()
    return result_df
