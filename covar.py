import glob
import re
import os
import pandas as pd
import itertools
# analyzeで入力した期間を入力
start_year = 2015
end_year = 2020
start_date = "01-01"
end_date = "12-10"


def read_file(path):
    print(path)
    if ".T.csv" in path:
        df = pd.read_csv(path, index_col=['Date'], parse_dates=['Date'])
        df = df[start:end]
        df['count'] = pd.to_datetime(df.index.values)
        df['Open2'] = df["Open"]
        df = df.resample('AS').first()
        df['change'] = df["Open2"].pct_change()
        print(df['change'].std())
    elif ".HK.csv" in path:
        df = pd.read_csv(path, index_col=['Date'], parse_dates=['Date'])
        df = df[start:end]
        df_ex = pd.read_csv("./exchange/HKDJPY=X.csv", index_col=['Date'], parse_dates=['Date'])
        df['count'] = pd.to_datetime(df.index.values)
        df["Open2"] = df["Open"] * df_ex["Open"]
        df = df.resample('AS').first()
        df['change'] = df["Open2"].pct_change()
        print(df['change'].std())
    elif ".L.csv" in path:
        df = pd.read_csv(path, index_col=['Date'], parse_dates=['Date'])
        df = df[start:end]
        df_ex = pd.read_csv("./exchange/GBPJPY=X.csv", index_col=['Date'], parse_dates=['Date'])
        df['count'] = pd.to_datetime(df.index.values)
        df["Open2"] = df["Open"] * df_ex["Open"]
        df = df.resample('AS').first()
        df['change'] = df["Open2"].pct_change()
        print(df['change'].std())
    else:
        df = pd.read_csv(path, index_col=['Date'], parse_dates=['Date'])
        df = df[start:end]
        df_ex = pd.read_csv("./exchange/JPY=X.csv", index_col=['Date'], parse_dates=['Date'])
        df['count'] = pd.to_datetime(df.index.values)
        df["Open2"] = df["Open"] * df_ex["Open"]
        df = df.resample('AS').first()
        df['change'] = df["Open2"].pct_change()
        print('Open2')
        print(df['change'].std())
        # print(df2)
    return df


start = str(start_year) + "-" + start_date
end = str(end_year) + "-" + start_date
stock_path_list = glob.glob("./data/*")
stock_path_list_len = len(stock_path_list)
stock_name = []
for path in stock_path_list:
    id0 = path.lstrip("./data/")
    id1 = id0.lstrip("\\")
    id = id1.rstrip(".csv")
    stock_name.append(id)
df00 = read_file(stock_path_list[0])
start_id = stock_name[0]
df00.columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'count', 'Open2', start_id]
df0 = df00[start_id]
for path_num in range(1, stock_path_list_len):
    df1 = read_file(stock_path_list[path_num])
    id0 = stock_path_list[path_num].lstrip("./data/")
    id1 = id0.lstrip("\\")
    id = id1.rstrip(".csv")
    df1.columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'count', 'Open2', id]
    df2 = df1[id]
    df0 = pd.concat([df0, df2], axis=1)

df0 = df0.dropna()
cov = df0.cov()
cov.to_csv('./result/cov.csv', header=False, index=False)
# print(a)
