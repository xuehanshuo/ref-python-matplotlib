import matplotlib.pyplot as plt
import numpy as np

# 共 1024 个点
n = 1024

# 正态随机数，平均值是0，方差是1
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)  # 颜色计算得出来

plt.scatter(X, Y, s=75, c=T, alpha=0.5)  # 大小，颜色计算，透明度
# plt.scatter(np.arange(5), np.arange(5))

plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))

# 隐藏x，y的ticks
plt.xticks(())
plt.yticks(())

plt.show()
