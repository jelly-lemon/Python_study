"""
面向过程方式：
plt 用到底

面向对象方式：
FigureCanvas（画布）、 Figure (图像)、 Axes (轴域)
"""

from matplotlib import pyplot as plt
import matplotlib.ticker as mtick
import random
import numpy as np


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
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=0.2)  # wspace 水平间距
    plt.suptitle("总标题", fontsize=16)
    plt.show()


def test_2():
    """
    文字注释
    """
    x = np.arange(0, 6)
    y = x * x

    plt.plot(x, y, marker='o')
    for xy in zip(x, y):
        # xytest 表示偏移 xy 的位置
        plt.annotate("(%s,%s)" % xy, xy=xy, xytext=(-10, 10), textcoords='offset points')
    plt.show()


def test_3():
    """
    面向对象方式画图
    """
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [0.5, 0.6, 0.7, 0.8, 0.9, 0.8, 0.7]

    # plt.plot(x, y) 是面向过程方式
    fig, axis = plt.subplots(1)
    axis.set_title("Hello World")
    axis.plot(x, y)
    fig.show()


def test_4():
    """
    TODO 设置各种字体
    """
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [0.5, 0.6, 0.7, 0.8, 0.9, 0.8, 0.7]

    my_font = {'family': 'Times New Roman',
               'weight': 'bold',
               'size': 24,
               }

    # plt.plot(x, y) 是面向过程方式
    fig, axis = plt.subplots(1)
    axis.set_title("Hello World", fontdict=my_font)

    fig.show()


if __name__ == '__main__':
    test_3()
