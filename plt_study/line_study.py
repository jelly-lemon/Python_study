"""
条状图
"""
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

if __name__ == '__main__':
    test_0()