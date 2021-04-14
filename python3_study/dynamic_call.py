"""
python 中的多态

所谓多态，就是可以用指向基类的指针变量来调用子类对象的方法

在 Python 中，一个变量可以存任何对象，你只要知道你的变量将来存的是什么对象，
你就可以直接写调用该对象的方法。语法检查是检查不出来错误的，要真正运行到了这一步，
才可知道是否会出现异常。比如，该对象根本就没有该方法。相比与 C++，Python 中多态就很
简单了。
"""


class Car:
    def printName(self):
        print("Car")


class BMWCar(Car):
    def printName(self):
        print("BMWCar")


def printName(car):
    car.printName()


def test_0():
    car_0 = BMWCar()
    car_1 = Car()
    printName(car_0)
    printName(car_1)


if __name__ == '__main__':
    test_0()
