import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
 •💣 ¦ اهـلا عـزيـزي. انا بــوت اقـوم بـتـشـغـيل الـموـسـيقي فـي الــمحــادثهةة الــصـوتـيـه♥
🕵 ¦ الـيك لـوحـة التـحـكم الـخـاصـة بالبوت [قناة السورس](t.me/b_1_4_7)...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ اضف البوت💣  ➕", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "• قناة البوت •", url=f"https://t.me/b_1_4_7"
                    ),
                    InlineKeyboardButton(
                        "• جــروب الدعــم •", url=f"https://t.me/c_3_517}"
                    )
                ],[
                    InlineKeyboardButton(
                        "• الاوامر •",/تشغيل +اسم الاغنيه
/تخطي ل تخطي الاغنيه وتشغيل الاغنيه التاليه
/ايقاف لإيقاف الاغنيه من المكالمه
/انضم لينضم حساب المساعد الى المجموعه
/فيديو لتحميل فيديو
/اغنيه لتنزيل اغنيه"
                    ),
                    InlineKeyboardButton(
                        "• مطور السورس •", url="https://t.me/Q_P_K_E"
                    )]
            ]
       ),
    )


