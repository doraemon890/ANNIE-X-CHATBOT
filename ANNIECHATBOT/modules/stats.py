from pyrogram import filters, Client
from pyrogram.types import Message

from ANNIECHATBOT import OWNER, app
from ANNIECHATBOT.database.chats import get_served_chats
from ANNIECHATBOT.database.users import get_served_users

async def fetch_stats():
    users_count = len(await get_served_users())
    chats_count = len(await get_served_chats())
    return users_count, chats_count

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
