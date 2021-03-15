"""
socket 客户端
"""

import socket

# 待发送数据
import time

messages = ['This is the message ', 'It will be sent ', 'in parts', ]

# 连接服务端地址
server_address = ('localhost', 8090)

# 创建两个 socket 实例
socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.socket(socket.AF_INET, socket.SOCK_STREAM), ]

# 连接服务器
print('connecting to %s port %s' % server_address)
for s in socks:
    s.connect(server_address)

# 向服务端发送数据，两个 socket 都发一次
for index, message in enumerate(messages):
    for s in socks:
        print('%s: sending "%s"' % (s.getsockname(), message + str(index)))
        s.send(bytes(message + str(index), encoding="utf-8"))

time.sleep(60)

# 接受服务端数据
for s in socks:
    # recv 阻塞运行，读到数据就返回（最多读取1024个字节）
    data = s.recv(1024)
    print('%s: received "%s"' % (s.getsockname(), data))
    print('closing socket', s.getsockname())
    s.close()
