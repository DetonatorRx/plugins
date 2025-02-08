import os
import sys
import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS, OWNER_ID, HEROKU_APP_NAME, HEROKU_API_KEY

async def edit_or_reply(message: Message, text: str):
    try:
        await message.edit(text)
    except:
        await message.reply(text)
def restart_heroku_app():
    url = f"https://api.heroku.com/apps/{HEROKU_APP_NAME}/dynos"
    headers = {
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3",
        "Content-Type": "application/json"
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        print("ʜᴇʀᴏᴋᴜ ᴀᴘᴘ ʀᴇꜱᴛᴀʀᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ.")
    else:
        print(f"ꜰᴀɪʟᴇᴅ ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ʜᴇʀᴏᴋᴜ ᴀᴘᴘ: {response.status_code}, {response.text}")


@Client.on_message(
    filters.command(["instantboot", "restart"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def restart_bot(_, e: Message):
    msg = await edit_or_reply(e, "ʀᴇꜱᴛᴀʀᴛɪɴɢ...")
    if msg:
        await msg.edit("⌛")
    else:
        print("ꜰᴀɪʟᴇᴅ ᴛᴏ ᴜᴘᴅᴀᴛᴇ ᴍᴇꜱꜱᴀɢᴇ ꜱᴛᴀᴛᴜꜱ, ʙᴜᴛ ʏᴏᴜʀ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ɪꜱ ʀᴇʙᴏᴏᴛɪɴɢ.")

    if restart_heroku_app():
        if msg:
            await msg.edit("ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ɪꜱ ʀᴇʙᴏᴏᴛɪɴɢ. ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ.")
    else:
        if msg:
            await msg.edit("ꜰᴀɪʟᴇᴅ ᴛᴏ ᴛʀɪɢɢᴇʀ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ʀᴇʙᴏᴏᴛ. ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʟᴏɢꜱ.")

    try:
        os.execvp("python3", ["python3", "boot.py"])  # Correctly execute boot.py using python3
    except Exception as e:
        print(f"Failed to execute boot.py: {e}")
