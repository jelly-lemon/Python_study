"""
判断文件或文件夹是否存在
"""

import os


# 文件或文件夹都可
if os.path.exists("./file_exist.py"):
    print("yes")
else:
    print("no")