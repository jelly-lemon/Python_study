"""
将控件移动到屏幕最中央


frameGeometry(): 控件尺寸，相对于父控件？看不懂
geometry of the widget relative to its parent including any window frame

与 geometry() 区别？

"""
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(600, 400)
        self.move_center()

        self.setWindowTitle('Center')
        self.show()

    def move_center(self):
        # 获得屏幕中心点
        center_point = QDesktopWidget().availableGeometry().center()

        # 窗口大小
        window_size = self.geometry()

        # 进行移动
        des_point = (center_point.x()-window_size.width()/2, center_point.y()-window_size.height()/2)
        self.move(des_point[0], des_point[1])




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())