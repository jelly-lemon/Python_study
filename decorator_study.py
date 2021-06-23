#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@property
@staticmethod
@classmethod
"""

class Phone:
    # 属性默认为类属性（可以给直接被类本身调用）
    num = 1


    def __init__(self):
        self._cost_price = 1999


    """
    使用 @property 属性，修饰方法，可以像属性一样访问
    如果使用property进行修饰后，又在调用的时候，方法后面添加了()，
    那么就会显示错误信息：TypeError: 'int' object is not callable，
    也就是说添加@property 后，这个方法就变成了一个属性，
    如果后面加入了()，那么就是当作函数来调用，而它却不是callable（可调用）的。
    
    作用：某个属性是通过其它属性计算得来的，
    调用 myPhone.sellingPrice 比 myPhone.sellingPrice() 更自然，看起来是成员属性，
    语义上更好理解
    """
    @property
    def sellingPrice(self):
        return self._cost_price * 1.9

    def getBrand(self):
        return "XiaoMi"

    """
    类静态方法
    【易错点】类静态方法不能有 self 参数
    staticmethod第一个参数不需要传入cls或self，故staticmethod中是无法访问类和对象的数据的。
    """
    @staticmethod
    def getCEO():
        return "LeiJun"


    """
    classmethod的第一个参数为类本身(cls)，正如实例方法的第一个参数为对象本身(self);
    
    特点：可以访问类属性和类方法，staticmethod 就不行
    """
    @classmethod
    def getNum(cls):
        return cls.num



def test_0():
    myPhone = Phone()
    print("price:", myPhone.sellingPrice)
    print("CEO:", Phone.getCEO())

if __name__ == '__main__':
    test_0()