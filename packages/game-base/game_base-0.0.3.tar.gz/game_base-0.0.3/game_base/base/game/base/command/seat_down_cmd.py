# coding=utf-8
import traceback

from pycore.data.entity import globalvar as gl

from game_base.base.constant import REDIS_ACCOUNT_SESSION, REDIS_ROOM_LOCK
from game_base.base.game.mode import room
from game_base.base.game.mode.room import seat2_user_info
from game_base.base.mode import currency_type, game_type
from game_base.base.protocol.base.base_pb2 import SEAT_DOWN_NO_SEAT, SEAT_DOWN, UNKNOWN_ERROR, SEAT_DOWN_ALREADY, \
    SELF_INFO, NOT_ENOUGH
from game_base.base.protocol.base.game_base_pb2 import ReqSeatDown, RecUpdateGameUsers
from game_base.base.send_message import send_to_gateway
from game_base.mode.data import base_mode
from game_base.mode.data.currency import Currency


def execute(sid, room_no, session_id, ip, data):
    r"""
    坐下
    :param sid: 连接id
    :param room_no: 房间号
    :param session_id: session
    :param ip: ip
    :param data: 收到的数据
    :return:
    """
    account_session = gl.get_v("redis").getobj(REDIS_ACCOUNT_SESSION + session_id)
    seat_down = ReqSeatDown()
    seat_down.ParseFromString(data)
    gl.get_v("redis").lock(REDIS_ROOM_LOCK + room_no)
    try:
        _room = room.get_room(room_no)
        seat = _room.get_watch_seat_by_account(account_session.account)
        if None is not seat:
            currency = 0
            if game_type.GOLD == _room.game_type or game_type.UNION_GOLD == _room.game_type:
                currency = base_mode.query(Currency.currency, 1, user_id=account_session.account,
                                           currency_type=currency_type.GOLD)
            elif game_type.UNION_SCORE == _room.game_type:
                currency = base_mode.query(Currency.currency, 1, user_id=account_session.account,
                                           currency_type=currency_type.UNION_SCORE, union_id=_room.union_id)
            if None is currency or currency < _room.in_score:
                send_to_gateway(SEAT_DOWN, None, account_session.account, NOT_ENOUGH)
                return
            if 0 == len(_room.seat_nos):
                send_to_gateway(SEAT_DOWN, None, account_session.account, SEAT_DOWN_NO_SEAT)
                return
            else:
                if 0 == seat_down.seatNo:
                    seat.seat_no = _room.seat_nos[0]
                    _room.seat_nos.remove(_room.seat_nos[0])
                else:
                    if seat_down.seatNo not in _room.seat_nos:
                        send_to_gateway(SEAT_DOWN, None, account_session.account, SEAT_DOWN_ALREADY)
                        return
                    seat.seat_no = seat_down.seatNo
                    _room.seat_nos.remove(seat_down.seatNo)
                _room.seats.append(seat)
                _room.watch_seats.remove(seat)
                send_to_gateway(SEAT_DOWN, None, account_session.account)
                user_info = seat2_user_info(seat, RecUpdateGameUsers.UserInfo())
                send_to_gateway(SELF_INFO, user_info.SerializeToString(), account_session.account)
                _room.update_player_info(0)
                seat.add_ready_timeout(_room)
                seat.add_leave_seat_timeout(_room)
                _room.save()
                return
        send_to_gateway(SEAT_DOWN, None, seat_down.seatNo, UNKNOWN_ERROR)
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        gl.get_v("redis").unlock(REDIS_ROOM_LOCK + room_no)
