import numpy as np

def test_0():
    """
    rand，用于生成随机数组
    随机样本取值范围是[0,1)
    """
    # 生成长度为 4 的 1 维数组
    arr = np.random.rand(4)
    print(arr)

    print("arr * 2:")
    print(arr * 2)

    # 生成 3x4 的二维数组
    arr1 = np.random.rand(3, 4)
    print(arr1)


if __name__ == '__main__':
    test_0()
