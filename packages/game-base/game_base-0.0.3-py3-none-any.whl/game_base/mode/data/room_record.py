import time

from sqlalchemy import Column, Integer, SmallInteger, String, BigInteger, BLOB

from game_base.mode.data import Base
from game_base.mode.data import base_mode


class RoomRecord(Base):
    # 数据库中存储的表名
    __tablename__ = "room_record"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    room_no = Column(String(8), nullable=False, comment="room no")
    create_time = Column(BigInteger, default=int(time.time()), comment="create time")
    game_id = Column(SmallInteger, nullable=False, comment="game ID")
    users = Column(String(256), nullable=False, comment="users")
    settle = Column(BLOB, comment="settle")
    union_id = Column(Integer, nullable=False, comment="union id")


base_mode.init("room_record")
