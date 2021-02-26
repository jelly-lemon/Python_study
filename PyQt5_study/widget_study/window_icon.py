"""
设置窗口的图标

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)    # 窗口起点和大小
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon('../../img/logo.png'))

        self.show()

if __name__ == '__main__':
    #创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()

    # 从代码来看，这个 ex 组件和 app 毫无关联
    # 组件里面调用了 show 这个函数
    sys.exit(app.exec_())