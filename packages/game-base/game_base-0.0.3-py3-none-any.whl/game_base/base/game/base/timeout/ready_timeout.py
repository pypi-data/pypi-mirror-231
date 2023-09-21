import traceback

from pycore.data.entity import globalvar as gl

from game_base.base.constant import REDIS_ROOM_LOCK
from game_base.base.game.mode import room
from game_base.base.game.mode.game_status import GameStatus


def execute(data):
    u"""
    准备超时
    :param data: 数据
    """
    room_no = data["room_no"]
    user_id = data["user_id"]
    into_time = data["into_time"]
    current_game_times = data["current_game_times"]
    redis = gl.get_v("redis")
    if room.exist_room(room_no):
        redis.lock(REDIS_ROOM_LOCK + room_no)
        try:
            _room = room.get_room(room_no)
            if _room.current_game_times == current_game_times and _room.game_status == GameStatus.WAITING:
                seat = _room.get_seat_by_account(user_id)
                if seat is not None and not seat.ready and seat.into_time == into_time:
                    seat.ready_timeout = None
                    seat.add_leave_seat_timeout(_room)
                    _room.update_player_info(0)
                    _room.save()
        except:
            gl.get_v("serverlogger").logger.error(traceback.format_exc())
        redis.unlock(REDIS_ROOM_LOCK + room_no)
