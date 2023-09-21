import pickle

from pycore.data.entity import globalvar as gl, config

from game_base.base.constant import REDIS_MAIL_MESSAGE


def send_verification_code(emails, code):
    return send_message('【' + config.get('login', 'sms_sign') + '】' + '验证码:' + code, emails)


def send_message(content, emails):
    message = {}
    message['content'] = content
    message['emails'] = emails
    gl.get_v("redis").lpush(REDIS_MAIL_MESSAGE, pickle.dumps(message))
