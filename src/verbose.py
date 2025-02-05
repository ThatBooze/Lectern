import logging


class ColoredFormatting(logging.Formatter):
    LOG_COLORS = {
        'DEBUG': '\033[92m',
        'INFO': '\033[97m',
        'WARNING': '\033[93m',
        'ERROR': '\033[91m',
        'EXCEPTION': '\033[91m',
        'CRITICAL': '\033[91m\033[40m'
    }

    RESET_COLOR = '\033[0m'

    def format(self, record: logging.LogRecord) -> str:
        log_color = self.LOG_COLORS.get(record.levelname, '\033[97m')

        formatter = logging.Formatter(
            f"{log_color}[%(asctime)s] [%(threadName)s/%(levelname)s]: %(message)s{self.RESET_COLOR}", "%H:%M:%S"
            )

        return formatter.format(record)


handler = logging.StreamHandler()
handler.setFormatter(ColoredFormatting())
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
