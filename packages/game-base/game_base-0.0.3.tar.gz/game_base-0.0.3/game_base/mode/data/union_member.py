import time
import traceback

import sqlalchemy
from pycore.data.entity import globalvar as gl
from sqlalchemy import Column, Integer, BigInteger, and_, func, SmallInteger
from sqlalchemy.orm import sessionmaker

from game_base import mode
from game_base.base.mode import currency_type
from game_base.mode.data import Base
from game_base.mode.data import base_mode
from game_base.mode.data.account import Account
from game_base.mode.data.club import Club
from game_base.mode.data.club_member import ClubMember
from game_base.mode.data.currency import Currency


class UnionMember(Base):
    # 数据库中存储的表名
    __tablename__ = "union_member"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    union_id = Column(Integer, index=True, comment="联盟id")
    create_time = Column(BigInteger, default=int(time.time()), comment="创建时间")
    club_id = Column(Integer, comment="亲友圈ID")
    status = Column(SmallInteger, default=0, comment="0.待审核 1.正常")


def union_member(union_id, limit, status=1):
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        _select = sqlalchemy.select(UnionMember, Club, Account, ClubMember, Currency,
                                    func.count(ClubMember.id)).outerjoin(Club,
                                                                         UnionMember.club_id == Club.id).outerjoin(
            Account, Club.owner_id == Account.id).outerjoin(ClubMember, and_(ClubMember.club_id == Club.id,
                                                                             ClubMember.user_id == Account.id)).outerjoin(
            Currency,
            and_(Currency.user_id == Account.id, Currency.currency_type == currency_type.UNION_SCORE,
                 Currency.union_id == union_id)).filter(UnionMember.union_id == union_id,
                                                        UnionMember.status == status).offset(limit[0] - 1).limit(
            limit[1])
        return session.execute(_select).all()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


base_mode.init("union_member")
