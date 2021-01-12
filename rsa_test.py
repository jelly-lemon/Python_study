"""
使用 rsa 模型进行简单地加密解密

源代码参考：
https://blog.csdn.net/whatday/article/details/97617461/

"""

import rsa

def rsaEncrypt(str):
    """
    对字符串进行 rsa 加密，并同时返回生成的私钥

    :param str: 待加密的字符串
    :return: 加密后的字符串，生成的密钥
    """
    # 生成公钥、密钥
    pubkey, privkey = rsa.newkeys(512)  # 生成长度为512的公钥
    print("生成公钥和密钥...")
    print("公钥：%s" % pubkey)
    print("密钥：%s" % privkey)

    # 对明文编码
    content = str.encode("utf-8")   # 对输入进来的字符串用 utf-8 进行编码，得到二进制编码

    # 公钥加密
    crypto = rsa.encrypt(content, pubkey)

    return crypto, privkey

def rsaDecrypt(str, privkey):
    """
    对 rsa 加密的密文进行解密

    :param str:密文
    :param privk: 私钥
    :return:解密后的明文
    """
    # 私钥解密
    content = rsa.decrypt(str, privkey)
    org_str = content.decode("utf-8")   # 对二进制进行解码，得到原始字符串

    return org_str

if __name__ == '__main__':
    org_str = "hello"
    enc_str, privkey = rsaEncrypt(org_str)
    print("原始字符串：%s" % org_str)
    print("公钥加密后：%s" % enc_str)
    dec_str = rsaDecrypt(enc_str, privkey)
    print("私钥解密后：%s" % dec_str)
