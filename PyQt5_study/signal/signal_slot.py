"""
信号与槽函数
"""


from PyQt5.QtCore import QObject, pyqtSignal


# 定义一个信号类(需继承自 QObject)
class MySignal(QObject):
    # 定义一个信号，一个信号可以定义任意多个参数
    # 【重点】必须是类静态变量
    sig = pyqtSignal(str, int)

    # 为了方便，我自己编写了一个信号绑定函数，就不用 MySignal.sig.emit 这么写了，不然看起来很臃肿
    def emit(self, s, n):
        self.sig.emit(s, n)  # 通过 run 方法来发出 message 信息 hello PyQt5

    def connect(self, f):
        self.sig.connect(f)


def func(msg, number):
    """
    一个普通函数
    """
    print("func：", msg, number)

if __name__ == "__main__":
    mySig = MySignal()
    mySig.connect(func) # 将信号与指定函数绑定
    mySig.emit("hello", 123)    # 发送信号，传值给绑定函数并执行
