import copy


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
    print(n)  # 1.5
    n = int(3 / 2)  # 向下取整，1
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
    print(f1)  # 0.0


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
    浮点数和整数判断相等，只要值相等就是 true
    """
    if 1. == 1:
        print("yes")


def test_6():
    """
    引用元素
    """
    # 把列表中的子列表赋值给某个变量，实际上是引用
    d1 = [[1, 2, 3], ['a', 'b', 'c']]
    d2 = d1[0]
    d2[0] = 'x'
    print(d1)  # [['x', 2, 3], ['a', 'b', 'c']]

    # 即使把子列表放到其它列表中，也是引用
    print()
    d1 = [[1, 2, 3], ['a', 'b', 'c']]
    d2 = [d1[0], d1[1]]
    d2[0][0] = 'a'
    print(d1)  # [['a', 2, 3], ['a', 'b', 'c']]

    # 浅拷贝，里面仍然是引用
    print()
    d1 = [[1, 2, 3], ['a', 'b', 'c']]
    d2 = copy.copy(d1)  # 或 d1.copy()，只拷贝了地址
    d2[0][0] = 'a'
    print(d1)  # [['a', 2, 3], ['a', 'b', 'c']]
    d2.clear()  # d2 clear 不影响 d1（前提是拷贝，如果是引用，d1 就会被清空）
    print(d1)  # [['a', 2, 3], ['a', 'b', 'c']]

    # 深拷贝
    print()
    d1 = [[1, 2, 3], ['a', 'b', 'c']]
    d2 = copy.deepcopy(d1)
    d2[0][0] = 'a'
    print(d1)  # [[1, 2, 3], ['a', 'b', 'c']]


if __name__ == '__main__':
    test_6()
