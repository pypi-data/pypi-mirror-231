# coding=utf-8
import traceback

from pycore.data.entity import globalvar as gl
from sqlalchemy.orm import load_only

from game_base.base.constant import REDIS_SUB_GATEWAY
from game_base.base.game.mode import room
from game_base.base.protocol.base.base_pb2 import ROOM_REVIEW, NOT_EXIST
from game_base.base.protocol.base.game_base_pb2 import ReqRoomReview, RecRoomReview
from game_base.base.send_message import send_to_subscribe
from game_base.mode.data import base_mode
from game_base.mode.data.account import Account
from game_base.mode.data.record import Record


def execute(sid, room_no, session_id, ip, data):
    r"""
    执行操作
    :param sid: 连接id
    :param room_no: 房间号
    :param session_id: session
    :param ip: ip
    :param data: 收到的数据
    :return:
    """
    review = ReqRoomReview()
    review.ParseFromString(data)
    try:
        _room = room.get_room(room_no)
        if review.gameTimes < _room.current_game_times:
            record_id = _room.record_ids[review.gameTimes - 1]
            record = base_mode.query_values(Record, load_only(Record.users, Record.settle), 1, record_id=record_id)
            if None is not record:
                users = record.users.split(',')
                users = base_mode.query_values_by(Account,
                                                  load_only(Account.account_name, Account.nickname, Account.head_url),
                                                  0, tuple([Account.id.in_(users)]))
                rec_view = RecRoomReview()
                for u in users:
                    user = rec_view.users.add()
                    user.id = u.id
                    user.userId = u.account_name
                    user.nick = u.nickname
                    user.head = u.head_url
                rec_view.settle.ParseFromString(record.settle)
                send_to_subscribe(REDIS_SUB_GATEWAY, sid, None, ROOM_REVIEW, rec_view.SerializeToString())
                return
        send_to_subscribe(REDIS_SUB_GATEWAY, sid, None, ROOM_REVIEW, None, NOT_EXIST)
        return
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
