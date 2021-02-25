"""
异步调用外部程序

不过打开程序没权限，不知道咋解决

p = subprocess.Popen(["\"C:\\Program Files (x86)\\Notepad++\\notepad++.exe\"", 'hello.txt']) # 无权限



# Check if process has completed
if p.poll() is not None:
    ...


# Wait for process to complete
p.wait()
"""
import os
import subprocess

# subprocess.Popen("\"C:\\Program Files (x86)\\Notepad++\\notepad++.exe\" hello.txt")
# subprocess.Popen("\"C:/Program Files (x86)/Notepad++/notepad++.exe\" hello.txt") # 斜线也可以

subprocess.Popen("hello.txt") # 斜线也可以




