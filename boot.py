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

from config import API_ID, API_HASH, SESSIONS
from pyrogram import Client, idle
import sys

CLIENTS = []

for i,SESSION in enumerate(SESSIONS):
    if SESSION:
        client = Client(
            name=f"STORM{i}",
            session_string=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            plugins=dict(root="STORM.modules"),
        )
        CLIENTS.append(client)


if __name__ == "__main__":
    for i, CLIENT in enumerate(CLIENTS):
        try:
            CLIENT.start()
            CLIENT.join_chat("STORM_CHATZ")
            CLIENT.join_chat("STORM_TECHH")
            CLIENT.join_chat("TORNADO_TRIBE")
            CLIENT.join_chat("BOT_DEVEPOLING")
            CLIENT.join_chat("rasedidstore")
            print(f"ꜱᴛᴏʀᴍ ꜱᴛᴀʀᴛᴇᴅ ᴀꜱ {i+1}")
            print(f"ʙᴏᴏᴛᴇᴅ/ꜱᴛᴀʀᴛᴇᴅ {CLIENT.me.first_name} 🎉")
        except Exception as e:
            print(f"[ꜱᴛᴏʀᴍ ᴀɪ] - ꜰᴏᴜɴᴅ ᴀ ᴇʀʀᴏʀ {e}")
            print("ꜰᴏᴜɴᴅ ᴀ ꜱᴇʀᴠᴇʀ ᴇʀʀᴏʀ. ʏᴏᴜʀ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ᴍᴀʏ ɴᴏᴛ ʙᴇ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ᴛʜᴇ ꜱᴛᴏʀᴍ'ꜱ ꜱᴇʀᴠᴇʀ. ꜱʜᴜᴛᴛɪɴɢ ᴅᴏᴡɴ ᴛʜᴇ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ᴛᴏ ᴋᴇᴇᴘ ʏᴏᴜʀ ʙᴏᴛ ꜱᴀꜰᴇ... 🔒")
            sys.exit(1)

    print("ꜱᴛᴏʀᴍ ᴜꜱᴇʀ ʙᴏᴛ ɪꜱ ᴅᴇᴘʟᴏʏᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 🌩️🥀")
    idle()

