import requests, json, re, time
import NorrisUtils.BuildConfig
import NorrisUtils.RawUtils
import base64
import codecs

# https://blog.csdn.net/weixin_47590344/article/details/129251757
# 积分不足 {'code': 4102, 'msg': '积分不足', 'data': None, 'time': 1694766032}
API_TCN = 'https://api.txapi.cn/v1/short_url/tcn'
API = 'https://api.txapi.cn/v1/short_url'
url = 'http://www.baidu.com'
token_other = 'Z1QljZOZiT4NTG'
token = '0jOL0NAj2Uj25Z'


class APItxApi(object):
    """
    txapi
    http://txapi.cn/api_detail?id=1609184287570001920
    """
    token = token_other

    def __init__(self):
        pass

    def set_token(self, token):
        self.token = token

    def parse_result(self, req):
        '''
        解析结果
        :param req:
        {"code":200,"msg":"OK","data":{"long_url":"http://www.baidu.com","short_url":"http://t.cn/Rxmm0XL"},"time":1695020937}
        {'code': 4102, 'msg': '积分不足', 'data': None, 'time': 1694766032}
        :return:
        '''
        try:
            parsed_data = json.loads(req.text)
            short_url = parsed_data['data']['short_url']
            print(short_url)
            return short_url
        except:
            pass
        return '提取失败:' + req.text

    def one_key_shorten(self, url, logfunc=print):
        """
        一键变短链
        :param url:
        :param logfunc:
        :return:
        """
        params = {
            'token': self.token,
            'url': url
        }
        req = requests.get(API, params=params, allow_redirects=False, verify=False)
        logfunc(req.url)
        logfunc(req.text)
        result = self.parse_result(req)
        logfunc(result)
        if result.__contains__("失败"):
            return url
        return result


# # 示例用法
# url = 'https://h5.m.jd.com/rn/42yjy8na6pFsq1cx9MJQ5aTgu3kX/index.html?has_native=0'
# (APItxApi().one_key_shorten(url, logfunc=print))
