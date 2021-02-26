"""
菜单栏
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(600, 400)

        menubar = QMenuBar()
        menubar.setStyleSheet("font-size:18px;")

        # 一级菜单
        management_menu = menubar.addMenu("管理(&F)")
        help_menu = menubar.addMenu("帮助")

        # 二级菜单
        create_menu = management_menu.addMenu("创建")
        quit_action = management_menu.addAction("退出")

        phone_action = help_menu.addAction("电话")
        web_action = help_menu.addAction("官网")

        # 三级菜单
        create_fiel_action = create_menu.addAction("文件")
        create_project_action = create_menu.addAction("项目")


        self.setMenuBar(menubar)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())