# coding=utf-8
import traceback

from pycore.data.entity import globalvar as gl

from game_base.base.constant import REDIS_ACCOUNT_SESSION, REDIS_ROOM_LOCK
from game_base.base.game.mode import room
from game_base.base.protocol.base.game_base_pb2 import ReqSendAction


def execute(sid, room_no, session_id, ip, data):
    r"""
    执行操作
    :param sid: 连接id
    :param room_no: 房间号
    :param session_id: session
    :param ip: ip
    :param data: 收到的数据
    :return:
    """
    account_session = gl.get_v("redis").getobj(REDIS_ACCOUNT_SESSION + session_id)
    action = ReqSendAction()
    action.ParseFromString(data)
    gl.get_v("redis").lock(REDIS_ROOM_LOCK + room_no)
    try:
        _room = room.get_room(room_no)
        gl.get_v("serverlogger").logger.info('''actionType---%d''' % action.actionType)
        gl.get_v("game_action")[str(action.actionType)].execute(_room, account_session.account, action.data)
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    gl.get_v("redis").unlock(REDIS_ROOM_LOCK + room_no)
