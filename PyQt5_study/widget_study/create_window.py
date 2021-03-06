"""
创建一个窗口并显示
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    # 创建一个应用程序对象
    # sys.argv 是一个列表，从命令行输入（跟在该文件名后面的那个参数？）
    app = QApplication(sys.argv)    # 创建应用对象

    # QWidget部件是 PyQt5 所有用户界面对象的基类
    w = QWidget()   # 创建一个控件
    w.resize(250, 150)  # 调整窗口大小
    w.move(300, 300)  # 移动窗口到指定位置
    w.setWindowTitle("Simple")
    w.show()  # 显示本窗口

    # 系统的 exit() 方法确保应用程序干净的退出（什么叫干净的退出？）
    # app.exec_()方法有下划线，是因为 exec 是 Python 关键字，不能用，因此用 exec_ 替代
    # 执行 app.exec_() 就会进入事件循环，直到关闭应用我们创建的 QT 应用程序，关闭时返回一个状态码
    # 要是我不用这个 sys.exit() 会有什么后果呢？（经过测试，感觉没有不同）
    sys.exit(app.exec_())    # 应用对象进入事件循环

