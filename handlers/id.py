from pyrogram import Client
from pyrogram.types import Message
from config import BOT_USERNAME
from helpers.filters import command
from helpers.filters import command2, other_filters
from helpers.get_file_id import get_file_id
from cache.admins import admins
from pyrogram import Client, filters
from helpers.decorators import authorized_users_only
from helpers.queues import QUEUE, clear_queue
from helpers.utils import skip_current_song, skip_item


@Client.on_message(command(["id", "stickerid", "stkid", "stckrid", f"id@{BOT_USERNAME}"]))
async def showid(_, message: Message):
    await message.delete()
    chat_type = message.chat.type

    if chat_type == "private":
        user_id = message.chat.id
        await message.reply_text(f"<code>{user_id}</code>")

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += "<b>ᴄʜᴀᴛ ɪᴅ</b>: " f"<code>{message.chat.id}</code>\n"
        if message.reply_to_message:
            _id += (
                "<b>ʀᴇᴩʟɪᴇᴅ ᴜsᴇʀ ɪᴅ</b>: "
                f"<code>{message.reply_to_message.from_user.id}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += "<b>ᴜsᴇʀ ɪᴅ</b>: " f"<code>{message.from_user.id}</code>\n"
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(_id)
 
@Client.on_message(command2(["ايدي","الايدي"]))
async def showid(_, message: Message):
    await message.delete()
    chat_type = message.chat.type

    if chat_type == "private":
        user_id = message.chat.id
        await message.reply_text(f"<code>{user_id}</code>")

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += "<b>ᴄʜᴀᴛ ɪᴅ</b>: " f"<code>{message.chat.id}</code>\n"
        if message.reply_to_message:
            _id += (
                "<b>ʀᴇᴩʟɪᴇᴅ ᴜsᴇʀ ɪᴅ</b>: "
                f"<code>{message.reply_to_message.from_user.id}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += "<b>ᴜsᴇʀ ɪᴅ</b>: " f"<code>{message.from_user.id}</code>\n"
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(_id)