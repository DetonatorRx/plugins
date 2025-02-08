#MIT License

#Copyright (c) 2024 ᴋᴜɴᴀʟ [AFK]

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from config import SUDO_USERS, HELP_PIC

from pyrogram import Client, filters
from pyrogram.types import Message

hl = "."

NEWS_TEXT = f"""
**•─╼⃝𖠁 ɪɴᴛᴇʀɴᴇᴛ ᴄᴏᴍᴍᴀɴᴅꜱ 𖠁⃝╾─•** 

🔹 `{hl}news` » ᴛᴏ ɢᴇᴛ ᴛᴏᴘ 5 ʜᴇᴀᴅʟɪɴᴇꜱ ᴏꜰ ɴᴇᴡꜱ  
🔹 `{hl}weather (ʏᴏᴜʀ ᴄɪᴛʏ)` » ᴛᴏ ɢᴇᴛ ᴡᴇᴀᴛʜᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ  
🔹 `{hl}ai (ʏᴏᴜʀ Qᴜᴇʀʏ)` » ᴄʜᴇᴄᴋ ʏᴏᴜʀꜱᴇʟꜰ  
🔹 `{hl}google (ʏᴏᴜʀ Qᴜᴇʀʏ)` » ᴄʜᴇᴄᴋ ʏᴏᴜʀꜱᴇʟꜰ  
🔹 `{hl}gitinfo` <username> » ᴛᴏ ɢᴇᴛ ɢɪᴛ ᴀᴄᴄ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ  
🔹 `{hl}video` <ᴠɪᴅᴇᴏ ɴᴀᴍᴇ> » ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴠɪᴅᴇᴏ ᴠɪᴀ [ʏᴏᴜᴛᴜʙᴇ](https://www.youtube.com)  
🔹 `{hl}music` <ᴍᴜꜱɪᴄ ɴᴀᴍᴇ> » ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴍᴜꜱɪᴄ ᴠɪᴀ ᴍᴘ3  
🔹 `{hl}telegraph` <ʀᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ/ᴛᴇxᴛ> » ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴍᴇᴅɪᴀ/ᴛᴇxᴛ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ  
🔹 `{hl}lyrics` <ᴍᴜꜱɪᴄ | ᴀʀᴛɪꜱᴛ ɴᴀᴍᴇ> » ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʟʏʀɪᴄꜱ  
🔹 `{hl}download` <ɪɴꜱᴛᴀɢʀᴀᴍ ᴘᴜʙ ʀᴇᴇʟ ᴜʀʟ> » ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴘᴜʙʟɪᴄ ʀᴇᴇʟ/ᴘᴏꜱᴛ/ꜱᴛᴏʀʏ  
"""

@Client.on_message(
    filters.command(["helpinternet"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def help(x: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await x.send_photo(msg.chat.id, HELP_PIC, caption=NEWS_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await x.send_video(msg.chat.   id, HELP_PIC, caption=NEWS_TEXT) 
