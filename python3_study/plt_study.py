from matplotlib import pyplot as plt
import matplotlib.ticker as mtick
import random


def test_1():
    """
    绘制多个子图
    """
    # 设置显示中文
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体

    x_ticks = [i for i in range(10)]
    data = [random.random() for t in range(10)]
    figure, axes = plt.subplots(2, 2)
    for i in range(2):
        for j in range(2):
            axes[i][j].plot(x_ticks, data)
            axes[i][j].set_title("子标题" + str(i) + str(j))
            axes[i][j].set_xlabel("编号")
            axes[i][j].set_ylabel("比例")
            axes[i][j].yaxis.set_major_formatter(mtick.FormatStrFormatter('%.4f'))

    # 调整间距
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=0.2)       # wspace 水平间距
    plt.suptitle("总标题", fontsize=16)
    plt.show()


if __name__ == '__main__':
    test_1()