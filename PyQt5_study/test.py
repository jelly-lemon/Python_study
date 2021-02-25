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


        self.setWindowTitle('Review')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())