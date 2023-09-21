# coding=utf-8
import time
import traceback

import pycore.data.entity.globalvar as gl
import redis

from game_base.base.protocol.base.base_pb2 import NetMessage, Opcode
from game_base.base.protocol.base.gateway_pb2 import GateWayMessage


class MessageHandle(object):
    r"""
    消息分发
    """

    def __init__(self):
        self.__close = False

    def close(self):
        self.__close = True

    def handle(self, redis_key):
        r"""
        执行消息分发
        :param redis_key
        :return:
        """
        while True:
            try:
                # 从redis里面获取消息
                data = gl.get_v("redis").brpop(redis_key, timeout=20)
                if None is not data:
                    froms, messages = data
                    if None is not messages:
                        # 消息解码
                        s = GateWayMessage()
                        s.ParseFromString(messages)
                        message = NetMessage()
                        message.ParseFromString(s.data)
                        # 消息分发到command
                        if str(message.opcode) in gl.get_v("command"):
                            gl.get_v("serverlogger").logger.info("处理消息%s" % Opcode.Name(message.opcode))
                            gl.get_v("command")[str(message.opcode)].execute(s.sid, s.roomNo, s.session_id, s.ip,
                                                                             message.data)
                        else:
                            gl.get_v("serverlogger").logger.info("消息头不存在%s" % Opcode.Name(message.opcode))
            except redis.exceptions.ConnectionError:
                time.sleep(10)
                gl.get_v("serverlogger").logger.error(traceback.format_exc())
            except:
                gl.get_v("serverlogger").logger.error(traceback.format_exc())
            finally:
                if self.__close:
                    break
