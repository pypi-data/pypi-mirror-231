import time
import traceback

import sqlalchemy
from pycore.data.entity import globalvar as gl
from sqlalchemy import Column, Integer, String, SmallInteger, Boolean, BigInteger
from sqlalchemy.orm import sessionmaker, load_only

from game_base import mode
from game_base.mode.data import Base
from game_base.mode.data import base_mode
from game_base.mode.data.club_member import ClubMember


class Club(Base):
    # 数据库中存储的表名
    __tablename__ = "club"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    club_id = Column(String(8), index=True, comment="亲友圈id")
    name = Column(String(32), nullable=False, comment="亲友圈名称")
    create_time = Column(BigInteger, default=int(time.time()), comment="创建时间")
    last_update_time = Column(BigInteger, onupdate=int(time.time()), comment="最后更新时间")
    status = Column(SmallInteger(), default=1, comment="状态 0.暂停 1.正常")
    owner_id = Column(Integer, comment="拥有者")
    join_audit = Column(Boolean, default=False, comment="加入需要审核")
    quit_audit = Column(Boolean, default=False, comment="退出需要审核")
    area_id = Column(Integer, comment="区域id")


def club_list(user_id, limit):
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        _select = sqlalchemy.select(Club).options(
            load_only(Club.club_id, Club.name, Club.area_id)).join(ClubMember, Club.id == ClubMember.club_id).filter(
            ClubMember.user_id == user_id, ClubMember.status > 0).offset(
            limit[0] - 1).limit(limit[1])
        return session.execute(_select).scalars().all()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


base_mode.init("club")
