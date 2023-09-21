import time

from sqlalchemy import Column, Integer, SmallInteger, DECIMAL, BigInteger

from game_base.mode.data import Base
from game_base.mode.data import base_mode


class BigDataControl(Base):
    # 数据库中存储的表名
    __tablename__ = "big_data_control"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    game_type = Column(SmallInteger(), default=0, comment="game type")
    game_id = Column(Integer, default=0, comment="game ID")
    score = Column(DECIMAL(10, 2), default=0, comment="底分")
    rate = Column(DECIMAL(10, 2), default=0, comment="介入比例")
    create_time = Column(BigInteger, default=int(time.time()), comment="创建时间")
    status = Column(SmallInteger, default=0, comment="0.启用 1.禁用")


base_mode.init("big_data_control")
