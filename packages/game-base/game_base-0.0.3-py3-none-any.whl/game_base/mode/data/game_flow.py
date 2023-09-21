import time

from sqlalchemy import Column, Integer, SmallInteger, String, BigInteger, DECIMAL

from game_base.mode.data import Base
from game_base.mode.data import base_mode


class GameFlow(Base):
    # 数据库中存储的表名
    __tablename__ = "game_flow"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    room_no = Column(String(8), nullable=False, comment="room no")
    create_time = Column(BigInteger, default=int(time.time()), comment="create time")
    game_id = Column(SmallInteger, nullable=False, comment="game ID")
    game_type = Column(SmallInteger, nullable=False, comment="game type")
    score = Column(DECIMAL(10, 2), nullable=False, comment="score")
    user_id = Column(Integer, nullable=False, comment="user id")
    win = Column(DECIMAL(10, 2), nullable=False, default=0, comment="win")
    union_id = Column(Integer, nullable=False, default=0, comment="union id")


base_mode.init("game_flow")
