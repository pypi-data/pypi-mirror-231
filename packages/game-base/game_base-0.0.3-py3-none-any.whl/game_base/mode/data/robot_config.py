from sqlalchemy import Column, Integer, String, SmallInteger, BigInteger, DECIMAL

from game_base.mode.data import Base
from game_base.mode.data import base_mode


class RobotConfig(Base):
    # 数据库中存储的表名
    __tablename__ = "robot_config"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    club_id = Column(Integer, default=0, comment="亲友圈id")
    name = Column(String(32), nullable=False, comment="名称")
    create_time = Column(BigInteger, default=0, comment="创建时间")
    status = Column(SmallInteger(), default=0, comment="状态 0.正常 1.暂停")
    game_type = Column(SmallInteger(), default=0, comment="game type")
    game_id = Column(Integer, default=0, comment="game ID")
    score = Column(DECIMAL(10, 2), default=0, comment="底分")
    robot_count = Column(SmallInteger(), default=0, comment="总人数")
    room_min_size = Column(SmallInteger(), default=0, comment="每桌最少人数")
    room_max_size = Column(SmallInteger(), default=0, comment="每桌最大人数")
    min_take_score = Column(DECIMAL(10, 2), default=0, comment="最低带入分")
    max_take_score = Column(DECIMAL(10, 2), default=0, comment="最高带入分")


base_mode.init("robot_config")
