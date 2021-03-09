"""
找出给定数组中第 k 大的数

思路 1：
选第一个数作为中轴，进行 1 次快速基排序，中轴的位置就是最终位置，不会再变化。
将 k 与中轴位置进行比较：
若 k < 中轴位置，则继续对前半部分进行快速基排序；
若 k == 中轴位置，那就找到了第 k 大的数字了；
若 k > 中轴位置，对后半部分进行快速基排序；

时间复杂度：
    最坏情况下：数组已经是升序数组，那么要进行 O(n) 次快速基排序。所以最坏时间复杂度为 O(n)
    最好情况下：
    平均情况下：

空间复杂度：O(1)

"""

def quick_base_sort(data):
    """
    快速基排序

    TODO 一次快速基排序的时间复杂度为多少呢？基操作是什么？

    :param data: 数组
    :return: 中轴元素最后位置
    """
    if data is None or len(data) == 0 or len(data) == 1:
        return 0

    center_index = 0  # 选第一个元素作为中轴元素
    low = 1
    high = len(data)-1
    while low < high:
        while data[high] >= data[center_index]:
            high -= 1
            if low > high:
                break
        if low > high:
            break
        t = data[center_index]
        data[center_index] = data[high]
        data[high] = t
        center_index = high
        while data[low] <= data[center_index]:
            low += 1
            if low > high:
                break
        if low > high:
            break
        t = data[center_index]
        data[center_index] = data[low]
        data[low] = t
        center_index = low

    return center_index

def find_top_1(data, k):
    """
    查找第 k 大的数（递归）

    :param data: 数组
    :param k: 第几大
    :return: 第 k 大的数
    """
    if len(data) < k:
        return None

    # 快速基排序，得到中轴位置
    center_index = quick_base_sort(data)
    print(data, "k=%d, center=%d" % (k, center_index+1))

    # 中轴元素最终位置恰好等于 k，说明该中轴元素就是第 k 大
    if k == center_index+1:
        return data[center_index]

    # 中轴位置大于 k，说明第 k 大在左边
    if k < center_index+1:
        return find_top_1(data[:center_index], k)

    # 中轴位置小于 k，说明第 k 大在右边
    if k > center_index+1:
        # k 值要更新为 k - center_index - 1
        # 因为传递进去的是数组右部分切片，k 代表右部分相里面第几大
        # 数组左部分都是比中轴元素小的元素，把左部分去掉
        return find_top_1(data[center_index+1:], k-center_index-1) # 难点

def find_top_2(data, k):
    """
    查找第 k 大的数（循环实现）
    """
    if len(data) < k:
        return None

    # 快速基排序，得到中轴位置
    center_index = quick_base_sort(data)
    print(data, "k=%d, center=%d" % (k, center_index+1))

    while True:
        if k < center_index + 1:
            data = data[:center_index]
            center_index = quick_base_sort(data)
            print(data, "k=%d, center=%d" % (k, center_index + 1))

        # 中轴元素最终位置恰好等于 k，说明该中轴元素就是第 k 大
        if k == center_index + 1:
            return data[center_index]

        if k > center_index + 1:
            # 难点
            data = data[center_index+1:]
            k = k - center_index - 1    # k 更新为相对位置
            center_index = quick_base_sort(data)
            print(data, "k=%d, center=%d" % (k, center_index + 1))

        if k == center_index + 1:
            return data[center_index]





if __name__ == '__main__':
    data_a = [5, 1, 3, 4, 6, 2, 8, 9]

    print("---------------------------")
    k = 2
    top_k = find_top_1(data_a.copy(), k)
    print("top %d is %d" % (k, top_k))

    print("---------------------------")
    k = 3
    top_k = find_top_2(data_a.copy(), k)
    print("top %d is %d" % (k, top_k))

    print("---------------------------")
    k = 4
    top_k = find_top_2(data_a.copy(), k)
    print("top %d is %d" % (k, top_k))

    print("---------------------------")
    k = 1
    top_k = find_top_2(data_a.copy(), k)
    print("top %d is %d" % (k, top_k))


