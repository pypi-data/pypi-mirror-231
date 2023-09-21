from sqlalchemy import Column, Integer, String, SmallInteger, BigInteger, BLOB

from game_base.mode.data import Base
from game_base.mode.data import base_mode


class RoomConfig(Base):
    # 数据库中存储的表名
    __tablename__ = "room_config"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    union_id = Column(Integer, default=0, comment="联盟id")
    name = Column(String(32), nullable=False, comment="名称")
    create_time = Column(BigInteger, default=0, comment="创建时间")
    status = Column(SmallInteger(), default=0, comment="状态 0.正常 1.暂停")
    game_type = Column(SmallInteger(), default=0, comment="game type")
    game_id = Column(Integer, default=0, comment="game ID")
    create_room = Column(BLOB, comment="create room")


base_mode.init("room_config")
