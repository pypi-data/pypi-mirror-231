import time
import traceback

import sqlalchemy
from pycore.data.entity import globalvar as gl
from sqlalchemy import Column, Integer, String, SmallInteger, Boolean, DECIMAL, BigInteger
from sqlalchemy.orm import sessionmaker, load_only

from game_base import mode
from game_base.mode.data import Base
from game_base.mode.data import base_mode
from game_base.mode.data.club import Club
from game_base.mode.data.club_member import ClubMember
from game_base.mode.data.union_member import UnionMember


class Union(Base):
    # 数据库中存储的表名
    __tablename__ = "union"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    union_id = Column(String(8), index=True, comment="联盟id")
    club_id = Column(String(8), index=True, comment="亲友圈id")
    name = Column(String(32), index=True, nullable=False, comment="联盟名称")
    create_time = Column(BigInteger, default=0, comment="创建时间")
    last_update_time = Column(BigInteger, onupdate=0, comment="最后更新时间")
    status = Column(SmallInteger, nullable=False, default=0, comment="status")
    game_status = Column(SmallInteger(), default=1, comment="状态 0.暂停 1.正常")
    union_status = Column(SmallInteger(), default=0, comment="状态 0.亲友圈 1.联盟")
    game_type = Column(SmallInteger(), default=3, comment="game_type")
    owner_id = Column(Integer, comment="拥有者")
    join_audit = Column(Boolean, default=False, comment="加入需要审核")
    quit_audit = Column(Boolean, default=False, comment="退出需要审核")
    score = Column(DECIMAL(10, 2), nullable=False, default=0, comment="总分数")
    notice = Column(String(255), default='', comment="公告")
    view_rooms = Column(SmallInteger, nullable=False, default=0, comment="开桌显示")


# def union_list(club_id, limit):
#     session = None
#     try:
#         Session = sessionmaker(mode.data.engine)
#         session = Session()
#         return session.query(Union.id, Union.union_id, Union.name).join(UnionMember,
#                                                                         Union.id == UnionMember.union_id).filter(
#             UnionMember.club_id == club_id).offset(limit[0] - 1).limit(limit[1])
#     except:
#         gl.get_v("serverlogger").logger.error(traceback.format_exc())
#     finally:
#         if None is not session:
#             session.close()

def union_list(club_id):
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        _select = sqlalchemy.select(Union).options(
            load_only(Union.union_id, Union.game_type, Union.union_status, Union.name, Union.owner_id)).join(
            UnionMember, Union.id == UnionMember.union_id).filter(UnionMember.club_id == club_id)
        return session.execute(_select).scalars().all()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


def union_players(union_id):
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        _select_clubs = sqlalchemy.select(Club.id) \
            .outerjoin(UnionMember, UnionMember.club_id == Club.id) \
            .where(UnionMember.union_id == union_id)
        club_ids = session.execute(_select_clubs).scalars().all()

        _select = sqlalchemy.select(ClubMember.user_id) \
            .where(ClubMember.club_id.in_(club_ids))
        return session.execute(_select).scalars().all()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()

base_mode.init("union")
