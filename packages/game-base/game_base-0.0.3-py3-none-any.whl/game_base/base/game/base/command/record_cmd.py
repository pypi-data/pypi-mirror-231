# coding=utf-8
import pickle
import traceback

from pycore.data.entity import globalvar as gl
from pycore.utils.stringutils import StringUtils

from game_base.mode.data import base_mode
from game_base.mode.data.record import Record


def execute(users, room_no, game_id, game_info, player_info, history_actions, settle):
    r"""
    战绩
    :param users: 玩家ID
    :param room_no: 房间号
    :param game_id: 游戏id
    :param game_info: 游戏信息
    :param player_info: 玩家信息
    :param history_actions: 操作记录
    :param settle: 结算数据
    :return:
    """
    try:
        record_id = StringUtils.randomStr(8).upper()
        while base_mode.query(Record, -1, record_id=record_id):
            record_id = StringUtils.randomStr(8).upper()
        record = Record()
        record.record_id = record_id
        record.room_no = room_no
        record.game_id = game_id
        record.users = users
        record.game_info = game_info
        record.player_info = player_info
        record.history_actions = pickle.dumps(history_actions, -1)
        record.settle = settle
        base_mode.add(record)
        return record_id
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    return None
