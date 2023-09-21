import json
import time
from urllib.parse import urlencode

from pycore.data.entity import config
from pycore.utils.http_utils import HttpUtils
from pycore.utils.stringutils import StringUtils

ACCOUNT = '20609'  # 用户名称*必填
USERNMAE = 'aootoo'  # 用户名称*必填
PASSWORD = 'aootoo123'  # 用户密码*必填
URL = '/v2sms.aspx?'
HOST = 'agent.izjun.cn'


def send_verification_code(mobiles, code):
    return send_message('【' + config.get('login', 'sms_sign') + '】' + '验证码:' + code, mobiles)


def send_message(content, mobiles):
    message = {}
    timestamp = str(int(time.time()))
    sign = StringUtils.md5(USERNMAE + PASSWORD + timestamp)
    message['action'] = 'send'
    message['userid'] = ACCOUNT
    message['rt'] = 'json'
    message['content'] = content
    message['mobile'] = mobiles
    message['timestamp'] = timestamp
    message['sign'] = sign
    url = urlencode(message)
    result = HttpUtils(HOST).post(URL + url, None)
    return json.loads(result)
