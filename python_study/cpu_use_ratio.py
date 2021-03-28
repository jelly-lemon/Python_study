"""
获取指定进程的 cpu 占用率

获取 cpu 占用率：psutil.cpu_percent()
计算占用率，分母是一段时间，所以 cpu_percent 是计算的一段时间内的

cpu_percent() 如果 interval=0 的话，第一次调用立即返回 0，第二次调用返回距离第一次调用这段时间内的 cpu 占用率
"""

import time
import psutil

def get_proc_by_name(exe_name):
    """
    获取进程信息（信息是一个对象）

    :param exe_name: 进程名
    :return: 进程信息列表
    """
    proc_list = []
    for proc in psutil.process_iter():
        if proc.name().lower() == exe_name.lower():
            proc_list.append(proc)
    return proc_list

def get_cpu_percent(exe_name):
    """
    获取某个程序的 cpu 使用率

    :param exe_name: 进程名
    :return: 该进程 cpu 占用率
    """
    all_cpu_per = 0

    for proc in psutil.process_iter():
        if proc.name().lower() == exe_name.lower():
            try:
                # 如果该进程是多线程，cpu_percent 返回值可能 > 100，返回值是每个逻辑核占用率的累加值
                all_cpu_per += proc.cpu_percent(interval=0)
            except Exception as e:
                print(e)

    return all_cpu_per

if '__main__' == __name__:
    # 获取指定进程的 cpu 占用率
    while True:
        print(get_cpu_percent("msedge.exe"))
        time.sleep(0.5)

    # 获取 cpu 占用率
    # while True:
    #     print(psutil.cpu_percent())
    #     time.sleep(0.5)
