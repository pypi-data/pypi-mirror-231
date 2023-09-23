# coding=utf-8

from greenformatics_ds2_utils import Singleton
from sqlalchemy import Sequence, MetaData
from greenformatics_ds2_utils.logger.database_connection import LoggingSession


class LoadingLogRepository(metaclass=Singleton):
    _session = None
    _schema = None

    def __init__(self, db_url, schema=None, sequence_name=None):
        # SingleSession is a singleton class, so calling constructor does not mean that a new object will be
        # initialized. That's why it can be called with None parameter.
        self._session = LoggingSession(db_url).get_session()
        self._schema = schema
        self._sequence_name = sequence_name

    def get_next_log_batch_id(self):
        meta = MetaData(schema=self._schema)
        return self._session.execute(Sequence(self._sequence_name, metadata=meta))
