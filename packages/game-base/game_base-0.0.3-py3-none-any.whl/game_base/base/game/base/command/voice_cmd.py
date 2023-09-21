# coding=utf-8
import traceback

from pycore.data.entity import globalvar as gl

from game_base.base.constant import REDIS_ACCOUNT_SESSION
from game_base.base.game.mode import room
from game_base.base.protocol.base.base_pb2 import PLAYER_VOICE
from game_base.base.protocol.base.game_base_pb2 import ReqPlayerVoice, RecPlayerVoice


def execute(sid, room_no, session_id, ip, data):
    r"""
    语音
    :param sid: 连接id
    :param room_no: 房间号
    :param session_id: session
    :param ip: ip
    :param data: 收到的数据
    :return:
    """
    req_player_voice = ReqPlayerVoice()
    req_player_voice.ParseFromString(data)
    rec_player_voice = RecPlayerVoice()
    rec_player_voice.voiceData = req_player_voice.voiceData
    account_session = gl.get_v("redis").getobj(REDIS_ACCOUNT_SESSION + session_id)
    rec_player_voice.playerId = account_session.account
    try:
        _room = room.get_room(room_no)
        _room.broadcast_all_to_gateway(PLAYER_VOICE, rec_player_voice.SerializeToString())
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
