import numpy as np
import pandas as pd

df = pd.read_csv("./result/std.csv")
array = df['probability'].values
a = np.loadtxt('./result/cov.csv')
x = np.dot(a, array)
print(x)
# array_main = df['std'].values
# array_main = np.empty((array.shape[0], 0), np.float64)
# print(array_main.shape)
# count = 0
# len = array.shape[0]
# for i in range(len):
#     print(array.shape)
#     array_main = np.insert(array_main, count, array, axis=1)
#     count += 1
# rint(array_main)
# print(array_main.shape)
# a = np.dot(array_main, array)
# print(a)
