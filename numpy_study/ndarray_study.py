from collections import Counter

import numpy as np


def test_0():
    """
    列表转 ndarray，和 list 没啥区别，只是类不同而已
    """
    # 如果列表中即存在字符串，又存在数字，统统转化为字符串
    names = [15, "Tom", "Jerry", 13]
    names = np.asarray(names)
    print(names)
    print(type(names))


def test_1():
    """
    数组对应位置相加
    """
    # 两个列表相加，相当于合并两个列表（在末尾合并）
    d1 = [1, 2, 3, 4]
    d2 = [5, 6, 7, 8]
    print(d1 + d2)

    # 两个 ndarray 相加，就是对应位置相加
    # 【注意】两者的 shape 必须相同
    d3 = np.array(d1) + np.array(d2)
    print(d3)


def test_2():
    """
    生成指定形状的数组，并填充指定数值
    """
    d1 = np.full((2, 3), 5, dtype="float32")
    print(d1)


def test_3():
    """
    数组拼接
    """
    # 按行拼接
    d1 = np.array([[1, 2, 3], [4, 5, 6]])
    d2 = np.array([7, 8, 9])
    d3 = np.vstack((d1, d2))
    print(d3)

    # 按行拼接 2
    d1 = np.array([1, 2, 3])
    d2 = np.array([4, 5, 6])
    d3 = np.vstack((d1, d2))
    print(d3)

    # 创建新的维度拼接
    d1 = np.array([1, 2, 3])
    d2 = np.array([4, 5, 6])
    d3 = np.stack((d1, d2))
    print(d3)

    # 按列拼接
    d1 = np.array([1, 2, 3])
    d2 = np.array([4, 5, 6])
    d3 = np.concatenate((d1, d2))
    print(d3)  # [1 2 3 4 5 6]


def test_4():
    """
    求最大元素下标
    """
    d1 = [[0.1, 0.2, 0.3], [0.3, 0.2, 0.1]]
    max_index = np.argmax(d1, axis=1)
    print(max_index)


def test_5():
    """
    改变 dtype
    """
    d1 = np.array([0., 1., 2., 1.5, 1.6, 1.9])
    d1 = d1.astype(dtype="int32")
    print(d1)  # [0 1 2 1 1 1]


def test_6():
    """
    统计某个数字出现的次数
    """
    # 方法 1：使用 sum
    d1 = np.array([1, 2, 3, 4, 5, 5, 5])
    n = sum(d1 == 5)
    print(n)

    # 方法 2：使用 Counter
    c = Counter(d1)
    print(c)


def test_7():
    """
    获取所有等于该值的索引
    """
    d1 = np.array([1, 2, 3, 4, 5, 5, 5])
    index = np.where(d1 == 5)[0]
    print(index) # [4 5 6]

def test_8():
    """
    数组比较：两两比较，相等为 True，不相等为 False
    """
    d1 = np.array([0, 1, 1, 1])
    d2 = np.array([0, 0, 1, 1])
    d3 = (d1 == d2)
    print(d3) # [ True False  True  True]

    # 统计两者相等的数量
    print(sum(d3[d3 == True]))


def test_9():
    """
    数组相乘
    """
    d1 = np.array([0, 1, 1, 1])
    d2 = np.array([0, 0, 1, 1])
    print(d1*d2)

def test_10():
    """
    求最大值：max，最小值：min
    """
    d1 = [1, 2, 3, 4]
    d1_max = max(d1)
    print(d1_max)

    # 求最小值
    d1_min = min(d1)
    print(d1_min)

def test_11():
    """
    求出现次数最多的数字
    """
    d1 = [1, 2, 3, 1, 3, 3]
    b1 = np.bincount(d1)    # 必须是正整数
    print(b1)
    n_most_times = np.argmax(b1)  # 可两步合并为一步：np.argmax(np.bincount(d1))
    print(n_most_times)

    # 二维数组，求出每一列出现次数最多的数值
    d1 = [[1,2,3,4,3], [1,2,3,4,5], [0,1,2,3,5]]
    d1_max = []
    for j in range(len(d1[0])):
        d2 = [d1[i][j] for i in range(len(d1))]
        max = np.argmax(np.bincount(d2)) #【注意】如果不存在出现次数最多的数值，返回第一个
        d1_max.append(max)
    print(d1_max)


if __name__ == '__main__':
    test_11()
