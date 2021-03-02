"""
行编辑输入限制
"""
import sys

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.edit = QLineEdit()
        self.edit.setText("hello")
        self.edit.setValidator(QIntValidator(0, 65535))

        self.setCentralWidget(self.edit)

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())