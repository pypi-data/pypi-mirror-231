from sqlalchemy import Column, Integer, BigInteger, DECIMAL, SmallInteger, Boolean

from game_base.mode.data import Base
from game_base.mode.data import base_mode


class RobotCXData(Base):
    # 数据库中存储的表名
    __tablename__ = "robot_cx_data"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    current_score = Column(DECIMAL(10, 1), default=0, comment="当前最低下注分")
    current_play = Column(DECIMAL(10, 1), default=0, comment="当前已下注")
    current_cards_size = Column(SmallInteger, default=0, comment="当前牌数")
    current_count = Column(SmallInteger, default=0, comment="当前当前剩余人数")
    current_max = Column(SmallInteger, default=0, comment="当前桌面最大值")
    current_has_q = Column(Boolean, default=0, comment="是否有q")
    current_has_2 = Column(Boolean, default=0, comment="是否有2")
    abandon_pass_count = Column(BigInteger, default=0, comment="丢休次数")
    play_1_count = Column(BigInteger, default=0, comment="下注小于2倍次数")
    play_2_count = Column(BigInteger, default=0, comment="下注小于5倍次数")
    play_3_count = Column(BigInteger, default=0, comment="下注小于10倍次数")
    play_4_count = Column(BigInteger, default=0, comment="下注小于20倍次数")
    play_5_count = Column(BigInteger, default=0, comment="下注小于50倍次数")
    play_6_count = Column(BigInteger, default=0, comment="下注小于100倍次数")
    play_7_count = Column(BigInteger, default=0, comment="下注小于200倍次数")
    play_8_count = Column(BigInteger, default=0, comment="下注小于500倍次数")
    play_9_count = Column(BigInteger, default=0, comment="下注小于1000倍次数")
    play_10_count = Column(BigInteger, default=0, comment="下注大于1000倍次数")


base_mode.init("robot_cx_data")
