import logging
from pyrogram import filters, Client
from pyrogram.types import Message
from ANNIECHATBOT import OWNER, app
from ANNIECHATBOT.database.chats import get_served_chats
from ANNIECHATBOT.database.users import get_served_users

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def fetch_stats():
    try:
        users_count = len(await get_served_users())
        chats_count = len(await get_served_chats())
        return users_count, chats_count
    except Exception as e:
        logger.error(f"Error fetching stats: {e}")
        return 0, 0

async def format_stats_message(cli: Client, users: int, chats: int) -> str:
    bot_mention = (await cli.get_me()).mention
    return (
        f"ᴛᴏᴛᴀʟ sᴛᴀᴛs ᴏғ {bot_mention} :\n\n"
        f"➻ **ᴄʜᴀᴛs :** {chats}\n"
        f"➻ **ᴜsᴇʀs :** {users}"
    )

@app.on_message(filters.command("stats") & filters.user(OWNER))
async def stats(cli: Client, message: Message):
    users_count, chats_count = await fetch_stats()
    stats_message = await format_stats_message(cli, users_count, chats_count)
    await message.reply_text(stats_message)
