"""
获取指定进程的 cpu 占用率

获取 cpu 占用率：psutil.cpu_percent()
计算占用率，分母是一段时间，所以 cpu_percent 是计算的一段时间内的
"""

import time
import psutil

def test_0():
    """
    获取进程信息（信息是一个对象）
    """
    exe_name = "msedge.exe"
    proc_list = []
    for proc in psutil.process_iter():
        if proc.name().lower() == exe_name.lower():
            proc_list.append(proc)
    print(proc_list)

def test_1():
    """
    获取某个程序的 cpu 使用率
    """
    exe_name = "msedge.exe"

    while True:
        all_cpu_per = 0
        for proc in psutil.process_iter():
            if proc.name().lower() == exe_name.lower():
                try:
                    # 如果该进程是多线程，cpu_percent 返回值可能 > 100，返回值是每个逻辑核占用率的累加值
                    # cpu_percent()：如果 interval=0 的话，第一次调用立即返回 0，第二次调用返回距离第一次调用这段时间内的 cpu 占用率
                    all_cpu_per += proc.cpu_percent(interval=0)
                except Exception as e:
                    print(e)
        print(all_cpu_per)
        time.sleep(1)

def test_2():
    """
    获取 CPU 利用率
    """
    while True:
        cpu_percent = psutil.cpu_percent(1)
        print(cpu_percent)
        time.sleep(1)




if '__main__' == __name__:
    test_2()

