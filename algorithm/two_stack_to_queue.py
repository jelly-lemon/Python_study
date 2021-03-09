"""
用两个栈实现一个队列

思路1：
一个进队栈，一个出队栈
数据进来：往进队栈放。
数据出去：进队栈元素依次出栈，放入出队栈，最后一个元素就是出队的元素。然后出队栈弹出所有元素，压入原来的入队栈。

入队列时间复杂度：O(1)
出队列时间复杂度：O(n)
空间复杂度：O(1)
"""


class Queue_1():
    """
    用两个栈实现一个队列，思路 1 的实现
    """
    in_stack = []   # 用列表模拟栈
    out_stack = []

    def pop(self):
        """
        队首元素出队

        :return: 队首元素
        """
        # 进队栈数据转移到出队栈
        while len(self.in_stack) > 1:
            self.out_stack.append(self.in_stack.pop())

        # 得到栈底元素，也就是该出队列的元素
        if len(self.in_stack) == 0:
            raise IndexError("队列中没有元素")
        else:
            pop_value = self.in_stack.pop()

        # 出队栈数据转移回去
        while len(self.out_stack) > 0:
            self.in_stack.append(self.out_stack.pop())

        return pop_value

    def append(self, value):
        """
        队尾追加元素
        """
        self.in_stack.append(value)

    def show(self):
        """
        打印队列
        """
        print(self.in_stack)


def test_1():
    """
    测试 Queue_1
    """
    q = Queue_1()
    q.append(7)
    q.append(6)
    q.append(4)
    q.append(3)
    q.show()
    print("出队列：", q.pop())
    q.show()
    print("出队列：", q.pop())
    q.show()
    q.append(9)
    print("入队列：", 9)
    q.show()




if __name__ == '__main__':
    test_1()

