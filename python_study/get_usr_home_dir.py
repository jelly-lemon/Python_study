"""
获取当前用户根目录

其实就是读取系统环境变量
"""
import os

print (os.environ['TEMP'])