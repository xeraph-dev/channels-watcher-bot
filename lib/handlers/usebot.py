from pyrogram import filters
from pyrogram.types import Message
from prisma.models import Channel

import lib.app as app
from lib.decorators import only_joined, userbot_inject
from lib.i18n import t


@app.userbot.on_message(filters.channel)
@userbot_inject
@only_joined
async def watcher(channel: Channel, message: Message):
    for filter in channel.filters:
        if filter.filter in message.text.lower():
            await app.bot.send_message(
                filter.user.id,
                t(filter.user.lang)(
                    "message_from_channel",
                    {
                        "channel": channel.name,
                        "filter": filter.filter,
                        "link": message.link,
                    },
                ),
            )
