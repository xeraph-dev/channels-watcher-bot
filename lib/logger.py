import logging
from prisma.models import User
from pyrogram.types import User as PyUser
from termcolor import colored


class UserFormatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: "%(levelname)s",
        logging.INFO: colored("%(levelname)s", "blue"),
        logging.WARN: colored("%(levelname)s", "yellow"),
        logging.ERROR: colored("%(levelname)s", "red"),
        logging.CRITICAL: colored("%(levelname)s", "red", None, ["bold"]),
    }

    def __init__(self, file: bool = False):
        super().__init__()
        self.file = file

    def format(self, record):
        time = "%(asctime)s" if self.file else colored("%(asctime)s", "magenta")
        level = "%(levelname)s" if self.file else self.FORMATS.get(record.levelno)
        fmt = f"{time} - {level} - {record.msg}"
        formatter = logging.Formatter(fmt)
        return formatter.format(record)


log = logging.getLogger("logger")
logger_level = logging.DEBUG

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logger_level)
file_handler.setFormatter(UserFormatter(True))

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logger_level)
stream_handler.setFormatter(UserFormatter())

log.addHandler(file_handler)
log.addHandler(stream_handler)
log.setLevel(logger_level)
