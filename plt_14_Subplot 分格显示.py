import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# method1:subplot2grid
###########################################
plt.figure()
# 分成3行3列，起点是0,0点，跨越3个列，1个行
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
ax1.plot([1, 2], [1, 2])
ax1.set_xlabel("x")  # 原来直接操作的命令，全部变成set_什么什么
ax1.set_title("ax1")

ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2, )
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2, )
ax4 = plt.subplot2grid((3, 3), (2, 0), )
ax5 = plt.subplot2grid((3, 3), (2, 1), )

# method2:gridspec
###########################################
plt.figure()
gs = gridspec.GridSpec(3, 3)  # 三行三列
ax6 = plt.subplot(gs[0, :])
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])
ax9 = plt.subplot(gs[2, 0])
ax10 = plt.subplot(gs[2, 1])

# method3:easy to define structure
###########################################
plt.figure()
f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1, 2], [1, 2])

plt.show()
