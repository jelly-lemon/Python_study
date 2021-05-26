import multiprocessing
import time


def worker_0(n):
    """
    进程函数
    """
    while n > 0:
        print("worker_0: The time is {0}".format(time.ctime()))
        time.sleep(1)
        n -= 1


def test_0():
    """
    创建一个进程
    """
    p = multiprocessing.Process(target=worker_0, args=(60,))
    p.start()

    while True:
        print("p_id:", p.pid)
        print("p_name", p.name)
        print("p_isAlive", p.is_alive())
        time.sleep(1)

if __name__ == '__main__':
    test_0()