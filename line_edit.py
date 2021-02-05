import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QMainWindow, QMenuBar, QLineEdit


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint &
        #                     ~Qt.WindowMinimizeButtonHint & Qt.FramelessWindowHint)
        #
        #
        # self.setContentsMargins(0, 0, 0, 0)

        self.edit = QLineEdit()
        self.edit.setText("hello")
        self.setCentralWidget(self.edit)

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())