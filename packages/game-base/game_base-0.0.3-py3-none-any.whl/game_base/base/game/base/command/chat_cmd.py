# coding=utf-8
import traceback

from pycore.data.entity import globalvar as gl

from game_base.base.constant import REDIS_ACCOUNT_SESSION
from game_base.base.game.mode import room
from game_base.base.protocol.base.base_pb2 import PLAYER_CHAT
from game_base.base.protocol.base.game_base_pb2 import ReqPlayerChat, RecPlayerChat


def execute(sid, room_no, session_id, ip, data):
    r"""
    聊天
    :param sid: 连接id
    :param room_no: 房间号
    :param session_id: session
    :param ip: ip
    :param data: 收到的数据
    :return:
    """
    req_player_chat = ReqPlayerChat()
    req_player_chat.ParseFromString(data)
    rec_player_chat = RecPlayerChat()
    rec_player_chat.msg = req_player_chat.msg
    rec_player_chat.type = req_player_chat.type
    account_session = gl.get_v("redis").getobj(REDIS_ACCOUNT_SESSION + session_id)
    rec_player_chat.playerId = account_session.account
    try:
        _room = room.get_room(room_no)
        _room.broadcast_all_to_gateway(PLAYER_CHAT, rec_player_chat.SerializeToString())
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
