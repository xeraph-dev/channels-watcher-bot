from pyrogram.types import Message
from prisma.models import User

import lib.database as db
import lib.app as app
from lib.i18n import t


def only_admin(fn):
    async def wrapper(user: User | None, message: Message, t):
        if user and user.admin:
            await fn(user=user, message=message, t=t)
        else:
            await message.reply(t("not_admin"))

    return wrapper


def only_invited(fn):
    async def wrapper(user: User | None, message: Message, t):
        if user and (user.admin or not user.id):
            await fn(user=user, message=message, t=t)
        else:
            await message.reply(t("not_allowed"))

    return wrapper


def only_allowed(fn):
    async def wrapper(user: User | None, message: Message, t):
        if user:
            await fn(user=user, message=message, t=t)
        else:
            await message.reply(t("not_allowed"))

    return wrapper


def inject(fn):
    async def wrapper(_, message: Message):
        code = message.from_user.language_code
        user = await db.find_user_by_id_or_username(message.from_user)

        if user and message.from_user.username != user.username:
            user = await db.update_user_username(user.uuid, message.from_user.username)

        if app.admin is None and user is None:
            app.admin = user = await db.create_admin(message.from_user)

        await fn(user=user, message=message, t=t(code))

    return wrapper
