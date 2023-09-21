from sqlalchemy import Column, Integer, SmallInteger, DECIMAL

from game_base.mode.data import Base
from game_base.mode.data import base_mode


class RoomCard(Base):
    # 数据库中存储的表名
    __tablename__ = "room_card"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    game_id = Column(SmallInteger, nullable=False, comment="game ID")
    times_type = Column(SmallInteger, nullable=False, comment="times type")
    game_times = Column(Integer, nullable=False, comment="game times")
    people_count = Column(SmallInteger, nullable=False, comment="people count")
    owner_currency = Column(DECIMAL(10, 2), nullable=False, default=0, comment="owner_currency")
    aa_currency = Column(DECIMAL(10, 2), nullable=False, default=0, comment="owner_currency")
    winner_currency = Column(DECIMAL(10, 2), nullable=False, default=0, comment="owner_currency")


base_mode.init("room_card")
