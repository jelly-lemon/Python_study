

def test_1():
    """
    对元素进行排序，返回排序后元素的下标
    :return:
    """
    a = [3, 4, 1, 7, 2]

    b = sorted(enumerate(a), key=lambda x: x[1])

    c = [x[0] for x in b]

    print(b)
    print(c)

if __name__ == '__main__':
    test_1()