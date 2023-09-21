# coding=utf-8
import traceback

from pycore.data.entity import globalvar as gl
from sqlalchemy.orm import load_only

from game_base.base.constant import REDIS_ACCOUNT_SESSION, REDIS_SUB_GATEWAY, REDIS_ROOM_LOCK, REDIS_ACCOUNT_GAME, \
    REDIS_ACCOUNT_CLUB, REDIS_CLUB_UNION
from game_base.base.game.mode import room
from game_base.base.mode import currency_type, game_type
from game_base.base.protocol.base.base_pb2 import ENTER_ROOM, ROOM_ALREADY, UNKNOWN_ERROR, NOT_EXIST, NOT_ENOUGH
from game_base.base.protocol.base.game_base_pb2 import ReqEnterRoom
from game_base.base.send_message import send_to_subscribe, send_to_gateway
from game_base.mode.data import base_mode
from game_base.mode.data.account import Account
from game_base.mode.data.create_room_config import RoomConfig
from game_base.mode.data.currency import Currency
from game_base.mode.data.room_card import RoomCard
from game_base.mode.data.union import Union


def execute(sid, room_no, session_id, ip, data):
    r"""
    进去房间
    :param sid: 连接id
    :param room_no: 房间号
    :param session_id: session
    :param ip: ip
    :param data: 收到的数据
    :return:
    """
    account_session = gl.get_v("redis").getobj(REDIS_ACCOUNT_SESSION + session_id)
    if gl.get_v("redis").hexists(REDIS_ACCOUNT_GAME, account_session.account):
        send_to_gateway(ENTER_ROOM, None, account_session.account, ROOM_ALREADY)
        return
    enter_room = ReqEnterRoom()
    enter_room.ParseFromString(data)
    room_no = enter_room.roomNo
    room_key = enter_room.roomNo + ',0'
    account = None
    union_id = None
    try:
        account = base_mode.get(Account, account_session.account)
        if None is account:
            send_to_subscribe(REDIS_SUB_GATEWAY, sid, None, ENTER_ROOM, None, UNKNOWN_ERROR)
            return
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    if gl.get_v("redis").hexists(REDIS_ACCOUNT_CLUB, account_session.account):
        club_id = gl.get_v("redis").hget(REDIS_ACCOUNT_CLUB, account_session.account)
        if gl.get_v("redis").hexists(REDIS_CLUB_UNION, club_id):
            union_id = gl.get_v("redis").hget(REDIS_CLUB_UNION, club_id)
            room_key = enter_room.roomNo + ',' + union_id
    if room.exist_room(room_key):
        gl.get_v("redis").lock(REDIS_ROOM_LOCK + room_no)
        _room = None
        need_create = False
        try:
            _room = room.get_room(room_key)
            room_card = None
            # TODO 扣房卡
            # if game_type.ROOM_CARD == _room.game_type or game_type.UNION_SCORE == _room.game_type or game_type.UNION_ROOM_CARD == _room.game_type:
                # room_card = base_mode.query_values(RoomCard,
                #                                    load_only(RoomCard.owner_currency, RoomCard.aa_currency,
                #                                              RoomCard.winner_currency),
                #                                    1, game_id=_room.game_id, times_type=_room.times_type,
                #                                    game_times=_room.game_times, people_count=_room.people_count)
                # if game_type.ROOM_CARD == _room.game_type:
                #     card = base_mode.query(Currency.currency, 1, user_id=account_session.account,
                #                            currency_type=currency_type.ROOM_CARD)
                #     # 房卡不足
                #     if (None is room_card or None is card) \
                #             or (0 == _room.pay_type and card < room_card.owner_currency_currency) \
                #             or (1 == _room.pay_type and card < room_card.aa_currency) \
                #             or (2 == _room.pay_type and card < room_card.winner_currency):
                #         send_to_subscribe(REDIS_SUB_GATEWAY, sid, None, ENTER_ROOM, None, NOT_ENOUGH)
                #         return
            if 0 == len(_room.seats) + len(_room.watch_seats) and 0 != _room.union_id:
                need_create = True
                # if game_type.UNION_SCORE == _room.game_type or game_type.UNION_ROOM_CARD == _room.game_type:
                #     owner_id = base_mode.query(Union.owner_id, 1, id=union_id)
                #     card = base_mode.query(Currency.currency, 1, user_id=owner_id,
                #                            currency_type=currency_type.ROOM_CARD)
                #     if (None is room_card or None is card) \
                #             or (0 == _room.pay_type and card < room_card.owner_currency_currency):
                #         send_to_subscribe(REDIS_SUB_GATEWAY, sid, None, ENTER_ROOM, None, NOT_ENOUGH)
                #     return
            _room.join_room(account, ip)
        except:
            gl.get_v("serverlogger").logger.error(traceback.format_exc())
        gl.get_v("redis").unlock(REDIS_ROOM_LOCK + room_no)

        if None is not _room and need_create:
            room_config = base_mode.get(RoomConfig, _room.room_config_id)
            if None is not room_config:
                gl.get_v("game_command")["create_union_room"].execute(_room.room_config_id, room_config.create_room)
    else:
        send_to_subscribe(REDIS_SUB_GATEWAY, sid, None, ENTER_ROOM, None, NOT_EXIST)
