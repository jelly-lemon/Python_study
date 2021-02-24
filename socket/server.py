"""
socket 服务端
"""


import socket

s = socket.socket() # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345    # 设置端口
s.bind((host, port))

print("server %s:%s" % (host, port))

s.listen(5) # 运行的连接数
while True:
    c, addr = s.accept()    # 建立客户端连接
    print("连接地址：%s" % str(addr))
    c.send(bytes("欢迎访问服务端！".encode("utf-8")))
    c.close()