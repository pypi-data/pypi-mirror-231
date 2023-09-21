import time

from sqlalchemy import Column, Integer, String, BigInteger

from game_base.mode.data import Base
from game_base.mode.data import base_mode


class IpInfo(Base):
    # 数据库中存储的表名
    __tablename__ = "ip_info"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    create_time = Column(BigInteger, default=int(time.time()), comment="创建时间")
    code = Column(String(4), nullable=False, default='', comment="code")
    ip = Column(String(16), default='', comment="ip")


base_mode.init("ip_info")
