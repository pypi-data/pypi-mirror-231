import time

from sqlalchemy import Column, Integer, SmallInteger, DECIMAL, Boolean, BigInteger

from game_base.mode.data import Base
from game_base.mode.data import base_mode


class PlayerControl(Base):
    # 数据库中存储的表名
    __tablename__ = "player_control"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    user_id = Column(Integer, nullable=False, comment="用户id")
    union_id = Column(Integer, comment="联盟id")
    game_type = Column(SmallInteger(), default=0, comment="game type")
    game_id = Column(Integer, default=0, comment="game ID")
    score = Column(DECIMAL(10, 2), default=0, comment="底分")
    rate = Column(DECIMAL(10, 2), default=0, comment="介入比例")
    min_value = Column(DECIMAL(10, 2), default=0, comment="最小值")
    max_value = Column(DECIMAL(10, 2), default=0, comment="最大值")
    current_value = Column(DECIMAL(10, 2), default=0, comment="当前分")
    finish_value = Column(DECIMAL(10, 2), default=0, comment="完成值")
    is_finish = Column(Boolean, default=False, comment="是否完成")
    create_time = Column(BigInteger, default=int(time.time()), comment="创建时间")
    status = Column(SmallInteger, default=0, comment="0.启用 1.禁用")


base_mode.init("player_control")
