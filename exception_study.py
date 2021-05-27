

def test_0():
    """
    try else 结构：没有任何异常就执行 else
    """
    try:
        print("hello")
    except Exception:
        print("exception")
    else:
        print("world")

def test_1():
    """
    捕获异常，打印异常
    """
    try:
        b = 0
        a = 2/b
    except Exception as err:
        print(err)
    # 捕获异常异常，后面语句接着执行
    print("hello")

def test_2():
    """
    主动抛出异常
    """
    raise IOError("can't create file")




if __name__ == '__main__':
    test_1()
