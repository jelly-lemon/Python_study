"""
客户端 socket 练习
"""

import socket

if __name__ == '__main__':
    s = socket.socket()
    host = socket.gethostname()
    port = 12345

    s.connect((host, port)) # 尝试连接（阻塞？）
    print(s.recv(1024).decode("utf-8"))
    s.close()