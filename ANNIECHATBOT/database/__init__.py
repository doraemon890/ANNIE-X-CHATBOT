from pymongo import MongoClient
import config
from pyrogram import Client  # Assuming bot is a pyrogram Client instance

# Establish the database connection
anniedb = MongoClient(config.MONGO_URL)
chatsdb = anniedb["AnnieDb"]["chats"]
usersdb = anniedb["AnnieDb"]["users"]

# Define the bot
app = Client("my_bot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)
OWNER = config.OWNER_ID

# Import modules to make them available
from .chats import *
from .users import *
from .broadcast import *
