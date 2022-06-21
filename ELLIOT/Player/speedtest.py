import os
import wget
import speedtest

from PIL import Image
from pyrogram.types import Message
from pyrogram import filters, Client

from ELLIOT.main import bot as app
from config import SUDO_USERS as SUDOERS

@app.on_message(filters.command("فحص") & ~filters.edited)
async def run_speedtest(_, message):
    userid = message.from_user.id
    m = await message.reply_text("__Processing__...")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = await m.edit("⚡️ __جاري فحص سرعه التحميل__")
        test.download()
        m = await m.edit("⚡️ __جاري فحص سرعه الرفع__")
        test.upload()
        test.results.share()
    except speedtest.ShareResultsConnectFailure:
        pass
    except Exception as e:
        await m.edit_text(e)
        return
    result = test.results.dict()
    m = await m.edit_text("🔄 التحضير للمعلومات")
    if result["share"]:
        path = wget.download(result["share"])
        try:
            img = Image.open(path)
            c = img.crop((17, 11, 727, 389))
            c.save(path)
        except BaseException:
            pass
    output = f"""💡 **نتائج الفحص**
    
<u>**Client:**</u>

**ISP:** {result['client']['isp']}
**الدوله:** {result['client']['country']}
  
<u>**السيرفر:**</u>

**الاسم:** {result['server']['name']}
**الدوله:** {result['server']['country']}, {result['server']['cc']}
**كفيل:** {result['server']['sponsor']}
**وقت الإستجابة:** {result['server']['latency']}  

⚡ **البنك:** {result['ping']}"""
    if result["share"]:
        msg = await app.send_photo(
            chat_id=message.chat.id, photo=path, caption=output
        )
        os.remove(path)
    else:
        msg = await app.send_message(
            chat_id=message.chat.id, text=output
        )
    await m.delete()
