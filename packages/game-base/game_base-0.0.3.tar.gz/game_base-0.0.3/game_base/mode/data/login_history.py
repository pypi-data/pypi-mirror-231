import time

from sqlalchemy import Column, Integer, SmallInteger, BigInteger, String

from game_base.mode.data import Base
from game_base.mode.data import base_mode


class LoginHistory(Base):
    # 数据库中存储的表名
    __tablename__ = "login_history"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    user_id = Column(Integer, nullable=False, comment="user id")
    login_type = Column(SmallInteger, nullable=False, comment="login type 0.device 1.account 2.phone 4.wechat")
    create_time = Column(BigInteger, default=int(time.time()), comment="create time")
    device = Column(String(64), default='', comment="device")
    ip = Column(String(16), default='', comment="ip")


base_mode.init("login_history")
