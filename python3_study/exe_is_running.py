"""
判断某个 psutil_study 程序是否在运行

判断的 exe 程序名字只能是文件名，不能是路径
如：
msedge.exe   (√)
C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe  (×)

"""
# 使用psutil来判断
import psutil
def proc_exist(process_name):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == process_name:
            return pid
# exe_name = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
exe_name = 'msedge.exe'
if isinstance(proc_exist(exe_name), int):
    print("%s 正在运行" % exe_name)
else:
    print('%s 没有运行' % exe_name)