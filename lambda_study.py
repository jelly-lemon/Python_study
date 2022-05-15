"""
lambda 是一种特殊的定义函数的形式，使用它可以定义一个匿名函数
即当你需要一个函数，但又不想费神去命名一个函数，这时候，就可以使用 lambda了

lambda [arg1 [,arg2,.....argn]]:expression
"""


def test_1():
    # x 是入参，x+1 是返回值
    # def g(x):
    # 	return x+1
    g = lambda x: x + 1  # 求 x+1 的和
    r = g(1)
    print("r:", r)
    r = g(2)
    print("r:", r)


if __name__ == '__main__':
    test_1()
