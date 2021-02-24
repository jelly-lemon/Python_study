"""
鼠标放在按钮上，可以显示相关提示
"""

import sys
# 为啥要加小括号？
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 静态方法设置字体
        QToolTip.setFont(QFont('SansSerif', 10))
        # 创建一个提示，字符串可以使用 html（窗口的提示？）
        self.setToolTip('This is a <b>QWidget</b> widget')
        # 创建一个 button，也设置一个提示
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # 既然使用默认尺寸，还有必要设置一下为默认尺寸吗？
        btn.resize(btn.sizeHint())

        btn.move(50,50)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Tooltips")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())