import json


def test_1():
    # 多行字符串常量
    print('''sdfaaf
    sdfafsadf
    
    sdfafd
    dasf
    asdf
    ''')

def test_2():
    # 空串为 False
    if "":
        print("yes")


def test_3():
    # 字符串查找
    s ="abc"
    if s.find("bc") != -1:
        print("yes")
        s = s.replace("bc", "aa")
        print(s)

def test_4():
    # 字符串转 dict
    config = '''{"company": "nsfocus", "phone": "%mobile%", "code": "验证码%code%"}'''
    # config = json.loads(config)   # json里面的字符串都是unicode（见http://json.org/）
    # print(config)
    config = eval(config)
    print(config)

def test_5():
    s = u"abc%code%123"
    s = s.replace("%code%", "验证码")
    print(s)


def test_6():
    s1 = u"【nsfocus】有内鬼，停止交易！"
    s1 = s1.encode("GBK")

    s2 = "你好"
    print(s2)

if __name__ == '__main__':
    s = "绿盟科技".encode("UTF-8")

    print(s)
