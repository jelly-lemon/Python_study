"""
学习设置 QMainWindow 的布局

QMainWindow 自带一个 layout，所以不能再用 setLayout
（我就把 QMainWindow 自带的 layout 叫做 MainWindowLayout）
"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QVBoxLayout, QMainWindow)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        # 控件
        title_label = QLabel('Title')

        # 布局对象（这些对象都是局部对象，为什么执行完该函数之后还存在？或者说，界面上还有？）
        v_layout = QVBoxLayout()
        v_layout.addWidget(title_label)  # 往布局里添加控件

        main_widget = QWidget()
        main_widget.setLayout(v_layout)

        self.setCentralWidget(main_widget)  # 设置 MainWindow 的中央空间
        self.setWindowTitle('Review')

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 初始化应用
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
