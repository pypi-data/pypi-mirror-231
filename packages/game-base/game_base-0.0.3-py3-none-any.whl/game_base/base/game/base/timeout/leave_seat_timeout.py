import time
import traceback

from pycore.data.entity import globalvar as gl

from game_base.base.constant import REDIS_ROOM_LOCK
from game_base.base.game.mode import room


def execute(data):
    u"""
    准备超时
    :param data: 数据
    """
    room_no = data["room_no"]
    user_id = data["user_id"]
    redis = gl.get_v("redis")
    if room.exist_room(room_no):
        redis.lock(REDIS_ROOM_LOCK + room_no)
        try:
            _room = room.get_room(room_no)
            seat = _room.get_seat_by_account(user_id)
            if seat is not None and seat.leave_seat <= int(time.time()):
                seat.leave_seat_timeout = None
                seat.leave_seat = 0
                _room.stand_up(user_id)
                _room.save()
        except:
            gl.get_v("serverlogger").logger.error(traceback.format_exc())
        redis.unlock(REDIS_ROOM_LOCK + room_no)
