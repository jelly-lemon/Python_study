
def get_enabled_config():
    """
    TODO 获取启用的网关配置

    :return 字符串, JSON 格式
    """
    pass

def create_sms_gateway(config_json):
    # TODO JSON 字符串转 字典
    config =

    # 根据厂商名创建对应的 SMS 网关
    sms_firm = config.pop("sms_firm").lower()
    if sms_firm == "Migu".lower():
        sms_gateway = MiguGateway(config)
        pass
    elif sms_firm == "Lingkai".lower():
        sms_gateway = LingkaiGateway(config)
        pass
    else:
        # 用户自定义的其它短信厂商
        sms_gateway = CustomSMSGateway(config)
        pass

    return sms_gateway


class CustomSMSGateway(SmsGateWay):
    def __init__(self, config):
        self.config = config

    def is_available(self):
        """
        检查短信厂商配置是否可用
        """
        pass

    def produce_send_content(self, mobile, content):
        if None == self.sign_name or None == content:
            return None
        if type(content) is not types.StringType:
            content = str(content)

        # 发送内容
        tmp_content = content + "【" + self.sign_name + "】"
        tmp_content = tmp_content.decode('utf-8')
        tmp_content = tmp_content.encode('gbk') #网关厂家规约，短信内容字符需要gbk或者GB2312格式的编码


        # 表单内容
        content_raw = self.config
        content_raw["Mobile"] = mobile
        content_raw["Content"] = tmp_content

        # 表单内容转 url 编码
        content_raw = urllib.urlencode(content_raw)
        return content_raw






