
def test_0():
    """
    第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
    """
    # 返回 map 对象（非 list）
    a = map(float, [1, 0])

    # 转为 list
    print(a)    # <map object at 0x0000024084B5C760>
    print(list(a))  # [1.0, 0.0]



if __name__ == '__main__':
    test_0()