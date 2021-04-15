"""
获取选择的文件
"""
import sys

from PyQt5.QtWidgets import QFileDialog, QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 初始化应用

    # 文件扩展名过滤，用双分号间隔
    file_name, file_type = QFileDialog.getOpenFileName(None, "选取文件", "C:\\", "All Files (*);;Text Files (*.txt)")
    if (file_name == ""):
        print("取消选择")
    else:
        print(file_name)
        print("文件筛选器类型: ", file_type)

    sys.exit(app.exec_())
