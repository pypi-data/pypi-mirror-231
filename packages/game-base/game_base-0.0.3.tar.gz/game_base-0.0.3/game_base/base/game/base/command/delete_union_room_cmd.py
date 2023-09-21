# coding=utf-8

from pycore.data.entity import globalvar as gl

from game_base.base.constant import REDIS_UNION_ROOM_MAP, REDIS_SUB_GATEWAY
from game_base.base.game.mode.game_status import GameStatus
from game_base.base.protocol.base.base_pb2 import DELETE_ROOM_CONFIG, UNKNOWN_ERROR
from game_base.base.send_message import send_to_subscribe
from game_base.mode.data import base_mode
from game_base.mode.data.create_room_config import RoomConfig
from protocol.club.club_pb2 import ReqDeleteRoomConfig


def execute(sid, room_config_id, session_id, ip, data):
    r"""
    创建房间
    :param sid: 连接id
    :param room_config_id: 房间配置id
    :param session_id: session
    :param ip: ip
    :param data: 收到的数据
    :return:
    """
    delete_room_config = ReqDeleteRoomConfig()
    delete_room_config.ParseFromString(data)

    room_config = base_mode.get(RoomConfig, delete_room_config.configId)
    if None is not room_config:
        all_room = gl.get_v("redis").hallobj(REDIS_UNION_ROOM_MAP + str(room_config.union_id))
        view_room = [n for n in all_room if (n.room_config_id == room_config_id)]
        for room in view_room:
            if 0 == len(room.seats) + len(room.watch_seats):
                room.game_status = GameStatus.DESTORY
                room.save()
        base_mode.remove(RoomConfig, id=delete_room_config.configId)
        send_to_subscribe(REDIS_SUB_GATEWAY, sid, None, DELETE_ROOM_CONFIG, None)
        return
    send_to_subscribe(REDIS_SUB_GATEWAY, sid, None, DELETE_ROOM_CONFIG, None, UNKNOWN_ERROR)
