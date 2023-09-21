import time
import traceback

import sqlalchemy
from pycore.data.entity import globalvar as gl
from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DECIMAL, SmallInteger, and_, or_
from sqlalchemy.orm import sessionmaker, load_only, aliased

from game_base import mode
from game_base.base.mode import currency_type
from game_base.mode.data import Base
from game_base.mode.data import base_mode
from game_base.mode.data.account import Account
from game_base.mode.data.currency import Currency


class ClubMember(Base):
    # 数据库中存储的表名
    __tablename__ = "club_member"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    club_id = Column(Integer, index=True, comment="亲友圈id")
    create_time = Column(BigInteger, default=int(time.time()), comment="创建时间")
    user_id = Column(Integer, comment="用户ID")
    agent = Column(Boolean, default=False, comment="是否代理")
    agent_id = Column(Integer, default=0, comment="上级代理")
    agent_ids = Column(String(255), default='', comment="代理关系")
    forewarn = Column(DECIMAL(10, 2), default=0, comment="预警值")
    score_ratio = Column(DECIMAL(3, 2), default=0, comment="分数分成")
    guarantees_ratio = Column(DECIMAL(3, 2), default=0, comment="保底分成")
    status = Column(SmallInteger, default=0, comment="0.待审核 1.正常 2.禁止游戏")
    administrator = Column(Boolean, default=False, comment="是否管理员")


def my_member(club_id, limit, agent_id, union_id):
    """
    我的成员
    :param club_id:
    :param limit:
    :param agent_id:
    :param union_id:
    :return:
    """
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        _select = sqlalchemy.select(ClubMember, Account, Currency).options(
            load_only(Account.account_name, Account.nickname, Account.head_url),
            load_only(Currency.currency, Currency.banker_currency)).outerjoin(Account,
                                                                              ClubMember.user_id == Account.id).outerjoin(
            Currency,
            and_(Currency.user_id == Account.id, Currency.currency_type == currency_type.UNION_SCORE,
                 Currency.union_id == union_id)).filter(ClubMember.club_id == club_id, ClubMember.agent_id == agent_id,
                                                        ClubMember.status > 0).offset(limit[0] - 1).limit(limit[1])
        return session.execute(_select).all()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


def audit_member(club_id, limit, union_id):
    """
    待审核
    :param club_id:
    :param limit:
    :param union_id:
    :return:
    """
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        self_info = aliased(Account)
        up_info = aliased(Account)
        _select = sqlalchemy.select(ClubMember, self_info, up_info, Currency).options(
            load_only(self_info.account_name, self_info.nickname, self_info.head_url),
            load_only(up_info.account_name, up_info.nickname, up_info.head_url),
            load_only(Currency.currency, Currency.banker_currency)).outerjoin(self_info,
                                                                              ClubMember.user_id == self_info.id).outerjoin(
            up_info, ClubMember.agent_id == up_info.id).outerjoin(Currency,
                                                                  and_(Currency.user_id == self_info.id,
                                                                       Currency.currency_type == currency_type.UNION_SCORE,
                                                                       Currency.union_id == union_id)).filter(
            ClubMember.club_id == club_id, ClubMember.status == 0).offset(limit[0] - 1).limit(limit[1])
        return session.execute(_select).all()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


def my_agent(club_id, limit, agent_id, union_id):
    """
    我的代理
    :param club_id:
    :param limit:
    :param agent_id:
    :param union_id:
    :return:
    """
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        self_info = aliased(ClubMember)
        _select = sqlalchemy.select(self_info, Account, Currency).options(
            load_only(self_info.forewarn, self_info.score_ratio, self_info.guarantees_ratio),
            load_only(Account.account_name, Account.nickname, Account.head_url),
            load_only(Currency.currency, Currency.banker_currency)) \
            .outerjoin(Account, self_info.user_id == Account.id) \
            .outerjoin(Currency,
                       and_(Currency.user_id == Account.id, Currency.currency_type == currency_type.UNION_SCORE,
                            Currency.union_id == union_id)) \
            .filter(self_info.club_id == club_id, self_info.agent_id == agent_id, self_info.agent == 1,
                    self_info.status > 0).offset(limit[0] - 1).limit(limit[1])
        return session.execute(_select).all()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


def userids_by_agent(club_id, agent_id):
    """
    代理下面的用户id
    :param club_id:
    :param agent_id:
    :return:
    """
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        _select = sqlalchemy.select(Account.id) \
            .outerjoin_from(ClubMember, Account, ClubMember.user_id == Account.id) \
            .where(ClubMember.club_id == club_id,
                   or_(ClubMember.agent_ids.like('%,' + str(agent_id)), ClubMember.agent_ids.like(str(agent_id) + ',%'),
                       ClubMember.agent_ids.like('%,' + str(agent_id) + ',%'), ClubMember.agent_ids == str(agent_id)))
        return session.execute(_select).scalars().all()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


def all_member(club_id, limit, union_id):
    """
    所有成员
    :param club_id:
    :param limit:
    :param union_id:
    :return:
    """
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        self_info = aliased(Account)
        up_info = aliased(Account)
        _select = sqlalchemy.select(ClubMember, self_info, up_info, Currency).options(
            load_only(self_info.account_name, self_info.nickname, self_info.head_url),
            load_only(up_info.account_name, up_info.nickname, up_info.head_url),
            load_only(Currency.currency, Currency.banker_currency)).outerjoin(self_info,
                                                                              ClubMember.user_id == self_info.id).outerjoin(
            up_info, ClubMember.agent_id == up_info.id).outerjoin(Currency,
                                                                  and_(Currency.user_id == self_info.id,
                                                                       Currency.currency_type == currency_type.UNION_SCORE,
                                                                       Currency.union_id == union_id)).filter(
            ClubMember.club_id == club_id, ClubMember.status > 0).offset(limit[0] - 1).limit(limit[1])
        return session.execute(_select).all()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


def search_member(club_id, union_id, user_id):
    """
    搜索成员
    :param club_id:
    :param union_id:
    :param user_id:
    :return:
    """
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        self_info = aliased(Account)
        up_info = aliased(Account)
        _select = sqlalchemy.select(ClubMember, self_info, up_info, Currency).options(
            load_only(self_info.account_name, self_info.nickname, self_info.head_url),
            load_only(up_info.account_name, up_info.nickname, up_info.head_url),
            load_only(Currency.currency, Currency.banker_currency)).outerjoin(self_info,
                                                                              ClubMember.user_id == self_info.id).outerjoin(
            up_info, ClubMember.agent_id == up_info.id).outerjoin(Currency,
                                                                  and_(Currency.user_id == self_info.id,
                                                                       Currency.currency_type == currency_type.UNION_SCORE,
                                                                       Currency.union_id == union_id)).filter(
            ClubMember.club_id == club_id, self_info.account_name.like('%' + user_id + '%'),
            ClubMember.status > 0)
        return session.execute(_select).all()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


def get_robot(club_id, agent_id):
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        _select = sqlalchemy.select(Account.account_name) \
            .outerjoin_from(ClubMember, Account, ClubMember.user_id == Account.id) \
            .filter(ClubMember.club_id == club_id, ClubMember.agent_id == agent_id, Account.is_robot == 1)
        return session.execute(_select).scalars().all()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


base_mode.init("club_member")
