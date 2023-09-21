import base64

from pycore.data.entity import globalvar as gl
from pycore.utils import aes_utils

from game_base.base.constant import REDIS_ACCOUNT_SID, REDIS_SUB_GATEWAY
from game_base.base.protocol.base.base_pb2 import NetMessage, SUCCESS, Opcode
from game_base.base.protocol.base.gateway_pb2 import GateWayMessage, ServerMessage


def send_data(opcode, data, to=None, skip=None, code=SUCCESS):
    r"""
    发送消息
    :param opcode: 消息码
    :param data: 数据
    :param to: 发送的人
    :param skip: 排除的人
    :param code: 错误码
    :return:
    """
    gl.get_v("serverlogger").logger.info("发送%s给%s" % (Opcode.Name(opcode), to))
    _net_message = NetMessage()
    _net_message.opcode = opcode
    _net_message.errorCode = code
    if data is not None:
        _net_message.data = data.SerializeToString()
    encrypt_send(data=base64.b64encode(_net_message.SerializeToString()).decode('utf-8'), to=to, skip=skip)


def send_message(message, to, skip=None):
    r"""
    发送消息
    :param message: 消息
    :param to: 发送的人
    :param skip: 排除的人
    :return:
    """
    encrypt_send(data=base64.b64encode(message).decode('utf-8'), to=to, skip=skip)


def encrypt_send(data, to, skip):
    r"""
    加密发送
    :param data: 数据
    :param to: 发送的人
    :param skip: 排除的人
    :return:
    """
    _server = gl.get_v("socketio")
    if to in gl.get_v("clients"):
        # m = {"message": aes_utils.aes_encode(data, gl.get_v("clients")[to]["key"]), "to": to, "skip_sid": skip}
        # gl.get_v("queue").put(m)
        _server.emit('message', aes_utils.aes_encode(data, gl.get_v("clients")[to]["key"]), to=to, skip_sid=skip)


def real_send():
    pass
    # while True:
    #     try:
    #         messages = gl.get_v("queue").getall(20, True, 20)
    #         for message in messages:
    #             gl.get_v("socketio").emit('message', message["message"], to=message["to"], skip_sid=message["skip_sid"])
    #     except queue.Empty:
    #         pass
    #     except:
    #         gl.get_v("serverlogger").logger.info(traceback.format_exc())


def send_to_server(key, data, ip, sid, room_no=None, session_id=None):
    r"""
    发送消息到其它服务器
    :param key: 其它服务器的监听
    :param data: 数据
    :param ip: ip
    :param sid: sid
    :param room_no: 房间号
    :param session_id: session id
    :return:
    """
    _send_data = GateWayMessage()
    _send_data.ip = ip
    _send_data.sid = sid
    if room_no is not None:
        _send_data.roomNo = room_no
    if session_id is not None:
        _send_data.session_id = session_id
    _send_data.data = data
    gl.get_v("redis").lpush(key, _send_data.SerializeToString())


def send_message_to_server(key, opcode, data, ip, sid, room_no=None, session_id=None):
    r"""
    发送消息到其它服务器
    :param key: 其它服务器的监听
    :param opcode: 消息码
    :param data: 数据
    :param ip:
    :param sid:
    :param room_no: 房间号
    :param session_id: session id
    :return:
    """
    _net_message = NetMessage()
    _net_message.opcode = opcode
    if None is not data:
        _net_message.data = data
    _send_data = GateWayMessage()
    _send_data.ip = ip
    if None is not sid:
        _send_data.sid = sid
    if room_no is not None:
        _send_data.roomNo = room_no
    if session_id is not None:
        _send_data.session_id = session_id
    _send_data.data = _net_message.SerializeToString()
    gl.get_v("serverlogger").logger.info("服务器发送%s给%s" % (Opcode.Name(opcode), sid))
    gl.get_v("redis").lpush(key, _send_data.SerializeToString())


def send_to_subscribe(sub, to, skip, opcode, data, code=SUCCESS):
    r"""
    发送消息到redis
    :param sub: redis监听
    :param to: 发送的人
    :param skip: 排除的人
    :param opcode: 消息码
    :param data: 数据
    :param code: 错误码
    :return:
    """
    gl.get_v("serverlogger").logger.info("服务器发送%s给%s" % (Opcode.Name(opcode), to))
    _net_message = NetMessage()
    _net_message.opcode = opcode
    _net_message.errorCode = code
    if None is not data:
        _net_message.data = data
    _message = ServerMessage()
    _message.to = to
    if None is not skip:
        _message.skip = skip
    _message.data = _net_message.SerializeToString()
    gl.get_v("redis").publish(sub, _message.SerializeToString())


def send_to_gateway(opcode, data, user_id, code=SUCCESS):
    r"""
    发送消息到网关
    :param opcode: 消息码
    :param data: 数据
    :param user_id: 发送的人
    :param code: 错误码
    :return:
    """
    _sid = user_id2_sid(user_id)
    if None is not _sid:
        send_to_subscribe(REDIS_SUB_GATEWAY, _sid, None, opcode, data, code)


def user_id2_sid(user_id):
    r"""
    user_id转sid
    :return:
    """
    # if user_id in gl.get_v("uid_sid"):
    #     return gl.get_v("uid_sid")[user_id]
    if gl.get_v("redis").hexists(REDIS_ACCOUNT_SID, user_id):
        _sid = gl.get_v("redis").hget(REDIS_ACCOUNT_SID, user_id)
        return _sid
    return None
