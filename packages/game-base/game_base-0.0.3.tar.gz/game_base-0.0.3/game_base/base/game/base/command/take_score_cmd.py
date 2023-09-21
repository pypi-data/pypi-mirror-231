# coding=utf-8
import traceback

from pycore.data.entity import globalvar as gl

from game_base.base.constant import REDIS_ACCOUNT_SESSION, REDIS_SUB_GATEWAY, REDIS_ROOM_LOCK, REDIS_ROOM_TIMEOUT_LIST
from game_base.base.game.mode import room
from game_base.base.game.mode.game_status import GameStatus
from game_base.base.mode import currency_type, game_type
from game_base.base.protocol.base.base_pb2 import ENTER_ROOM, NOT_EXIST, NOT_ENOUGH, UNKNOWN_ERROR, TAKE_SCORE
from game_base.base.protocol.base.game_base_pb2 import ScoreAction
from game_base.base.send_message import send_to_subscribe, send_to_gateway
from game_base.mode.data import base_mode
from game_base.mode.data.currency import Currency, operation_currency


def execute(sid, room_no, session_id, ip, data):
    r"""
    带分
    :param sid: 连接id
    :param room_no: 房间号
    :param session_id: session
    :param ip: ip
    :param data: 收到的数据
    :return:
    """
    account_session = gl.get_v("redis").getobj(REDIS_ACCOUNT_SESSION + session_id)
    score_action = ScoreAction()
    score_action.ParseFromString(data)
    # score_action.score = 100
    try:
        if room.exist_room(room_no):
            gl.get_v("redis").lock(REDIS_ROOM_LOCK + room_no)
            try:
                _room = room.get_room(room_no)
                currency = 0
                if game_type.GOLD == _room.game_type or game_type.UNION_GOLD == _room.game_type:
                    currency = base_mode.query(Currency.currency, 1, user_id=account_session.account,
                                               currency_type=currency_type.GOLD)
                elif game_type.UNION_SCORE == _room.game_type:
                    currency = base_mode.query(Currency.currency, 1, user_id=account_session.account,
                                               currency_type=currency_type.UNION_SCORE, union_id=_room.union_id)
                if None is currency or currency < score_action.score:
                    send_to_subscribe(REDIS_SUB_GATEWAY, sid, None, TAKE_SCORE, None, NOT_ENOUGH)
                    return
                seat = _room.get_seat_by_account(account_session.account)
                if None is seat:
                    return
                if game_type.GOLD == _room.game_type or game_type.UNION_GOLD == _room.game_type:
                    operation_currency(account_session.account, currency_type.GOLD, -score_action.score, 0,
                                       currency_type.GAME, _room.room_no)
                elif game_type.UNION_SCORE == _room.game_type:
                    operation_currency(account_session.account, currency_type.UNION_SCORE, -score_action.score, 0,
                                       currency_type.GAME, _room.room_no, _room.union_id)

                if _room.game_status == GameStatus.WAITING:
                    seat.score += score_action.score
                else:
                    seat.take_score += score_action.score
                seat.leave_seat = 0
                if None is not seat.leave_seat_timeout:
                    gl.get_v("redis").zrem(REDIS_ROOM_TIMEOUT_LIST + str(_room.game_id), seat.leave_seat_timeout)
                    seat.leave_seat_timeout = None
                    seat.leave_seat = 0
                _room.update_player_info(0)
                send_to_gateway(TAKE_SCORE, None, account_session.account)
                _room.check_ready()
                _room.save()
            except:
                gl.get_v("serverlogger").logger.error(traceback.format_exc())
            gl.get_v("redis").unlock(REDIS_ROOM_LOCK + room_no)
        else:
            send_to_subscribe(REDIS_SUB_GATEWAY, sid, None, ENTER_ROOM, None, NOT_EXIST)
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
        send_to_gateway(TAKE_SCORE, None, account_session.account, UNKNOWN_ERROR)
