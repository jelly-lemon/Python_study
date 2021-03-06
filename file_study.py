

import os


def test_0():
    """
    判断文件或文件夹是否存在
    """
    # 方法 1
    # 文件或文件夹都可
    if os.path.exists("./file_study.py"):
        print("yes")
    else:
        print("no")

    # 方法 2，直接尝试读取文件，不存在就报异常
    file = open("./hello.txt")


def test_1():
    """
    判断文件是否创建成功
    """
    # 文件打开（创建）成功时返回文件对象，打开（创建）失败时抛出 IOError
    file1 = open("./0519.txt", "w")
    file1.write("hello, 0519")
    file1.close()

def test_2():
    """
    创建多级目录
    """
    dir = "./0519/test"
    if (os.path.exists(dir) is False):
        print(dir, "not exists")
        os.makedirs(dir)
        if (os.path.exists(dir)):
            print(dir, "create success")
        else:
            print(dir, "create failed")

def test_3():
    """
    提取路径中的目录
    """
    dir = "./0519/test/hello"
    head, tail = os.path.split(dir)
    print(head, tail)

def test_4():
    """
    打印出指定目录下的所有文件夹
    """
    dir = ".."
    dir_name = []
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isdir(path):
            dir_name.append(path)
            print(path)

def test_5():
    """
    读取文件全部内容
    """
    # 【易错点】默认打开文件的编码是 GBK
    file = open("file_study.py", encoding="utf-8")
    content = file.readlines()
    print(content)


if __name__ == '__main__':
    test_5()