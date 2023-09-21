# coding=utf-8
import traceback

from pycore.data.entity import globalvar as gl
from sqlalchemy.orm import load_only

from game_base.base.constant import REDIS_SUB_GATEWAY
from game_base.base.game.mode import room
from game_base.base.protocol.base.base_pb2 import UNKNOWN_ERROR, ROOM_WIN_LOSE
from game_base.base.protocol.base.game_base_pb2 import RecRoomWinLose
from game_base.base.send_message import send_to_subscribe
from game_base.mode.data import base_mode
from game_base.mode.data.account import Account


def execute(sid, room_no, session_id, ip, data):
    r"""
    房间输赢
    :param sid: 连接id
    :param room_no: 房间号
    :param session_id: session
    :param ip: ip
    :param data: 收到的数据
    :return:
    """
    try:
        _room = room.get_room(room_no)
        total_win_lose_items = sorted(_room.total_win_lose.items(), key=lambda d: d[1]['score'], reverse=True)
        all_user_id = []
        for k, v in total_win_lose_items:
            all_user_id.append(k)
        arges = []
        arges.append(Account.id.in_(all_user_id))
        account_dict = {}
        accounts = base_mode.query_values_by(Account,
                                             load_only(Account.account_name, Account.nickname, Account.head_url), 0,
                                             tuple(arges))
        for account in accounts:
            account_dict[str(account.id)] = account
        rec_room_win_lose = RecRoomWinLose()
        rec_room_win_lose.totalTake = 0
        rec_room_win_lose.totalScore = 0
        for k, v in total_win_lose_items:
            win_lost = rec_room_win_lose.wins.add()
            if k in account_dict:
                win_lost.info.id = account_dict[k].id
                win_lost.info.userId = account_dict[k].account_name
                win_lost.info.nick = account_dict[k].nickname
                win_lost.info.head = account_dict[k].head_url
                score = 0
                seat = _room.get_seat_by_account(k)
                if None is not seat:
                    score = seat.score
                win_lost.take = -v['score'] + score
                win_lost.score = v['score']
                rec_room_win_lose.totalTake += win_lost.take
                if 0 < v['score']:
                    rec_room_win_lose.totalScore += v['score']
        send_to_subscribe(REDIS_SUB_GATEWAY, sid, None, ROOM_WIN_LOSE, rec_room_win_lose.SerializeToString())
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
        send_to_subscribe(REDIS_SUB_GATEWAY, sid, None, ROOM_WIN_LOSE, None, UNKNOWN_ERROR)
