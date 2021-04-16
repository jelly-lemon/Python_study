"""
对话框
"""
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()  # 调用父对象初始化方法

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)    # 设置窗口起点和大小
        self.setWindowTitle('Message box')
        self.show() # 显示窗口

    # 重写父类的方法（覆盖）
    def closeEvent(self, event):
        """
        必须要掉用 event.accept 或 ignore 吗？

        经过测试，如果不主动调用 accept 或者 ignore，默认调用 accept
        :param event:
        :return:
        """
        reply = QMessageBox.question(self, 'Message',
                                     'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # accept 就会关闭
            event.accept()
        else:
            # ignore 忽略本次关闭点击，即不做任何操作
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
