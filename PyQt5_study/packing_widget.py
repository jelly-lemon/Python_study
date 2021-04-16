"""
包装其它窗口
"""
import sys

from PyQt5.QtWidgets import QWidget, QFileDialog, QFormLayout, QLabel, QVBoxLayout, QApplication


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(QLabel("MyWidget"))
        vbox_layout.addWidget(QFileDialog())
        self.setLayout(vbox_layout)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    myWidget = MyWidget()

    sys.exit(app.exec_())


