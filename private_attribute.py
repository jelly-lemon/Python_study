"""
类私有、公开属性
"""


class Human:
    # 静态变量
    live = "有理想"  # 类公开属性
    # 经过我的测试，不管是 _ 还是 __ 都表示私有
    __desires = "有欲望"  # （程序级别）类私有属性
    _desires = "有欲望"  # （开发者之间的约定俗称，语义上的）类私有的属性

    def __init__(self, name, age, gender, hobby):
        # 在函数里面，self 开头的属性都是成员属性
        self.name = name
        self.age = age
        self.gender = gender
        self.__hobby = hobby  # 对象的私有属性

    def printHobby(self):
        print(self.__hobby)

    def printDesires(self):
        print(self.__desires)

    def __abc(self):
        """
        私有方法
        """
        print("is abc")


if __name__ == '__main__':
    human = Human("beauty", 28, "male", "woman")
    print(human.name)
    print(Human.live)
    Human.live = "无脑"
    print(Human.live)
