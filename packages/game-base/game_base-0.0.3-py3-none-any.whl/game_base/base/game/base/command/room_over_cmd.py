# coding=utf-8
import time

from pycore.data.entity import globalvar as gl

from game_base.base.constant import REDIS_ACCOUNT_GAME
from game_base.base.game.mode.game_status import GameStatus
from game_base.base.mode import currency_type, game_type
from game_base.base.protocol.base.base_pb2 import ROOM_OVER
from game_base.base.protocol.base.game_base_pb2 import RecRoomSettle
from game_base.mode.data.currency import operation_currency


def execute(room, users, content):
    r"""
    退出房间
    :param room: 房间信息
    :param users: 用户id
    :param content: 总结算
    :return:
    """

    room.game_status = GameStatus.DESTORY
    room_settle = RecRoomSettle()
    room_settle.time = int(time.time())
    room_settle.curPlayCount = room.current_game_times
    room_settle.gameId = room.game_id
    room_settle.roomNo = room.room_no
    room_settle.recordIds.extend(room.record_ids)
    room_settle.content = content
    room.broadcast_seat_to_gateway(ROOM_OVER, room_settle.SerializeToString())
    for seat in room.seats:
        gl.get_v("redis").hdelobj(REDIS_ACCOUNT_GAME, seat.user_id)
        if game_type.GOLD == room.game_type or game_type.UNION_GOLD == room.game_type:
            operation_currency(seat.user_id, currency_type.GOLD, seat.score, 0, currency_type.GAME, room.room_no)
        elif game_type.UNION_SCORE == room.game_type:
            operation_currency(seat.user_id, currency_type.UNION_SCORE, seat.score, 0, currency_type.GAME, room.room_no,
                               room.union_id)

    for seat in room.watch_seats:
        gl.get_v("redis").hdelobj(REDIS_ACCOUNT_GAME, seat.user_id)
    if 0 < len(users):
        gl.get_v("command")["room_record"].execute(users, room.room_no, room.game_id, room_settle.SerializeToString(),
                                                   room.union_id)
