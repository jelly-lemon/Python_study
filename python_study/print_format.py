def test_1():
    """
    中文和英文一样，也占一个位置
    """
    print("%-20s%-20s%-20s" % ("姓名", "年龄", "职业"))  # 一个汉字和英文字母一样占一个位置，不是两个
    print("%-20s%-20s%-20s" % ("name", "year", "job"))
    print("%-20s%-20s%-20s" % ("Linmeng", "24", "Engineer"))


def test_2():
    """
    中文没法和英文对齐
    """
    print("|%-20s|" % "数据集")
    print("|%-20s|" % "----")


if __name__ == '__main__':
    test_2()
