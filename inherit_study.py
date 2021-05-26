"""
继承父类，私有函数和私有属性会被子类继承吗？
不会。仅继承公开函数和属性
"""

class Car:
    def __init__(self):
        self.father = "Fute"
        self._create_time = "2020"

    def printName(self):
        print("Car")

    def _printCreateTime(self):
        print(self._create_time)


class BMWCar(Car):
    pass


def test_0():
    car_0 = BMWCar()
    car_0.printName()   # 调用父类公开方法
    print(car_0.father) # 访问父类公开属性

if __name__ == '__main__':
    test_0()