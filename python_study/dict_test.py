

def test_1():
    """
    是否可以 a[1] = 1 创建键值对？√
    """
    a = {}

    a["a"] = "abc"
    a[2] = 2222
    a[1] = 1111

    a[1] -= 1
    # 如果 a 是字典，则 a[1] 表示 1 为 key 值，不是数组下标的意思
    print(a[1])

def test_2():
    """
    字典按 value 排序
    """
    # 声明字典
    key_value = {}

    # 初始化
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323


    # print(key_value.items())
    # print("按值(value)排序:")
    # key_value = sorted(key_value.items(), key=lambda item: item[1])
    # print(key_value)
    # print(dict(key_value))




test_2()