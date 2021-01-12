import numpy as np
import pandas as pd

# グラフに表示する点数
number = 5000
df = pd.read_csv("./result/analyze.csv", decimal=',')
# ランダムに株の割合を生成
percent = df['percent'].values
percent = percent.astype(np.float64)
percent_T = percent.T
# 共分散行列を読み込み
cov = np.loadtxt('./result/cov.csv', delimiter=',')
cov = cov.astype(np.float64)
# 共分散行列に割合を掛けてリスクを計算
x = np.dot(percent, cov)
ss = np.dot(x, percent_T)
# 分散なので0.5乗して標準偏差に
s = ss ** 0.5
change = df['per_change'].values
change = change.astype(np.float64)
ret = np.dot(change, percent_T)
sharp = (ret-0.001)/s
print("sharp_ratio:" + str(round(sharp, 5)))
