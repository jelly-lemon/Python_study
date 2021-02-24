"""
学习设置 QMainWindow 的布局

QMainWindow 自带一个 layout（具体是什么呢？），(不能再用 setLayout ?)

第一步：
创建一个QWidget实例，并将这个实例设置为centralWidget：
QWidget *widget = new QWidget();//也可以是自己定义的一个类。

第二步：
创建一个主布局mainLayout，并把所需要的所有控件都往里面放（工具栏、菜单栏、状态栏除外）：
QHBoxLayout *mainLayout = new QHBoxLayout;
mainLayout->addWidget(...);
mainLayout->addLayout(...);

第三步：
this->setCentralWidget(widget);
"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QVBoxLayout, QMainWindow)

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        # QWidget 带不带 self 的区别（也就是设置 parent 与否的区别？）？
        # 其中参数 parent 指向父窗口，如果这个参数为 0，则窗口就成为一个顶级窗口（什么叫顶级窗口？最前面的窗口？）
        main_widget = QWidget()

        title = QLabel('Title')
        v_layout = QVBoxLayout()
        v_layout.addWidget(title)

        main_widget.setLayout(v_layout)

        self.setCentralWidget(main_widget)
        self.setWindowTitle('Review')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())