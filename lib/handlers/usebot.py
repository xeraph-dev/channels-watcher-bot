from pyrogram import filters
from pyrogram.types import Message
from prisma.models import Channel

import lib.app as app
from lib.decorators import only_joined, userbot_inject
from lib.i18n import t

normalize_dict = {
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u",
    "ü": "u",
    "b": "v",
    "z": "s",
    "ca": "ka",
    "ce": "se",
    "ci": "si",
    "co": "ko",
    "cu": "ku",
    ",": " ",
    ".": " ",
    ";": " ",
    "ll": "y",
}


def normalize(s: str) -> str:
    s = s.lower()
    for [f, t] in normalize_dict.items():
        s = s.replace(f, t)
    return s


@app.userbot.on_message([filters.channel, filters.group])
@userbot_inject
@only_joined
async def watcher(channel: Channel, message: Message):
    for filter in channel.filters:
        if normalize(filter.filter) in normalize(message.text):
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
