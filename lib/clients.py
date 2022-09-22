from pyrogram import Client

from lib.utils import Env


class Clients:
    bot: Client
    user: Client

    def __new__(cls):
        if Env.BOT_SESSION and Env.USER_SESSION:
            cls.bot: Client = Client("bot", session_string=Env.BOT_SESSION)
            cls.user: Client = Client("user", session_string=Env.USER_SESSION)
        elif Env.USER_SESSION and Env.API_ID and Env.API_HASH:
            cls.bot: Client = Client(
                "bot",
                bot_token=Env.BOT_TOKEN,
                api_id=Env.API_ID,
                api_hash=Env.API_HASH,
            )
            cls.user: Client = Client("user", api_id=Env.API_ID, api_hash=Env.API_HASH)
        else:
            print("Environments variables no configured")
            exit(1)

        if not hasattr(cls, "instance"):
            cls.instance = super(Clients, cls).__new__(cls)
        return cls.instance
