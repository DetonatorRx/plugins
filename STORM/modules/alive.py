import sys
import datetime
from os import execle, environ
from config import ALIVE_PIC, SUDO_USERS
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import __version__ as versipyro
from config import OWNER_ID

@Client.on_message(
    filters.command(["alive"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def alive(x: Client, msg: Message):
    bot_user = await x.get_me()
    KEX = f"""
**⧼ ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ ‌🪽 ⧽**
➖➖➖➖➖➖➖➖➖➖➖
**• ᴍʏ ᴍᴀꜱᴛᴇʀ** 💕: [{bot_user.mention}](tg://user?id={OWNER_ID})
➖➖➖➖➖➖➖➖➖➖➖
**• ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ**: `3.11.3`
**• ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ**: `{versipyro}`
**• ᴜꜱᴇʀʙᴏᴛ ᴠᴇʀꜱɪᴏɴ**: `M2.1.1`
**• ᴜꜱᴇʀʙᴏᴛ ᴠ-ꜱᴛᴀᴛᴜꜱ**: `ꜱ-ᴘʀɪᴍᴇ 2.1.1@ᴍᴀɪɴ`
➖➖➖➖➖➖➖➖➖➖➖
**• ɢʀᴏᴜᴘ: [ꜱᴛᴏʀᴍ ᴄʜᴀᴛᴢ 🥀](https://t.me/STORM_CHATZ)**
**• ᴄʜᴀɴɴᴇʟ: [ꜱᴛᴏʀᴍ ᴛᴇᴄʜ 🥀](https://t.me/STORM_TECHH)**
**• ᴅᴇᴠ: [ᴋᴇx 🥀](https://t.me/KEXX_XD)**
**• ᴅᴇᴘʟᴏʏ: [ʜᴇʀᴏᴋᴜ 💤](https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FKEX001%2FSTORM-UB)**
**• ᴘᴏᴡᴇʀᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ᴀɪ 🤖**
➖➖➖➖➖➖➖➖➖➖➖
"""

    if ".jpg" in ALIVE_PIC or ".png" in ALIVE_PIC:
        await x.send_photo(msg.chat.id, ALIVE_PIC, caption=KEX)
    elif ".mp4" in ALIVE_PIC or ".MP4" in ALIVE_PIC:
        await x.send_video(msg.chat.id, ALIVE_PIC, caption=KEX)
