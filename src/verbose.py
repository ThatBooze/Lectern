import logging
from colorama import init, Fore, Back, Style

init(autoreset=True)


class ColoredFormatting(logging.Formatter):
    LOG_COLORS = {
        'DEBUG': Fore.GREEN,
        'INFO': Fore.WHITE,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'EXCEPTION': Fore.RED,
        'CRITICAL': Fore.RED + Back.BLACK,
    }

    def format(self, record):
        log_color = self.LOG_COLORS.get(record.levelname, Fore.WHITE)
        formatter = logging.Formatter(
            f"{log_color}[%(asctime)s] [%(threadName)s/%(levelname)s]: %(message)s{Style.RESET_ALL}", "%H:%M:%S")

        return formatter.format(record)


handler = logging.StreamHandler()
handler.setFormatter(ColoredFormatting())
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
