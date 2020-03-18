import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()

plt.xlim((-1, 2))
plt.ylim((-2, 3))

plt.xlabel('I am X')
plt.ylabel('I am Y')

new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$really\ good$'])

ax = plt.gca()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 传label，取名字
l1, = plt.plot(x, y2, label='up')
l2, = plt.plot(x, y1, color='red', linewidth=5.0, linestyle='--', label='down')

# 使用legend添加默认图例
# loc = [‘best’ , 'upper right' , 'center left' , 'lower right']
# handle表示希望显示哪条线
# label表示线的名称
plt.legend(handles=[l1, l2, ], labels=['aaa', 'bbb'], loc='best')
plt.show()
