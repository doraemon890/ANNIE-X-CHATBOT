import requests
from pyrogram import filters
from pyrogram.types import Message

from ANNIECHATBOT import app

# Constants
DOWNLOADING_STICKER_ID = (
    "CAACAgUAAxkBAAPVZgABdwwsYQ43p3HC5oa7sgr0dxJyAAKZCQAC06xgVfO2MI3ouF1cHgQ"
)
API_URL = "https://karma-api2.vercel.app/instadl"  # Replace with your actual API URL


# Function to handle the instadl command
async def instadl_command_handler(client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("Please provide an Instagram link after the command.")
            return
        
        link = message.command[1]

        # Reply with downloading sticker
        downloading_sticker = await message.reply_sticker(DOWNLOADING_STICKER_ID)

        # Make request to the API
        response = requests.get(API_URL, params={"url": link})
        data = response.json()

        if "url" in data:
            video_url = data["url"]
            await message.reply_video(video_url)
        else:
            await message.reply_text("No content found in the response.")

    except Exception as e:
        await message.reply_text(f"An error occurred while processing the request: {e}")

    finally:
        await downloading_sticker.delete()


# Registering the handler
@app.on_message(filters.command(["ig", "instagram", "insta", "instadl"]))
async def handle_instadl_command(client, message: Message):
    await instadl_command_handler(client, message)
