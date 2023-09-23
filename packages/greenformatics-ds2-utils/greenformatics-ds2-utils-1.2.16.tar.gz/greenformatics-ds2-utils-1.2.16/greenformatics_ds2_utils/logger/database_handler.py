# coding=utf-8

from logging import StreamHandler
from greenformatics_ds2_utils.logger.database_connection import LoggingSession


class DatabaseHandler(StreamHandler):
    """Customized logging handler that puts logs to the database."""

    terminator = ''

    def __init__(self, stream=None, db_url=None, model_class=None, log_batch_id_getter=None):
        if stream is None:
            stream = LoggingSession(db_url).get_session()
        super().__init__(stream)
        self._model_class = model_class
        self._log_batch_id = log_batch_id_getter()

    def emit(self, record):
        """Emit a record."""

        # Replacing empty args with empty strings to avoid errors
        if len(record.args) < 1:
            record.args = ('', '')
        if len(record.args) < 2:
            record.args = (record.args[0], '')

        # Truncating args to two items to avoid errors
        if len(record.args) > 2:
            record.args = record.args[:2]

        # Replacing excessive conversion specifiers with %% to avoid errors
        if record.msg.count('%') > 2:
            record.msg = record.msg.replace('%', '%%', record.msg.count('%') - 2)

        # Adding missing conversion specifiers to avoid errors
        if record.msg.count('%') < 1:
            record.msg = f'{record.msg} %s'

        if record.msg.count('%') < 2:
            record.msg = f'{record.msg} %s'

        try:
            msg = self.format(record).strip()
            log_record = self._model_class(batch_id=self._log_batch_id, notes=msg, log_name=record.args[0],
                                           status=record.args[1])
            self.stream.write(log_record)
            self.flush()
        except RecursionError:
            raise
        except Exception:
            self.handleError(record)
