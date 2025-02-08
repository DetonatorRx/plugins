from pyrogram import Client, filters
from STORM.Database.pm import *
from STORM.powers import get_id
from config import PM_PIC, SUDO_USERS
hl = "."
pm_watcher = 5
KEX = PM_PIC

TEXT = """
•            **[ꜱᴛᴏʀᴍ](https://github.com/KEX001/STORM-UB)**
╰• **ᴏᴡɴᴇʀ** » {}
• **ᴛʜɪs ɪs ᴋᴇx ᴘᴍ sᴇᴄᴜʀɪᴛʏ 🛡️**
➖➖➖➖➖➖➖➖➖➖➖ 
    **ʜᴇʏ ʙᴜᴅᴅʏ** 🥀
    **ɪғ ʏᴏᴜ sᴘᴀᴍ ʜᴇʀᴇ ᴡɪᴛʜᴏᴜᴛ ᴍʏ**
    **ꜱᴇɴꜱᴇɪ's ᴀᴘᴘʀᴏᴠᴀʟ ʏᴏᴜ ᴡɪʟʟ ʙᴇ**
    **ʙʟᴏᴄᴋᴇᴅ** 
• **ᴡᴀʀɴ ʟɪᴍɪᴛs** » {}      
• **ʏᴏᴜʀ ᴡᴀʀɴs** » {}
╰• **ᴘᴏᴡᴇʀᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ᴀɪ 🤖**
➖➖➖➖➖➖➖➖➖➖➖
•           **[ꜱᴜᴘᴘᴏʀᴛ](https://t.me/STORM_CHATZ)**
"""

@Client.on_message(
    filters.command(["pmpermit"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def pmpermit(client, message):
    x = await is_pm_on()
    try:
        tg = message.text.split()[1].lower()
    except:
        return await message.edit(f"{hl}pmpermit [on | off]")
    if not tg in ["on", "off"]:
        return await message.edit(f"{hl}pmpermit [on | off]")
    if tg == "on":
        if x:
            return await message.edit("ᴘᴍᴘᴇʀᴍɪᴛ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ ᴛᴏ ᴛᴜʀɴ ɪᴛ ᴏꜰꜰ ᴜꜱᴇ `.pmpermit off`")
        await toggle_pm()
        if await limit() == 0:
            await update_warns(3)
        return await message.edit("ᴘᴍᴘᴇʀᴍɪᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴇɴᴀʙʟᴇᴅ.. ᴛᴏ ᴛᴜʀɴ ɪᴛ ᴏꜰꜰ ᴜꜱᴇ `.pmpermit off`")
    if not x:
        return await message.edit("ᴘᴍᴘᴇʀᴍɪᴛ ɪꜱ ɴᴏᴛ ᴇɴᴀʙʟᴇᴅ....ᴛᴏ ᴛᴜʀɴ ɪᴛ ᴏɴ ᴜꜱᴇ `.pmpermit on`")
    await toggle_pm()
    return await message.edit("ᴘᴍᴘᴇʀᴍɪᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅɪꜱᴀʙʟᴇᴅ....ᴛᴏ ᴛᴜʀɴ ɪᴛ ᴏɴ ᴜꜱᴇ `.pmpermit on`")

@Client.on_message(
    filters.command(["approve", "disapprove", "a", "da", "allow", "disallow"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def appr_dis(client, message):
    if str(message.chat.id)[0] == "-":
        try:
            id = await get_id(_, message)
        except:
            return await message.edit("ꜰᴏʀ ᴀᴘᴘʀᴏᴠᴇ ᴜꜱᴇʀ ɪɴ ɢʀᴏᴜᴘ ᴜ ᴡᴀɴᴛ ᴛᴏ ɢɪᴠᴇ ᴍᴇ ɪ'ᴅ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴀᴛ ᴜꜱᴇʀ..")
    else:
        id = message.chat.id
    tg = message.text.split()[0][1]
    x = await is_approved(id)
    if tg == "d":
        if not x:
            return await message.edit("ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ɴᴏᴛ ᴀᴘᴘʀᴏᴠᴇᴅ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ..")
        await disapprove(id)
        return await message.edit("ᴜꜱᴇʀ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅɪꜱᴀᴘᴘʀᴏᴠᴇᴅ ꜰʀᴏᴍ ᴘᴍ...")
    if x:
        return await message.edit("ᴜꜱᴇʀ ᴀʟʀᴇᴀᴅʏ ᴀᴘᴘʀᴏᴠᴇᴅ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ....")
    await approve(id)
    await reset_warns(id)
    return await message.edit("ᴜꜱᴇʀ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴀᴘᴘʀᴏᴠᴇᴅ ꜰᴏʀ ᴘᴍ....")


@Client.on_message(
    filters.command(["setwarns"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def setwarn(client, message):
    try:
        count = int(message.text.split()[1])
    except:
        return await message.edit(f"ᴏʜᴏ, ʏᴏᴜ ᴛʏᴘᴇᴅ ɪᴛ ᴡʀᴏɴɢ! ᴜꜱᴇ ɪᴛ ʟɪᴋᴇ ᴛʜɪꜱ: .setwarns [ᴠᴀʟᴜᴇ].")
    if count == 0:
        return await message.edit("ꜰᴏᴜɴᴅ ᴀ ꜱʏɴᴛᴀx ᴇʀʀᴏʀ. ɪɴᴘᴜᴛ ᴛʜᴇ ᴠᴀʟᴜᴇ ᴛᴏ ꜱᴇᴛ ᴡᴀʀɴꜱ.")
    await update_warns(count)
    await message.edit(f"ᴅᴍ ᴡᴀʀɴꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴄᴀʟɪʙʀᴀᴛᴇᴅ ᴛᴏ {count}")
    
@Client.on_message(filters.private, group=pm_watcher)
async def wtch(client, message):
    user_ = message.from_user
    if message.from_user.id == client.me.id:
        return
    if not await is_pm_on():
        return
    if user_.is_bot:
        return
    if await is_approved(message.from_user.id):
        return
    await add_warn(message.from_user.id)
    if await limit() <= await get_warns(message.from_user.id):
        await message.reply("ꜱᴘᴀᴍᴍᴇʀ ɴᴇᴜᴛʀᴀʟɪᴢᴇᴅ ᴀɴᴅ ᴇʟɪᴍɪɴᴀᴛᴇᴅ ⚠️")
        await reset_warns(message.from_user.id)
        return await client.block_user(message.from_user.id)
    await message.reply_photo(KEX, caption=TEXT.format((await client.get_me()).first_name, await limit(), await get_warns(message.from_user.id)))
