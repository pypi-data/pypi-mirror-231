# coding=utf-8
import traceback

from pycore.data.entity import globalvar as gl

from game_base.mode.data import base_mode
from game_base.mode.data.room_record import RoomRecord


def execute(users, room_no, game_id, settle, union_id):
    r"""
    房间战绩
    :param users: 玩家ID
    :param room_no: 房间信息
    :param game_id: 房间信息
    :param settle: 结算数据
    :param union_id: 联盟id
    :return:
    """
    try:
        room_record = RoomRecord()
        room_record.room_no = room_no
        room_record.game_id = game_id
        room_record.users = users
        room_record.settle = settle
        room_record.union_id = union_id
        base_mode.add(room_record)
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
