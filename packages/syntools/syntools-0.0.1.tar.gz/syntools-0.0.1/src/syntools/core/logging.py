import os
import logging
from datetime import datetime
from .utils import Utils


class Logging:
    _log_file = None

    @classmethod
    def configure(cls, log_dir=None, log_level=None):
        if log_dir is None:
            log_dir = Utils.app_log_dir()
        if log_level is None:
            log_level = 'INFO'

        log_level = log_level.upper()
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        cls._log_file = os.path.join(log_dir, '{0}.log'.format(timestamp))
        Utils.ensure_dirs(os.path.dirname(cls._log_file))
        logging.basicConfig(
            filename=cls._log_file,
            filemode='w',
            format='%(asctime)s %(levelname)s: %(message)s',
            level=log_level,
            force=True
        )

        # Remove synapseclient stream handlers so they don't pollute the screen.
        logging.getLogger('synapseclient_default').handlers.clear()

        # TODO: Fix "Connection pool is full, discarding connection:" and remove the log filter.
        logging.getLogger('urllib3.connectionpool').addFilter(LogFilter())

    @classmethod
    def _ensure_configured(cls):
        if cls._log_file is None:
            cls.configure()

    @classmethod
    def log_file(cls):
        cls._ensure_configured()
        return cls._log_file

    @classmethod
    def print_log_file_path(cls):
        print('Logging output to: {0}'.format(cls.log_file()))

    @classmethod
    def info(cls, msg, console=False, *args, **kwargs):
        cls._ensure_configured()
        logging.info(msg, *args, **kwargs)
        if console:
            print(msg)

    @classmethod
    def warning(cls, msg, console=False, *args, **kwargs):
        cls._ensure_configured()
        logging.warning(msg, *args, **kwargs)
        if console:
            print(msg)

    @classmethod
    def error(cls, msg, console=False, *args, **kwargs):
        cls._ensure_configured()
        logging.error(msg, *args, **kwargs)
        if console:
            print(msg)

    @classmethod
    def debug(cls, msg, console=False, *args, **kwargs):
        cls._ensure_configured()
        logging.debug(msg, *args, **kwargs)
        if console:
            print(msg)

    @classmethod
    def exception(cls, msg, console=False, *args, exc_info=True, **kwargs):
        cls._ensure_configured()
        logging.exception(msg, *args, exc_info=exc_info, **kwargs)
        if console:
            print(msg)


class LogFilter(logging.Filter):
    FILTERS = [
        'Connection pool is full, discarding connection:'
    ]

    def filter(self, record):
        for filter in self.FILTERS:
            if filter in record.msg:
                return False
        return True
