

def test_0():
    """
    子函数可以直接使用父函数里面的变量
    """
    print(student)


if __name__ == '__main__':
    student = "goodman"

    test_0()