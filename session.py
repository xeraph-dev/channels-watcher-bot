from pyrogram import Client
from dotenv import set_key
from lib.clients import Clients

from lib.utils import Env


clients = Clients(True)
bot = clients.bot
user = clients.user


async def main():
    await bot.start()
    print("Exporting bot session...")
    set_key(".env", "BOT_SESSION", await bot.export_session_string())
    await bot.stop()
    await user.start()
    print("Exporting user session...")
    set_key(".env", "USER_SESSION", await user.export_session_string())
    await user.stop()


bot.run(main())
