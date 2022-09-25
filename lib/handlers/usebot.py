from pyrogram import filters
from pyrogram.types import Message
from prisma.models import Channel

import lib.app as app
from lib.decorators import only_joined, userbot_inject


@app.userbot.on_message(filters.channel)
@userbot_inject
@only_joined
async def watcher(channel: Channel, message: Message):
    print(channel.name)
