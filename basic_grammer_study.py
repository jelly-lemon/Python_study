def test_0():
    """
    单行 if-else 结构，如果不成立，返回 else 的结果
    """
    isPrint = False
    print("yes" if isPrint else "no")


def test_1():
    """
    整数相除，得到浮点数
    """
    n = 3 / 2
    print(n)
    n = int(3 / 2)  # 向下取整
    print(n)


def test_2():
    """
    for 循环
    """
    for i in range(10):
        print(i)


def test_3():
    """
    分子为 0
    """
    f1 = 0 / 3
    print(f1) # 0.0


def test_4():
    """
    同步遍历两个数组：zip
    如果两者长度不等，到最短长度结束
    """
    d1 = [1, 2, 3, 4, 5]
    d2 = ['a', 'b', 'c', 'd']
    for n1, n2 in zip(d1, d2):
        print(n1, n2)

def test_5():
    """
    判断相等
    """
    if 1. == 1:
        print("yes")


if __name__ == '__main__':
    test_5()
