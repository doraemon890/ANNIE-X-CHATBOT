from pymongo import MongoClient
import config
from pyrogram import Client  # Assuming bot is a pyrogram Client instance

# Establish the database connection
anniedb = MongoClient(config.MONGO_URL)
annie = anniedb["AnnieDb"]["Annie"]
chatsdb = anniedb["AnnieDb"]["chats"]
usersdb = anniedb["AnnieDb"]["users"]

# Import modules to make them available
from .chats import *
from .users import *
