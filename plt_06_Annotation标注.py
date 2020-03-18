import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2 * x + 1

plt.figure(num=1, figsize=(8, 5))
plt.plot(x, y)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 首先确定要找哪一个点
x0 = 1
y0 = 2 * x0 + 1
# 绘制点 (s 大小，color 颜色blue)
plt.scatter(x0, y0, s=50, color='b')
# 添加连接到坐标轴的线 (左边是横坐标首末，右边是纵坐标首末，使用black的---线绘制，线宽为2.5)
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)

# 标注1
# 表达式内容，表达式点，xy依据是线上的数据，表达式的位置，表达式的基准，字号，箭头（箭头样子和连接偏转）
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30), textcoords='offset points',
             fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))

# 标注2
plt.text(-1.7, 3, r'$This\ is\ the\ text.\ \mu\ \sigma_i\ \alpha_t$',
         fontsize=16, color='r')
plt.show()
