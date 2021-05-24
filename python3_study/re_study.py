"""
正则表达式
"""

import re

def test_0():
    """
    判断字符串是否包含数字
    """
    s = "abc123def2hi3"
    # + 号代表前面的字符必须至少出现一次（1次或多次）。
    # * 号代表前面的字符可以不出现，也可以出现一次或者多次（0次、或1次、或多次）。
    # ? 问号代表前面的字符最多只可以出现一次（0次、或1次）
    pattern = re.compile("[0-9]+")
    match = pattern.findall(s)  # 列表形式返回找到符合规则的所有子串
    print(match)

def test_1():
    """
    判断是否存在英文字母
    """
    s = "abc123def2hi3"
    pattern = re.compile("[a-zA-z]+")
    match = pattern.findall(s)  # 列表形式返回找到符合规则的所有子串
    print(match)

def test_2():
    """
    判断是否包含特殊字符
    """
    s = "abc123def2hi3-\\[ ]"
    pattern = re.compile("[,./;\'\\\[\]`~!@#$%^&*()_+\-=]+")
    match = pattern.findall(s)  # 列表形式返回找到符合规则的所有子串
    print(s)
    print(match)

def test_3():
    """
    判断是否即存在大写字母，也存在小写字母
    """
    s = "abc123def2hi3"
    pattern_1 = re.compile("[a-z]+")
    match_1 = pattern_1.findall(s)  # 列表形式返回找到符合规则的所有子串
    pattern_2 = re.compile("[A-Z]+")
    match_2 = pattern_2.findall(s)
    if (match_1 and match_2):
        print(match_1)
        print(match_2)

def test_4():
    """
    数字查找
    """
    result = re.findall("\d+.\d+", "nihao 12.34 hello66.34")
    print(result)

if __name__ == '__main__':
    test_4()
