"""
获取文件所在目录
"""
import os


def test_0():
    """
    获取文件所在目录
    """
    file_dir = os.path.dirname("C:\\hello\\test.txt")
    print(file_dir)


def test_1():
    """
    获取文件名：带后缀和不带后缀
    """
    file_path = "C:\\hello\\test.txt"
    file_dir, file_name = os.path.split(file_path)
    file_name_without_suffix, file_extension = os.path.splitext(file_name)
    print(file_name_without_suffix)
    print(file_extension)


if __name__ == '__main__':
    test_1()
