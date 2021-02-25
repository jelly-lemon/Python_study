import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QVBoxLayout, QMainWindow)

class Example(QMainWindow):

    def __init__(self):
        super().__init__()


        self.setWindowTitle('Review')
        # self.setWindowFlags(self.windowFlags())

        self.show()
        self.hide()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

