"""
遍历显卡列表：

我的电脑显卡：
video: Intel(R) HD Graphics 630
"""

import wmi


c = wmi.WMI()
for gpu in c.Win32_VideoController():
    print(gpu)

