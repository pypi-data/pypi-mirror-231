import traceback

import sqlalchemy
from pycore.data.entity import globalvar as gl
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker, scoped_session

from game_base import mode
from game_base.mode.data import Base, engine


def init(table_name):
    session = None
    try:
        session = scoped_session(sessionmaker(bind=engine))
        if not session.connection().dialect.has_table(session.connection(), table_name):
            Base.metadata.tables[table_name].create(session.connection())
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    session.remove()


def get(entity, id):
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        return session.get(entity, id)
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


def query(entities, limit, **kwargs):
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        _select = sqlalchemy.select(entities).filter_by(**kwargs)
        if 1 == limit:
            return session.execute(_select).scalars().first()
        elif 0 == limit:
            return session.execute(_select).scalars().all()
        elif -1 == limit:
            _select.where(sqlalchemy.exists())
            return session.execute(_select).scalar()
        else:
            return session.execute(_select.offset((limit[0] - 1) * limit[1]).limit(limit[1])).scalars().all()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


def query_by(entities, limit, criterias):
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        if 0 != len(criterias):
            _select = sqlalchemy.select(entities).where(*criterias)
        else:
            _select = sqlalchemy.select(entities)
        if 1 == limit:
            return session.execute(_select).scalars().first()
        elif 0 == limit:
            return session.execute(_select).scalars().all()
        elif -1 == limit:
            _select.where(sqlalchemy.exists())
            return session.execute(_select).scalar()
        else:
            return session.execute(_select.offset((limit[0] - 1) * limit[1]).limit(limit[1])).scalars().all()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


def query_values(entities, options, limit, **kwargs):
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        _select = sqlalchemy.select(entities).options(options).filter_by(**kwargs)
        if 1 == limit:
            return session.execute(_select).scalars().first()
        elif 0 == limit:
            return session.execute(_select).scalars().all()
        elif -1 == limit:
            _select.where(sqlalchemy.exists())
            return session.execute(_select).scalar()
        else:
            return session.execute(_select.offset((limit[0] - 1) * limit[1]).limit(limit[1])).scalars().all()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


def query_values_by(entities, options, limit, criterias):
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        if 0 != len(criterias):
            _select = sqlalchemy.select(entities).options(options).where(*criterias)
        else:
            _select = sqlalchemy.select(entities).options(options)
        if 1 == limit:
            return session.execute(_select).scalars().first()
        elif 0 == limit:
            return session.execute(_select).scalars().all()
        elif -1 == limit:
            _select.where(sqlalchemy.exists())
            return session.execute(_select).scalar()
        else:
            return session.execute(_select.offset((limit[0] - 1) * limit[1]).limit(limit[1])).scalars().all()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


def count(entities, **kwargs):
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        _select = sqlalchemy.select(func.count(entities.id)).filter_by(**kwargs)
        return session.execute(_select).scalar()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


def count_by(entities, criterias):
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        _select = sqlalchemy.select(func.count(entities.id)).where(*criterias)
        return session.execute(_select).scalar()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


def update(entity, data, **kwargs):
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        _update = sqlalchemy.update(entity).filter_by(**kwargs).values(data).execution_options(
            synchronize_session="auto")
        result = session.execute(_update)
        session.commit()
        return result.rowcount
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()
    return 0


def add(instance):
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        session.add(instance)
        session.commit()
        return instance.id
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


def add_all(instances):
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        session.add_all(instances)
        session.commit()
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()


def remove(entities, **kwargs):
    session = None
    try:
        Session = sessionmaker(mode.data.engine)
        session = Session()
        _update = sqlalchemy.delete(entities).filter_by(**kwargs)
        result = session.execute(_update)
        session.commit()
        return result.rowcount
    except:
        gl.get_v("serverlogger").logger.error(traceback.format_exc())
    finally:
        if None is not session:
            session.close()
    return 0
