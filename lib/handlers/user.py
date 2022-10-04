from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums.chat_type import ChatType
from prisma.models import User

from lib.decorators import bot_inject, log_access, log_try_access, only_allowed
from lib.app import commands
import lib.app as app
import lib.database as db


@app.bot.on_message(filters.command(["start", "help", "ayuda"]))
@log_try_access
@bot_inject
@only_allowed
@log_access
async def help(user: User, message: Message, t):
    text = f"{t('help_title')}\n\n"
    for command in commands:
        text += f"/{t(f'commands.{command}.command')} {t(f'commands.{command}.description')}\n"
    await message.reply(text)


@app.bot.on_message(filters.command(["list_channels", "listar_canales"]))
@log_try_access
@bot_inject
@only_allowed
@log_access
async def list_channels(user: User, message: Message, t):
    text = f"{t('channels')}\n\n"
    for channel in user.channels:
        text += f"- `{channel.name}`\n"
    await message.reply(text)


@app.bot.on_message(filters.command(["add_channel", "agregar_canal"]))
@log_try_access
@bot_inject
@only_allowed
@log_access
async def add_channel(user: User, message: Message, t):
    name = message.command[1]
    chat = await app.userbot.get_chat(name)
    if chat.type == ChatType.CHANNEL:
        await app.userbot.join_chat(chat.id)
    else:
        await message.reply(t("cant_join", {"chat": name}))
    channel = await db.user_add_channel(chat, user)
    await message.reply(t("channel_added_success", {"channel": channel.name}))


@app.bot.on_message(filters.command(["delete_channel", "eliminar_canal"]))
@log_try_access
@bot_inject
@only_allowed
@log_access
async def delete_channel(user: User, message: Message, t):
    name = message.command[1]
    await db.user_delete_channel(name, user)
    await message.reply(t("channel_deleted_success", {"channel": name}))


@app.bot.on_message(filters.command(["list_filters", "listar_filtros"]))
@log_try_access
@bot_inject
@only_allowed
@log_access
async def list_filters(user: User, message: Message, t):
    text = ""

    for channel in user.channels:
        text += f"{t('filters_for_channel', {'channel': channel.name})}\n"
        filters = [
            filter for filter in user.filters if filter.channel.name == channel.name
        ]
        for filter in filters:
            text += f"- `{filter.filter}`\n"
        text += "\n"

    await message.reply(text)


@app.bot.on_message(
    filters.command(["list_channel_filters", "listar_filtros_por_canal"])
)
@log_try_access
@bot_inject
@only_allowed
@log_access
async def list_channel_filters(user: User, message: Message, t):
    channel = message.command[1]
    text = f"{t('filters_for_channel', {'channel': channel})}\n\n"
    filters = [filter for filter in user.filters if filter.channel.name == channel]
    for filter in filters:
        text += f"- `{filter.filter}`\n"

    await message.reply(text)


@app.bot.on_message(filters.command(["add_filter", "agregar_filtro"]))
@log_try_access
@bot_inject
@only_allowed
@log_access
async def add_filter(user: User, message: Message, t):
    channel = message.command[1]
    filter = " ".join(message.command[2:])
    await db.user_add_filter(filter, channel, user)
    await message.reply(
        t("filter_added_success", {"filter": filter, "channel": channel})
    )


@app.bot.on_message(filters.command(["delete_filter", "eliminar_filtro"]))
@log_try_access
@bot_inject
@only_allowed
@log_access
async def delete_filter(user: User, message: Message, t):
    channel = message.command[1]
    filter = " ".join(message.command[2:])
    await db.user_delete_filter(filter, channel, user)
    await message.reply(
        t("filter_deleted_success", {"filter": filter, "channel": channel})
    )
