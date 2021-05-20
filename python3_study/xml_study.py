

def test_0():
    """
    字符串转 xml
    """
    import xml.etree.cElementTree as ET

    xml_string = """<?xml version="1.0" encoding="utf-8" ?>
<license type="try" id="285801">
  <product type="ICEYE" mode="OSMS" />
  <expiration begin="20201016" end="20221011" />
  <user name="test25567" />
  <hashes count="1">
        <hash value="08C6-48BC-4ACC-0065" sign="TlNGTAABAABgAAAAdUt17cVN5KlBYhoRLrI91Nxjq6WLUeU9wlH2JPHTxhFAjRm2P5YiDuvleHOyvC7z8HAV6oz1TAt7i2eS3XC2K+cnVU71xcZVk/cD0rQZxu3OihQAlUDY3chckykRFcgofmxBPQ==" authType="espc" />
  </hashes>
  <serial value="0D41-28E4-D529-EA79"/>
  <desc value=""/>
  <private>
    <config type="engine" mode="monitor" nic="4" model="sas h" user="0" server="0" language="zh_CN"/>
  </private>
  <nscloudsms isuse="false" value="200"/>
  <publiccloud type="none"/>
    <logengine screenrecord="true" />
</license> 
"""
    root = ET.fromstring(xml_string)
    print(type(root))
    print(root)


def test_1():
    """
    读取 xml 元素属性值
    """
    import xml.etree.cElementTree as ET

    xml_string = """<?xml version="1.0" encoding="utf-8"?>
<catalog>
    <maxid>4</maxid>hello, I'm tail.
    <login username="pytest" passwd='123456'>
        <caption>Python</caption>
        <item id="4">
            <caption>测试</caption>
        </item>
    </login>
    <item id="2">
        <caption>Zope</caption>
    </item>
    <product type="ICEYE" mode="OSMS" />
</catalog>"""
    # ElementTree 表示整个 xml 文档，也就是文档树
    # Element 表示子元素
    root = ET.fromstring(xml_string)
    print(root)
    print("tag:", root.tag) # 元素名
    print("attrib:", root.attrib)  # 元素属性
    print("text:", root.text)    # 元素值
    print("tail:", root.tail)    # <></>标签对后面的文本

    # 读取子元素
    for child in root:
        print("tag:", child.tag)
        print("attrib:", child.attrib)
        print("text:", child.text)
        print("tail:", child.tail)

    # 使用 find 查找子元素
    print(root.find("login").find("caption"))


def test_2():
    """
    xml 文件转对象
    """
    import xml.etree.cElementTree as ET

    root = ET.parse("test.xml")
    print(type(root))
    print(root)

def test_3():
    """
    替换 xml 元素属性值
    """
    import xml.etree.cElementTree as ET

    xml_string = """<?xml version="1.0" encoding="utf-8"?>
    <book catalog="computer">
        <name>Java</name>
    </book>"""
    # ElementTree 表示整个 xml 文档，也就是文档树
    # Element 表示子元素
    root = ET.fromstring(xml_string)
    print(type(root))
    print(root)
    print("tag:", root.tag)  # 元素名
    print("attrib:", root.attrib)  # 元素属性
    print("text:", root.text)  # 元素值
    print("tail:", root.tail)  #

    # 使用 set 设置或修改属性值
    root.set("catalog", "hello")
    print("attrib:", root.attrib)  # 元素属性

    # 通过字典
    root.attrib["catalog"] = "by dict"
    print("attrib:", root.attrib)  # 元素属性

def test_4():
    """
    xml 对象转字符串
    """
    import xml.etree.cElementTree as ET

    xml_string = """<?xml version="1.0" encoding="utf-8"?>
    <catalog>
        <maxid>4</maxid>hello, I'm tail.
        <login username="pytest" passwd='123456'>
            <caption>Python</caption>
            <item id="4">
                <caption>测试</caption>
            </item>
        </login>
        <item id="2">
            <caption>Zope</caption>
        </item>
        <product type="ICEYE" mode="OSMS" />
    </catalog>"""
    root = ET.fromstring(xml_string)

    # 直接全部输出 xml 对象
    ET.dump(root)

    # 转成字符串
    s = ET.tostring(root, encoding="utf-8").decode("utf-8")
    print(s)

if __name__ == '__main__':
    test_4()