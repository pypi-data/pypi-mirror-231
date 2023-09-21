import decimal

from sqlalchemy import Column, Integer, SmallInteger, DECIMAL

from game_base.base.constant import REDIS_MESSAGE_LIST_COORDINATE_SERVER
from game_base.base.mode import currency_type
from game_base.base.protocol.base.base_pb2 import UPDATE_CURRENCY
from game_base.base.send_message import send_message_to_server, user_id2_sid
from game_base.mode.data import Base
from game_base.mode.data import base_mode
from game_base.mode.data.currency_history import CurrencyHistory


class Currency(Base):
    # 数据库中存储的表名
    __tablename__ = "currency"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    user_id = Column(Integer, nullable=False, comment="user id")
    currency = Column(DECIMAL(10, 2), nullable=False, default=0, comment="currency")
    banker_currency = Column(DECIMAL(10, 2), nullable=False, default=0, comment="banker currency")
    currency_type = Column(SmallInteger, nullable=False, comment="currency type")
    union_id = Column(Integer, nullable=False, default=0, comment="union id")


def init_account_currency(account_id):
    currencies = []
    currency = Currency()
    currency.user_id = account_id
    currency.currency_type = currency_type.GOLD
    currencies.append(currency)
    currency = Currency()
    currency.user_id = account_id
    currency.currency_type = currency_type.ROOM_CARD
    currencies.append(currency)
    currency = Currency()
    currency.user_id = account_id
    currency.currency_type = currency_type.VOUCHERS
    currencies.append(currency)
    base_mode.add_all(currencies)


def add_currency(user_id, _currency_type, union_id=0):
    if not base_mode.query(Currency, -1, user_id=user_id, currency_type=currency_type, union_id=union_id):
        currency = Currency()
        currency.user_id = user_id
        currency.currency_type = _currency_type
        currency.union_id = union_id
        base_mode.add(currency)


def operation_currency(user_id, _currency_type, currency, bank_currency, optype, source, union=0):
    if 0 == currency and 0 == bank_currency:
        return
    before_currency = base_mode.query(Currency, 1, user_id=user_id, currency_type=_currency_type)
    operation = {}
    if 0 != currency:
        operation['currency'] = Currency.currency + decimal.Decimal.from_float(currency)
    if 0 != bank_currency:
        operation['banker_currency'] = Currency.banker_currency + decimal.Decimal.from_float(bank_currency)

    base_mode.update(Currency, operation, user_id=user_id, currency_type=_currency_type, union_id=union)
    currency_history = CurrencyHistory()
    currency_history.user_id = user_id
    currency_history.currency_type = _currency_type
    currency_history.union_id = union
    currency_history.currency = currency
    currency_history.banker_currency = bank_currency
    currency_history.before_currency = float(before_currency.currency)
    currency_history.before_banker_currency = float(before_currency.banker_currency)
    currency_history.after_currency = float(before_currency.currency) + currency
    currency_history.after_banker_currency = float(before_currency.banker_currency) + bank_currency
    currency_history.type = optype
    currency_history.source = source
    base_mode.add(currency_history)
    sid = user_id2_sid(user_id)
    send_message_to_server(REDIS_MESSAGE_LIST_COORDINATE_SERVER, UPDATE_CURRENCY, None, '', sid)


base_mode.init("currency")
