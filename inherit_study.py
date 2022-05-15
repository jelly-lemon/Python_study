class Car:
    def __init__(self):
        """
        初始化函数
        """
        self.father = "Fute"
        self._create_time = "2020"  # 私有属性

    def printName(self):
        print("Car")

    def _printCreateTime(self):
        """
        函数前加_ 表示私有函数
        """
        print(self._create_time)

    def print_class_name(self):
        """
        打印类名
        """
        print(self.__class__.__name__)


class BMWCar(Car):
    """
    继承自 Car
    """
    pass


def test_0():
    """
    使用子类对象，调用父类方法
    """
    car_0 = BMWCar()
    car_0.printName()       # 调用父类公开方法
    print(car_0.father)     # 访问父类公开属性


def test_1():
    """
    访问 self.__class__.__name__，是子类的呢还是父类的？
    子类的
    """
    car = BMWCar()
    car.print_class_name()  # BMWCar


if __name__ == '__main__':
    test_1()
