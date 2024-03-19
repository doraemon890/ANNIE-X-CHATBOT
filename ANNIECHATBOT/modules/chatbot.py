import random
from Abg.chat_status import adminsOnly
from pymongo import MongoClient
from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from pyrogram.types import InlineKeyboardMarkup, Message
from config import MONGO_URL
from ANNIECHATBOT import app
from ANNIECHATBOT.modules.helpers import CHATBOT_ON, is_admins

# Command to enable/disable chatbot (admin only)
@app.on_cmd("chatbot", group_only=True)
@adminsOnly("can_delete_messages")
async def chaton_(_, m: Message):
    await m.reply_text(
        f"ᴄʜᴀᴛ: {m.chat.title}\n**ᴄʜᴏᴏsᴇ ᴀɴ ᴏᴩᴛɪᴏɴ ᴛᴏ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ.**",
        reply_markup=InlineKeyboardMarkup(CHATBOT_ON),
    )

# Function to handle text messages in chat
@app.on_message(
    (filters.text | filters.sticker | filters.group) & ~filters.private & ~filters.bot, group=4
)
async def chatbot_text(client: Client, message: Message):
    try:
        if message.text.startswith("!") or message.text.startswith("/") or message.text.startswith("?") or message.text.startswith("@") or message.text.startswith("#"):
            return
    except Exception:
        pass

    chatdb = MongoClient(MONGO_URL)
    chatai = chatdb["Word"]["WordDb"]

    if not message.reply_to_message:
        await handle_non_reply_message(client, message, chatai)
    else:
        await handle_reply_message(client, message, chatai)

# Function to handle sticker messages in chat
@app.on_message(
    (filters.sticker | filters.group | filters.text) & ~filters.private & ~filters.bot, group=4
)
async def chatbot_sticker(client: Client, message: Message):
    try:
        if message.text.startswith("!") or message.text.startswith("/") or message.text.startswith("?") or message.text.startswith("@") or message.text.startswith("#"):
            return
    except Exception:
        pass

    chatdb = MongoClient(MONGO_URL)
    chatai = chatdb["Word"]["WordDb"]

    if not message.reply_to_message:
        await handle_non_reply_message(client, message, chatai)
    else:
        await handle_reply_message(client, message, chatai)

# Function to handle private messages
@app.on_message(
    (filters.text | filters.sticker | filters.group) & ~filters.private & ~filters.bot, group=4
)
async def chatbot_pvt(client: Client, message: Message):
    try:
        if message.text.startswith("!") or message.text.startswith("/") or message.text.startswith("?") or message.text.startswith("@") or message.text.startswith("#"):
            return
    except Exception:
        pass

    chatdb = MongoClient(MONGO_URL)
    chatai = chatdb["Word"]["WordDb"]

    if not message.reply_to_message:
        await handle_non_reply_message(client, message, chatai)
    else:
        await handle_reply_message(client, message, chatai)

# Function to handle sticker messages in private chats
@app.on_message(
    (filters.sticker | filters.sticker | filters.group) & ~filters.private & ~filters.bot, group=4
)
async def chatbot_sticker_pvt(client: Client, message: Message):
    try:
        if message.text.startswith("!") or message.text.startswith("/") or message.text.startswith("?") or message.text.startswith("@") or message.text.startswith("#"):
            return
    except Exception:
        pass

    chatdb = MongoClient(MONGO_URL)
    chatai = chatdb["Word"]["WordDb"]

    if not message.reply_to_message:
        await handle_non_reply_message(client, message, chatai)
    else:
        await handle_reply_message(client, message, chatai)

# Helper function to handle non-reply messages
async def handle_non_reply_message(client, message, chatai):
    anniedb = MongoClient(MONGO_URL)
    annie = anniedb["AnnieDb"]["Annie"]
    is_annie = annie.find_one({"chat_id": message.chat.id})

    if not is_annie:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)
        K = []
        is_chat = chatai.find({"word": message.text})
        k = chatai.find_one({"word": message.text})

        if k:
            for x in is_chat:
                K.append(x["text"])
            hey = random.choice(K)
            is_text = chatai.find_one({"text": hey})
            Yo = is_text["check"]
            if Yo == "sticker":
                await message.reply_sticker(f"{hey}")
            if not Yo == "sticker":
                await message.reply_text(f"{hey}")

# Helper function to handle reply messages
async def handle_reply_message(client, message, chatai):
    anniedb = MongoClient(MONGO_URL)
    annie = anniedb["AnnieDb"]["Annie"]
    is_annie = annie.find_one({"chat_id": message.chat.id})

    if message.reply_to_message.from_user.id == client.id:
        if not is_annie:
            await client.send_chat_action(message.chat.id, ChatAction.TYPING)
            K = []
            is_chat = chatai.find({"word": message.text})
            k = chatai.find_one({"word": message.text})

            if k:
                for x in is_chat:
                    K.append(x["text"])
                hey = random.choice(K)
                is_text = chatai.find_one({"text": hey})
                Yo = is_text["check"]
                if Yo == "sticker":
                    await message.reply_sticker(f"{hey}")
                if not Yo == "sticker":
                    await message.reply_text(f"{hey}")
