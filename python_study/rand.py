
import numpy as np

def test_1():
    """
    根据 shape 生成随机数组
    """
    shape = (3, 4)
    a = np.random.rand(i for i in shape)
    print(a)

def test_2():
    # rand 函数只能传单个参数，不能传 shape
    a = np.random.rand(3, 4)
    print(a)



test_1()