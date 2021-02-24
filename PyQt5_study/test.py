import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget, \
    QPushButton, QListWidget, QListWidgetItem


class RelaxWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        list_widget = QListWidget()
        for dir in ["test1", "test2"]:
            dir_label = QLabel(dir)
            delete_btn = QPushButton("删除")

            dir_line_layout = QHBoxLayout()
            dir_line_layout.addWidget(dir_label)
            dir_line_layout.addWidget(delete_btn)
            dir_delete_widget = QWidget()
            dir_delete_widget.setLayout(dir_line_layout)

            item = QListWidgetItem()
            list_widget.addItem(item)
            list_widget.setItemWidget(item, dir_delete_widget)

        self.setCentralWidget(list_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    relaxWindow = RelaxWindow()
    relaxWindow.show()
    sys.exit(app.exec_())