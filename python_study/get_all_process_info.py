import time

import psutil
from psutil import NoSuchProcess


def get_proc_by_id(pid):
    return psutil.Process(pid)


def get_proc_by_name(pname):
    """ get process by name

    return the first process if there are more than one
    """
    for proc in psutil.process_iter():
        try:
            if proc.name().lower() == pname.lower():
                return proc  # return if found one
                # print(proc)
        except psutil.AccessDenied:
            pass
        except psutil.NoSuchProcess:
            pass
    return None

def getProcessInfo(p):
    """取出指定进程占用的进程名，进程ID，进程实际内存, 虚拟内存,CPU使用率
    """
    try:
        cpu = int(p.cpu_percent(interval=0))
        # rss, vms = p.memory_info()
        mem = p.memory_info()
        name = p.name
        pid = p.pid

    except NoSuchProcess as e:
        name = "Closed_Process"
        pid = 0
        # rss = 0
        # vms = 0
        mem = 0
        cpu = 0
    print([name, pid, mem, cpu])

def getAllProcessInfo():
    """取出全部进程的进程名，进程ID，进程实际内存, 虚拟内存,CPU使用率
    """
    instances = []
    all_processes = list(psutil.process_iter())
    for proc in all_processes:
        # proc.get_cpu_percent(interval=0)
        proc.cpu_percent(interval=0)
    #此处sleep1秒是取正确取出CPU使用率的重点
    time.sleep(1)
    for proc in all_processes:
        getProcessInfo(proc)
        # instances.append(getProcessInfo(proc))
        # print(proc)
    # return instances

if '__main__' == __name__:
    # p = get_proc_by_name("msedge.exe")
    # print(get_proc_by_id(4364))

    getAllProcessInfo()
