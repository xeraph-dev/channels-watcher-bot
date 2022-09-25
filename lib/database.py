from pyrogram.types import User as PyUser, Chat
from prisma.types import UserInclude
from prisma.models import User

from lib.app import prisma

user_include: UserInclude = {
    "channels": {"include": {"filters": True}},
}


async def create_admin(user: PyUser):
    return await prisma.user.create(
        data={
            "admin": True,
            "id": user.id,
            "username": user.username,
        }
    )


async def find_user_by_id_or_username(user: PyUser):
    return await prisma.user.find_first(
        where={
            "id": user.id,
            "OR": [{"username": user.username}],
        },
        include=user_include,
    )


async def update_user_username(uuid: str, username: str):
    return await prisma.user.update(
        where={"uuid": uuid}, data={"username": username}, include=user_include
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


async def find_channel(id: int):
    return await prisma.channel.find_first(where={"id": id})
