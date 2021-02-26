"""
在程序中模拟使用 cmd

注意：
如果路径中间有空格，记得把路径用双引号括起来；
os.system 是阻塞的，并且该进程结束，打开的程序也会结束（可以用子线程来打开）

如何判断给的路径是不是一个可执行程序呢？
难道要执行一遍吗？可以判断文件是否存在
"""

import os
from threading import Thread
from time import sleep

def open_file():
    os.system("\"C:\\Program Files (x86)\\Notepad++\\notepad++.exe\" hello.txt")
    print("child finished")


t = Thread(target=open_file)
t.setDaemon(True)
t.start()

for i in range(5):
    print("main")
    sleep(1)
