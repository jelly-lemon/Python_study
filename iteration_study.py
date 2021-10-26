

def test_0():
    """
    遍历列表
    """
    # 方法 1
    names = ["zhang", "li", "wang"]
    for i in range(len(names)):
        print(names[i])

    # 方法 2
    it = iter(names)
    while 1:
        e = next(it, None)
        if e:
            print(e)
        else:
            break


if __name__ == '__main__':
    test_0()