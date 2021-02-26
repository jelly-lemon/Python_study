"""
设置 QWidget 的布局

为什么 QWidget 的 show 效果和 QMainWindow 的 show 效果是一样的？
个人猜测：QT 框架会判断 show 的是不是 QMainWindow，如果不是，会套一个 Window 吧

"""
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QVBoxLayout)

# 注意继承自 QWidget
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        v_layout = QVBoxLayout()
        v_layout.addWidget(title)

        self.setLayout(v_layout)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())