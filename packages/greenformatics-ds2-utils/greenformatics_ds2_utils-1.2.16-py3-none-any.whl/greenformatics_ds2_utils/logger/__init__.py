# coding=utf-8

from greenformatics_ds2_utils.logger.database_handler import DatabaseHandler
from greenformatics_ds2_utils.logger.database_connection import DatabaseStream
from greenformatics_ds2_utils.logger.loading_log_repository import LoadingLogRepository
from greenformatics_ds2_utils.logger.loading_log import get_log_model
import logging

file_log = logging.getLogger('db_log')


def _init_stream_handler(logger_name, level=logging.INFO):
    # Initializing logger and set log level
    log_setup = logging.getLogger(logger_name)
    log_setup.setLevel(level)
    # Init stream logging to stdout and add it to the logger
    stream_handler = logging.StreamHandler()
    log_setup.addHandler(stream_handler)
    return log_setup


def setup_db_logger_from_db_url(logger_name: str, db_url: str, log_schema_name: str, log_table_name: str,
                                sequence_name: str, level=logging.INFO):
    # Initializing stream handler
    log_setup = _init_stream_handler(logger_name, level)
    # Init loading log repository
    log_repo = LoadingLogRepository(db_url, log_schema_name, sequence_name)
    # Init stream logging to database and add it to the logger
    db_handler = DatabaseHandler(None, db_url, get_log_model(log_schema_name, log_table_name),
                                 log_repo.get_next_log_batch_id)
    log_setup.addHandler(db_handler)


def setup_db_logger_from_db_stream(logger_name: str, db_stream: DatabaseStream, log_schema_name: str,
                                   sequence_name: str, log_table_name: str, level=logging.INFO):
    # Initializing stream handler
    log_setup = _init_stream_handler(logger_name, level)
    # Init loading log repository
    log_repo = LoadingLogRepository(db_stream.get_bind().url, log_schema_name, sequence_name)
    # Init stream logging to database and add it to the logger
    db_handler = DatabaseHandler(db_stream, None, get_log_model(log_schema_name, log_table_name),
                                 log_repo.get_next_log_batch_id)
    log_setup.addHandler(db_handler)
