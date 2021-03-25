# encoding=utf-8


def test_1():
    s = u"绿盟%code%"

    if s.find(u"code") != -1:
        print "yes"


def test_2():
    s = '''{"name": "unknown"}'''
    print s

def test_3():
    print("hello" + "world")

if __name__ == '__main__':
    test_3()