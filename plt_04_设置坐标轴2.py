import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=5.0, linestyle='--')

# 设置坐标轴范围limit
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# 设置坐标轴的label
plt.xlabel('I am X')
plt.ylabel('I am Y')

# 设置小标ticks
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$really\ good$'])

# gca='get current axis'
ax = plt.gca()
# 取消掉上方后右边的脊梁，设为隐形色
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 设置默认坐标轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 设置坐标轴位置 参数有data outward axes(对应百分比)
ax.spines['bottom'].set_position(('data', 0))  # 将x轴设置到y=0的位置上作为起点
ax.spines['left'].set_position(('data', 0))

plt.show()
