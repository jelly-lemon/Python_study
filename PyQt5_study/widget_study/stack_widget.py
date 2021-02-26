"""
堆栈式界面显示，就像 tab 那样，可以在一个窗口切换显示多个页面
"""
from PyQt5.QtWidgets import QApplication, QStackedWidget, QMainWindow, QMenuBar, QLabel, QAction
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stackedWidget = QStackedWidget()
        self.setLayout()


        self.setCentralWidget(self.stackedWidget)


        self.stackedWidget.addAction(QAction("label1"))
        self.stackedWidget.addAction(QAction("label2"))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


