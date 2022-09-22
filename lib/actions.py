from enum import Enum
from pyrogram.types import Message
from lib.clients import Clients

clients = Clients()
bot = clients.bot
user = clients.user


class Action(Enum):
    CHOOSE_CHANNEL: int = 0
    ADD_CHANNEL: int = 1
    DELETE_CHANNEL: int = 2
    ADD_FILTER: int = 3
    DELETE_FILTER: int = 4


class Actions:
    __action: Action = None
    __channel: str = None

    def __new__(cls) -> Action:
        if not hasattr(cls, "instance"):
            cls.instance = super(Actions, cls).__new__(cls)
        return cls.instance

    def clear(self) -> None:
        self.__action = None
        self.__channel = None

    def set_action(self, action: Action) -> None:
        self.__action = action

    def execute(self, message: Message) -> None:
        pass
