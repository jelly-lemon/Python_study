from threading import Thread, Lock
from time import sleep

mutex = Lock()
def t1():
    while True:
        mutex.acquire() # 阻塞等待
        print("t1:aaaaaaaaaa")
        sleep(3)
        mutex.release()

def t2():
    while True:
        mutex.acquire()
        print("t2:bbbbbbbbbb")
        mutex.release()
        sleep(0.5)


if __name__ == '__main__':

    t_1 = Thread(target=t1)
    t_1.start()

    t_2 = Thread(target=t2)
    t_2.start()
