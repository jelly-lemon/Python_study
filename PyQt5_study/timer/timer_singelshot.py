"""
只执行一次的 Timer

-----------------------------------
方法1：静态函数
# 调用两次，就会有两个定时器
QTimer.singleShot(1000, myfunc)  # 静态方法
QTimer.singleShot(2000, myfunc)

-----------------------------------
方法2：实例设置 singleShot 为 True
self.timer = QTimer()
self.timer.setSingleShot(True)
self.timer.timeout.connect(myfunc)
self.timer.start(1000)

即使 timer 已经执行完毕了，再次调用 start 还可以再来
"""
from threading import Thread
from PyQt5.QtCore import QTimer
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow




class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Review')

        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.test)

        Thread(target=self.start).start()




    def test(self):
        print("test")

    def start(self):
        print("thread_start")
        self.timer.start(1000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())