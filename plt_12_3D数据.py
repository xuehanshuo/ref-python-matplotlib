import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)  # 设置3D坐标轴

# 设置X,Y
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)  # 生成网格点坐标矩阵
R = np.sqrt(X ** 2 + Y ** 2)

# 设置高
Z = np.sin(R)
# stride为跨度
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, edgecolor='black', cmap=plt.get_cmap('rainbow'))
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')
ax.set_zlim(-2, 2)
plt.show()
