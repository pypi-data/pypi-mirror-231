import logging

import xnat
from textual.app import App
from textual.widgets import RichLog
from xnat.exceptions import XNATAuthError, XNATLoginFailedError, XNATExpiredCredentialsError, XNATNotConnectedError

from src.log_handler import TextualLogHandler


class XnatBase(App):
    DEFAULT_CSS = """
    RichLog.remove {
        display: none;
    }
    
    #rich_log {
        height: 4;
        border: hkey;
    }
        """

    def __init__(self, server: str, log_level: int = logging.INFO) -> None:
        super().__init__()
        self.title = f'{self.__class__.__name__} ({server})'
        self._server = server
        self.logger = logging.getLogger('xnat_browser')
        self.logger.setLevel(log_level)

        try:
            self.session = xnat.connect(server=self._server, default_timeout=300)
        except (XNATAuthError, XNATLoginFailedError, XNATExpiredCredentialsError, XNATNotConnectedError) as e:
            self.logger.error('Error connecting to XNAT server.')
            self.logger.debug(e)

    def _setup_logging(self) -> RichLog:
        log_window = RichLog(id='rich_log', name='Log')

        log_handler = TextualLogHandler(log_window)
        log_handler.setFormatter(
            logging.Formatter('%(asctime)s %(levelname)7s [%(filename)15s:%(lineno)3s - %(funcName)20s()] %(message)s'))

        self.logger.addHandler(log_handler)

        if self.logger.level > logging.DEBUG:
            log_window.set_class(True, 'remove')

        return log_window
