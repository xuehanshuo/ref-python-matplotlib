import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    # the height function
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
# 设置网格
X, Y = np.meshgrid(x, y)

# 添加颜色fill  hot cool ，8 代表把等高线分成 10 部分
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)

# 画等高线
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidths=.5)

# 添加label
plt.clabel(C, inline=True, fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()
