"""
在程序中模拟使用 cmd


# 注意
os.system 是阻塞的，但是如果两次 os.system 打开同一个程序，前一次 os.system 就会立即返回；
如果路径中间有空格，记得把路径用双引号括起来；
os.system 是阻塞的，并且该进程结束，打开的程序也会结束（可以用子线程来打开，这样打开的程序就不会退出）;

使用 os.system 带来的问题：调用两次就会出现两个程序，但正常情况应该是用之前打开的程序来打开新的文件。
（其实不会，只是该应用程序不支持并列在一起。）


# 思路
问：如何判断给的路径是不是一个可执行程序呢？难道要执行一遍吗？
答：可以判断文件是否存在，判断文件后缀是不是 *.exe

# 其它
print 不是线程安全的，会出现抢占的情况，
一个线程正在 print，此时另外一个线程可以抢占，导致上一个线程看起来没有输出
"""

import os
from threading import Thread
from time import sleep

def open_file():
    print("child 1")
    os.system("\"C:\\Program Files (x86)\\Notepad++\\notepad++.exe\" ../test_txt/a.txt")
    print("child 1 end")

    print("child 1.1")
    os.system("\"C:\\Program Files (x86)\\Notepad++\\notepad++.exe\" ../test_txt/b.txt")
    print("child 1.1 end")


def open_file2():
    print("child 2")
    os.system("\"C:\\Program Files (x86)\\Notepad++\\notepad++.exe\" ../test_txt/c.txt")
    print("child 2 end")



if __name__ == '__main__':
    # 路径测试
    # exe 和文件同时加上双引号，就提示不是内部命令，奇怪
    player = "C:/Program Files (x86)/Notepad++/notepad++.exe"
    file_path = "D:/0-0-pycharm/Python_study/python_study/test_txt/a b.txt"
    # cmd = """\"%s\" \"%s\"""" % (player, file_path)
    # print(cmd)
    os.system(player)

    # 多线程测试
    # t = Thread(target=open_file)
    # t.setDaemon(True)
    # t.start()
    #
    # t2 = Thread(target=open_file2)
    # t2.setDaemon(True)
    # t2.start()
    #
    # for i in range(5):
    #     print("main")
    #     sleep(1)
