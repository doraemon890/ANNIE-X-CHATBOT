import asyncio
import importlib
import logging

from pyrogram import idle

from ANNIECHATBOT import LOGGER, app
from ANNIECHATBOT.modules import ALL_MODULES

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

async def jarvis_boot():
    try:
        logger.debug("Starting bot...")
        await app.start()
    except Exception as ex:
        logger.error(f"Failed to start the bot: {ex}")
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("ANNIECHATBOT.modules." + all_module)

    logger.debug(f"Bot @{app.username} started.")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(jarvis_boot())
    logger.info("Stopping app Bot...")
