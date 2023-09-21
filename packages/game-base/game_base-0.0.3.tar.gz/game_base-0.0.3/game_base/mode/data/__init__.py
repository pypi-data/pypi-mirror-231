from pycore.data.entity import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# 创建引擎
engine = create_engine(
    config.get('db', 'url'),
    # 超过链接池大小外最多创建的链接
    max_overflow=10,
    pool_size=50,
    pool_timeout=10,
    pool_recycle=3600,
    echo=True
)
