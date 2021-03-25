# encoding:utf-8
import json



def test_1():
    """
    字典转 JSON 字符串
    """
    d = {u"name": u"绿盟"}
    d = json.dumps(d)   # 返回字符串
    print d

def test_2():
    """
    遍历字典
    """
    d = {u"name": u"绿盟"}
    for k, v in d.items():
        print type(v)

def test_3():
    """
    JSON 字符串转字典
    """
    s = '''{"code": "\\u3010\\u7eff\\u76df\\u79d1\\u6280\\u3011\\u9a8c\\u8bc1\\u78015769"}'''
    d = json.loads(s)
    print d
    print d["code"]


if __name__ == '__main__':
    test_3()