import matplotlib.pyplot as plt
import numpy as np

a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3, 3)

# 显示图片，interpolation表示什么样子的，upper和lower表示黑白顺序
plt.imshow(a, interpolation='nearest', cmap='bone', origin='upper')
plt.colorbar(shrink=0.9)  # 压缩成0.9

plt.xticks(())
plt.yticks(())
plt.show()
