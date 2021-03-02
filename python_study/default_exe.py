"""
获取 windows 默认程序

注意：
没有接口可以获取某一个文件夹下到底有多少个键值对

在下面内容中提取文件名：
"%ProgramFiles(x86)%\Windows Media Player\wmplayer.exe" /prefetch:6 /Open "%L"
不能以空格作为分割，文件名可能有空格
"""
import os
import winreg

def get_file_name(path):
    # 按 \ 进行分割，得到文件名开头的字串
    for s in path.split('\\'):
        end = s.find(".exe")    # 得到文件名结束下标
        if end != -1:
            # 提取文件名切片
            return s[:end] + ".exe"


if __name__ == '__main__':
    with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"WMP11.AssocFile.MP4\shell\open\command") as key:
        try:
            i = 0
            while True:
                name, value, type = winreg.EnumValue(key, i)
                print("name:", name, "value:", value,  "type:", type)
                i += 1
        except Exception as e:
            print(e)
            print("over")

        print(get_file_name(value))



