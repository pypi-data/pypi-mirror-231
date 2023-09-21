import datetime
import time

from sqlalchemy import Column, Integer, String, Enum, DateTime, BigInteger

from game_base.mode.data import Base
from game_base.mode.data import base_mode


class UserInfo(Base):
    # 数据库中存储的表名
    __tablename__ = "user_info"
    # 对于必须插入的字段，采用nullable=False进行约束，它相当于NOT NULL
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(32), index=True, nullable=False, comment="姓名")
    age = Column(Integer, nullable=False, comment="年龄")
    phone = Column(String(16), nullable=False, unique=True, comment="手机号")
    address = Column(String(64), nullable=False, comment="地址")
    gender = Column(Enum("male", "female"), default="male", comment="性别")
    create_time = Column(BigInteger, default=int(time.time()), comment="创建时间")
    last_update_time = Column(DateTime, onupdate=datetime.datetime.now, comment="最后更新时间")


base_mode.init("user_info")
