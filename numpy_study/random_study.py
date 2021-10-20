import numpy as np

import random
import pandas

def test_0():
    """
    rand，用于生成随机数组
    随机样本取值范围是[0,1)
    """
    # 生成长度为 4 的 1 维数组
    arr = np.random.rand(4)
    print(arr)

    print("arr * 2:")
    print(arr * 2)

    # 生成 3x4 的二维数组
    arr1 = np.random.rand(3, 4)
    print(arr1)


def test_1():
    """
    生成一个随机整数
    """
    # 生成的随机数包含第二个参数
    print(random.randint(0, 1))


def test_2():
    """
    根据 shape 生成随机数组
    """
    shape = (3, 4)
    a = np.random.rand(*(shape))  # rand 函数只能传单个参数，不能传 shape
    print(a)


def test_3():
    """
    随机选择数组的元素
    """
    data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    new_data = np.random.choice(data, 5, replace=False)  # replace=False 表示不放回
    print(new_data)


def test_4():
    """
    随机打乱数组
    """
    d1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    np.random.shuffle(d1)
    print(d1)

    # 随机同步打乱两个数组
    d1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    d2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    state = np.random.get_state()
    np.random.shuffle(d1)
    print(d1)
    np.random.set_state(state)
    np.random.shuffle(d2)
    print(d2)


if __name__ == '__main__':
    test_4()
