"""
简单单元测试
"""
import unittest

def my_abs(n):
    if n < 0:
        return -n
    else:
        return n

# 单元测试类必须继承自 unittest.TestCase 类
class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_my_abs(self):
        rst = my_abs(-10)
        # 第一个参数是期望值，第二个参数是实际值
        self.assertEqual(-10, rst)


if __name__ == '__main__':
    # 运行所有测试用例
    unittest.main()
