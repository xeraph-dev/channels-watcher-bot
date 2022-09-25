from pyrogram.methods.utilities.idle import idle

from lib.app import prisma, set_bot_commands, set_current_admin

import lib.app as app
import lib.handlers.admin
import lib.handlers.user
import lib.handlers.usebot


async def main():
    print("Staring...")
    await prisma.connect()
    print("Database connected")
    await set_current_admin()
    print("Cached current admin")
    await app.bot.start()
    print("Bot started")
    print("Bot commands setted")
    await app.userbot.start()
    print("Userbot started")
    await set_bot_commands()
    await idle()
    await app.bot.stop()
    print("Bot stopped")
    await app.userbot.stop()
    print("Userbot stoped")
    await prisma.disconnect()
    print("Database disconnected")


if __name__ == "__main__":
    app.bot.run(main())
