"""
磁盘利用率，指的是使用了多少空间的占比


"""

import psutil
from psutil._common import sdiskpart


def get_disk_usage():
    # TODO 不能利用率直接相加，要改
    total_usage = 0
    diskpart_list = psutil.disk_partitions()
    for disk_part in diskpart_list:
        name = disk_part.device # 盘符
        print(psutil.disk_usage(name))
        total_usage += psutil.disk_usage(name).percent  # 该分区的利用率

    return total_usage

if __name__ == '__main__':
    print(get_disk_usage())
