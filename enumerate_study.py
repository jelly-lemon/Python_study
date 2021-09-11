def test_0():
    """
    zip 封装两个列表，同步取数据

    """
    list1 = [1, 2, 3]
    list2 = ["a", "b", "c"]

    zipped_data = zip(list1, list2)
    for i, (val1, val2) in enumerate(zipped_data):
        print(i, val1, val2)


if __name__ == '__main__':
    test_0()
