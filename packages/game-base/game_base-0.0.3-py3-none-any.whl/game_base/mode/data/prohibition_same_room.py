import time

from sqlalchemy import Column, Integer, BigInteger, String

from game_base.mode.data import Base
from game_base.mode.data import base_mode


class ProhibitionSameRoom(Base):
    # 数据库中存储的表名
    __tablename__ = "prohibition_same_room"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    union_id = Column(Integer, comment="联盟id")
    user_ids = Column(String(255), nullable=False, comment="user ids")
    create_time = Column(BigInteger, default=0, comment="创建时间")


base_mode.init("prohibition_same_room")
