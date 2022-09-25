import logging
from pyrogram import filters
from pyrogram.types import Message
from prisma.models import User

from lib.decorators import (
    bot_inject,
    log_access,
    log_try_access,
    only_admin,
    only_allowed,
)
import lib.database as db
import lib.app as app


@app.bot.on_message(filters.command(["invited"]))
@log_try_access
@bot_inject
@only_allowed
@only_admin
@log_access
async def invited(user: User, message: Message, t):
    users = await db.find_users_invited()

    text = f"{t('invited_users')}\n"
    for u in users:
        text += f"- `{u.username}`"

    await message.reply(text)


@app.bot.on_message(filters.command(["invite"]))
@log_try_access
@bot_inject
@only_allowed
@only_admin
@log_access
async def invite(user: User, message: Message, t):
    username = message.command[1]
    created = await db.create_user_invited(username)
    await message.reply(t("user_invited_success", {"user": created.username}))


@app.bot.on_message(filters.command(["uninvite"]))
@log_try_access
@bot_inject
@only_allowed
@only_admin
@log_access
async def uninvite(user: User, message: Message, t):
    username = message.command[1]
    res = await db.delete_invited_user(username)

    return (
        await message.reply(t("user_not_found", {"user": username}))
        if res is None
        else await message.reply(t("user_uninvited_success", {"user": username}))
        if res
        else await message.reply(t("user_was_accepted", {"user": username}))
    )


@app.bot.on_message(filters.command(["accepted"]))
@log_try_access
@bot_inject
@only_allowed
@only_admin
@log_access
async def accepted(user: User, message: Message, t):
    users = await db.find_users_accepted()

    text = f"{t('accepted_users')}\n"
    for u in users:
        text += f"- `{u.id}`: `{u.username}`\n"

    await message.reply(text)


@app.bot.on_message(filters.command(["list_users"]))
@log_try_access
@bot_inject
@only_allowed
@only_admin
@log_access
async def list_users(user: User, message: Message, t):
    invited = await db.find_users_invited()
    accepted = await db.find_users_accepted()

    text = f"{t('invited_users')}\n"
    for u in invited:
        text += f"- `{u.username}`\n"

    text += "\n"
    text += f"{t('accepted_users')}\n"
    for u in accepted:
        text += f"- `{u.id}`: `{u.username}`\n"

    await message.reply(text)


@app.bot.on_message(filters.command(["delete_user"]))
@log_try_access
@bot_inject
@only_allowed
@only_admin
@log_access
async def delete_user(user: User, message: Message, t):
    id = message.command[1]
    deleted = await db.delete_user(id)

    await message.reply(t("user_deleted_success", {"user": deleted.username}))
