import glob
import pandas as pd
# シャープレシオを出したい年
start_year = 2010
end_year = 2020
# シャープレシオを出したい月
start_date = "01-01"
end_date = "12-10"
start = str(start_year) + "-" + start_date
end = str(end_year) + "-" + start_date
with open("./result/analyze.csv", "w") as fw:
    head = "id,per_change,cagr,percent\n"
    fw.write(head)
    stock_path_list = glob.glob("./data/*")
    for path in stock_path_list:
        print(path)
        # .T(Tokyo)日本株の結果整理
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
            df2['CAGR'] = ((df2['Open']/df_select)**(1/(df2['count'])))-1
            df2 = df2.dropna()
            cagr_line = df2.tail(1)
            cagr = cagr_line.iloc[0, 8]
            mean = df['Open'].mean()
            id0 = path.lstrip("./data/")
            id1 = id0.lstrip("\\")
            id = id1.rstrip(".csv")
            txt = id + "," + str(change) + "," + str(cagr) + "\n"
            fw.write(txt)
        # .HK(HongKong)香港株の結果整理
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
            df2['CAGR'] = ((df2['Open2']/df_select)**(1/(df2['count'])))-1
            df2 = df2.dropna()
            cagr_line = df2.tail(1)
            cagr = cagr_line.iloc[0, 9]
            mean = df['Open2'].mean()
            id0 = path.lstrip("./data/")
            id1 = id0.lstrip('\\')
            id = id1.rstrip(".csv")
            txt = id + "," + str(change) + "," + str(cagr) + "\n"
            fw.write(txt)
        # .L(London)ロンドン株の結果整理
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
            df2['CAGR'] = ((df2['Open2']/df_select)**(1/(df2['count'])))-1
            df2 = df2.dropna()
            cagr = df2.tail(1)
            cagr = cagr_line.iloc[0, 9]
            mean = df['Open2'].mean()
            change = df2['change'].mean()
            id0 = path.lstrip("./data/")
            id1 = id0.lstrip("\\")
            id = id1.rstrip(".csv")
            txt = id + "," + str(change) + "," + str(cagr) + "\n"
            fw.write(txt)
        # アメリカ株の結果整理(上記以外全部ここに入るので注意。シンガポールや豪州、EUやりたい場合は追加する必要あり)
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
            txt = id + "," + str(change) + "," + str(cagr) + "\n"
            fw.write(txt)
