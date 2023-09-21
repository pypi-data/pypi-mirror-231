import time

from pycore.utils.stringutils import StringUtils
from sqlalchemy import Column, Integer, String, BigInteger, SmallInteger, Boolean

from game_base.mode.data import Base
from game_base.mode.data import base_mode


class Account(Base):
    # 数据库中存储的表名
    __tablename__ = "account"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    account_name = Column(String(32), index=True, nullable=False, comment="account")
    nickname = Column(String(8), nullable=False, default='', comment="nickname")
    sex = Column(SmallInteger, nullable=False, default=0, comment="sex(0.unknown 1.man 2.woman)")
    head_url = Column(String(32), nullable=False, default='', comment="head url")
    pwd = Column(String(32), comment="pwd")
    salt = Column(String(32), comment="salt")
    create_time = Column(BigInteger, default=0, comment="create time")
    status = Column(SmallInteger, nullable=False, default=0, comment="status")
    bank_pwd = Column(String(32), comment="bank pwd")
    # 权限
    authority = Column(SmallInteger, nullable=False, default=0, comment="authority")
    phone = Column(String(16), default='', comment="phone number")
    email = Column(String(64), default='', comment="email")
    wechat = Column(String(64), default='', comment="register wechat")
    device = Column(String(64), default='', comment="register device")
    ip = Column(String(16), default='', comment="register ip")
    code = Column(String(4), default='', comment="code")
    is_robot = Column(Boolean, default=False, comment="robot")


def create_account(phone, email, wechat, device, ip, password=None, is_robot=False, account_name=None):
    salt = None
    _password = None
    if None is not password:
        salt = StringUtils.randomStr(32)
        _password = StringUtils.md5(password + salt)
    code = StringUtils.randomStr(4).upper()
    while base_mode.query(Account, -1, code=code):
        code = StringUtils.randomStr(4).upper()
    if None is account_name:
        account_name = StringUtils.randomNum(6)
        while base_mode.query(Account, -1, account_name=account_name):
            account_name = StringUtils.randomNum(6)
    account = Account()
    account.account_name = account_name
    account.nickname = "dd_" + StringUtils.randomStr(4)
    account.phone = phone
    account.email = email
    account.wechat = wechat
    account.device = device
    account.salt = salt
    account.pwd = _password
    account.is_robot = is_robot
    account.create_time = int(time.time())
    account.ip = ip
    account.code = code
    account_id = base_mode.add(account)
    from game_base.mode.data import currency
    currency.init_account_currency(account_id)
    return base_mode.get(Account, account_id)

base_mode.init("account")
