"""
将控件移动到屏幕最中央
"""
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        # 不清楚怎么移动到屏幕中央的
        # 假设只能窗口的左上角位置和窗口大小
        # 那想把窗口位置居中，首先得知道屏幕中心点
        # 从屏幕中心点左上角移动窗口大小一半的距离，就让窗口居中了
        # 这么常用的功能，应该有一个库函数的
        # 获得窗口（什么窗口？我们创建的窗口？）
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心（qr 是个什么东西？一个矩形？）
        qr.moveCenter(cp)
        self.move(qr.topLeft()) # 移动到 qr 的左上角？


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())