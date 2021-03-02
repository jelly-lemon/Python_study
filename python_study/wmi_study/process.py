"""
获取进程信息

操作比较耗时，要几秒钟
"""

import wmi
c = wmi.WMI()
print(c.Win32_Process(name="msedge.exe"))
for process in c.Win32_Process(name="msedge.exe"):
    print("%5s  %s" % (process.ProcessId, process.Name))
    print(process)

