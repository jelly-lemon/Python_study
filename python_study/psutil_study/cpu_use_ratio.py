"""
获取指定进程的 cpu 占用率

获取 cpu 占用率：psutil.cpu_percent()
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
        try:
            if proc.name().lower() == exe_name.lower():
                proc_list.append(proc)
        except Exception as e:
            print(e)
    return proc_list

def get_cpu_percent(exe_name):
    """
    获取某个程序的 cpu 使用率

    :param exe_name:
    :return:
    """
    proc_list = get_proc_by_name(exe_name)
    print(proc_list)
    all_cpu_per = 0
    for proc in proc_list:
        try:
            # cpu_percent 返回每个核的 cpu 使用率，所以总使用率会超过 100
            all_cpu_per += proc.cpu_percent(interval=0)
        except Exception as e:
            print(e)

    return all_cpu_per

if '__main__' == __name__:
    # while True:
    #     print(get_cpu_percent("msedge.exe"))
    #     time.sleep(0.5)

    while True:
        print(psutil.cpu_percent())
        time.sleep(0.5)
