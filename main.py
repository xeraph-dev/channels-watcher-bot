from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.methods.utilities.idle import idle
from pyrogram.types import Message
from lib.clients import Clients
from lib.database import Database
from lib.utils import *
from lib.decorators import *
from lib.actions import *


clients = Clients()
bot = clients.bot
user = clients.user


actions = Actions()
database = Database()


### Bot handlers ###

## Commands ##
@bot.on_message(filters.command(["invited"]))
@inject_messages
@only_admin
async def invited(_, message: Message, messages: dict):
    text = ""
    for user in database.invited_users:
        text += f"\n{user}"
    await message.reply(f"{messages['invited_users']}\n{text}")


@bot.on_message(filters.command(["invite"]))
@inject_messages
@only_admin
async def invite(_, message: Message, messages: dict):
    database.invite_user(message.command[1])
    await message.reply(messages["user_invited_success"])


@bot.on_message(filters.command(["uninvite"]))
@inject_messages
@only_admin
async def uninvite(_, message: Message, messages: dict):
    database.uninvite_user(message.command[1])
    await message.reply(messages["user_uninvited_success"])


@bot.on_message(filters.command(["list_users"]))
@inject_messages
@only_admin
async def list_users(_, message: Message, messages: dict):
    text = ""
    for user in database.users:
        text += f"\n{user.id}: {user.username}"
    await message.reply(f"{messages['users']}\n{text}")


@bot.on_message(filters.command(["delete_user"]))
@inject_messages
@only_admin
async def delete_user(_, message: Message, messages: dict):
    database.delete_user(int(message.command[1]))
    await message.reply(messages["user_deleted_success"])


@bot.on_message(filters.command("start"))
@inject_messages
@only_invited
async def start(_, message: Message, messages: dict):
    database.accept_invitation(message.from_user)
    text = ""
    for command in commands:
        text += f"\n/{messages[command]['command']} {messages[command]['description']}"
    await message.reply(f"{messages['help']['title']}\n{text}")


@bot.on_message(filters.command(["help", "ayuda"]))
@inject_messages
@only_allowed
async def help(_, message: Message, messages: dict):
    text = ""
    for command in commands:
        text += f"\n/{messages[command]['command']} {messages[command]['description']}"
    await message.reply(f"{messages['help']['title']}\n{text}")


@bot.on_message(filters.command(["cancel", "cancelar"]))
@inject_messages
@only_allowed
async def cancel(_, message: Message, messages: dict):
    await message.reply(messages["command_not_implemented"])


@bot.on_message(filters.command(["list_channels", "listar_canales"]))
@inject_messages
@only_allowed
async def cancel(_, message: Message, messages: dict):
    await message.reply(messages["command_not_implemented"])


@bot.on_message(filters.command(["add_channel", "añadir_canal"]))
@inject_messages
@only_allowed
async def cancel(_, message: Message, messages: dict):
    await message.reply(messages["command_not_implemented"])


@bot.on_message(filters.command(["delete_channel", "eliminar_canal"]))
@inject_messages
@only_allowed
async def cancel(_, message: Message, messages: dict):
    await message.reply(messages["command_not_implemented"])


@bot.on_message(filters.command(["list_filters", "listar_filtros"]))
@inject_messages
@only_allowed
async def cancel(_, message: Message, messages: dict):
    await message.reply(messages["command_not_implemented"])


@bot.on_message(filters.command(["list_channel_filters", "listar_filtros_por_canal"]))
@inject_messages
@only_allowed
async def cancel(_, message: Message, messages: dict):
    await message.reply(messages["command_not_implemented"])


@bot.on_message(filters.command(["add_filter", "añadir_filtro"]))
@inject_messages
@only_allowed
async def cancel(_, message: Message, messages: dict):
    await message.reply(messages["command_not_implemented"])


@bot.on_message(filters.command(["delete_filter", "eliminar_filtro"]))
@inject_messages
@only_allowed
async def cancel(_, message: Message, messages: dict):
    await message.reply(messages["command_not_implemented"])


### User handlers ###


@user.on_message(filters.channel)
async def watcher(_, message: Message):
    pass


async def set_commands():
    for locale in locales:
        await bot.set_bot_commands(bot_commands[locale], language_code=locale)


async def main():
    await bot.start()
    await user.start()
    await set_commands()
    await idle()
    await bot.stop()
    await user.stop()


print("Starting bot...")

bot.run(main())
