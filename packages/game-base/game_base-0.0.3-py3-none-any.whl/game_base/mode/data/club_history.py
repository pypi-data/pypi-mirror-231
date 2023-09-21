import traceback

import sqlalchemy
from pycore.data.entity import globalvar as gl
from sqlalchemy import Column, Integer, BigInteger, String
from sqlalchemy.orm import sessionmaker

from game_base import mode
from game_base.mode.data import Base
from game_base.mode.data import base_mode


class ClubHistory(Base):
    # 数据库中存储的表名
    __tablename__ = "club_history"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    user_id = Column(Integer, nullable=False, comment="user id")
    club_id = Column(Integer, nullable=False, comment="club id")
    union_id = Column(Integer, nullable=False, comment="union id")
    create_time = Column(BigInteger, default=0, comment="create time")
    ip = Column(String(16), default='', comment="ip")


def last_club_id(user_id):
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        _select = sqlalchemy.select(ClubHistory.club_id).where(ClubHistory.user_id == user_id).order_by(
            ClubHistory.create_time.desc())
        return session.execute(_select).scalars().first()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


base_mode.init("club_history")
