import os
from pyrogram import Client, filters
from pyrogram.types import Message
from STORM.helper.basic import edit_or_reply
from config import SUDO_USERS

@Client.on_message(
    filters.command(["env"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def env(_, e: Message):
    env_vars = "\n".join([f"{key}={value}" for key, value in os.environ.items()])
    await edit_or_reply(e, f"```\n{env_vars}\n```")
