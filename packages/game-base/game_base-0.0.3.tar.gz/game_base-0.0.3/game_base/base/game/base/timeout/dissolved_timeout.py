import traceback

import pycore.data.entity.globalvar as gl

from game_base.base.constant import REDIS_ROOM_LOCK, REDIS_ROOM_TIMEOUT_LIST
from game_base.base.game.mode import room
from game_base.base.protocol.base.base_pb2 import DISSOLVE_CONFIRM
from game_base.base.protocol.base.game_base_pb2 import RecDissolvedConfirm


def execute(data):
    room_no = data["room_no"]
    redis = gl.get_v("redis")
    if room.exist_room(room_no):
        redis.lock(REDIS_ROOM_LOCK + room_no)
        try:
            _room = room.get_room(room_no)
            if None is not _room.dissolved_timeout:
                rec_dissolved = RecDissolvedConfirm()
                gl.get_v("redis").zrem(REDIS_ROOM_TIMEOUT_LIST + str(_room.game_id), _room.dissolved_timeout)
                _room.dissolved_timeout = None
                rec_dissolved.dissolved = False
                _room.broadcast_seat_to_gateway(DISSOLVE_CONFIRM, rec_dissolved.SerializeToString())
        except:
            gl.get_v("serverlogger").logger.error(traceback.format_exc())
        redis.unlock(REDIS_ROOM_LOCK + room_no)
