import logging
import threading

from flask import Flask, has_request_context, request
from flask.logging import default_handler
from flask_socketio import SocketIO
from pycore.data.entity import config, globalvar as gl
from pycore.utils.batch_queue import BatchQueue
from pycore.utils.logger_utils import LoggerUtils
from pycore.utils.redis_utils import RedisUtils
from pycore.utils.stringutils import StringUtils

from game_base.utils.send_mail import SendMail

config.init("./conf/pyg.conf")
gl.init()


def init_logger():
    pass
    # log_fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    # logging.basicConfig(level=logging.DEBUG, format=log_fmt)
    # formatter = RequestFormatter(log_fmt)
    # log_file_handler = TimedRotatingFileHandler(
    #     filename='./logs/geventwebsocket.log', when="H", interval=1, backupCount=24, encoding='utf-8')
    # log_file_handler.suffix = "%Y-%m-%d_%H.log"
    # log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
    # log_file_handler.setFormatter(formatter)
    # log_file_handler.setLevel(logging.DEBUG)
    # logger = logging.getLogger('geventwebsocket.handler')
    # logger.addHandler(log_file_handler)
    #
    # log_file_handler = TimedRotatingFileHandler(
    #     filename='./logs/engineio.log', when="H", interval=1, backupCount=24, encoding='utf-8')
    # log_file_handler.suffix = "%Y-%m-%d_%H.log"
    # log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
    # log_file_handler.setFormatter(formatter)
    # log_file_handler.setLevel(logging.DEBUG)
    # logger = logging.getLogger('engineio.server')
    # logger.addHandler(log_file_handler)
    #
    # formatter = RequestFormatter(log_fmt)
    # log_file_handler = TimedRotatingFileHandler(
    #     filename='./logs/socketio.log', when="H", interval=1, backupCount=24, encoding='utf-8')
    # log_file_handler.suffix = "%Y-%m-%d_%H.log"
    # log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
    # log_file_handler.setFormatter(formatter)
    # log_file_handler.setLevel(logging.DEBUG)
    # logger = logging.getLogger('socketio.server')
    # logger.addHandler(log_file_handler)


class Server(object):
    @staticmethod
    def init(name, api=None, port=None, handles=None, redis_keys=None, subject=None, sub_handle=None, s_handle=None,
             mail=False):
        uuid = StringUtils.randomStr(32)
        gl.set_v("uuid", uuid)
        gl.set_v("serverlogger", LoggerUtils(name))
        gl.set_v("redis", RedisUtils())
        gl.set_v("uid_sid", {})
        if None is not subject:
            gl.get_v("redis").startSubscribe(subject, sub_handle)
        if None is not handles:
            i = 0
            for handle in handles:
                threading.Thread(target=handle.handle, args=(handle(), redis_keys[i]),
                                 name=name + 'handle').start()  # 线程对象.
                i += 1
        if mail:
            threading.Thread(target=SendMail.handle, args=(SendMail(),), name=name + 'mail_handle').start()  # 线程对象.
        if None is not port:
            gl.set_v("close", False)
            gl.set_v("clients", {})
            gl.set_v("queue", BatchQueue())
            app = Flask(__name__)
            app.secret_key = "l0pgtb2k4lfstpuau672q4f67c7cyrsj"
            app.register_blueprint(api)
            app.jinja_env.auto_reload = True
            formatter = RequestFormatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            default_handler.setFormatter(formatter)
            init_logger()
            socketio = SocketIO(app, cors_allowed_origins="*", async_mode="gevent", ping_interval=5, logger=True,
                                max_http_buffer_size=1024)
            gl.set_v("socketio", socketio)
            gl.get_v("socketio").on_event('message', s_handle.on_message)
            gl.get_v("socketio").on_event('connect', s_handle.on_connect)
            gl.get_v("socketio").on_event('disconnect', s_handle.on_disconnect)
            # threading.Thread(target=send_message.real_send, name=name + 'real_send').start()  # 线程对象.
            socketio.run(app, host="0.0.0.0", port=port)

    @staticmethod
    def init_command(command, name="command"):
        gl.set_v(name, command)


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)
