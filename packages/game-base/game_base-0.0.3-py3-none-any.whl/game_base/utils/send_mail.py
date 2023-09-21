import pickle
import smtplib
import time
import traceback
from email.header import Header
from email.mime.text import MIMEText

import redis
from pycore.data.entity import config, globalvar as gl

from game_base.base.constant import REDIS_MAIL_MESSAGE


class SendMail(object):
    def __init__(self):
        self.mail_sender = None
        self.server = None

    def init_server(self):
        try:
            self.mail_sender = config.get("mail", "mail_sender")  # 发件人邮箱账号
            mail_pass = config.get("mail", "mail_pass")  # 发件人邮箱密码
            print(time.time())
            self.server = smtplib.SMTP(config.get("mail", "mail_host"),
                                       int(config.get("mail", "mail_port")))  # 发件人邮箱中的SMTP服务器，端口是25
            self.server.ehlo()  # 向邮箱发送SMTP 'ehlo' 命令
            self.server.starttls()
            print(time.time())
            self.server.login(self.mail_sender, mail_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        except:
            gl.get_v("serverlogger").logger.error(traceback.format_exc())
            time.sleep(10)

    def close_server(self):
        try:
            if None is not self.server:
                self.server.quit()
                self.server = None
        except:
            gl.get_v("serverlogger").logger.error(traceback.format_exc())

    def send(self, content, emails):
        receivers = emails  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        subject = 'dm code'
        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = Header("dm", 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        self.server.sendmail(self.mail_sender, receivers, message.as_string())

    def handle(self):
        r"""
        执行消息分发
        :return:
        """
        while True:
            try:
                redis_key = REDIS_MAIL_MESSAGE
                # 从redis里面获取消息
                data = gl.get_v("redis").brpop(redis_key, timeout=20)
                if None is not data:
                    froms, messages = data
                    if None is not messages:
                        message_data = pickle.loads(messages)
                        while None is self.server:
                            self.init_server()
                        try:
                            receivers = message_data['emails']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
                            # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
                            subject = 'dm code'
                            message = MIMEText(message_data['content'], 'plain', 'utf-8')
                            message['From'] = Header("dm", 'utf-8')
                            message['Subject'] = Header(subject, 'utf-8')
                            self.server.sendmail(self.mail_sender, receivers, message.as_string())
                        except:
                            gl.get_v("serverlogger").logger.error(traceback.format_exc())
                            self.close_server()
                            gl.get_v("redis").lpush(redis_key, messages)

            except redis.exceptions.ConnectionError:
                time.sleep(10)
                gl.get_v("serverlogger").logger.error(traceback.format_exc())
            except:
                gl.get_v("serverlogger").logger.error(traceback.format_exc())
