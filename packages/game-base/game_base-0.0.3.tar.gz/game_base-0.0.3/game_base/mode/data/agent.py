import time

from sqlalchemy import Column, Integer, BigInteger, String, Boolean

from game_base.mode.data import Base
from game_base.mode.data import base_mode


class Agent(Base):
    # 数据库中存储的表名
    __tablename__ = "agent"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    create_time = Column(BigInteger, default=int(time.time()), comment="创建时间")
    user_id = Column(Integer, comment="用户ID")
    agent = Column(Boolean, default=False, comment="是否代理")
    agent_id = Column(Integer, default=0, comment="上级代理")
    agent_ids = Column(String(255), default='', comment="代理关系")


base_mode.init("agent")
