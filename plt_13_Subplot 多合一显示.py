import matplotlib.pyplot as plt

# 2+2
plt.figure()
# 将figure分为两行两列，在第一个区域画图
plt.subplot(2, 2, 1)
# 坐标为从0到1
plt.plot([0, 1], [0, 1])

plt.subplot(2, 2, 2)
plt.plot([0, 1], [0, 2])

plt.subplot(2, 2, 3)
plt.plot([0, 1], [0, 3])

plt.subplot(224)
plt.plot([0, 1], [0, 4])

# 1+3
plt.figure()
# 将figure分为2行1列，占第一个
plt.subplot(2, 1, 1)
plt.plot([0, 1], [0, 1])
# 再将figure分为2行3列，上面第一个已经占了3个，所以从4开始
plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 2])

plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 3])

plt.subplot(236)
plt.plot([0, 1], [0, 4])

plt.show()
