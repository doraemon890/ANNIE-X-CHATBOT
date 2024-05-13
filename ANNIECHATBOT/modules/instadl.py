import requests
from pyrogram import Client, filters
from pyrogram.types import *
from ANNIECHATBOT  import app

RAPIDAPI_KEY = "923bca7ccdmsh620363d2a9cf295p15f78bjsnfa1040c941aa"

@app.on_message(filters.command("insta"))
async def download_instagram_reel(client, message):
    try:
        if len(message.text.split(" ")) == 1:
            await message.reply_text("Please provide an Instagram link after the command.")
            return
        
        url = message.text.split(" ", 1)[1]
        payload = {"url": url}
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": RAPIDAPI_KEY,
            "X-RapidAPI-Host": "instagram-bulk-scraper-latest.p.rapidapi.com"
        }
        response = requests.post("https://instagram-bulk-scraper-latest.p.rapidapi.com/media_download_from_url", json=payload, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            # Assuming the response structure matches the provided schema
            if "key1" in data and "key2" in data:
                video_url = data["key1"]
                await message.reply_video(video_url)
            else:
                await message.reply_text("Invalid response structure.")
        else:
            await message.reply_text(f"Request failed with status code: {response.status_code}")
    except Exception as e:
        await message.reply_text(f"Something went wrong: {e}")
