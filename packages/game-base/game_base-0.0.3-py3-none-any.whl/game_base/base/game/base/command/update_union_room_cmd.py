# coding=utf-8

from pycore.data.entity import globalvar as gl

from game_base.base.constant import REDIS_UNION_ROOM_MAP
from game_base.base.game.mode.game_status import GameStatus
from protocol.club.club_pb2 import ReqUpdateRoomConfig


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
    update_room_config = ReqUpdateRoomConfig()
    update_room_config.ParseFromString(data)
    all_room = gl.get_v("redis").hallobj(REDIS_UNION_ROOM_MAP + str(update_room_config.createRoom.unionId))
    view_room = [n for n in all_room if (n.room_config_id == room_config_id)]

    for room in view_room:
        if 0 == len(room.seats) + len(room.watch_seats):
            room.game_status = GameStatus.DESTORY
            room.save()

    gl.get_v("game_command")["create_union_room"].execute(int(room_config_id), update_room_config.createRoom.unionId,
                                                          update_room_config.createRoom)
