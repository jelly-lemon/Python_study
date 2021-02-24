"""
信号与槽函数
"""


from PyQt5.QtCore import QObject, pyqtSignal


# 定义一个信号类
class MyTypesignal(QObject):
    # 定义一个信号
    senmsg = pyqtSignal(object)

    # 编写一个信号相关触发的触发函数
    def run(self):
        self.senmsg.emit("hello PyQT5")  # 通过run方法来发出message信息hello PyQt5


# 定义一个槽函数类
class MySlot(QObject):
    def get(self, msg):
        print("信息：" + msg)

def show(msg):
    print(msg)


if __name__ == "__main__":
    send = MyTypesignal()
    slot = MySlot()

    # # 将信号与槽函数连接
    # send.senmsg.connect(slot.get)
    # send.run()
    #
    # # 将信号与槽函数断开
    # send.senmsg.disconnect(slot.get)
    # send.run()  # 断开之后，发送信号，没人接收

    # connect连接，只要是一个函数就行，不是必须得继承 QObejct
    send.senmsg.connect(show)
    send.run()
