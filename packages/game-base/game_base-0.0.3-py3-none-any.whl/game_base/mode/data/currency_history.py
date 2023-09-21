import time
import traceback

import sqlalchemy
from pycore.data.entity import globalvar as gl
from sqlalchemy import Column, Integer, SmallInteger, DECIMAL, String, BigInteger
from sqlalchemy.orm import sessionmaker, aliased, load_only

from game_base import mode
from game_base.mode.data import Base
from game_base.mode.data import base_mode
from game_base.mode.data.account import Account


class CurrencyHistory(Base):
    # 数据库中存储的表名
    __tablename__ = "currency_history"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    user_id = Column(Integer, nullable=False, comment="user id")
    currency_type = Column(SmallInteger, nullable=False, comment="currency type  1.room card 2.gold")
    union_id = Column(Integer, nullable=False, default=0, comment="union id")
    currency = Column(DECIMAL(10, 2), nullable=False, default=0, comment="currency")
    create_time = Column(BigInteger, default=int(time.time()), comment="create time")
    banker_currency = Column(DECIMAL(10, 2), nullable=False, default=0, comment="banker currency")
    before_currency = Column(DECIMAL(10, 2), nullable=False, default=0, comment="before currency")
    before_banker_currency = Column(DECIMAL(10, 2), nullable=False, default=0, comment="before banker currency")
    after_currency = Column(DECIMAL(10, 2), nullable=False, default=0, comment="after currency")
    after_banker_currency = Column(DECIMAL(10, 2), nullable=False, default=0, comment="after banker currency")
    type = Column(SmallInteger, nullable=False, comment="type 1.game 2.register 3.invite")
    remark = Column(String(64), default='', comment="remark")
    source = Column(String(64), default='', comment="source")


def give_score_history(limit, criterias):
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        self_info = aliased(Account)
        source_info = aliased(Account)
        _select = sqlalchemy.select(CurrencyHistory, self_info, source_info).options(
            load_only(self_info.account_name, self_info.nickname, self_info.head_url),
            load_only(source_info.account_name, source_info.nickname, source_info.head_url)).outerjoin(self_info,
                                                                                                       CurrencyHistory.user_id == self_info.id).outerjoin(
            source_info, CurrencyHistory.source == source_info.id).where(*criterias).offset(limit[0] - 1).limit(
            limit[1])
        return session.execute(_select).all()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


base_mode.init("currency_history")
