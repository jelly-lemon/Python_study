"""
鼠标事件监听器是一个线程，所有的回调函数都会在独立的线程中运行。

调用pynput.mouse.Listener.stop，发起StopException异常，
或者回调函数中返回False都会停止事件的监听。

有两种方法，一种是函数式、非阻塞型（即本文），另一种是语句式、阻塞型。
"""

from pynput import mouse

def on_move(x, y):
    print("move", x, y)


def on_click(x, y, button, pressed):
    print("{0} at {1}".format("Pressed" if pressed else "Released", (x, y)))


# 为什么滚动鼠标滑轮这个回调函数没有被执行呢？
# 原来是参数 on_scroll 写错成 on_scorll 了
def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))


with mouse.Listener(on_move = on_move,
                    on_click = on_click,
                    on_scroll = on_scroll) as listener:
    listener.join()

print("test")
