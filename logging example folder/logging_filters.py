import logging


class ErrorLogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname == 'ERROR'


class DebugWarningFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname == 'WARNING'


class CriticalLogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname == 'CRITICAL'
