"""
条状图
"""
from math import log

from matplotlib import pyplot as plt


def test_0():
    """
    折线图
    """
    x = [1,2,3,4,5,6,7]
    y = [0.5,0.6,0.7,0.8,0.9,0.8,0.7]
    plt.plot(x, y)
    plt.show()

def test_1():
    """
    画函数 1/(IR*log2IR)
    """
    x = [i for i in range(2, 200)]
    y = [1/(IR*log(IR, 2)) for IR in x]
    print(x)
    print(y)
    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    test_1()