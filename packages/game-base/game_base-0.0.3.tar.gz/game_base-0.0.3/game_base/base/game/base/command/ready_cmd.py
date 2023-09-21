# coding=utf-8
import traceback

from pycore.data.entity import globalvar as gl

from game_base.base.constant import REDIS_ACCOUNT_SESSION, REDIS_ROOM_LOCK, REDIS_ROOM_TIMEOUT_LIST
from game_base.base.game.mode import room
from game_base.base.game.mode.game_status import GameStatus
from game_base.base.protocol.base.base_pb2 import READY
from game_base.base.protocol.base.game_base_pb2 import ReqReadyGame, RecReadyGame


def execute(sid, room_no, session_id, ip, data):
    r"""
    准备
    :param sid: 连接id
    :param room_no: 房间号
    :param session_id: session
    :param ip: ip
    :param data: 收到的数据
    :return:
    """
    account_session = gl.get_v("redis").getobj(REDIS_ACCOUNT_SESSION + session_id)
    ready = ReqReadyGame()
    ready.ParseFromString(data)
    gl.get_v("redis").lock(REDIS_ROOM_LOCK + room_no)
    try:
        _room = room.get_room(room_no)
        if _room.game_status == GameStatus.WAITING:
            seat = _room.get_seat_by_account(account_session.account)
            if seat is not None:
                if None is not seat.ready_timeout:
                    gl.get_v("redis").zrem(REDIS_ROOM_TIMEOUT_LIST + str(_room.game_id), seat.ready_timeout)
                    seat.ready_timeout = None
                seat.ready = ready.ready
                ready_game = RecReadyGame()
                ready_game.seatNo = seat.seat_no
                ready_game.ready = seat.ready
                _room.broadcast_seat_to_gateway(READY, ready_game.SerializeToString())
                _room.check_ready()
                _room.save()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    gl.get_v("redis").unlock(REDIS_ROOM_LOCK + room_no)
