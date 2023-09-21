# coding=utf-8
import traceback

from pycore.data.entity import globalvar as gl

from game_base.base.constant import REDIS_ROOM_LOCK
from game_base.base.game.mode import room
from game_base.base.protocol.base.base_pb2 import PLAYER_ONLINE
from game_base.base.protocol.base.game_base_pb2 import RecUpdatePlayerOnline


def execute(user_id, room_no, session_id, ip, data):
    r"""
    在线状态
    :param user_id: 掉线的人
    :param room_no: 房间号
    :param session_id: session
    :param ip: ip
    :param data: 收到的数据
    :return:
    """
    rec_player_online = RecUpdatePlayerOnline()
    rec_player_online.state = False
    rec_player_online.playerId = int(user_id)
    gl.get_v("redis").lock(REDIS_ROOM_LOCK + room_no)
    try:
        _room = room.get_room(room_no)
        _room.broadcast_all_to_gateway(PLAYER_ONLINE, rec_player_online.SerializeToString())
        seat = _room.get_watch_seat_by_account(user_id)
        if seat is not None and seat.online:
            seat.online = False
            _room.exit(user_id)
        seat = _room.get_seat_by_account(user_id)
        if seat is not None:
            seat.online = False
            # _room.exit(user_id)
        _room.save()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    gl.get_v("redis").unlock(REDIS_ROOM_LOCK + room_no)
