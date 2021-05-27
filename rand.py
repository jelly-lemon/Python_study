"""
生成随机数
"""
import random

import numpy as np

def test_0():
    """
    生成一个随机整数
    """
    # 生成的随机数包含第二个参数
    print(random.randint(0, 1))


def test_1():
    """
    根据 shape 生成随机数组
    """
    shape = (3, 4)
    a = np.random.rand(i for i in shape)    # rand 函数只能传单个参数，不能传 shape
    print(a)




if __name__ == '__main__':
    test_0()