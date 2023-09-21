# coding=utf-8
import traceback

from pycore.data.entity import globalvar as gl
from sqlalchemy.orm import load_only

from game_base.base.constant import REDIS_ACCOUNT_SESSION, REDIS_SUB_GATEWAY, REDIS_ACCOUNT_GAME
from game_base.base.mode import currency_type, game_type
from game_base.base.protocol.base.base_pb2 import CREATE_ROOM, ENTER_ROOM, ROOM_ALREADY, NOT_ENOUGH
from game_base.base.protocol.base.game_base_pb2 import ReqCreateRoom, ReqEnterRoom
from game_base.base.send_message import send_to_subscribe, send_to_gateway
from game_base.mode.data import base_mode
from game_base.mode.data.currency import Currency
from game_base.mode.data.room_card import RoomCard


def execute(sid, room_no, session_id, ip, data):
    r"""
    创建房间
    :param sid: 连接id
    :param room_no: 房间号
    :param session_id: session
    :param ip: ip
    :param data: 收到的数据
    :return:
    """
    account_session = gl.get_v("redis").getobj(REDIS_ACCOUNT_SESSION + session_id)
    create_room = ReqCreateRoom()
    create_room.ParseFromString(data)
    if gl.get_v("redis").hexists(REDIS_ACCOUNT_GAME, account_session.account):
        send_to_gateway(CREATE_ROOM, None, account_session.account, ROOM_ALREADY)
        return
    if game_type.GOLD == create_room.gameType:
        try:
            room_no = gl.get_v("game_command")["create_room"].execute(account_session.account, create_room)
            gl.get_v("serverlogger").logger.info("房间号" + str(room_no))
            send_to_subscribe(REDIS_SUB_GATEWAY, sid, None, CREATE_ROOM, None)
            enter_room = ReqEnterRoom()
            enter_room.roomNo = room_no
            gl.get_v("command")[str(ENTER_ROOM)].execute(sid, room_no, session_id, ip, enter_room.SerializeToString())
        except:
            gl.get_v("serverlogger").logger.error(traceback.format_exc())
    elif game_type.ROOM_CARD == create_room.gameType:
        room_card = base_mode.query_values(RoomCard,
                                           load_only(RoomCard.owner_currency_currency, RoomCard.aa_currency,
                                                     RoomCard.winner_currency),
                                           1, game_id=create_room.gameId, times_type=create_room.timesType,
                                           game_times=create_room.gameTimes, people_count=create_room.peopleCount)
        card = base_mode.query(Currency.currency, 1, user_id=account_session.account,
                               currency_type=currency_type.ROOM_CARD)
        # 房卡不足
        if (None is room_card or None is card) \
                or (0 == create_room.payType and card < room_card.owner_currency_currency) \
                or (1 == create_room.payType and card < room_card.aa_currency) \
                or (2 == create_room.payType and card < room_card.winner_currency):
            send_to_subscribe(REDIS_SUB_GATEWAY, sid, None, CREATE_ROOM, None, NOT_ENOUGH)
            return
        try:
            room_no = gl.get_v("game_command")["create_room"].execute(account_session.account, create_room)
            gl.get_v("serverlogger").logger.info("房间号" + str(room_no))
            send_to_subscribe(REDIS_SUB_GATEWAY, sid, None, CREATE_ROOM, None)
            enter_room = ReqEnterRoom()
            enter_room.roomNo = room_no
            gl.get_v("command")[str(ENTER_ROOM)].execute(sid, room_no, session_id, ip, enter_room.SerializeToString())
        except:
            gl.get_v("serverlogger").logger.error(traceback.format_exc())
