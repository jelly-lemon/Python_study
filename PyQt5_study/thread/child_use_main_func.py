"""
子线程中修改主线程的变量

结论：只要能拿到地址，可以
"""
import sys
from threading import Thread

from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Review')
        self.show()
        self.count = 0

        Thread(target=self.add_count).start()



    def add_count(self):
        print("count", self.count)
        self.count += 1
        print("count", self.count)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

