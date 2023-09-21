# coding=utf-8
import pickle
import time

from pycore.data.entity import config, globalvar as gl

from game_base.base.constant import REDIS_ROOM_TIMEOUT_LIST
from game_base.base.game.mode.timeout_type import TimeoutType


class Seat(object):

    def __init__(self):
        self.seat_no = 0
        self.user_id = 0
        self.account = None
        self.create_time = 0
        self.nickname = ''
        self.head = ''
        self.sex = 0
        self.score = 0
        self.address = ''
        self.is_robot = False
        self.ready = False
        self.online = True
        self.ip = ''
        self.gps_info = ''
        self.into_time = 0
        self.play_score = 0
        self.win_lose = 0
        self.gaming = False
        self.end = False
        self.cards = []
        self.operation = False
        self.take_score = 0
        self.leave_seat = 0
        self.ready_timeout = None
        self.leave_seat_timeout = None
        self.play_timeout = None
        self.dissolved = None
        self.is_robot = False

    def clear(self):
        self.ready = False
        self.play_score = 0
        self.end = False
        self.cards.clear()

    def add_ready_timeout(self, room):
        if 0 != room.operation_time:
            if None is not self.ready_timeout:
                gl.get_v("redis").zrem(REDIS_ROOM_TIMEOUT_LIST + str(room.game_id), self.ready_timeout)
                self.ready_timeout = None
            data = pickle.dumps(
                {"timeout_type": TimeoutType.READY, "room_no": room.get_room_key(),
                 "user_id": self.user_id, "current_game_times": room.current_game_times, "into_time": self.into_time},
                -1)
            op_time = int(time.time()) + room.operation_time
            gl.get_v("redis").zadd(REDIS_ROOM_TIMEOUT_LIST + str(room.game_id), {data: op_time})
            self.ready_timeout = data

    def add_leave_seat_timeout(self, room):
        if None is not self.leave_seat_timeout:
            gl.get_v("redis").zrem(REDIS_ROOM_TIMEOUT_LIST + str(room.game_id), self.leave_seat_timeout)
            self.leave_seat_timeout = None
        data = pickle.dumps(
            {"timeout_type": TimeoutType.LEAVE_SEAT, "room_no": room.get_room_key(), "user_id": self.user_id}, -1)
        op_time = int(time.time()) + int(config.get("game", "leave_time"))
        gl.get_v("redis").zadd(REDIS_ROOM_TIMEOUT_LIST + str(room.game_id), {data: op_time})
        self.leave_seat_timeout = data
        self.leave_seat = op_time
