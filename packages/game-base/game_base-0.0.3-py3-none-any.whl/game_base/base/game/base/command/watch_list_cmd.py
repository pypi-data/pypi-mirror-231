# coding=utf-8
import traceback

from pycore.data.entity import globalvar as gl

from game_base.base.constant import REDIS_SUB_GATEWAY
from game_base.base.game.mode import room
from game_base.base.protocol.base.base_pb2 import WATCH_LIST, UNKNOWN_ERROR
from game_base.base.protocol.base.game_base_pb2 import RecWatchList
from game_base.base.send_message import send_to_subscribe


def execute(sid, room_no, session_id, ip, data):
    r"""
    观战列表
    :param sid: 连接id
    :param room_no: 房间号
    :param session_id: session
    :param ip: ip
    :param data: 收到的数据
    :return:
    """
    try:
        _room = room.get_room(room_no)
        rec_watch_list = RecWatchList()
        for seat in _room.watch_seats:
            watch_item = rec_watch_list.watchList.add()
            watch_item.id = seat.user_id
            watch_item.userId = seat.account
            watch_item.nick = seat.nickname
            watch_item.head = seat.head
        send_to_subscribe(REDIS_SUB_GATEWAY, sid, None, WATCH_LIST, rec_watch_list.SerializeToString())
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
        send_to_subscribe(REDIS_SUB_GATEWAY, sid, None, WATCH_LIST, None, UNKNOWN_ERROR)
