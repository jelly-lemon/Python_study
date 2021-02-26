"""
想在子线程中启动主线程中的 timer

问题：子线程不能 start 主线程的 timer ？

详细描述：主线程创建两个一个 timer 实例，子线程想要启动 timer，但是实验表明无法启动

代码如下：
class Example(QMainWindow):
    def __init__(self):
        ...
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.test)

        Thread(target=self.start).start()

    def test(self):
        print("test")

    def start(self):
        print("thread_start")
        self.timer.start(1000)

start 函数能够正常执行，但是 self.timer.start(1000) 没有任何反应（这是为什么呢？）

摘自 Qt 文档：
In multithreaded applications, you can use QTimer in any thread that has an event loop.
To start an event loop from a non-GUI thread, use QThread::exec().
Qt uses the timer's thread affinity to determine which thread will emit the timeout() signal.
Because of this, you must start and stop the timer in its thread;
it is not possible to start a timer from another thread.

Qt 使用 “计时器的关联线程” 来决定哪个线程发出 timeout() 信号。读不懂

解决办法：用 Qt 提供的 Signal
在主线程中，创建 signal，绑定函数；
在子线程中，调用主线程中的 signal.emit;
"""

from threading import Thread
from time import sleep

from PyQt5.QtCore import QTimer, QObject, pyqtSignal
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MySignal(QObject):
    sig = pyqtSignal()

    def connect(self, func):
        self.sig.connect(func)

    def emit(self):
        self.sig.emit()


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Review')

        self.init_timer()

        self.timer_sig = MySignal()
        self.timer_sig.connect(self.start_timer)

        Thread(target=self.listen_mouse).start()

    def init_timer(self):
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.test)

    def listen_mouse(self):
        while True:
            self.timer_sig.emit()
            sleep(1)

    def test(self):
        print("test")

    def start_timer(self):
        self.timer.start(500)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
