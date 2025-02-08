import os
from pyrogram import Client, filters
from pyrogram.types import Message
from STORM.helper.basic import edit_or_reply, get_text, get_user
from config import SUDO_USERS

OWNER = os.environ.get("OWNER", None)
BIO = os.environ.get("BIO", "@STORM_CHATZ")


original_name = None

@Client.on_message(
    filters.command(["clone"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def clone(client: Client, message: Message):
    global original_name

    text = get_text(message)
    op = await edit_or_reply(message, "ᴄʟᴏɴɪɴɢ....")
    userk = get_user(message, text)[0]
    user_ = await client.get_users(userk)
    if not user_:
        await op.edit("ᴡʜᴏᴍ ɪ ꜱʜᴏᴜʟᴅ ᴄʟᴏɴᴇ.....?")
        return

    original_name = (await client.get_me()).first_name

    get_bio = await client.get_chat(user_.id)
    f_name = user_.first_name
    c_bio = get_bio.bio
    pic = user_.photo.big_file_id
    poto = await client.download_media(pic)

    await client.set_profile_photo(photo=poto)
    await client.update_profile(
        first_name=f_name,
        bio=c_bio,
    )
    await message.edit(f"**ɴᴏᴡ ɪ'ᴍ** {f_name}")


@Client.on_message(
    filters.command(["revert"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def revert(client: Client, message: Message):
    global original_name

    await message.edit("ʀᴇᴠᴇʀᴛɪɴɢ....")
    r_bio = BIO

    if original_name is not None:
        await client.update_profile(
            first_name=original_name,
            bio=r_bio,
        )
    else:
        await client.update_profile(
            first_name=OWNER,
            bio=r_bio,
        )
    photos = [p async for p in client.get_chat_photos("me")]
    if photos:
        await client.delete_profile_photos(photos[0].file_id)

    await message.edit("ɪ ᴀᴍ ʙᴀᴄᴋ....!")
