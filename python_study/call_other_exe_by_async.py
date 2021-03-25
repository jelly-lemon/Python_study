"""
异步调用外部程序（就是函数调用外部程序之后就立刻返回）

不过打开程序没权限，不知道咋解决
p = subprocess.Popen(["\"C:\\Program Files (x86)\\Notepad++\\notepad++.exe\"", 'hello.txt']) # 无权限

笨蛋，搞不懂上面加个 [] 干嘛，用下面这种方法：
player = "C:/Program Files (x86)/Notepad++/notepad++.exe"
file_path = "D:/0-0-pycharm/Python_study/python_study/test_txt/a b.txt"
p = subprocess.Popen('"%s" "%s"' % (player, file_path))

p.poll()：检查程序是否结束
p.wait()：等待程序结束
"""
import os
import subprocess

# 几种不同的写法
# subprocess.Popen("\"C:\\Program Files (x86)\\Notepad++\\notepad++.exe\" hello.txt")
# subprocess.Popen("\"C:/Program Files (x86)/Notepad++/notepad++.exe\" hello.txt") # 斜线也可以
# subprocess.Popen("hello.txt") # 以默认程序打开文件

player = "C:/Program Files (x86)/Notepad++/notepad++.exe"
file_path = "D:/0-0-pycharm/Python_study/python_study/test_txt/a b.txt"
p = subprocess.Popen('"%s" "%s"' % (player, file_path))



