"""
模拟双击打开文件。

和双击打开文件一样，非阻塞。

只能用斜线，不能用双反斜线 D:/0-0-pycharm/Python_study/img/head.jpg
"""
import os


def test_0():
    os.startfile("D:/0-0-pycharm/Python_study/img/head.jpg")
    print("1")
    os.startfile("D:/0-0-pycharm/Python_study/img/logo.png")
    print("2")


if __name__ == '__main__':
    test_0()