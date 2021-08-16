"""
星号表达式
"""


def add(a, b):
    print(a + b)


def test_0():
    """
    * 星号表达式的使用：解压的意思
    """
    a = [13, 12.0]

    add(*a)


if __name__ == '__main__':
    test_0()