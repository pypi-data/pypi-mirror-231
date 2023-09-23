# coding=utf-8

from sqlalchemy import Column, String, Integer
from greenformatics_ds2_utils.connector.database import Base


def get_log_model(schema, tablename):
    class LoadingLog(Base):
        __tablename__ = tablename
        __table_args__ = {'schema': schema, 'extend_existing': True}

        id = Column(Integer, primary_key=True, nullable=False)
        batch_id = Column(Integer, nullable=False)
        notes = Column(String)
        log_name = Column(String)
        status = Column(String)

    return LoadingLog
