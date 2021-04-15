import sys
from tkinter import BaseWidget

from PyQt5.QtWidgets import QFormLayout, QLineEdit, QDialog, QApplication


def test_0():
    form_layout = QFormLayout()
    passwd_input = QLineEdit()
    passwd_input.setEchoMode(QLineEdit.Password)
    form_layout.addRow("解密口令", passwd_input)

    dialog = QDialog()
    dialog.setLayout(form_layout)

    dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    test_0()

    sys.exit(app.exec_())