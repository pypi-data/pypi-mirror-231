# coding=utf-8

from pycore.data.entity import globalvar as gl


def execute(sid, room_config_id, session_id, ip, data):
    r"""
    创建房间
    :param sid: 连接id
    :param room_config_id: 房间配置id
    :param session_id: session
    :param ip: ip
    :param data: 收到的数据
    :return:
    """
    gl.get_v("game_command")["create_union_room"].execute(int(room_config_id), data)
