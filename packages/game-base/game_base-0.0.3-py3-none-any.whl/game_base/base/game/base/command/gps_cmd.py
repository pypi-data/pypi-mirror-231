# coding=utf-8
import traceback

from pycore.data.entity import globalvar as gl

from game_base.base.constant import REDIS_ACCOUNT_SESSION, REDIS_ROOM_LOCK
from game_base.base.game.mode import room
from game_base.base.protocol.base.base_pb2 import PLAYER_GPS
from game_base.base.protocol.base.game_base_pb2 import ReqGpsInfo


def execute(sid, room_no, session_id, ip, data):
    r"""
    gps
    :param sid: 连接id
    :param room_no: 房间号
    :param session_id: session
    :param ip: ip
    :param data: 收到的数据
    :return:
    """
    req_gps_info = ReqGpsInfo()
    req_gps_info.ParseFromString(data)
    account_session = gl.get_v("redis").getobj(REDIS_ACCOUNT_SESSION + session_id)
    gl.get_v("redis").lock(REDIS_ROOM_LOCK + room_no)
    try:
        _room = room.get_room(room_no)
        seat = _room.get_seat_by_account(account_session.account)
        if seat is not None:
            seat.gps_info = req_gps_info.gpsInfo
            _room.broadcast_all_to_gateway(PLAYER_GPS, _room.get_gpa_info().SerializeToString())
            _room.save()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    gl.get_v("redis").unlock(REDIS_ROOM_LOCK + room_no)
