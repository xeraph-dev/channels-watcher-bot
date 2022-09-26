from pyrogram.types import User as PyUser, Chat
from prisma.types import UserInclude, ChannelInclude
from prisma.models import User

from lib.app import prisma

user_include: UserInclude = {
    "channels": {"include": {"filters": True}},
    "filters": {"include": {"channel": True, "user": True}},
}

channel_include: ChannelInclude = {"filters": {"include": {"user": True}}}


async def create_admin(user: PyUser):
    return await prisma.user.create(
        data={
            "admin": True,
            "id": user.id,
            "username": user.username,
        }
    )


async def update_user(uuid: str, user: PyUser):
    return await prisma.user.update(
        where={"uuid": uuid},
        data={"username": user.username, "lang": user.language_code},
        include=user_include,
    )


async def update_user_username(uuid: str, username: str):
    return await prisma.user.update(
        where={"uuid": uuid}, data={"username": username}, include=user_include
    )


async def update_user_id(uuid: str, id: int):
    return await prisma.user.update(
        where={"uuid": uuid}, data={"id": id}, include=user_include
    )


async def find_users_invited():
    return await prisma.user.find_many(
        where={"admin": False, "id": None, "admin": False}, include=user_include
    )


async def create_user_invited(username: str):
    return await prisma.user.create(data={"username": username}, include=user_include)


async def delete_invited_user(username: str):
    user = await prisma.user.find_first(
        where={"username": username}, include=user_include
    )

    if user is None:
        return None
    elif user.id:
        return False

    await prisma.user.delete(where={"uuid": user.uuid})
    return True


async def find_user_accepted(id: int):
    return await prisma.user.find_first(where={"id": id}, include=user_include)


async def find_user_invited(username: str):
    return await prisma.user.find_first(
        where={"admin": False, "username": username}, include=user_include
    )


async def find_users_accepted():
    return await prisma.user.find_many(
        where={"admin": False, "id": {"not": {"equals": None}}}, include=user_include  # type: ignore
    )


async def delete_user(uuid: str):
    return await prisma.user.delete(where={"uuid": uuid})


async def user_add_channel(chat: Chat, user: User):
    return await prisma.channel.upsert(
        where={"id": chat.id},
        data={
            "create": {
                "id": chat.id,
                "name": chat.username,
                "users": {"connect": {"uuid": user.uuid}},
            },
            "update": {
                "name": chat.username,
                "users": {"connect": {"uuid": user.uuid}},
            },
        },
    )


async def find_channel_with_users(id: int):
    return await prisma.channel.find_first(
        where={"id": id, "users": {"some": {}}}, include=channel_include
    )


async def user_delete_channel(name: str, user: User):
    await prisma.user.update(
        where={"uuid": user.uuid}, data={"channels": {"disconnect": {"name": name}}}
    )


async def user_add_filter(filter: str, channel: str, user: User):
    c = await prisma.channel.find_unique(where={"name": channel})
    return await prisma.filter.create(
        data={
            "channelUuid": c.uuid,
            "filter": filter,
            "userUuid": user.uuid,
        }
    )


async def user_delete_filter(filter: str, channel: str, user: User):
    c = await prisma.channel.find_unique(where={"name": channel})
    f = await prisma.filter.find_first(
        where={
            "channelUuid": c.uuid,
            "filter": filter,
            "userUuid": user.uuid,
        }
    )
    return await prisma.filter.delete(
        where={"uuid": f.uuid},
    )
