# coding=utf-8
import traceback

from pycore.data.entity import globalvar as gl

from game_base.base.constant import REDIS_ACCOUNT_SESSION, REDIS_ROOM_LOCK
from game_base.base.game.mode import room


def execute(sid, room_no, session_id, ip, data):
    r"""
    站起
    :param sid: 连接id
    :param room_no: 房间号
    :param session_id: session
    :param ip: ip
    :param data: 收到的数据
    :return:
    """
    account_session = gl.get_v("redis").getobj(REDIS_ACCOUNT_SESSION + session_id)
    gl.get_v("redis").lock(REDIS_ROOM_LOCK + room_no)
    try:
        _room = room.get_room(room_no)
        _room.stand_up(account_session.account)
        _room.save()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    gl.get_v("redis").unlock(REDIS_ROOM_LOCK + room_no)
