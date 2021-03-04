"""
socket 服务端
"""

import socket

if __name__ == '__main__':
    s = socket.socket()  # 创建 socket 对象
    host = socket.gethostname()  # 获取本地主机名
    port = 12345  # 设置监听端口
    s.bind((host, port))
    print("server %s:%s" % (host, port))

    s.listen(5)  # 最大监听数量
    while True:
        conn, addr = s.accept()  # 接受连接
        print("客户端地址：%s" % str(addr))
        conn.send("欢迎访问服务端！".encode("utf-8"))  # 向客户端发送数据
        conn.close()  # 关闭连接
