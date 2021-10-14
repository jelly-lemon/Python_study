

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
    n = 3/2
    print(n)
    n = int(3/2)    # 向下取整
    print(n)

def test_2():
    """
    for 循环
    """
    for i in range(10):
        print(i)

if __name__ == '__main__':
    test_2()