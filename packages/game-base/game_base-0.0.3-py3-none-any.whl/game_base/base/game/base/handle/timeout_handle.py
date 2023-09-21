# coding=utf-8
import pickle
import time
import traceback

import pycore.data.entity.globalvar as gl
import redis


class TimeoutHandle(object):
    r"""
    计数器处理
    """

    def __init__(self):
        self.__close = False

    def close(self):
        self.__close = True

    def handle(self, redis_key):
        r"""
        处理超时线程
        :param redis_key
        :return:
        """
        while True:
            try:
                # 从redis里面获取消息
                data = gl.get_v("redis").zrangebyscore(redis_key, 0, int(time.time()), 0, 1, True)
                if data is not None and 0 < len(data):
                    data, score = data[0]
                    if gl.get_v("redis").zrem(redis_key, data):
                        data = pickle.loads(data)
                        if str(data["timeout_type"]) in gl.get_v("timeout"):
                            gl.get_v("timeout")[str(data["timeout_type"])].execute(data)
                        else:
                            gl.get_v("serverlogger").logger.error("未注册计时器" + str(data["timeout_type"]))
                else:
                    time.sleep(0.2)
            except redis.exceptions.ConnectionError:
                time.sleep(10)
                gl.get_v("serverlogger").logger.error(traceback.format_exc())
            except ValueError:
                time.sleep(0.2)
            except:
                gl.get_v("serverlogger").logger.error(traceback.format_exc())
            finally:
                if self.__close:
                    break
