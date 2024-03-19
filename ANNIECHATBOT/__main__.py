import asyncio
import importlib

from pyrogram import idle

from ANNIECHATBOT import LOGGER, app
from ANNIECHATBOT.modules import ALL_MODULES


async def jarvis_boot():
    try:
        await app.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("ANNIECHATBOT.modules." + all_module)

    LOGGER.info(f"@{app.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(jarvis_boot())
    LOGGER.info("Stopping app Bot...")
