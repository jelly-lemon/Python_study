"""
print() 函数是可抢占资源，现在来加一个互斥锁，实现线程同步
抢占的具体现象：上一个 print 还没输出完，就接着输出下一个 print

我的测试(测试抢占情况)：print() 内容比较短时，内容倒是不会被打断，但是跟着的换行就被挤在了后面
加锁之后：就没有出现挤掉换行的情况了

mutex.acquire() 默认阻塞等待
"""
from threading import Thread, Lock
from time import sleep

mutex = Lock()
def t1():
    while True:
        mutex.acquire() # 阻塞等待
        print("t1:aaaaaaaaaa")
        mutex.release()
        sleep(0.5)

def t2():
    while True:
        mutex.acquire()
        print("t2:bbbbbbbbbb")
        mutex.release()
        sleep(0.5)

def t3():
    while True:
        mutex.acquire()
        print("t3:cccccccccc")
        mutex.release()
        sleep(0.5)

if __name__ == '__main__':

    t_1 = Thread(target=t1)
    t_1.start()

    t_2 = Thread(target=t2)
    t_2.start()

    t_3 = Thread(target=t3)
    t_3.start()