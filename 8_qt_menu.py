import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QMainWindow, QMenuBar


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint &
                            ~Qt.WindowMinimizeButtonHint & Qt.FramelessWindowHint)


        self.setContentsMargins(0, 0, 0, 0)

        menubar = QMenuBar()
        self.setMenuBar(menubar)
        menubar.setStyleSheet("font-size:18px;")

        #
        # 一级菜单
        #
        management_menu = menubar.addMenu("管理(&F)")
        management_menu.addMenu("1")
        management_menu.addAction("2")

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())