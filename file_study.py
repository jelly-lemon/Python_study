
import shutil
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

    # ./0519/test hello
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

def test_6():
    """
    按行读取文件
    """
    with open("file_study.py", encoding="utf-8") as file:

        s = file.readline()
        while s != "":
            print(s)
            s = file.readline()

def test_7():
    """
    拷贝文件
    """
    r = shutil.copy("./file_study.py", "./img")
    print(r)

def test_8():
    """
    获取目录下所有文件名

    输出：
    ./img
    []
    ['head.jpg', 'logo.png', 'xiaoniu.jpg']
    """
    for root, dirs, files in os.walk("./img"):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有文件


if __name__ == '__main__':
    test_8()