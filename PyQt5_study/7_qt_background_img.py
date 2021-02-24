import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

app = QApplication(sys.argv)
win = QMainWindow()

#设置窗口标题与初始大小
win.setWindowTitle("界面背景图片设置")
win.resize(350, 250)
#设置对象名称
win.setObjectName("MainWindow")

# 设置窗口背景图片
win.setStyleSheet("#MainWindow{border-image:url(./img/xiaoniu.jpg);}")


win.show()
sys.exit(app.exec_())