import matplotlib.pyplot as plt


def test_0():
    """
    在子图中添加表格
    """
    plt.rcParams['font.family'] = 'simhei'
    fig, axes = plt.subplots(1, 2)

    # 表格数据
    data = [[1, 1], [1, 1]]

    # 默认表格样式
    axes[0].table(data)
    # 隐藏x轴刻度，以防遮盖表格
    axes[0].set_xticks([])
    axes[0].set_title("默认样式")
    axes[0].plot([1,2,3,4], [3,4,1,2])

    # 演示表格参数
    axes[1].table(cellText=data, cellColours=[['grey', 'grey'], ['grey', 'red']], cellLoc='center', colWidths=[0.1, 0.1],
                  rowLabels=['a', 'b'], rowColours=['blue', 'blue'], rowLoc='center', colLabels=['A', 'B'],
                  colColours=['green', 'green'], colLoc='left', loc='bottom right', bbox=None, edges='closed')
    # 隐藏x轴刻度，以防遮盖表格
    axes[1].set_xticks([])
    axes[1].set_title("自定义样式")

    plt.show()


if __name__ == '__main__':
    test_0()