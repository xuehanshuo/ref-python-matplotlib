import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
# uniform均匀分布
Y1 = (1 - X / n) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / n) * np.random.uniform(0.5, 1.0, n)

plt.xlim(-.5, n)
plt.ylim(-1.25, 1.25)
plt.xticks(())
plt.yticks(())

plt.bar(X, +Y1, facecolor='#ff4500', edgecolor='white')
plt.bar(X, -Y2, facecolor='#228B22', edgecolor='white')

for x, y in zip(X, Y1):
    # xy的位置，输出值，对齐方式ha：horizontal alignment
    plt.text(x, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    plt.text(x, - y - 0.05, '-%.2f' % y, ha='center', va='top')

plt.show()
