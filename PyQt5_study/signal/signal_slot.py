"""
信号与槽函数
"""


from PyQt5.QtCore import QObject, pyqtSignal


# 定义一个信号类(需继承自 QObject)
class MySignal(QObject):
    # 定义一个信号
    sig = pyqtSignal(str, int)

    # 编写一个信号相关触发的触发函数
    def emit(self, s, n):
        self.sig.emit(s, n)  # 通过run方法来发出message信息hello PyQt5

    def connect(self, f):
        self.sig.connect(f)

def func(msg, number):
    print("func：", msg, number)

if __name__ == "__main__":
    mySig = MySignal()
    mySig.connect(func)
    mySig.emit("hello", 123)
