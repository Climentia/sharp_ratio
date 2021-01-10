import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


returns = np.array([])
risks = np.array([])
results = np.array([])
count = 0
max = 0
max_percent = 0
max_risk = 0
max_return = 0
for i in range(5000):
    df = pd.read_csv("./result/std.csv", decimal=',')
    # ランダムに株の割合を生成
    percent = df['percent'].values
    n = len(percent)
    arr = np.random.randint(0, 100, n)
    percent = arr / arr.sum()
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
    # sharp = (ret-0.007)/end
    sharp = (ret-0.001)/s
    # print("///////////////////////////////////")
    # print("return:" + str(ret))
    # print("risk:" + str(end))
    # print("shape:" + str(sharp))
    returns = np.append(returns, ret)
    risks = np.append(risks, s)
    results = np.append(results, sharp)
    print(str(sharp))
    if sharp > max:
        max = sharp
        max_risk = s
        max_return = ret
        max_percent = percent
    count += 1
    print(count)
print(risks)
print("----------------------------------------")
print(returns)
fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)

ax.scatter(risks, returns)

ax.set_title('first scatter plot')
ax.set_xlabel('Risk')
ax.set_ylabel('Return')
print(str(max))
print(str(max_risk))
print(str(max_return))
print(max_percent)
fig.show()
input()
