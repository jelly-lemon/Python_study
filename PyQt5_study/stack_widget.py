"""
堆栈式界面显示
"""


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QStackedWidget, QMainWindow, QMenuBar, QLabel
import sys

class MainWindow(QMainWindow):
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

        self.stackedWidget = QStackedWidget()
        self.Layout.addWidget(self.stackedWidget)

        self.label1 = QLabel()
        self.label1.setText("label1")

        self.label2 = QLabel()
        self.label2.setText("label2")

        self.stackedWidget.addAction(self.label1)
        self.stackedWidget.addAction(self.label2)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


