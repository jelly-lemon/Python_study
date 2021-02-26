"""
获取磁盘忙碌比，就是带宽利用率，怎么计算的？

猜测：1s 时间内读写数据量/ 1s 内最大读写数据量
1s 内最大读写数量和具体的物理磁盘有关，只能说有一个参考值，不会有一个确定的指
和具体设备相关

忙碌率（个人猜测）：
1s 内读时间+写时间 / 1s

read_time=11312，假如是 ms 的话，换成秒也有 1.1s啊，这个读取时间是如何统计的？
"""
import psutil
from psutil._compat import xrange

# n_c = tuple(psutil.disk_io_counters())
# n_c = [(100.0 * n_c[i + 1])/ n_c[i] for i in xrange(0, len(n_c), 2)]
# print(n_c)

print(psutil.disk_io_counters(perdisk=True))