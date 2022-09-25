from pyrogram import filters
from pyrogram.types import Message
from prisma.models import User

from lib.decorators import bot_inject, only_allowed
from lib.app import commands
import lib.app as app
import lib.database as db


@app.bot.on_message(filters.command(["start", "help", "ayuda"]))
@bot_inject
@only_allowed
async def help(user: User, message: Message, t):
    text = f"{t('help_title')}\n\n"
    for command in commands:
        text += f"/{t(f'commands.{command}.command')} {t(f'commands.{command}.description')}\n"
    await message.reply(text)


@app.bot.on_message(filters.command(["list_channels", "listar_canales"]))
@bot_inject
@only_allowed
async def list_channels(user: User, message: Message, t):
    command = message.command[0]
    await message.reply(t("command_not_implemented", {"command": command}))


@app.bot.on_message(filters.command(["add_channel", "agregar_canal"]))
@bot_inject
@only_allowed
async def add_channel(user: User, message: Message, t):
    name = message.command[1]
    chat = await app.userbot.get_chat(name)
    channel = await db.user_add_channel(chat, user)
    await app.userbot.join_chat(channel.name)
    await message.reply(t("channel_added_success", {"channel": channel.name}))


@app.bot.on_message(filters.command(["delete_channel", "eliminar_canal"]))
@bot_inject
@only_allowed
async def delete_channel(user: User, message: Message, t):
    command = message.command[0]
    await message.reply(t("command_not_implemented", {"command": command}))


@app.bot.on_message(filters.command(["list_filters", "listar_filtros"]))
@bot_inject
@only_allowed
async def list_filters(user: User, message: Message, t):
    command = message.command[0]
    await message.reply(t("command_not_implemented", {"command": command}))


@app.bot.on_message(
    filters.command(["list_channel_filters", "listar_filtros_por_canal"])
)
@bot_inject
@only_allowed
async def list_channel_filters(user: User, message: Message, t):
    command = message.command[0]
    await message.reply(t("command_not_implemented", {"command": command}))


@app.bot.on_message(filters.command(["add_filter", "añadir_filtro"]))
@bot_inject
@only_allowed
async def add_filter(user: User, message: Message, t):
    command = message.command[0]
    await message.reply(t("command_not_implemented", {"command": command}))


@app.bot.on_message(filters.command(["delete_filter", "eliminar_filtro"]))
@bot_inject
@only_allowed
async def delete_filter(user: User, message: Message, t):
    command = message.command[0]
    await message.reply(t("command_not_implemented", {"command": command}))
