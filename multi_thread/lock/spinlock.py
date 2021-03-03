"""
自旋锁
"""
from threading import Lock, Thread
from time import sleep

mutex = Lock()

def t_1():
    while True:
        while mutex.acquire(blocking=False) is False:
            print("t_1 waiting lock")

        print("t_1")
        mutex.release()
        sleep(0.5)

def t_2():
    while True:
        while mutex.acquire(blocking=False) is False:
            print("t_2 waiting lock")

        print("t_2")
        mutex.release()
        sleep(0.5)
        
if __name__ == '__main__':
    Thread(target=t_1).start()
    Thread(target=t_2).start()
