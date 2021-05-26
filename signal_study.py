"""
进程可以无视信号，可以采取默认操作，还可以自定义操作
【注意】
signal 包主要是针对 UNIX 平台(比如Linux, MAC OS)，
而Windows内核中由于对信号机制的支持不充分，
所以在Windows上的Python不能发挥信号系统的功能。
"""