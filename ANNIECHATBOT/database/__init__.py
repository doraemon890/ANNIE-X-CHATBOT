from pymongo import MongoClient

import config

anniedb = MongoClient(config.MONGO_URL)
annie = anniedb["AnnieDb"]["Annie"]


from .chats import *
from .users import *
