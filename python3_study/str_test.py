# -*- encoding:utf-8 -*-
import json
import sys


def test_1():
    # 多行字符串常量
    print('''sdfaaf
    sdfafsadf
    
      sdfafd
    dasf
    asdf
    ''')
    print('''abc\ndef''')

def test_2():
    # 空串为 False
    if "":
        print("yes")


def test_3():
    # 字符串查找
    s ="abc"
    if s.find("bc") != -1:
        print("yes")

def test_4():
    # 字符串转 dict
    config = '''{"company": "nsfocus", "phone": "%mobile%", "code": "验证码%code%"}'''
    # 方法 1
    # config = json.loads(config)   # json里面的字符串都是 unicode 字符（见http://json.org/）
    # print(config)

    # 方法2
    config = eval(config)
    print(config)

def test_5():
    print("默认编码方式：")
    print(sys.getdefaultencoding())
    print("控制台编码方式：")
    print(sys.stdout.encoding)  # 打印stdout的编码方式


def test_6():
    """
    字符串替换
    """
    s = "!@#$!@#$"
    s = s.replace("!", "\!")    # 会替换所有
    print(s)



if __name__ == '__main__':
    test_6()















