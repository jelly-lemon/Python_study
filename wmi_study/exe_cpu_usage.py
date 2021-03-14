import wmi

w = wmi.WMI()
cpu = w.Win32_Processor()[0]    # 默认第一颗 CPU
print("cpu usage", cpu.LoadPercentage)