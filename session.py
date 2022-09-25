from dotenv import set_key

import lib.app as app


async def main():
    await app.bot.start()
    print("Exporting bot session...")
    set_key(".env", "BOT_SESSION", await app.bot.export_session_string())
    await app.bot.stop()
    await app.userbot.start()
    print("Exporting user session...")
    set_key(".env", "USER_SESSION", await app.userbot.export_session_string())
    await app.userbot.stop()


app.bot.run(main())
