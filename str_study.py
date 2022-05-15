# -*- encoding:utf-8 -*-
import json
import os
import re
import sys


def test_1():
    """
    多行字符串常量，原汁原味输入，换行不用输入转义字符
    注意第二行前面其实有空格
    """
    print('''sdfaaf
    sdfafsadf
    
      sdfafd
    dasf
    asdf
    ''')
    print('''abc\ndef''')


def test_2():
    """
    空串为 False
    """
    if "":
        print("yes")


def test_3():
    """
    字符串查找
    """
    s = "abc"
    if s.find("bc") != -1:
        print("yes")


def test_4():
    """
    字符串转 dict
    """
    config = '''{"company": "nsfocus", "phone": "%mobile%", "code": "验证码%code%"}'''
    # 方法 1
    config = json.loads(config)  # json 里面的字符串都是 unicode 字符
    print(config)

    # 方法2
    config = '''{"company": "nsfocus", "phone": "%mobile%", "code": "验证码%code%"}'''
    config = eval(config)
    print(config)


def test_5():
    """
    控制台乱码问题

    IDLE 是 Python 自带的 IDE
    """
    print("python IDLE default encoding：", sys.getdefaultencoding())
    print("stdout default encoding:", sys.stdout.encoding)  # 打印stdout的编码方式
    print("stderr default encoding:", sys.stderr.encoding)

    print("windows cmd 默认编码方式：")
    os.system("chcp")
    print("执行 C:/abc.exe：")
    os.system("C:/abc.exe")

    print("设置 windows cmd 编码方式：")
    os.system("chcp 65001")  # 设置 windows 编码为 utf-8
    print("windows cmd 默认编码方式：")
    os.system("chcp")
    print("执行 C:/abc.exe：")
    os.system("C:/abc.exe")


def test_6():
    """
    字符串替换
    """
    s = "!@#$!@#$"
    s = s.replace("!", "\!")  # 会替换所有
    print(s)


def test_7():
    """
    打印 list
    """
    name = ['aaa', 'bbb', 'ccc']
    print("my friends:%s" % name)


def test_8():
    """
    split 分割字符串
    """
    s = "hhh./img/hello/world1".split("./img/hello/world")
    print(s)    # ['hhh', '1']

    # 如果匹配的字串刚好在最前，则返回结果会有一个空串
    s = "./img/hello/world1".split("./img/hello/world")
    print(s)    # ['', '1']


def test_9():
    """
    正则表达式
    """
    # 默认从开头匹配，其余位置都不算匹配到，返回 None
    result = re.match("crypto", "crypto.encrypt")
    # 打印匹配到的字符串
    print(result.group(0))  # crypto


def test_10():
    """
    字符串格式化

    如果要输出 %，用 %% 表示，而不是 \%
    """
    s = "%.2f%%, %8.4f" % (1, 2)
    print(s)    # 1.00%,   2.0000

    s = "{},world, {}".format("hello", 1)
    print(s)    # hello,world, 1

if __name__ == '__main__':
    test_10()
