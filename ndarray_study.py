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

if __name__ == '__main__':
    test_0()
