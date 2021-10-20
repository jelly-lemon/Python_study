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
    d3 = np.stack((d1, d2))
    print(d3)

    # 按列拼接
    d3 = np.concatenate((d1, d2))
    print(d3)   # [1 2 3 4 5 6]




if __name__ == '__main__':
    test_3()
