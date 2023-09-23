# coding=utf-8

from unittest import TestCase
from greenformatics_ds2_utils.logger import *
from unittest.mock import Mock, patch
from logging import LogRecord, INFO


class LoggerUtilityTestCase(TestCase):
    """Tests for the logger utility functions."""

    def setUp(self):
        # Create a mock model class for testing
        self.model_class = Mock()
        self.log_batch_id_getter = Mock(return_value=123)  # Mock log_batch_id_getter

    @patch('greenformatics_ds2_utils.logger.database_handler.LoggingSession')  # Mock the LoggingSession class
    def test_init_with_default_stream(self, mock_logging_session):
        # Mock the LoggingSession constructor
        mock_session = Mock()
        mock_logging_session.return_value.get_session.return_value = mock_session

        # Create a DatabaseHandler instance with a default stream
        handler = DatabaseHandler(db_url='mock_db_url', model_class=self.model_class,
                                  log_batch_id_getter=self.log_batch_id_getter)

        # Verify that the LoggingSession constructor was called with the db_url
        mock_logging_session.assert_called_once_with('mock_db_url')

        # Verify that the get_session method was called
        mock_logging_session.return_value.get_session.assert_called_once()

        # Verify that the stream of the handler is the mock session
        self.assertEqual(handler.stream, mock_session)

    def test_format_with_args(self):
        # Create a mock stream
        mock_stream = Mock()

        # Create a DatabaseHandler instance with mock dependencies
        handler = DatabaseHandler(stream=mock_stream, model_class=self.model_class,
                                  log_batch_id_getter=self.log_batch_id_getter)
        log_record = Mock()
        log_record.args = ('Process name', 'Status')
        log_record.msg = 'Process started. Process name: %s Status: %s'  # Set the log message
        log_record.getMessage = Mock(return_value=log_record.msg % log_record.args)
        log_record.exc_info = None
        log_record.exc_text = None
        log_record.stack_info = None

        handler.emit(log_record)

        # Verify that the model_class constructor was called with the expected arguments
        self.model_class.assert_called_once_with(batch_id=123,
                                                 notes='Process started. Process name: Process name Status: Status',
                                                 log_name='Process name', status='Status')

        # Verify that the stream's write method was called with the log record
        mock_stream.write.assert_called_once_with(self.model_class.return_value)

    def test_format_without_args(self):
        # Create a mock stream
        mock_stream = Mock()

        # Create a DatabaseHandler instance with mock dependencies
        handler = DatabaseHandler(stream=mock_stream, model_class=self.model_class,
                                  log_batch_id_getter=self.log_batch_id_getter)

        # Create a log record without args
        log_record = LogRecord('log', INFO, 'greenformatics_ds2_utils/tests/test_logger.py', 42,
                               'Process started. Process name: %s Status: %s', (), None)

        handler.emit(log_record)

        # Verify that the model_class constructor was called with the expected arguments
        self.model_class.assert_called_once_with(batch_id=123, notes='Process started. Process name:  Status:',
                                                 log_name='', status='')

        # Verify that the stream's write method was called with the log record
        mock_stream.write.assert_called_once_with(self.model_class.return_value)

    def test_format_with_excessive_args(self):
        # Create a mock stream
        mock_stream = Mock()

        # Create a DatabaseHandler instance with mock dependencies
        handler = DatabaseHandler(stream=mock_stream, model_class=self.model_class,
                                  log_batch_id_getter=self.log_batch_id_getter)

        # Create a log record with an extra argument
        log_record = LogRecord('log', INFO, 'greenformatics_ds2_utils/tests/test_logger.py', 42,
                               'Process started. Process name: %s Status: %s',
                               ('Process name', 'Status', 'Extra Argument'), None)

        handler.emit(log_record)

        # Verify that the model_class constructor was called with the expected arguments
        self.model_class.assert_called_once_with(batch_id=123,
                                                 notes='Process started. Process name: Process name Status: Status',
                                                 log_name='Process name', status='Status')

        # Verify that the stream's write method was called with the log record
        mock_stream.write.assert_called_once_with(self.model_class.return_value)

    def test_format_with_no_conversion_specifiers(self):
        # Create a mock stream
        mock_stream = Mock()

        # Create a DatabaseHandler instance with mock dependencies
        handler = DatabaseHandler(stream=mock_stream, model_class=self.model_class,
                                  log_batch_id_getter=self.log_batch_id_getter)

        # Create a log record with an extra argument
        log_record = LogRecord('log', INFO, 'greenformatics_ds2_utils/tests/test_logger.py', 42, 'Process started.',
                               ('Process name', 'Status'), None)

        handler.emit(log_record)

        # Verify that the model_class constructor was called with the expected arguments
        self.model_class.assert_called_once_with(batch_id=123, notes='Process started. Process name Status',
                                                 log_name='Process name', status='Status')

        # Verify that the stream's write method was called with the log record
        mock_stream.write.assert_called_once_with(self.model_class.return_value)

    def test_format_with_one_conversion_specifiers(self):
        # Create a mock stream
        mock_stream = Mock()

        # Create a DatabaseHandler instance with mock dependencies
        handler = DatabaseHandler(stream=mock_stream, model_class=self.model_class,
                                  log_batch_id_getter=self.log_batch_id_getter)

        # Create a log record with an extra argument
        log_record = LogRecord('log', INFO, 'greenformatics_ds2_utils/tests/test_logger.py', 42,
                               'Process started. Process name: %s', ('Process name', 'Status'), None)

        handler.emit(log_record)

        # Verify that the model_class constructor was called with the expected arguments
        self.model_class.assert_called_once_with(batch_id=123,
                                                 notes='Process started. Process name: Process name Status',
                                                 log_name='Process name', status='Status')

        # Verify that the stream's write method was called with the log record
        mock_stream.write.assert_called_once_with(self.model_class.return_value)

    def test_format_with_excessive_conversion_specifiers(self):
        # Create a mock stream
        mock_stream = Mock()

        # Create a DatabaseHandler instance with mock dependencies
        handler = DatabaseHandler(stream=mock_stream, model_class=self.model_class,
                                  log_batch_id_getter=self.log_batch_id_getter)

        # Create a log record with an extra argument
        log_record = LogRecord('log', INFO, 'greenformatics_ds2_utils/tests/test_logger.py', 42,
                               'Process %s started. Process name: %s Status: %s', ('Process name', 'Status'), None)

        handler.emit(log_record)

        # Verify that the model_class constructor was called with the expected arguments
        self.model_class.assert_called_once_with(batch_id=123,
                                                 notes='Process %s started. Process name: Process name Status: Status',
                                                 log_name='Process name', status='Status')

        # Verify that the stream's write method was called with the log record
        mock_stream.write.assert_called_once_with(self.model_class.return_value)
