#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
字符串、字节串互转
"""

def test_0():
    """
    str 与 bytes 类型
    """
    s = "你好"
    print(type(s))

    b = s.encode("utf-8")
    print(type(b))


if __name__ == '__main__':
    test_0()
