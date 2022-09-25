from pyrogram import filters
from pyrogram.types import Message
from prisma.models import User

from lib.decorators import inject, only_admin, only_allowed
import lib.database as db
import lib.app as app


@app.bot.on_message(filters.command(["invited"]))
@inject
@only_allowed
@only_admin
async def invited(user: User, message: Message, t):
    users = await db.find_users_invited()

    text = f"{t('invited_users')}\n"
    for u in users:
        text += f"- `{u.username}`"

    await message.reply(text)


@app.bot.on_message(filters.command(["invite"]))
@inject
@only_allowed
@only_admin
async def invite(user: User, message: Message, t):
    username = message.command[1]
    created = await db.create_user_invited(username)
    await message.reply(t("user_invited_success", {"user": created.username}))


@app.bot.on_message(filters.command(["uninvite"]))
@inject
@only_allowed
@only_admin
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


@app.bot.on_message(filters.command(["list_users"]))
@inject
@only_allowed
@only_admin
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
@inject
@only_allowed
@only_admin
async def delete_user(user: User, message: Message, t):
    id = message.command[1]
    deleted = await db.delete_user(id)

    await message.reply(t("user_deleted_success", {"user": deleted.username}))
