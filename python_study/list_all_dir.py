# encoding=utf-8
import os

def list_dir_1(dir):
    """
    打印出指定目录下的所有文件夹

    :param dir: 目录
    """
    dir_name = []
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isdir(path):
            dir_name.append(path)
            print(path)


if __name__ == '__main__':
    list_dir_1("./")
    