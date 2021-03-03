"""
测试一下主线程退出，子线程是否会退出
（线线均平等）

结果：
子线程不会因为主线程的结束而结束，整个程序不会结束，子线程继续正常运行。

问：那怎么才能达到“主线程退出，子线程也全部退出”的效果呢？
答：可以设置子线程为守护线程。用 setDaemon 方法

问：子线程 setDaemon 之后，子线程退出了，主线程会怎样？
答：主线程不受影响

问：setDaemon 到底是什么作用呢？
答：设置该线程为守护线程，主线程(启动守护线程的那个线程)与守护线程关联

"""
from threading import Thread
from time import sleep


def func():
    for i in range(5):
        print("child", i)
        sleep(0.5)
    print("child thread finished")


if __name__ == '__main__':
    t = Thread(target=func)
    t.setDaemon(True)
    t.start()

    i = 0
    while True:
        i += 1
        print("main", i)
        sleep(0.5)

    print("main thread finished")