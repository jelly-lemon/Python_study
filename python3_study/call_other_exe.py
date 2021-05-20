
def test_0():
    """
    异步调用外部程序（就是函数调用外部程序之后就立刻返回）

    p.poll()：检查程序是否结束
    p.wait()：等待程序结束

    # 几种不同的写法
    # subprocess.Popen("\"C:\\Program Files (x86)\\Notepad++\\notepad++.exe\" hello.txt")
    # subprocess.Popen("\"C:/Program Files (x86)/Notepad++/notepad++.exe\" hello.txt") # 斜线也可以
    # subprocess.Popen("hello.txt") # 以默认程序打开文件
    """
    import subprocess

    player = "C:/Program Files (x86)/Notepad++/notepad++.exe"
    file_path = "D:/0-0-pycharm/Python_study/python3_study/test_txt/a b.txt"
    p = subprocess.Popen('"%s" "%s"' % (player, file_path)) # 相当于在 cmd 中执行

def test_1():
    """
    同步调用外部程序
    """
    import os

    # 方法 1
    # 这种方法只能执行外部程序，无法获得返回值
    res = os.system("help") # 调用正常返回 1
    print(res)

    # 方法 2，管道通信
    res = os.popen("help")
    print(res.read())


if __name__ == '__main__':
    test_1()