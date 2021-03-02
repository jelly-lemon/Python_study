"""
遍历显卡列表：
video: Intel(R) HD Graphics 630
"""

import wmi


c = wmi.WMI()
print(c.Win32_Processor())

for cpu in c.Win32_Processor():
    print(cpu)
    print('%s: %d%%' % (cpu.DeviceID, cpu.LoadPercentage))

for gpu in c.Win32_VideoController():
    print(type(gpu))
    print(gpu)

