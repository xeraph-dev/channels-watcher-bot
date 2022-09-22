from dataclasses import dataclass
import os
import yaml
from pyrogram.types import BotCommand
from dotenv import load_dotenv

load_dotenv()


class Env:
    API_ID = os.environ["API_ID"]
    API_HASH = os.environ["API_HASH"]
    BOT_TOKEN = os.environ["BOT_TOKEN"]
    ADMIN_ID = int(os.environ["ADMIN_ID"])
    BOT_SESSION = os.environ["BOT_SESSION"]
    USER_SESSION = os.environ["USER_SESSION"]


locales: list[str] = []
messages: dict = {}

for locale in os.listdir("locales"):
    code: str = locale.split(".yaml")[0]
    locales.append(code)
    with open(os.path.join("locales", locale), "r") as file:
        messages[code] = yaml.safe_load(file)

commands: list[str] = [
    "help",
    "list_channels",
    "add_channel",
    "delete_channel",
    "list_filters",
    "list_channel_filters",
    "add_filter",
    "delete_filter",
]
bot_commands: dict = {}

for locale in locales:
    bot_commands[locale] = []
    for command in commands:
        bot_commands[locale].append(
            BotCommand(
                messages[locale][command]["command"],
                messages[locale][command]["description"],
            )
        )
