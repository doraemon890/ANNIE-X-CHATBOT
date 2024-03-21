

import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import OWNER_USERNAME
from ANNIECHATBOT import app
from ANNIECHATBOT.database.chats import add_served_chat
from ANNIECHATBOT.database.users import add_served_user
from ANNIECHATBOT.modules.helpers import PNG_BTN


#----------------IMG-------------#



# Random Start Images
IMG = [
    "https://telegra.ph/file/61670d3373f2c8bdc2bcb.png",
    "https://telegra.ph/file/74d333a2eb853d6d340e5.png",
    "https://telegra.ph/file/e29c7352ac8a29c6d7d1c.png",
    "https://telegra.ph/file/024c4d788089a549f7c18.png",
    "https://telegra.ph/file/21a6c46b6b997c9baa507.png",
    "https://telegra.ph/file/e4205a5896e9cd1354df4.png",
    "https://telegra.ph/file/ceaee4640a3af5acdb717.png",
    "https://telegra.ph/file/98f40c919b0598586d697.png",
    "https://graph.org/file/36af423228372b8899f20.jpg",
  
]



#----------------IMG-------------#

#---------------STICKERS---------------#

# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]

#---------------STICKERS---------------#



@app.on_cmd("Annieping")
async def ping(_, message: Message):
    await message.reply_sticker(sticker=random.choice(STICKER))
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢɪɴɢ...",
    )
    try:
        await message.delete()
    except:
        pass

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"нey вαву!!\n{app.name} ιѕ alιve 🥀 αnd worĸιng ғιne wιтн a pιng oғ\n➥ `{ms}` ms\n\n<b>мαdє ву [𝙹ᴀʀᴠɪs](https://t.me/{OWNER_USERNAME}) </b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
