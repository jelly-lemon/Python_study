import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow
from PyQt5.QtCore import QCoreApplication


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())