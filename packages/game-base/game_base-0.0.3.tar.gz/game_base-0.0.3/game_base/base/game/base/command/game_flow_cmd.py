# coding=utf-8
import time
import traceback

from pycore.data.entity import globalvar as gl
from pycore.utils import time_utils

from game_base.mode.data import base_mode
from game_base.mode.data.game_flow import GameFlow


def execute(win_lose, room):
    r"""
    输赢流水
    :param win_lose: 玩家输赢
    :param room: 房间号
    :return:
    """
    try:
        for k, v in win_lose.items():
            if 0 == v:
                continue
            game_flow = GameFlow()
            game_flow.room_no = room.room_no
            game_flow.create_time = int(time.time())
            game_flow.game_id = room.game_id
            game_flow.game_type = room.game_type
            game_flow.score = room.score
            game_flow.user_id = k
            game_flow.win = v
            game_flow.union_id = room.union_id
            base_mode.add(game_flow)
            cache_win_name = room.get_cache_win_name()
            total = 0
            if gl.get_v("redis").hexists(cache_win_name, k):
                total = float(gl.get_v("redis").hget(cache_win_name, k))
            total += v
            gl.get_v("redis").hset(cache_win_name, k, v)
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    return None
