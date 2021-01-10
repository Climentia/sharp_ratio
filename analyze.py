import glob
import re
import os
import pandas as pd
start_year = 2010
end_year = 2020
start_date = "01-01"
end_date = "12-10"


start = str(start_year) + "-" + start_date
end = str(end_year) + "-" + start_date
with open("./result/std.csv", "w") as fw:
    head = "id,std,per_change,start,percent\n"
    fw.write(head)
    stock_path_list = glob.glob("./data/*")
    for path in stock_path_list:
        print(path)
        if ".T.csv" in path:
            df = pd.read_csv(path, index_col=['Date'], parse_dates=['Date'])
            df = df[start:end]
            df['count'] = pd.to_datetime(df.index.values)
            df['count'] = df['count'].dt.year.astype('int') - start_year
            df_select = df.iloc[2, 0]
            std = df["Open"].std()
            df2 = df.resample('AS').first()
            df2['change'] = df2['Open'].pct_change()
            change = df2['change'].mean()
            df2['CAGR'] = ((df2['Open']/df_select)**(1/(df2['count']))-1)
            df2 = df2.dropna()
            cagr_line = df2.tail(1)
            cagr = cagr_line.iloc[0, 8]
            mean = df['Open'].mean()
            id0 = path.lstrip("./data/")
            id1 = id0.lstrip("\\")
            id = id1.rstrip(".csv")
            txt = id + "," + str(std) + "," + str(cagr) + "," + str(cagr) + "\n"
            fw.write(txt)
        elif "JPYUSD=X.csv" in path:
            df = pd.read_csv(path, index_col=['Date'], parse_dates=['Date'])
            df = df[start:end]
            df['count'] = pd.to_datetime(df.index.values)
            df['count'] = df['count'].dt.year.astype('int') - start_year
            df_select = df.iloc[0, 0]
            std = df["Open"].std()
            df2 = df.resample('AS').first()
            df2['change'] = df2['Open'].pct_change()
            change = df2['change'].mean()
            df2['CAGR'] = ((df2['Open']/df_select)**(1/(df2['count']))-1)
            df2 = df2.dropna()
            cagr_line = df2.tail(1)
            cagr = cagr_line.iloc[0, 9]
            mean = df['Open'].mean()
            id0 = path.lstrip("./data/")
            id1 = id0.lstrip("\\")
            id = id1.rstrip(".csv")
            txt = id + "," + str(std) + "," + str(cagr) + "," + str(cagr) + "\n"
            fw.write(txt)
        elif ".HK.csv" in path:
            df = pd.read_csv(path, index_col=['Date'], parse_dates=['Date'])
            df = df[start:end]
            df['count'] = pd.to_datetime(df.index.values)
            df['count'] = df['count'].dt.year.astype('int') - start_year
            df_ex = pd.read_csv("./exchange/HKDJPY=X.csv", index_col=['Date'], parse_dates=['Date'])
            df["Open2"] = df["Open"] * df_ex["Open"]
            df_select = df.iloc[0, 7]
            std = df["Open2"].std()
            df2 = df.resample('AS').first()
            df2['change'] = df2['Open2'].pct_change()
            change = df2['change'].mean()
            df2['CAGR'] = ((df2['Open2']/df_select)**(1/(df2['count']))-1)
            df2 = df2.dropna()
            cagr_line = df2.tail(1)
            cagr = cagr_line.iloc[0, 9]
            mean = df['Open2'].mean()
            id0 = path.lstrip("./data/")
            id1 = id0.lstrip('\\')
            id = id1.rstrip(".csv")
            txt = id + "," + str(std) + "," + str(cagr) + "," + str(cagr) + "\n"
            fw.write(txt)
        elif ".L.csv" in path:
            df = pd.read_csv(path, index_col=['Date'], parse_dates=['Date'])
            df = df[start:end]
            df['count'] = pd.to_datetime(df.index.values)
            df['count'] = df['count'].dt.year.astype('int') - start_year
            df_ex = pd.read_csv("./exchange/GBPJPY=X.csv", index_col=['Date'], parse_dates=['Date'])
            df["Open2"] = df["Open"] * df_ex["Open"]
            df_select = df.iloc[0, 7]
            var = df["Open2"].var()
            df2 = df.resample('AS').first()
            df2['change'] = df2['Open2'].pct_change()
            df2['CAGR'] = ((df2['Open2']/df_select)**(1/(df2['count']))-1)
            df2 = df2.dropna()
            cagr = df2.tail(1)
            cagr = cagr_line.iloc[0, 9]
            mean = df['Open2'].mean()
            change = df2['change'].mean()
            id0 = path.lstrip("./data/")
            id1 = id0.lstrip("\\")
            id = id1.rstrip(".csv")
            txt = id + "," + str(std) + "," + str(cagr) + "," + str(cagr) + "\n"
            fw.write(txt)
        else:
            df = pd.read_csv(path, index_col=['Date'], parse_dates=['Date'])
            df = df[start:end]
            df['count'] = pd.to_datetime(df.index.values)
            df['count'] = df['count'].dt.year.astype('int') - start_year
            df_ex = pd.read_csv("./exchange/JPY=X.csv", index_col=['Date'], parse_dates=['Date'])
            df["Open2"] = df["Open"] * df_ex["Open"]
            df_select = df.iloc[0, 7]
            std = df["Open2"].std()
            df2 = df.resample('AS').first()
            df2['change'] = df2['Open2'].pct_change()
            df2['CAGR'] = ((df2['Open2']/df_select)**(1/(df2['count']))-1)
            df2 = df2.dropna()
            cagr_line = df2.tail(1)
            cagr = cagr_line.iloc[0, 9]
            mean = df['Open2'].mean()
            change = df2['change'].mean()
            id0 = path.lstrip("./stock/data/")
            id1 = id0.lstrip("\\")
            id = id1.rstrip(".csv")
            txt = id + "," + str(std) + "," + str(cagr) + "," + str(cagr) + "\n"
            fw.write(txt)
