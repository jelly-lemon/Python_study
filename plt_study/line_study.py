"""
条状图
"""
from math import log

from matplotlib import pyplot as plt

def draw_line(x:list, y:list) -> None:
    """
    折线图
    """
    plt.plot(x, y)
    plt.show()

def draw_some_lines(x:list, y:list) -> None:
    """
    多个折线图位于一个画布内
    """



def test_0():
    """
    画折线图
    """
    x = [1,2,3,4,5,6,7]
    y = [0.5,0.6,0.7,0.8,0.9,0.8,0.7]
    draw_line(x, y)

def test_1():
    """
    画函数 1/(IR*log2IR)
    """
    x = [i for i in range(2, 200)]
    y = [1/(IR*log(IR, 2)) for IR in x]
    print(x)
    print(y)
    draw_line(x, y)

if __name__ == '__main__':
    test_1()