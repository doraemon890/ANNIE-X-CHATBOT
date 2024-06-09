import logging
from pyrogram import filters, Client
from pyrogram.types import Message
from ANNIECHATBOT import app, OWNER
from ANNIECHATBOT.database.chats import get_served_chats
from ANNIECHATBOT.database.users import get_served_users

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def send_media_message(chat_id: int, message: Message):
    try:
        if message.text:
            await app.send_message(chat_id, message.text)
        elif message.photo:
            await app.send_photo(chat_id, photo=message.photo.file_id, caption=message.caption)
        elif message.video:
            await app.send_video(chat_id, video=message.video.file_id, caption=message.caption)
        elif message.document:
            await app.send_document(chat_id, document=message.document.file_id, caption=message.caption)
        # Add support for more media types as needed
        logger.info(f"Message sent to {chat_id}")
    except Exception as e:
        logger.error(f"Failed to send message to {chat_id}: {e}")

async def broadcast_message(message: Message):
    served_chats = await get_served_chats()
    served_users = await get_served_users()
    
    successful_chats = 0
    successful_users = 0

    for chat in served_chats:
        try:
            await send_media_message(chat['chat_id'], message)
            successful_chats += 1
        except Exception as e:
            logger.error(f"Failed to send message to chat {chat['chat_id']}: {e}")
    
    for user in served_users:
        try:
            await send_media_message(user['user_id'], message)
            successful_users += 1
        except Exception as e:
            logger.error(f"Failed to send message to user {user['user_id']}: {e}")

    return successful_chats, successful_users

@app.on_message(filters.command("broadcast") & filters.user(OWNER))
async def handle_broadcast(cli: Client, message: Message):
    if not any([message.text, message.photo, message.video, message.document]):
        await message.reply_text("Please provide a message or media to broadcast.")
        return
    
    successful_chats, successful_users = await broadcast_message(message)
    await message.reply_text(
        f"Broadcast message sent to {successful_chats} chats and {successful_users} users."
    )
