# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from greenformatics_ds2_utils import Singleton

Base = declarative_base()


class LoggingSession(metaclass=Singleton):
    """ This singleton class ensures that one database session is active one time during the program run. """

    _session = None

    def __init__(self, db_url):
        if not self._session:
            self.engine = create_engine(db_url,
                                        pool_size=100,
                                        max_overflow=0,
                                        pool_pre_ping=True,
                                        connect_args={"keepalives": 1,
                                                      "keepalives_idle": 60,
                                                      "keepalives_interval": 5,
                                                      "keepalives_count": 5})
            self._target_session = sessionmaker(bind=self.engine, autoflush=False, expire_on_commit=False)
            self._session = DatabaseStream(self._target_session())

    def get_session(self):
        if not self._session:
            self._session = DatabaseStream(self._target_session())
        return self._session

    def close_session(self):
        self._session.close()
        return self

    def __enter__(self):
        return self.get_session()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_session()


class DatabaseStream:
    """ This is a wrapper class to session to act as a stream. """

    def __init__(self, session):
        self._session = session

    def __getattr__(self, item):
        return getattr(self._session, item)

    def write(self, log_record):
        self._session.add(log_record)

    def flush(self):
        self._session.commit()
