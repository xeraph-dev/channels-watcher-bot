from pyrogram.types import Message, User
from lib.database import Database
from lib.utils import Env, messages, locales

database = Database()


def is_admin(user: User):
    return user.id == Env.ADMIN_ID


def only_admin(fn):
    async def wrapper(_, message: Message, messages: dict):
        if is_admin(message.from_user):
            await fn(_, message, messages)

    return wrapper


def only_invited(fn):
    async def wrapper(_, message: Message, messages: dict):
        if is_admin(message.from_user) or database.is_user_invited(message.from_user):
            await fn(_, message, messages)
        else:
            await message.reply(messages["not_allowed"])

    return wrapper


def only_allowed(fn):
    async def wrapper(_, message: Message, messages: dict):
        if is_admin(message.from_user) or database.user_exists(message.from_user):
            await fn(_, message, messages)
        else:
            await message.reply(messages["not_allowed"])

    return wrapper


def inject_messages(fn):
    async def wrapper(_, message: Message):
        code: str = message.from_user.language_code
        if code in locales:
            await fn(_, message, messages[code])

    return wrapper
