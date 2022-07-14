import asyncio
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import MessageNotModified
from ELLIOT.main import Test, bot as Client
from config import START_PIC, UPDATES_CHANNEL, GROUP_SUPPORT


ALIVE_PIC = START_PIC
HOME_TEXT = "👋🏻 **مرحبا [{}](tg://user?id={})** \n\n🤖 انا **ايــثــون**. \n**استطيع تشغيل الموسيقي, والراديو, Vc Raid, وفديوهات اليوتيوب & وايضا تشغيل فديوهات التلجرام والصوت **"
HELP_TEXT = """
🏷️ **دليل الإعداد** :

\u2022 ابدأ محادثة صوتية في مجموعتك.
\u2022 إضافة  البوت وحساب  المساعد  في الدردشة مع حقوق المسؤول.
\u2022 تمت عملية الإعداد ، اقرأ الأوامر أدناه 👇.
"""



USER_TEXT = """
🏷️ **اوامر الاعضاء** :

\u2022 /تشغيل <Query> اسم الاغنيه او رابط.
\u2022 /فيدديو <Query> عنوان او رابط فيديو.
\u2022 /مباشر <Live Url> لتشغيل فيديو في البث 👇\n /تحميل تحميل اغنيه من اليوتيوب. \n /تحمييل_ف تحميل فيديو من اليوتيوب\n /كلمات بحث عن كلمات اغنيه.
"""

SPAM_TEXT = """
🏷️ **مساعده  @U_K_M8** :

\u2022 /spam <Count> ضع رسالة االاسبام.
\u2022 /fspam <Count> رسالة الاسبام.
\u2022 /delayspam <Count> رسالة الاسبام.
"""

RAID_TEXT = """
🏷️ **اوامر الراديو @Confgat_EG** :

\u2022 /vcraid <chatid> - اعطاء سوزر الدردشه.
\u2022 /vraid <chatid + Reply To Video File> - راديو فيديو.
\u2022 /raidpause - ايقاف الرديو.
\u2022 /raidresume استئناف الرديو.
\u2022 /raidend <chatid> لانهاء الرديو في الدردشه.
"""

ADMIN = """
🏷️ **اوامر الادمن** :

\u2022 /انضم دعوة الحساب المساعد للدردشه.
\u2022 /انهاء انهاء التشغيل.
\u2022 /توقف ايقاف مؤقت.
\u2022 /استئناف استئناف التشغيل.
\u2022 /صوت ضبط الصوت.
\u2022 /تخطي تخطي المسار الحالي.
"""

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("👮 الاوامر", url="https://telegra.ph/%D8%B3%D9%88%D8%B1%D8%B3-%D8%A7%D9%8A%D8%AB%D9%88%D9%86-%D8%A7%D9%84%D8%B5%D9%88%D8%AA%D9%8A-EITHON1-06-21"),
                InlineKeyboardButton("🗨️ الاعضاء", callback_data="users"),
            ],
            [
                InlineKeyboardButton("🤬 الراديو", callback_data="raid"),
                InlineKeyboardButton("🗨️ سبام", callback_data="spam"),
            ],
            [
                InlineKeyboardButton("🤖 مصنع بوتات", url="t.me/O_K_8Bot"),
            ],
            [
                InlineKeyboardButton("🔙 رجوع", callback_data="home"),
                InlineKeyboardButton("🤷 اغلاق", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="home":
        get_me = await client.get_me()
        USERNAME = get_me.username
        buttons = [
            [
                InlineKeyboardButton("🧐 اضفني الي مجموعتك", url='https://t.me/{USERNAME}?startgroup=true'),
            ],
            [
                InlineKeyboardButton("💌 جروب الدعم", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton("🏷️ قناة السورس", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            [
                InlineKeyboardButton("🤖 𝑆𝑂𝑅𝑆 𝐴𝐿 𝑀𝐸𝑀", url="https://t.me/U_K_M8"),
            ],
            [
                InlineKeyboardButton("🤔 المساعده & الاوامر", callback_data="help"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HOME_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="users":
        buttons = [
            [
                InlineKeyboardButton("🔙 رجوع", callback_data="help"),
                InlineKeyboardButton("🤷 اغلاق", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                USER_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="admins":
        buttons = [
            [
                InlineKeyboardButton("🔙 رجوع", callback_data="help"),
                InlineKeyboardButton("🤷 اغلاق", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(ADMIN, reply_markup=reply_markup)
        except MessageNotModified:
            pass

    elif query.data=="raid":
        buttons = [
            [
                InlineKeyboardButton("🔙 رجوع", callback_data="help"),
                InlineKeyboardButton("🤷 اغلاق", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                RAID_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="spam":
        buttons = [
            [
                InlineKeyboardButton("🔙 رجوع", callback_data="help"),
                InlineKeyboardButton("🤷 اغلاق", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                SPAM_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    get_me = await client.get_me()
    USERNAME = get_me.username
    buttons = [
            [
                InlineKeyboardButton("🧐 Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀᴛ", url=f'https://t.me/{USERNAME}?startgroup=true'),
            ],
            [
                InlineKeyboardButton("💌 جروب الدعم", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton("🏷️ قناة السورس", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            [
                InlineKeyboardButton("🤖 𝑆𝑂𝑅𝑆 𝐴𝐿 𝑀𝐸𝑀", url="https://t.me/U_K_M8"),
            ],
            [
                InlineKeyboardButton("🤔 المساعده & الاوامر", callback_data="help"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=f"{ALIVE_PIC}", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client: Client, message: Message):
    get_me = await client.get_me()
    self.username = get_me.username
    buttons = [
            [
                InlineKeyboardButton("👮 الاوامر", url="https://telegra.ph/%D8%B3%D9%88%D8%B1%D8%B3-%D8%A7%D9%8A%D8%AB%D9%88%D9%86-%D8%A7%D9%84%D8%B5%D9%88%D8%AA%D9%8A-EITHON1-06-21"),
                InlineKeyboardButton("🗨️ الاعضاء", callback_data="users"),
            ],
            [
                InlineKeyboardButton("🤬 الراديو", callback_data="raid"),
                InlineKeyboardButton("🗨️ اسبام", callback_data="spam"),
            ],
            [
                InlineKeyboardButton("🤖 مصنع حمايه", url="t.me/O_K_8Bot"),
            ],
            [
                InlineKeyboardButton("🔙 رجوع", callback_data="home"),
                InlineKeyboardButton("🤷 اغلاق", callback_data="close"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=f"{ALIVE_PIC}", caption=f"{HELP_TEXT}", reply_markup=reply_markup)
