import datetime
from pyrogram import Client, filters
from pyrogram.types import Message
from STORM.helper.basic import edit_or_reply
from config import SUDO_USERS

@Client.on_message(
    filters.command(["ping"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def ping(_, e: Message):
    start = datetime.datetime.now()
    msg = await edit_or_reply(e, "⚡")
    ms = (datetime.datetime.now() - start).microseconds / 1000
    await msg.edit(
        f"""
        **⧼ ꜱʏɴᴛʜᴇᴛɪᴄ ʀᴇꜱᴘᴏɴꜱᴇ ᴀᴄᴛɪᴠᴇ ⧽**
        **❏ ꜱ ᴛ ᴏ ʀ ᴍ 🥀**      
        **├•** **ꜱᴛᴀᴛᴜꜱ: ᴀᴄᴛɪᴠᴇ**
        **├•** **ʀᴇꜱᴘᴏɴꜱᴇ ᴛɪᴍᴇ:** `{ms} ᴍꜱ`          
        **├•** **ᴠᴇʀꜱɪᴏɴ:** `ꜱ-ᴘʀɪᴍᴇ 2.1.1@ᴍᴀɪɴ`          
        **├• ᴛʜᴇ ᴄᴀʟᴍ ʙᴇꜰᴏʀᴇ ᴛʜᴇ ꜱᴛᴏʀᴍ ⚡**
        **└• ᴘᴏᴡᴇʀᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ᴀɪ 🤖**
        """
    )
