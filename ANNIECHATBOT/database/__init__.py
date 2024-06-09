from pymongo import MongoClient
import config

# Establish the database connection
anniedb = MongoClient(config.MONGO_URL)
chatsdb = anniedb["AnnieDb"]["chats"]
usersdb = anniedb["AnnieDb"]["users"]

# Import modules to make them available
from .chats import *
from .users import *
from .broadcast import *
