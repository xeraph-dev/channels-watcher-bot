import sys
from pyrogram.client import Client
from pyrogram.types import BotCommand
from prisma import Prisma
from prisma.models import User

import lib.env as env
import lib.i18n as i18n


prisma = Prisma()
bot: Client
userbot: Client
admin: User | None

if env.BOT_SESSION and env.USER_SESSION:
    print("hola")
    bot = Client("bot", session_string=env.BOT_SESSION)
    userbot = Client("user", session_string=env.USER_SESSION)
elif env.BOT_TOKEN and env.API_ID and env.API_HASH:
    bot = Client(
        "bot",
        bot_token=env.BOT_TOKEN,
        api_id=env.API_ID,
        api_hash=env.API_HASH,
    )
    userbot = Client("user", api_id=env.API_ID, api_hash=env.API_HASH)
else:
    print("Environments variables no configured")
    sys.exit(1)


async def set_current_admin():
    global admin
    admin = await prisma.user.find_first(where={"admin": True})


admin_commands = ["invited", "invite", "uninvite", "list_users", "delete_user"]
user_commands = ["help"]
commands = admin_commands + user_commands


async def set_bot_commands():
    bot_commands: dict = {}

    for locale in i18n.locales:
        t = i18n.t(locale)
        bot_commands[locale] = []
        for command in commands:
            bot_commands[locale].append(
                BotCommand(
                    t(f"commands.{command}.command"),
                    t(f"commands.{command}.description"),
                )
            )

    for locale in i18n.locales:
        await bot.set_bot_commands(bot_commands[locale], language_code=locale)
