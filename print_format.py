import sys
from pprint import pprint


def test_1():
    """
    %格式化

    中文和英文一样，也占一个位置
    """
    print("%-20s%-20s%-20s" % ("姓名", "年龄", "职业"))  # 一个汉字和英文字母一样占一个位置，不是两个
    print("%-20s%-20s%-20s" % ("name", "year", "job"))
    print("%-20s%-20s%-20s" % ("Linmeng", "24", "Engineer"))

    # 中文没法和英文对齐
    print("|%-20s|" % "数据集")
    print("|%-20s|" % "----")

def test_2():
    """
    format 格式化
    """
    # 格式化时记得加冒号
    print("{:.2f} hello {}".format(1, "world"))

def test_3():
    """
    pretty printer

    用于打印复杂的数据结构对象，例如多层嵌套的列表、元组和字典等。
    使用 pprint 模块的 pprint() 替代 print()，可以解决如下痛点：
    设置合适的行宽度，适当的换行
    设置打印的缩进、层级，进行格式化打印
    判断对象中是否有无限循环，并优化打印内容
    """
    pprint(str("hello"))


def test_4():
    """
    退格
    """
    # 输出换行后，就无法对上一行进行退格
    print("hello\b\b", "world")
    print("\b\b")


def test_5():
    """
    sys.stdout 是原始输出，print 是经过封装的输出函数
    """
    sys.stdout.write("hello")
    sys.stdout.write("world")


if __name__ == '__main__':
    test_2()
