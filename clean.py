import os
from dotenv import set_key


print("Cleaning API ID...")
set_key(".env", "API_ID", "")

print("Cleaning API HASH...")
set_key(".env", "API_HASH", "")

print("Cleaning Bot Token...")
set_key(".env", "BOT_TOKEN", "")

print("Deleting session files")
os.remove("bot.session")
os.remove("user.session")
