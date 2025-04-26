# coding:utf8

import pandas as pd


def for_confirmAdd(ur):
    df1 = pd.read_csv(ur)
    df2 = df1.sort_values(by='confirmAdd')
    df_result = df2.tail(10)
    return df_result


def for_confirm(ur):
    df1 = pd.read_csv(ur)
    df2 = df1.sort_values(by='confirm')
    df_result = df2.tail(10)
    return df_result


def for_nowConfirm(ur):
    df1 = pd.read_csv(ur)
    df2 = df1.sort_values(by='nowConfirm')
    df_result = df2.tail(10)
    return df_result
