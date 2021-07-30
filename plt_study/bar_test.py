"""
条状图
"""
import numpy as np
import matplotlib.pyplot as plt

def test_1():
    bar_width = 0.09
    # 数组表示有多少个数据集
    # 子数组表示所有分类器在一个数据上的分类结果
    data = [[0.79, 0.83, 0.81, 0.84], [0.91, 0.89, 0.93, 0.90], [0.56, 0.60, 0.63, 0.59]]
    x_ticks = np.array([i for i in range(1, len(data)+1)], dtype=np.float)
    # ticks 表明在哪个位置，labels 表明显示什么
    plt.xticks(ticks=x_ticks, labels=x_ticks)
    space = 0.01
    data_width = bar_width * len(data[0]) + space * (len(data[0]) - 1)
    for i, d in enumerate(data):
        start = (i+1) - data_width/2 + bar_width/2
        # x 是条状的中间点，不是起始点
        x = [start + j * (bar_width+space) for j in range(len(d))]
        b = plt.bar(x=x, height=d, width=bar_width)


    plt.show()


def test_2():
    legend = ("kNN", "DT", "Our")
    bar_width = 0.09
    # 数组表示有多少分类器
    # 子数组表示一个分类器在所有数据集的分类结果
    data = [[0.79, 0.83, 0.81, 0.84], [0.91, 0.89, 0.93, 0.90], [0.56, 0.60, 0.63, 0.59]]
    x_ticks = np.array([i for i in range(1, len(data[0]) + 1)], dtype=np.float)
    # ticks 表明在哪个位置，labels 表明显示什么
    plt.xticks(ticks=x_ticks, labels=x_ticks)
    space = 0.01
    data_width = bar_width * len(data) + space * (len(data) - 1)

    start = x_ticks - data_width / 2 + bar_width / 2
    all_b = []
    for i, d in enumerate(data):
        b = plt.bar(x=start, height=d, width=bar_width)
        start += bar_width+space
        all_b.append(b)

    # upper right
    plt.legend(all_b, legend, loc="best")

    plt.show()

test_2()