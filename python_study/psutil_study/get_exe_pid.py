"""
获取某个程序的 PID

根据进程号获取某个进程的信息：
psutil.Process(pid)

进程信息如下：
psutil.Process(pid=1008, name='msedge.exe', status='running', started='09:13:46')

"""
import psutil


def get_proc_by_id(pid):
    return psutil.Process(pid)


def get_proc_by_name(pname):
    proc_list = []
    for proc in psutil.process_iter():
        try:
            if proc.name().lower() == pname.lower():
                proc_list.append(proc)
        except Exception as e:
            print(e)
            continue
    return proc_list


if '__main__' == __name__:
    print(get_proc_by_name("msedge.exe"))
    # print(get_proc_by_id(4364))
