import time

from sqlalchemy import Column, Integer, SmallInteger, String, BigInteger, BLOB

from game_base.mode.data import Base
from game_base.mode.data import base_mode


class Record(Base):
    # 数据库中存储的表名
    __tablename__ = "record"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    record_id = Column(String(8), index=True, nullable=False, comment="record ID")
    room_no = Column(String(8), nullable=False, comment="room no")
    create_time = Column(BigInteger, default=int(time.time()), comment="create time")
    game_id = Column(SmallInteger, nullable=False, comment="game ID")
    users = Column(String(256), nullable=False, comment="users")
    game_info = Column(BLOB, comment="game info")
    player_info = Column(BLOB, comment="player info")
    history_actions = Column(BLOB, comment="history actions")
    settle = Column(BLOB, comment="settle")


base_mode.init("record")
