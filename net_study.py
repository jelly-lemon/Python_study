# -*- coding: utf-8 -*-
import socket

def test_0():
    """
    获取本机 ip
    """
    # 获取计算机名称
    hostname = socket.gethostname()
    print(hostname)
    # 获取本机IP
    ip = socket.gethostbyname(hostname)
    print(ip)

if __name__ == '__main__':
    test_0()


