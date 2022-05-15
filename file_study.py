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

    os.makedirs：即使父目录不存在也可以
    """
    dir = "./0519/abc/test"
    if os.path.exists(dir) is False:
        print(dir, "not exists")
        os.makedirs(dir)
        if os.path.exists(dir):
            print(dir, "create success")
        else:
            print(dir, "create failed")


def test_3():
    """
    提取路径中的目录
    """
    dir = "./0519/test/hello"
    head, tail = os.path.split(dir)

    print(head, tail)   # ./0519/test hello


def test_4():
    """
    打印出指定目录下的所有文件夹
    """
    dir = ".."
    dir_name = []
    for name in os.listdir(dir):    # 列出所有文件夹和文件名
        path = os.path.join(dir, name)
        if os.path.isdir(path):
            dir_name.append(path)
            print(path)


def test_5():
    """
    读取文件全部内容
    """
    # 【易错点】默认打开文件的编码是 GBK
    # 在 text 模式下，如果未指定 encoding，
    # 则通过 locale.getpreferredencoding(False) 获取
    file = open("file_study.py", encoding="utf-8")
    content = file.readlines()  # 读取所有行
    print(content)


def test_6():
    """
    按行读取文件

    with 所求值的对象必须有一个 __enter__() 方法，一个 __exit__() 方法。
    紧跟 with 后面的语句被求值后，对象的 __enter__() 方法被调用，
    这个方法的返回值将被赋值给 as 后面的变量。
    当 with 后面的代码块全部被执行完之后，将调用前面返回对象的 __exit__() 方法
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
        print(root)     # 当前目录路径
        print(dirs)     # 当前路径下所有子目录
        print(files)    # 当前路径下所有文件


if __name__ == '__main__':
    test_2()
