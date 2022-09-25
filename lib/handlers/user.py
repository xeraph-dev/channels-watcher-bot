from pyrogram import filters
from pyrogram.types import Message
from prisma.models import User

from lib.decorators import inject, only_allowed
from lib.app import commands
import lib.app as app


@app.bot.on_message(filters.command(["start", "help", "ayuda"]))
@inject
@only_allowed
async def help(user: User, message: Message, t):
    text = f"{t('help_title')}\n\n"
    for command in commands:
        text += f"/{t(f'commands.{command}.command')} {t(f'commands.{command}.description')}\n"
    await message.reply(text)


# @bot.on_message(filters.command(["list_channels", "listar_canales"]))
# @inject()
# @only_allowed
# async def cancel(
#     bot: Client,
#     userbot: Client,
#     prisma: Prisma,
#     user: User,
#     message: Message,
#     messages: dict,
# ):
#     text = ""
#     for channel in user.channels:
#         text += f"\n{channel.name}"
#     await message.reply(f"{messages['channels']}\n{text}")


# @bot.on_message(filters.command(["add_channel", "añadir_canal"]))
# @inject()
# @only_allowed
# async def cancel(
#     bot: Client,
#     userbot: Client,
#     prisma: Prisma,
#     user: User,
#     message: Message,
#     messages: dict,
# ):
#     name = message.command[1]
#     channel: Channel | None = None
#     for c in user.channels:
#         if c.name == name:
#             channel = c
#             break
#     if channel:
#         return await message.reply(message["channel_exists"])
#     await message.reply(messages["channel_added_succefully"])


# @bot.on_message(filters.command(["delete_channel", "eliminar_canal"]))
# @inject()
# @only_allowed
# async def cancel(
#     bot: Client,
#     userbot: Client,
#     prisma: Prisma,
#     user: User,
#     message: Message,
#     messages: dict,
# ):
#     await message.reply(messages["command_not_implemented"])


# @bot.on_message(filters.command(["list_filters", "listar_filtros"]))
# @inject()
# @only_allowed
# async def cancel(
#     bot: Client,
#     userbot: Client,
#     prisma: Prisma,
#     user: User,
#     message: Message,
#     messages: dict,
# ):
#     await message.reply(messages["command_not_implemented"])


# @bot.on_message(filters.command(["list_channel_filters", "listar_filtros_por_canal"]))
# @inject()
# @only_allowed
# async def cancel(
#     bot: Client,
#     userbot: Client,
#     prisma: Prisma,
#     user: User,
#     message: Message,
#     messages: dict,
# ):
#     await message.reply(messages["command_not_implemented"])


# @bot.on_message(filters.command(["add_filter", "añadir_filtro"]))
# @inject()
# @only_allowed
# async def cancel(
#     bot: Client,
#     userbot: Client,
#     prisma: Prisma,
#     user: User,
#     message: Message,
#     messages: dict,
# ):
#     await message.reply(messages["command_not_implemented"])


# @bot.on_message(filters.command(["delete_filter", "eliminar_filtro"]))
# @inject()
# @only_allowed
# async def cancel(
#     bot: Client,
#     userbot: Client,
#     prisma: Prisma,
#     user: User,
#     message: Message,
#     messages: dict,
# ):
#     await message.reply(messages["command_not_implemented"])


### User handlers ###
