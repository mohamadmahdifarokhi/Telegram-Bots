from pyrogram import Client
from pyrogram import filters
from pyrogram.types import *
import pyromod.listen
import mysql.connector
import jdatetime
from datetime import timedelta, datetime

bot = Client(session_name="online_project",
             api_id=14632339,
             api_hash="",
             bot_token="")

bot_2 = Client(session_name="online_project_2",
               api_id=14632339,
               api_hash="",
               bot_token="")

bot_22 = Client(session_name="online_project_22",
                api_id=14632339,
                api_hash="",
                bot_token="")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="online_project")
mycursor = mydb.cursor()

'''mydb= mysql.connector.connect(
host= "localhost",
user= "onprojir_mt",
password= "3910844000lte000",
database= "onprojir_onproj")
mycursor= mydb.cursor()'''


@bot.on_callback_query()
async def answer(client, call):
    if call.data[0:2] == "s%":
        user_id = call.from_user.id
        user_name = call.from_user.username
        first_name = call.from_user.first_name
        message_id = call.message.message_id
        ad_number = call.data.split("%")[1]
        skill = call.data.split("%")[2]
        i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
        i = mycursor.fetchall()
        a = ["فنی و مهندسی ", "پزشکی", "علوم انسانی ", "زبان خارجه", "ادبیات", "علوم پایه", "علوم اجتماعی",
             "مقاله و پژوهش"]
        b = ["هفتم", "هشتم", "نهم", "متوسطه اول", "ریاضی فیزیک", "علوم تجربی", "علوم انسانی", "فنی و حرفه ای",
             "کار و دانش", "معارف اسلامی", "متوسطه دوم"]
        c = ["وبسایت", "موبایل", "برنامه نویسی", "سئو و بازاریابی", "نرم افزار", "سخت افزار", "علم داده",
             "امنیت و شبکه", "هوش مصنوعی", "ویندوز و آفیس", "اپلیکیشن", "سرور", "آی تی و برنامه نویسی",
             "تبلیغات", "لوگو/پوستر", "فوتوشاپ", "سه بعدی", "رابط کاربری", "انیمیشن", "طراحی قالب", "خدمات ویدئویی",
             "طراحی و نقاشی", "طراحی و گرافیک",
             "کامپیوتر", "مکانیک", "برق", "عمران ", "شیمی و پلیمر", "بیومکانیک", "اتوماسیون", "طراحی صنعتی", "صنایع",
             "مکاترونیک", "الکترونیک", "معماری", "نفت و دریا", "نقشه کشی", "مدیریت", "فنی و مهندسی",
             "تولید محتوا", "ترجمه", "نگارش/گزارش", "مقاله", "وبلاگ", "تایپ", "نویسندگی", "پژوهش", "کپی رایتینگ",
             "زیرنویس", "دوبله", "ادمین", "محتوا و ترجمه"]

        if "%" not in i[0][4]:
            mycursor.execute("UPDATE ads SET skill= \"%s\" WHERE ad_number= \"%s\"" % ("%" + skill + "%", ad_number))

            if skill in a:
                count = -1
                for m in a:
                    count += 1
                    if m == skill:
                        a[count] += " ✅"
                        await bot.edit_message_reply_markup(user_id, message_id, reply_markup=InlineKeyboardMarkup([
                            [InlineKeyboardButton(a[2], callback_data="s" + "%" + ad_number + "%" + a[2]),
                             InlineKeyboardButton(a[1], callback_data="s" + "%" + ad_number + "%" + a[1]),
                             InlineKeyboardButton(a[0], callback_data="s" + "%" + ad_number + "%" + a[0])],
                            [InlineKeyboardButton(a[5], callback_data="s" + "%" + ad_number + "%" + a[5]),
                             InlineKeyboardButton(a[4], callback_data="s" + "%" + ad_number + "%" + a[4]),
                             InlineKeyboardButton(a[3], callback_data="s" + "%" + ad_number + "%" + a[3])],
                            [InlineKeyboardButton(a[7], callback_data="s" + "%" + ad_number + "%" + a[7]),
                             InlineKeyboardButton(a[6], callback_data="s" + "%" + ad_number + "%" + a[6])]
                        ]))

            elif skill in b:
                count = -1
                for m in b:
                    count += 1
                    if m == skill:
                        b[count] += " ✅"
                        await bot.edit_message_reply_markup(user_id, message_id, reply_markup=InlineKeyboardMarkup([
                            [InlineKeyboardButton(b[3], callback_data=" ")],
                            [InlineKeyboardButton(b[2], callback_data="s" + "%" + ad_number + "%" + b[2]),
                             InlineKeyboardButton(b[1], callback_data="s" + "%" + ad_number + "%" + b[1]),
                             InlineKeyboardButton(b[0], callback_data="s" + "%" + ad_number + "%" + b[0])],
                            [InlineKeyboardButton(b[10], callback_data=" ")],
                            [InlineKeyboardButton(b[6], callback_data="s" + "%" + ad_number + "%" + b[6]),
                             InlineKeyboardButton(b[5], callback_data="s" + "%" + ad_number + "%" + b[5]),
                             InlineKeyboardButton(b[4], callback_data="s" + "%" + ad_number + "%" + b[4])],
                            [InlineKeyboardButton(b[9], callback_data="s" + "%" + ad_number + "%" + b[9]),
                             InlineKeyboardButton(b[8], callback_data="s" + "%" + ad_number + "%" + b[8]),
                             InlineKeyboardButton(b[7], callback_data="s" + "%" + ad_number + "%" + b[7])]
                        ]))

            elif skill in c:
                count = -1
                for m in c:
                    count += 1
                    if m == skill:
                        c[count] += " ✅"
                        await bot.edit_message_reply_markup(user_id, message_id, reply_markup=InlineKeyboardMarkup([
                            [InlineKeyboardButton(c[12], callback_data=" ")],
                            [InlineKeyboardButton(c[2], callback_data="s" + "%" + ad_number + "%" + c[2]),
                             InlineKeyboardButton(c[1], callback_data="s" + "%" + ad_number + "%" + c[1]),
                             InlineKeyboardButton(c[0], callback_data="s" + "%" + ad_number + "%" + c[0])],
                            [InlineKeyboardButton(c[5], callback_data="s" + "%" + ad_number + "%" + c[5]),
                             InlineKeyboardButton(c[4], callback_data="s" + "%" + ad_number + "%" + c[4]),
                             InlineKeyboardButton(c[3], callback_data="s" + "%" + ad_number + "%" + c[3])],
                            [InlineKeyboardButton(c[8], callback_data="s" + "%" + ad_number + "%" + c[8]),
                             InlineKeyboardButton(c[7], callback_data="s" + "%" + ad_number + "%" + c[7]),
                             InlineKeyboardButton(c[6], callback_data="s" + "%" + ad_number + "%" + c[6])],
                            [InlineKeyboardButton(c[11], callback_data="s" + "%" + ad_number + "%" + c[11]),
                             InlineKeyboardButton(c[10], callback_data="s" + "%" + ad_number + "%" + c[10]),
                             InlineKeyboardButton(c[9], callback_data="s" + "%" + ad_number + "%" + c[9])],
                            [InlineKeyboardButton(c[22], callback_data=" ")],
                            [InlineKeyboardButton(c[15], callback_data="s" + "%" + ad_number + "%" + c[15]),
                             InlineKeyboardButton(c[14], callback_data="s" + "%" + ad_number + "%" + c[14]),
                             InlineKeyboardButton(c[13], callback_data="s" + "%" + ad_number + "%" + c[13])],
                            [InlineKeyboardButton(c[18], callback_data="s" + "%" + ad_number + "%" + c[18]),
                             InlineKeyboardButton(c[17], callback_data="s" + "%" + ad_number + "%" + c[17]),
                             InlineKeyboardButton(c[16], callback_data="s" + "%" + ad_number + "%" + c[16])],
                            [InlineKeyboardButton(c[21], callback_data="s" + "%" + ad_number + "%" + c[21]),
                             InlineKeyboardButton(c[20], callback_data="s" + "%" + ad_number + "%" + c[20]),
                             InlineKeyboardButton(c[19], callback_data="s" + "%" + ad_number + "%" + c[19])],
                            [InlineKeyboardButton(c[38], callback_data=" ")],
                            [InlineKeyboardButton(c[25], callback_data="s" + "%" + ad_number + "%" + c[25]),
                             InlineKeyboardButton(c[24], callback_data="s" + "%" + ad_number + "%" + c[24]),
                             InlineKeyboardButton(c[23], callback_data="s" + "%" + ad_number + "%" + c[23])],
                            [InlineKeyboardButton(c[28], callback_data="s" + "%" + ad_number + "%" + c[28]),
                             InlineKeyboardButton(c[27], callback_data="s" + "%" + ad_number + "%" + c[27]),
                             InlineKeyboardButton(c[26], callback_data="s" + "%" + ad_number + "%" + c[26])],
                            [InlineKeyboardButton(c[31], callback_data="s" + "%" + ad_number + "%" + c[31]),
                             InlineKeyboardButton(c[30], callback_data="s" + "%" + ad_number + "%" + c[30]),
                             InlineKeyboardButton(c[29], callback_data="s" + "%" + ad_number + "%" + c[29])],
                            [InlineKeyboardButton(c[34], callback_data="s" + "%" + ad_number + "%" + c[34]),
                             InlineKeyboardButton(c[33], callback_data="s" + "%" + ad_number + "%" + c[33]),
                             InlineKeyboardButton(c[32], callback_data="s" + "%" + ad_number + "%" + c[32])],
                            [InlineKeyboardButton(c[37], callback_data="s" + "%" + ad_number + "%" + c[37]),
                             InlineKeyboardButton(c[36], callback_data="s" + "%" + ad_number + "%" + c[36]),
                             InlineKeyboardButton(c[35], callback_data="s" + "%" + ad_number + "%" + c[35])],
                            [InlineKeyboardButton(c[51], callback_data=" ")],
                            [InlineKeyboardButton(c[41], callback_data="s" + "%" + ad_number + "%" + c[41]),
                             InlineKeyboardButton(c[40], callback_data="s" + "%" + ad_number + "%" + c[40]),
                             InlineKeyboardButton(c[39], callback_data="s" + "%" + ad_number + "%" + c[39])],
                            [InlineKeyboardButton(c[44], callback_data="s" + "%" + ad_number + "%" + c[44]),
                             InlineKeyboardButton(c[43], callback_data="s" + "%" + ad_number + "%" + c[43]),
                             InlineKeyboardButton(c[42], callback_data="s" + "%" + ad_number + "%" + c[42])],
                            [InlineKeyboardButton(c[47], callback_data="s" + "%" + ad_number + "%" + c[47]),
                             InlineKeyboardButton(c[46], callback_data="s" + "%" + ad_number + "%" + c[46]),
                             InlineKeyboardButton(c[45], callback_data="s" + "%" + ad_number + "%" + c[45])],
                            [InlineKeyboardButton(c[50], callback_data="s" + "%" + ad_number + "%" + c[50]),
                             InlineKeyboardButton(c[49], callback_data="s" + "%" + ad_number + "%" + c[49]),
                             InlineKeyboardButton(c[48], callback_data="s" + "%" + ad_number + "%" + c[48])]
                        ]))

            await new_ad_2(ad_number, user_id, user_name, first_name)

    elif call.data[:12] == "freelancers%":
        user_id = call.from_user.id
        user_name = call.from_user.username
        first_name = call.from_user.first_name
        message_id = call.message.message_id
        data = call.data.split("%")[1]
        a = ["فنی و مهندسی ", "پزشکی", "علوم انسانی ", "زبان خارجه", "ادبیات", "علوم پایه", "علوم اجتماعی",
             "مقاله و پژوهش"]
        b = ["هفتم", "هشتم", "نهم", "متوسطه اول", "ریاضی فیزیک", "علوم تجربی", "علوم انسانی", "فنی و حرفه ای",
             "کار و دانش", "معارف اسلامی", "متوسطه دوم"]
        c = ["وبسایت", "موبایل", "برنامه نویسی", "سئو و بازاریابی", "نرم افزار", "سخت افزار", "علم داده",
             "امنیت و شبکه", "هوش مصنوعی", "ویندوز و آفیس", "اپلیکیشن", "سرور", "آی تی و برنامه نویسی",
             "تبلیغات", "لوگو/پوستر", "فوتوشاپ", "سه بعدی", "رابط کاربری", "انیمیشن", "طراحی قالب", "خدمات ویدئویی",
             "طراحی و نقاشی", "طراحی و گرافیک",
             "کامپیوتر", "مکانیک", "برق", "عمران ", "شیمی و پلیمر", "بیومکانیک", "اتوماسیون", "طراحی صنعتی", "صنایع",
             "مکاترونیک", "الکترونیک", "معماری", "نفت و دریا", "نقشه کشی", "مدیریت", "فنی و مهندسی",
             "تولید محتوا", "ترجمه", "نگارش/گزارش", "مقاله", "وبلاگ", "تایپ", "نویسندگی", "پژوهش", "کپی رایتینگ",
             "زیرنویس", "دوبله", "ادمین", "محتوا و ترجمه"]
        i = mycursor.execute("SELECT * FROM freelancers WHERE user_id= \"%s\"" % (user_id))
        i = mycursor.fetchall()

        if "%" not in i[0][4]:
            mycursor.execute("UPDATE freelancers SET skill= \"%s\" WHERE user_id= \"%s\"" % ("%" + data + "%", user_id))

            if data in a:
                count = -1
                for m in a:
                    count += 1
                    if data == m:
                        a[count] += " ✅"
                        await bot.edit_message_reply_markup(user_id, message_id, reply_markup=InlineKeyboardMarkup([
                            [InlineKeyboardButton(a[2], callback_data="freelancers" + "%" + a[2]),
                             InlineKeyboardButton(a[1], callback_data="freelancers" + "%" + a[1]),
                             InlineKeyboardButton(a[0], callback_data="freelancers" + "%" + a[0])],
                            [InlineKeyboardButton(a[5], callback_data="freelancers" + "%" + a[5]),
                             InlineKeyboardButton(a[4], callback_data="freelancers" + "%" + a[4]),
                             InlineKeyboardButton(a[3], callback_data="freelancers" + "%" + a[3])],
                            [InlineKeyboardButton(a[7], callback_data="freelancers" + "%" + a[7]),
                             InlineKeyboardButton(a[6], callback_data="freelancers" + "%" + a[6])]
                        ]))

            elif data in b:
                count = -1
                for m in b:
                    count += 1
                    if data == m:
                        b[count] += " ✅"
                        await bot.edit_message_reply_markup(user_id, message_id, reply_markup=InlineKeyboardMarkup([
                            [InlineKeyboardButton(b[3], callback_data=" ")],
                            [InlineKeyboardButton(b[2], callback_data="freelancers" + "%" + b[2]),
                             InlineKeyboardButton(b[1], callback_data="freelancers" + "%" + b[1]),
                             InlineKeyboardButton(b[0], callback_data="freelancers" + "%" + b[0])],
                            [InlineKeyboardButton(b[10], callback_data=" ")],
                            [InlineKeyboardButton(b[6], callback_data="freelancers" + "%" + b[6]),
                             InlineKeyboardButton(b[5], callback_data="freelancers" + "%" + b[5]),
                             InlineKeyboardButton(b[4], callback_data="freelancers" + "%" + b[4])],
                            [InlineKeyboardButton(b[9], callback_data="freelancers" + "%" + b[9]),
                             InlineKeyboardButton(b[8], callback_data="freelancers" + "%" + b[8]),
                             InlineKeyboardButton(b[7], callback_data="freelancers" + "%" + b[7])]
                        ]))

            elif data in c:
                count = -1
                for m in c:
                    count += 1
                    if data == m:
                        c[count] += " ✅"
                        await bot.edit_message_reply_markup(user_id, message_id, reply_markup=InlineKeyboardMarkup([
                            [InlineKeyboardButton(c[12], callback_data=" ")],
                            [InlineKeyboardButton(c[2], callback_data="freelancers" + "%" + c[2]),
                             InlineKeyboardButton(c[1], callback_data="freelancers" + "%" + c[1]),
                             InlineKeyboardButton(c[0], callback_data="freelancers" + "%" + c[0])],
                            [InlineKeyboardButton(c[5], callback_data="freelancers" + "%" + c[5]),
                             InlineKeyboardButton(c[4], callback_data="freelancers" + "%" + c[4]),
                             InlineKeyboardButton(c[3], callback_data="freelancers" + "%" + c[3])],
                            [InlineKeyboardButton(c[8], callback_data="freelancers" + "%" + c[8]),
                             InlineKeyboardButton(c[7], callback_data="freelancers" + "%" + c[7]),
                             InlineKeyboardButton(c[6], callback_data="freelancers" + "%" + c[6])],
                            [InlineKeyboardButton(c[11], callback_data="freelancers" + "%" + c[11]),
                             InlineKeyboardButton(c[10], callback_data="freelancers" + "%" + c[10]),
                             InlineKeyboardButton(c[9], callback_data="freelancers" + "%" + c[9])],
                            [InlineKeyboardButton(c[22], callback_data=" ")],
                            [InlineKeyboardButton(c[15], callback_data="freelancers" + "%" + c[15]),
                             InlineKeyboardButton(c[14], callback_data="freelancers" + "%" + c[14]),
                             InlineKeyboardButton(c[13], callback_data="freelancers" + "%" + c[13])],
                            [InlineKeyboardButton(c[18], callback_data="freelancers" + "%" + c[18]),
                             InlineKeyboardButton(c[17], callback_data="freelancers" + "%" + c[17]),
                             InlineKeyboardButton(c[16], callback_data="freelancers" + "%" + c[16])],
                            [InlineKeyboardButton(c[21], callback_data="freelancers" + "%" + c[21]),
                             InlineKeyboardButton(c[20], callback_data="freelancers" + "%" + c[20]),
                             InlineKeyboardButton(c[19], callback_data="freelancers" + "%" + c[19])],
                            [InlineKeyboardButton(c[38], callback_data=" ")],
                            [InlineKeyboardButton(c[25], callback_data="freelancers" + "%" + c[25]),
                             InlineKeyboardButton(c[24], callback_data="freelancers" + "%" + c[24]),
                             InlineKeyboardButton(c[23], callback_data="freelancers" + "%" + c[23])],
                            [InlineKeyboardButton(c[28], callback_data="freelancers" + "%" + c[28]),
                             InlineKeyboardButton(c[27], callback_data="freelancers" + "%" + c[27]),
                             InlineKeyboardButton(c[26], callback_data="freelancers" + "%" + c[26])],
                            [InlineKeyboardButton(c[31], callback_data="freelancers" + "%" + c[31]),
                             InlineKeyboardButton(c[30], callback_data="freelancers" + "%" + c[30]),
                             InlineKeyboardButton(c[29], callback_data="freelancers" + "%" + c[29])],
                            [InlineKeyboardButton(c[34], callback_data="freelancers" + "%" + c[34]),
                             InlineKeyboardButton(c[33], callback_data="freelancers" + "%" + c[33]),
                             InlineKeyboardButton(c[32], callback_data="freelancers" + "%" + c[32])],
                            [InlineKeyboardButton(c[37], callback_data="freelancers" + "%" + c[37]),
                             InlineKeyboardButton(c[36], callback_data="freelancers" + "%" + c[36]),
                             InlineKeyboardButton(c[35], callback_data="freelancers" + "%" + c[35])],
                            [InlineKeyboardButton(c[51], callback_data=" ")],
                            [InlineKeyboardButton(c[41], callback_data="freelancers" + "%" + c[41]),
                             InlineKeyboardButton(c[40], callback_data="freelancers" + "%" + c[40]),
                             InlineKeyboardButton(c[39], callback_data="freelancers" + "%" + c[39])],
                            [InlineKeyboardButton(c[44], callback_data="freelancers" + "%" + c[44]),
                             InlineKeyboardButton(c[43], callback_data="freelancers" + "%" + c[43]),
                             InlineKeyboardButton(c[42], callback_data="freelancers" + "%" + c[42])],
                            [InlineKeyboardButton(c[47], callback_data="freelancers" + "%" + c[47]),
                             InlineKeyboardButton(c[46], callback_data="freelancers" + "%" + c[46]),
                             InlineKeyboardButton(c[45], callback_data="freelancers" + "%" + c[45])],
                            [InlineKeyboardButton(c[50], callback_data="freelancers" + "%" + c[50]),
                             InlineKeyboardButton(c[49], callback_data="freelancers" + "%" + c[49]),
                             InlineKeyboardButton(c[48], callback_data="freelancers" + "%" + c[48])]
                        ]))

            await freelancers_3(user_id, user_name, first_name, data)

    elif call.data[:10] == "Correction":

        try:
            user_id = call.from_user.id
            ad_number = call.data.split("%")[1]
            i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
            i = mycursor.fetchall()
            message_id = call.message.message_id
            message_id_2 = i[0][5].split("%")[2]
            message_id_3 = i[0][5].split("%")[3]
            mark = InlineKeyboardMarkup([
                [InlineKeyboardButton("واگذاری", callback_data="assignment" + "%" + ad_number)],
                [InlineKeyboardButton("پشتیبانی", url="https://t.me/onprojsup")]
            ])
            mark_2 = InlineKeyboardMarkup([
                [InlineKeyboardButton("پشتیبانی", url="https://t.me/onprojsup")]
            ])
            mark_3 = InlineKeyboardMarkup([
                [InlineKeyboardButton("انجام این پروژه",
                                      url=f"https://telegram.me/onprojbot?start={'2' + i[0][0].replace('&', '111111111101111111111')}")]
            ])

            await bot.send_message(user_id, """
⚖️ قوانین و مقررات درج آگهی ⚖️

🖋 درج آگهی امتحان و پروپزال و پایان نامه اکیداً ممنوع است

🖋 آگهی شما باید منطبق با عرف و حفظ شئونات باشد و از استفاده کلمات توهین آمیز جدا خودداری کنید

🖋 استفاده از هرگونه لینک و موارد تبلیغاتی در آگهی ممنوع میباشد ( برای ثبت تبلیغات به @onprojad مراجعه فرمایید )     
""", reply_markup=ReplyKeyboardRemove(all))

            while True:
                try:
                    a = await bot.ask(user_id, """
🖍 حالا متن آگهیت رو اینجا برامون بنویس : 

📋 نمونه : به یک نفر مسلط به فیزیک عمومی ۱ جهت رفع اشکال نیازمندم

/Cancel - لغو
""", reply_markup=ReplyKeyboardRemove(all))
                    if a.text == "/Cancel":
                        mycursor.execute("DELETE FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                        await bot.send_message(user_id, "لغو شد", reply_markup=ReplyKeyboardRemove(all))
                        break
                    elif len(a.text) < 20:
                        await bot.send_message(user_id, "متنت خیلی کمه", reply_markup=ReplyKeyboardRemove(all))
                    else:
                        x = ["None", "FiNiShEd", "Paid Intermediation", "Posted Ad", "Paid Ad", "💰", "📌", "👋🏻", "❌",
                             "⭕️", "✅", "🇮🇷", "⚠️", "❕", "⛔️", "❤️", "⬅️", "‼️", "@", "^", "*", "$", "!", "&", "%", "#",
                             "/"]
                        for m in x:
                            if m in a.text:
                                await bot.send_message(user_id,
                                                       f"استفاده از کلمه یا حرف <strong>{m}</strong> مجاز نیست",
                                                       reply_markup=ReplyKeyboardRemove(all))
                                a.text = "NO"
                        if a.text != "NO":
                            mycursor.execute("UPDATE ads SET ad= \"%s\" WHERE ad_number= \"%s\"" % (
                            i[0][5].replace(i[0][5].split("%")[0], a.text), ad_number))
                            break
                except Exception as e:
                    await bot.send_message(user_id, "لطفا آگهی تون رو به صورت متن بدون استیکر بنویسید",
                                           reply_markup=ReplyKeyboardRemove(all))

            if a.text != "/Cancel":
                i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                i = mycursor.fetchall()
                await bot.delete_messages(chat_id="me", message_ids=message_id)
                await bot.send_message(user_id, "تایید شد", reply_markup=ReplyKeyboardRemove(all))

                if "we" in i[0][2]:
                    await bot_22.start()
                    if "FiNiShEd" not in i[0][5]:
                        await bot.edit_message_text(user_id, int(message_id_2), f"""
📌 {i[0][5].split("%")[0]}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}</strong>
""", reply_markup=mark)
                        if "we I" == i[0][2]:
                            b = await bot_22.edit_message_text("@onproj", int(message_id_3), f"""
<strong>فوری</strong>

📌 {i[0][5].split("%")[0]}

💰Budget : {i[0][6]}

bot : @onprojbot
Channel : @onproj
""", reply_markup=mark_3)
                            await bot_22.pin_chat_message(
                                chat_id="@onproj",
                                message_id=b.message_id
                            )
                        else:
                            await bot_22.edit_message_text("@onproj", int(message_id_3), f"""
📌 {i[0][5].split("%")[0]}

💰Budget : {i[0][6]}

bot : @onprojbot
Channel : @onproj
""", reply_markup=mark_3)

                    else:
                        await bot.edit_message_text(user_id, int(message_id_2), f"""
<strong>واگذاری شد</strong>

📌 {i[0][5].split("%")[0]}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}</strong>
""", reply_markup=mark_2)
                        if "we I" == i[0][2]:
                            await bot_22.edit_message_text("@onproj", int(message_id_3), f"""
<strong>فوری</strong>

📌 {i[0][5].split("%")[0]}

💰Budget : {i[0][6]}

bot : @onprojbot
Channel : @onproj
""")
                        else:
                            await bot_22.edit_message_text("@onproj", int(message_id_3), f"""
📌 {i[0][5].split("%")[0]}

💰Budget : {i[0][6]}

bot : @onprojbot
Channel : @onproj
""")
                    await bot_22.stop()

                else:
                    await bot_2.start()
                    if "FiNiShEd" not in i[0][5]:
                        await bot.edit_message_text(user_id, int(message_id_2), f"""
📌 {i[0][5].split("%")[0]}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}</strong>
""", reply_markup=mark)
                        await bot_2.edit_message_text("@onproj", int(message_id_3), f"""
📌 {i[0][5].split("%")[0]}

💰Budget : {i[0][6]}

bot : @onprojbot
Channel : @onproj
""", reply_markup=mark_3)
                    else:
                        await bot.edit_message_text(user_id, int(message_id_2), f"""
<strong>واگذاری شد</strong>

📌 {i[0][5].split("%")[0]}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}</strong>
""", reply_markup=mark_2)
                        await bot_2.edit_message_text("@onproj", int(message_id_3), f"""
📌 {i[0][5].split("%")[0]}

💰Budget : {i[0][6]}

bot : @onprojbot
Channel : @onproj
""")
                    await bot_2.stop()

        except Exception as e:
            pass

    elif call.data[:10] == "assignment":

        try:
            ad_number = call.data.split("%")[1]
            i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
            i = mycursor.fetchall()
            mark = InlineKeyboardMarkup([
                [InlineKeyboardButton("پشتیبانی", url="https://t.me/onprojsup")]
            ])

            if "FiNiShEd" not in i[0][5]:
                await bot.edit_message_text(i[0][1], int(i[0][5].split("%")[2]), f"""
<strong>واگذاری شد</strong>

📌 {i[0][5].split("%")[0]}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}</strong>
""", reply_markup=mark)
                mycursor.execute(
                    "UPDATE ads SET ad= \"%s\" WHERE ad_number= \"%s\"" % (i[0][5] + "%" + "!FiNiShEd", i[0][0]))

        except Exception as e:
            pass

    elif call.data == "freelancers_edit":
        user_id = call.from_user.id
        user_name = call.from_user.username
        first_name = call.from_user.first_name
        message_id = call.message.message_id
        i = mycursor.execute("SELECT * FROM freelancers WHERE user_id= \"%s\"" % (user_id))
        i = mycursor.fetchall()

        mycursor.execute(
            "UPDATE freelancers SET type= \"%s\",skill= \"%s\",explanation= \"%s\",linkedin= \"%s\",score= \"%s\" WHERE user_id= \"%s\"" % (
            "", "", "", "", "%" + i[0][7] + "%", user_id))
        await bot.edit_message_text(user_id, message_id, "نوع فریلنسریتو")
        await freelancers_2(user_id, user_name, first_name, "انتخاب کن")

    elif call.data.split("%")[0] == "dtp":
        await start_2(client, call, call.data.split("%")[1])

    elif call.data[:9] == "selection":

        try:
            user_id = call.from_user.id
            user_id_2 = call.data.split("%")[2]
            user_name = call.from_user.username
            message_id = call.message.message_id
            ad_number = call.data.split("%")[1]
            i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
            i = mycursor.fetchall()
            j = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (user_id))
            j = mycursor.fetchall()
            k = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (user_id_2))
            k = mycursor.fetchall()
            mark = InlineKeyboardMarkup([
                [InlineKeyboardButton("تایید", callback_data="emac" + "%" + ad_number + "%" + user_id_2)]
            ])
            mark_2 = InlineKeyboardMarkup([
                [InlineKeyboardButton("پی وی", url=f"https://t.me/{k[0][0]}")]
            ])

            for m in i[0][8].split("%%%")[:-1]:
                if user_id_2 + "!" == m.split("%")[0]:
                    offer_text = m.split("%")[1]
                    offer_cost = m.split("%")[2]

            while True:
                try:
                    a = await bot.ask(user_id, """
🖍 لطفا متن و شروط توافقتون رو بنویس :

📋 پ.ن : این بخش مربوط به مواقعیه که با بروز اختلاف در تأییدیه نهایی ، طرفین نیاز به داوری توسط ادمین دارن

/Cancel - لغو
""", reply_markup=ReplyKeyboardRemove(all))
                    if a.text == "/Cancel":
                        await bot.send_message(user_id, "لغو شد", reply_markup=ReplyKeyboardRemove(all))
                        break
                    elif len(a.text) < 20:
                        await bot.send_message(user_id, "متنت خیلی کمه", reply_markup=ReplyKeyboardRemove(all))
                    else:
                        x = ["None", "FiNiShEd", "Paid Intermediation", "Posted Ad", "Paid Ad", "💰", "📌", "👋🏻", "❌",
                             "⭕️", "✅", "🇮🇷", "⚠️", "❕", "⛔️", "❤️", "⬅️", "‼️", "@", "^", "*", "$", "!", "&", "%", "#",
                             "/"]
                        for m in x:
                            if m in a.text:
                                await bot.send_message(user_id,
                                                       f"استفاده از کلمه یا حرف <strong>{m}</strong> مجاز نیست",
                                                       reply_markup=ReplyKeyboardRemove(all))
                                a.text = "NO"
                        if a.text != "NO":
                            break
                except Exception as e:
                    await bot.send_message(user_id, "لطفا توافق تون رو به صورت متن بدون استیکر بنویسید",
                                           reply_markup=ReplyKeyboardRemove(all))

            if a.text != "/Cancel":
                while True:
                    b = await bot.ask(user_id, """
🖍 حالا قیمت توافق شده رو به تومان بنویس : 

📋 نمونه : 50000

/Cancel - لغو
""", reply_markup=ReplyKeyboardRemove(all))
                    try:
                        if b.text == "/Cancel":
                            await bot.send_message(user_id, "لغو شد", reply_markup=ReplyKeyboardRemove(all))
                            break
                        else:
                            if 100000000 >= int(b.text) >= 10000:
                                x = {"۰": "0", "۱": "1", "۲": "2", "۳": "3", "۴": "4", "۵": "5", "۶": "6", "۷": "7",
                                     "۸": "8", "۹": "9"}
                                z = ""
                                for m in str(b.text):
                                    if m in "۰۱۲۳۴۵۶۷۸۹":
                                        z += x[m]
                                    else:
                                        z += m
                                if 4 <= len(z) <= 6:
                                    m = z[:-3] + ',' + z[-3:]
                                elif 7 <= len(z) <= 9:
                                    m = z[:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                                elif 10 <= len(z) <= 12:
                                    m = z[:-9] + ',' + z[-9:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                                budget = m + " T"
                                total_cost = int(b.text) + 3000
                                z = ""
                                for m in str(total_cost):
                                    if m in "۰۱۲۳۴۵۶۷۸۹":
                                        z += x[m]
                                    else:
                                        z += m
                                if 4 <= len(z) <= 6:
                                    m = z[:-3] + ',' + z[-3:]
                                elif 7 <= len(z) <= 9:
                                    m = z[:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                                elif 10 <= len(z) <= 12:
                                    m = z[:-9] + ',' + z[-9:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                                total_cost = m + " T"
                                break
                            else:
                                await bot.send_message(user_id, "خارج از محدوده")
                    except Exception as e:
                        await bot.send_message(user_id, "فرمت درست نیست")

                if b.text != "/Cancel":
                    c = await bot.send_message(user_id, f"""
📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {a.text}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {budget}
Bot Cost : 3,000 T
Total Cost : {total_cost}</strong>
""", reply_markup=mark)

                    j = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                    j = mycursor.fetchall()
                    if j[0][9] == "":
                        m = "1"
                    else:
                        m = str(len(j[0][9].split("%%%")) - 1) + "%%%" + "%%%".join(j[0][9].split("%%%")[1:-1])
                    mycursor.execute("UPDATE ads SET intermediation= \"%s\" WHERE ad_number= \"%s\"" % (
                    m + "%%%" + user_id_2 + "%" + a.text + "%" + budget + "%" + str(c.message_id) + "%%%", ad_number))
                    l = mycursor.execute("SELECT * FROM freelancers WHERE user_id= \"%s\"" % (user_id))
                    l = mycursor.fetchall()

                    if "%" in l[0][7]:
                        await bot.edit_message_text(user_id, message_id, f"""
📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}</strong>
""", reply_markup=mark_2)

                    else:
                        await bot.edit_message_text(user_id, message_id, f"""
📌 {i[0][5].split("%")[0]}

📝 {offer_text}

📋 {l[0][5].split("%")[0]}

Linkedin : {l[0][6]}
Online Project Score : {l[0][7].replace("%", "")}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}</strong>
""", reply_markup=mark_2)

                    for m in i[0][8].split("%%%")[:-1]:
                        if str(user_id_2) + "!" == m.split("%")[0]:
                            mycursor.execute("UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (
                            i[0][8].replace(m, m + "%" + "FiNiShEd"), ad_number))

        except Exception as e:
            pass

    elif call.data[:4] == "emac":

        try:
            user_id = call.from_user.id
            user_id_2 = call.data.split("%")[2]
            ad_number = call.data.split("%")[1]
            i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
            i = mycursor.fetchall()
            j = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (user_id))
            j = mycursor.fetchall()
            k = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (user_id_2))
            k = mycursor.fetchall()
            mark = InlineKeyboardMarkup([
                [InlineKeyboardButton("تایید", callback_data="frac" + "%" + ad_number + "%" + user_id_2)]
            ])

            for m in i[0][8].split("%%%")[:-1]:
                if user_id_2 + "!" == m.split("%")[0]:
                    offer_text = m.split("%")[1]
                    offer_cost = m.split("%")[2]

            n = i[0][9].split("%%%")[0] + "%%%"
            for m in i[0][9].split("%%%")[1:-1]:
                if user_id_2 == m.split("%")[0]:
                    o = m.split("%")[1]
                    p = m.split("%")[2]
                    message_id = m.split("%")[3]
                    total_cost = int(p.replace(" T", "").replace(",", "")) + 3000
                    y = {"۰": "0", "۱": "1", "۲": "2", "۳": "3", "۴": "4", "۵": "5", "۶": "6", "۷": "7", "۸": "8",
                         "۹": "9"}
                    z = ""
                    for x in str(total_cost):
                        if x in "۰۱۲۳۴۵۶۷۸۹":
                            z += y[x]
                        else:
                            z += x
                    if 4 <= len(z) <= 6:
                        x = z[:-3] + ',' + z[-3:]
                    elif 7 <= len(z) <= 9:
                        x = z[:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                    elif 10 <= len(z) <= 12:
                        x = z[:-9] + ',' + z[-9:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                    total_cost = x + " T"

                    await bot.edit_message_text(user_id, int(message_id), f"""
<strong>در انتظار تایید فریلنسر</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}
Bot Cost : 3,000 T
Total Cost : {total_cost}</strong>
""")
                    a = await bot.send_message(user_id_2, f"""
📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 <strong>@{j[0][1]}</strong>
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}
Bot Cost : 3,000 T</strong>
""", reply_markup=mark)

                    m = m + "%" + str(a.message_id) + "%" + "em" + "%%%"

                else:
                    m = m + "%%%"

                n += m

            mycursor.execute("UPDATE ads SET intermediation= \"%s\" WHERE ad_number= \"%s\"" % (n, ad_number))

        except Exception as e:
            pass

    elif call.data[:4] == "frac":

        try:
            ad_number = call.data.split("%")[1]
            user_id_2 = call.data.split("%")[2]
            i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
            i = mycursor.fetchall()
            user_id = i[0][1]
            j = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (user_id))
            j = mycursor.fetchall()
            k = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (user_id_2))
            k = mycursor.fetchall()

            for m in i[0][8].split("%%%")[:-1]:
                if user_id_2 + "!" == m.split("%")[0]:
                    offer_text = m.split("%")[1]
                    offer_cost = m.split("%")[2]

            n = i[0][9].split("%%%")[0] + "%%%"
            for m in i[0][9].split("%%%")[1:-1]:
                if user_id_2 == m.split("%")[0]:
                    o = m.split("%")[1]
                    p = m.split("%")[2]
                    message_id = m.split("%")[3]
                    message_id_2 = m.split("%")[4]
                    total_cost = int(p.replace(" T", "").replace(",", "")) + 3000
                    y = {"۰": "0", "۱": "1", "۲": "2", "۳": "3", "۴": "4", "۵": "5", "۶": "6", "۷": "7", "۸": "8",
                         "۹": "9"}
                    z = ""
                    for x in str(total_cost):
                        if x in "۰۱۲۳۴۵۶۷۸۹":
                            z += y[x]
                        else:
                            z += x
                    if 4 <= len(z) <= 6:
                        x = z[:-3] + ',' + z[-3:]
                    elif 7 <= len(z) <= 9:
                        x = z[:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                    elif 10 <= len(z) <= 12:
                        x = z[:-9] + ',' + z[-9:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                    total_cost = x + " T"
                    mark_2 = InlineKeyboardMarkup([
                        [InlineKeyboardButton("پرداخت",
                                              url=f"https://onproj.ir/zp/request/{int(p.replace(',', '').replace(' T', '')) + 3000}/{ad_number.replace('&', '111111111101111111111')}111111111101111111111{user_id_2}")]
                    ])

                    await bot.edit_message_text(user_id, int(message_id), f"""
<strong>پرداخت</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}
Bot Cost : 3,000 T</strong>
""", reply_markup=mark_2)
                    await bot.edit_message_text(user_id_2, int(message_id_2), f"""
<strong>در انتظار پرداخت کارفرما</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}
Bot Cost : 3,000 T</strong>
""")

                    m = m + "%" + "fr" + "!" + "%%%"

                else:
                    m = m + "%%%"

                n += m

            mycursor.execute("UPDATE ads SET intermediation= \"%s\" WHERE ad_number= \"%s\"" % (n, ad_number))

        except Exception as e:
            pass

    elif call.data[:4] == "frco":

        try:
            user_id_2 = call.data.split("%")[2]
            ad_number = call.data.split("%")[1]
            date = jdatetime.datetime.now().strftime("%Y-%m-%d")
            i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
            i = mycursor.fetchall()
            user_id = i[0][1]
            j = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (user_id))
            j = mycursor.fetchall()
            k = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (user_id_2))
            k = mycursor.fetchall()
            mark = InlineKeyboardMarkup([
                [InlineKeyboardButton("تایید پروژه", callback_data="emco" + "%" + ad_number + "%" + k[0][0])],
                [InlineKeyboardButton("ارجاع به داوری", callback_data="emca" + "%" + ad_number + "%" + k[0][0])]
            ])

            for m in i[0][8].split("%%%")[:-1]:
                if user_id_2 + "!" == m.split("%")[0]:
                    offer_text = m.split("%")[1]
                    offer_cost = m.split("%")[2]

            n = i[0][9].split("%%%")[0] + "%%%"
            for m in i[0][9].split("%%%")[1:-1]:
                if user_id_2 == m.split("%")[0]:
                    m = m + "%" + "frco" + "&" + date + "%%%"
                    o = m.split("%")[1]
                    p = m.split("%")[2]
                    message_id = m.split("%")[3]
                    message_id_2 = m.split("%")[4]

                    await bot.edit_message_text(user_id, int(message_id), f"""
<strong>تایید Vs ارجاع</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark)
                    await bot.edit_message_text(user_id_2, int(message_id_2), f"""
<strong>در انتظار تایید پروژه توسط کارفرما</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""")

                else:
                    m = m + "%%%"

                n += m

            mycursor.execute("UPDATE ads SET intermediation= \"%s\" WHERE ad_number= \"%s\"" % (n, ad_number))

        except Exception as e:
            pass

    elif call.data[:4] == "emco" or call.data[:4] == "emca":
        try:
            user_id_2 = call.data.split("%")[2]
            ad_number = call.data.split("%")[1]
            date = jdatetime.datetime.now().strftime("%Y-%m-%d")
            i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
            i = mycursor.fetchall()
            user_id = i[0][1]
            j = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (user_id))
            j = mycursor.fetchall()
            k = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (user_id_2))
            k = mycursor.fetchall()
            mark = InlineKeyboardMarkup([
                [InlineKeyboardButton("امتیاز به فریلنسر", callback_data="score" + "%" + ad_number + "%" + user_id_2)]
            ])
            mark_2 = InlineKeyboardMarkup([
                [InlineKeyboardButton("داوری", url="https://t.me/+A3SrS37IE702NzI0")]
            ])

            for m in i[0][8].split("%%%"):
                if user_id_2 + "!" == m.split("%")[0]:
                    offer_text = m.split("%")[1]
                    offer_cost = m.split("%")[2]

            n = i[0][9].split("%%%")[0] + "%%%"
            for m in i[0][9].split("%%%")[1:-1]:
                if user_id_2 == m.split("%")[0]:
                    o = m.split("%")[1]
                    p = m.split("%")[2]
                    message_id = m.split("%")[3]
                    message_id_2 = m.split("%")[4]
                    mark_3 = InlineKeyboardMarkup([
                        [InlineKeyboardButton("شماره کارت", callback_data="sheba" + "%" + ad_number + "%" + user_id_2)]
                    ])

                    if call.data[:4] == "emco":
                        await bot.edit_message_text(user_id, int(message_id), f"""
<strong>لطفا از 0 تا 5 به عملکرد فریلنسر امتیاز بدید</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark)
                        await bot.edit_message_text(user_id_2, int(message_id_2), f"""
<strong>لطفا شماره کارتتون رو برای واریز بنویسید</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark_3)

                    elif call.data[:4] == "emca":
                        await bot.send_message(-1001725099359, f"""
📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

@{j[0][1]} 🤝 @{k[0][1]}
Ad Number : <code>{ad_number + "&" + user_id_2}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=ReplyKeyboardRemove(all))
                        await bot.edit_message_text(user_id, int(message_id), f"""
<strong>داوری</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark_2)
                        await bot.edit_message_text(user_id_2, int(message_id_2), f"""
<strong>داوری</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark_2)

                    m = m.replace(m.split("%")[7], m.split("%")[7].split("&")[0]) + "%" + call.data[:4] + "%%%"

                else:
                    m = m + "%%%"

                n += m

            mycursor.execute("UPDATE ads SET intermediation= \"%s\" WHERE ad_number= \"%s\"" % (n, ad_number))

        except Exception as e:
            pass

    elif call.data[:6] == "sheba%":

        try:
            message_id = call.message.message_id
            user_id_2 = call.from_user.id
            ad_number = call.data.split("%")[1]
            i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
            i = mycursor.fetchall()
            j = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (i[0][1]))
            j = mycursor.fetchall()
            k = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (user_id_2))
            k = mycursor.fetchall()

            for m in i[0][8].split("%%%")[:-1]:
                if str(user_id_2) + "!" == m.split("%")[0]:
                    offer_text = m.split("%")[1]
                    offer_cost = m.split("%")[2]

            n = i[0][9].split("%%%")[0] + "%%%"
            for m in i[0][9].split("%%%")[1:-1]:
                if str(user_id_2) == m.split("%")[0]:
                    o = m.split("%")[1]
                    p = int(m.split("%")[2].replace(",", "").replace(" T", "")) - 3000
                    y = {"۰": "0", "۱": "1", "۲": "2", "۳": "3", "۴": "4", "۵": "5", "۶": "6", "۷": "7", "۸": "8",
                         "۹": "9"}
                    z = ""
                    for x in str(p):
                        if x in "۰۱۲۳۴۵۶۷۸۹":
                            z += y[x]
                        else:
                            z += x
                    if 4 <= len(z) <= 6:
                        x = z[:-3] + ',' + z[-3:]
                    elif 7 <= len(z) <= 9:
                        x = z[:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                    elif 10 <= len(z) <= 12:
                        x = z[:-9] + ',' + z[-9:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                    p = x + " T"

                    a = await bot.ask(user_id_2, f"""
🖍 شماره کارت : 

📋 نمونه : 1234123412341234

/Cancel
""", reply_markup=ReplyKeyboardRemove(all))

                    if a.text != "/Cancel":
                        b = await bot.ask(user_id_2, f"""
🖍 نام و نام خانوادگی : 

📋 نمونه : علی صادقی

/Cancel
""", reply_markup=ReplyKeyboardRemove(all))

                        if b.text != "/Cancel":
                            m = m + "%" + "fr" + "&" + a.text + "&" + b.text + "%%%"
                            await bot.edit_message_text(user_id_2, message_id, f"""
<strong>FiNiShEd</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""")
                            await bot.send_message(user_id_2, """
<strong>تایید شد</strong>

📋 حداکثر تا 3 ساعت بعد وجه به صورت کارت به کارت واریز خواهد شد
""", reply_markup=ReplyKeyboardRemove(all))
                            await bot.send_message(-1001618763577, f"""
💳 card_number : <code>{a.text}</code>

👤 Name : {b.text}

💶 Cost: <code>{p.replace(" T", "")}</code> T

Fr @{k[0][1]}
Number : <code>{ad_number + "&" + str(user_id_2)}</code>
""", reply_markup=ReplyKeyboardRemove(all))

                        else:
                            m = m + "%%%"
                            await bot.send_message(user_id_2, "لغو شد", reply_markup=ReplyKeyboardRemove(all))

                    else:
                        m = m + "%%%"
                        await bot.send_message(user_id_2, "لغو شد", reply_markup=ReplyKeyboardRemove(all))

                else:
                    m = m + "%%%"
                n += m

            mycursor.execute("UPDATE ads SET intermediation= \"%s\" WHERE ad_number= \"%s\"" % (n, ad_number))
            mycursor.execute(
                "UPDATE users SET card_number= \"%s\" WHERE user_id= \"%s\"" % (k[0][3] + a.text + "%%%", user_id_2))

        except Exception as e:
            pass

    elif call.data[:7] == "shebaf%":

        try:
            user_id_2 = call.from_user.id
            message_id = call.message.message_id
            ad_number = call.data.split("%")[1]
            i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
            i = mycursor.fetchall()
            j = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (i[0][1]))
            j = mycursor.fetchall()
            k = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (user_id_2))
            k = mycursor.fetchall()

            for m in i[0][8].split("%%%")[:-1]:
                if str(user_id_2) + "!" == m.split("%")[0]:
                    offer_text = m.split("%")[1]
                    offer_cost = m.split("%")[2]

            n = i[0][9].split("%%%")[0] + "%%%"
            for m in i[0][9].split("%%%")[1:-1]:
                if str(user_id_2) == m.split("%")[0]:
                    o = m.split("%")[1]
                    p = m.split("%")[2]
                    cost = int(m.split("%")[9].split("&")[1].split("-")[1]) - 3000
                    y = {"۰": "0", "۱": "1", "۲": "2", "۳": "3", "۴": "4", "۵": "5", "۶": "6", "۷": "7", "۸": "8",
                         "۹": "9"}
                    z = ""
                    for x in str(cost):
                        if x in "۰۱۲۳۴۵۶۷۸۹":
                            z += y[x]
                        else:
                            z += x
                    if 4 <= len(z) <= 6:
                        x = z[:-3] + ',' + z[-3:]
                    elif 7 <= len(z) <= 9:
                        x = z[:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                    elif 10 <= len(z) <= 12:
                        x = z[:-9] + ',' + z[-9:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                    cost = x + " T"

                    a = await bot.ask(user_id_2, f"""
🖍 شماره کارت : 

📋 نمونه : 1234123412341234

/Cancel
""", reply_markup=ReplyKeyboardRemove(all))

                    if a.text != "/Cancel":
                        b = await bot.ask(user_id_2, f"""
🖍 نام و نام خانوادگی : 

📋 نمونه : علی صادقی

/Cancel
""", reply_markup=ReplyKeyboardRemove(all))

                        if b.text != "/Cancel":
                            m = m + "%" + "fr" + "&" + a.text + "&" + b.text + "%%%"
                            await bot.edit_message_text(user_id_2, message_id, f"""
<strong>FiNiShEd

⚠️ {m.split("%")[9].split("&")[0][2:]}</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""")
                            await bot.send_message(user_id_2, """
<strong>تایید شد</strong>

📋 حداکثر تا 3 ساعت بعد وجه به صورت کارت به کارت واریز خواهد شد
""", reply_markup=ReplyKeyboardRemove(all))
                            await bot.send_message(-1001618763577, f"""
💳 card_number : <code>{a.text}</code>

👤 Name : {b.text}

💶 Cost: <code>{cost.replace(" T", "")}</code> T

Fr @{k[0][1]}
Number : <code>{ad_number + "&" + str(user_id_2)}</code>
""", reply_markup=ReplyKeyboardRemove(all))

                        else:
                            m = m + "%%%"
                            await bot.send_message(user_id_2, "لغو شد", reply_markup=ReplyKeyboardRemove(all))

                    else:
                        m = m + "%%%"
                        await bot.send_message(user_id_2, "لغو شد", reply_markup=ReplyKeyboardRemove(all))

                else:
                    m = m + "%%%"
                n += m

            mycursor.execute("UPDATE ads SET intermediation= \"%s\" WHERE ad_number= \"%s\"" % (n, ad_number))
            mycursor.execute(
                "UPDATE users SET card_number= \"%s\" WHERE user_id= \"%s\"" % (k[0][3] + a.text + "%%%", user_id_2))

        except Exception as e:
            pass

    elif call.data[:7] == "shebae%":

        try:
            user_id = call.from_user.id
            user_id_2 = call.data.split("%")[2]
            message_id = call.message.message_id
            ad_number = call.data.split("%")[1]
            i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
            i = mycursor.fetchall()
            j = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (i[0][1]))
            j = mycursor.fetchall()
            k = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (user_id_2))
            k = mycursor.fetchall()

            for m in i[0][8].split("%%%")[:-1]:
                if str(user_id_2) + "!" == m.split("%")[0]:
                    offer_text = m.split("%")[1]
                    offer_cost = m.split("%")[2]

            n = i[0][9].split("%%%")[0] + "%%%"
            for m in i[0][9].split("%%%")[1:-1]:
                if str(user_id_2) == m.split("%")[0]:
                    o = m.split("%")[1]
                    p = m.split("%")[2]
                    if m.split("%")[9].split("&")[1].split("-")[1] == "0":
                        cost = int(m.split("%")[9].split("&")[1].split("-")[0]) - 3000
                    else:
                        cost = int(m.split("%")[9].split("&")[1].split("-")[0])
                    y = {"۰": "0", "۱": "1", "۲": "2", "۳": "3", "۴": "4", "۵": "5", "۶": "6", "۷": "7", "۸": "8",
                         "۹": "9"}
                    z = ""
                    for x in str(cost):
                        if x in "۰۱۲۳۴۵۶۷۸۹":
                            z += y[x]
                        else:
                            z += x
                    if 4 <= len(z) <= 6:
                        x = z[:-3] + ',' + z[-3:]
                    elif 7 <= len(z) <= 9:
                        x = z[:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                    elif 10 <= len(z) <= 12:
                        x = z[:-9] + ',' + z[-9:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                    cost = x + " T"

                    a = await bot.ask(user_id, f"""
🖍 شماره کارت : 

📋 نمونه : 1234123412341234

/Cancel
""", reply_markup=ReplyKeyboardRemove(all))

                    if a.text != "/Cancel":
                        b = await bot.ask(user_id, f"""
🖍 نام و نام خانوادگی : 

📋 نمونه : علی صادقی

/Cancel
""", reply_markup=ReplyKeyboardRemove(all))

                        if b.text != "/Cancel":
                            m = m + "%" + "em" + "&" + a.text + "&" + b.text + "%%%"
                            await bot.edit_message_text(user_id, message_id, f"""
<strong>FiNiShEd

⚠️ {m.split("%")[9].split("&")[0][2:]}</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""")
                            await bot.send_message(user_id, """
<strong>تایید شد</strong>

📋 حداکثر تا 3 ساعت بعد وجه به صورت کارت به کارت واریز خواهد شد
""", reply_markup=ReplyKeyboardRemove(all))
                            await bot.send_message(-1001618763577, f"""
💳 card_number : <code>{a.text}</code>

👤 Name : {b.text}

💶 Cost: <code>{cost.replace(" T", "")}</code> T

em @{j[0][1]}
Number : <code>{ad_number + "&" + str(user_id_2)}</code>
""", reply_markup=ReplyKeyboardRemove(all))

                        else:
                            m = m + "%%%"
                            await bot.send_message(user_id, "لغو شد", reply_markup=ReplyKeyboardRemove(all))

                    else:
                        m = m + "%%%"
                        await bot.send_message(user_id, "لغو شد", reply_markup=ReplyKeyboardRemove(all))

                else:
                    m = m + "%%%"
                n += m

            mycursor.execute("UPDATE ads SET intermediation= \"%s\" WHERE ad_number= \"%s\"" % (n, ad_number))
            mycursor.execute(
                "UPDATE users SET card_number= \"%s\" WHERE user_id= \"%s\"" % (j[0][3] + a.text + "%%%", user_id))

        except Exception as e:
            pass

    elif call.data[:5] == "score":

        try:
            user_id = call.from_user.id
            user_id_2 = call.data.split("%")[2]
            message_id = call.message.message_id
            ad_number = call.data.split("%")[1]
            i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
            i = mycursor.fetchall()
            j = mycursor.execute("SELECT * FROM freelancers WHERE user_id= \"%s\"" % (user_id_2))
            j = mycursor.fetchall()
            k = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (user_id_2))
            k = mycursor.fetchall()
            mark = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton("5")],
                [KeyboardButton("4")],
                [KeyboardButton("3")],
                [KeyboardButton("2")],
                [KeyboardButton("1")],
                [KeyboardButton("0")],
                [KeyboardButton("لغو")]
            ], resize_keyboard=True, one_time_keyboard=True)

            for m in i[0][8].split("%%%")[:-1]:
                if str(user_id_2) + "!" == m.split("%")[0]:
                    offer_text = m.split("%")[1]
                    offer_cost = m.split("%")[2]

            n = i[0][9].split("%%%")[0] + "%%%"
            for m in i[0][9].split("%%%")[1:-1]:
                if user_id_2 == m.split("%")[0]:
                    o = m.split("%")[1]
                    p = m.split("%")[2]

                    a = await bot.ask(user_id, f"""
انتخاب کنید :
""", reply_markup=mark)

                    if int(a.text) in [0, 1, 2, 3, 4, 5]:
                        await bot.edit_message_text(user_id, message_id, f"""
<strong>FiNiShEd</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""")
                        await bot.send_message(user_id, "تایید شد", reply_markup=ReplyKeyboardRemove(all))
                        m = m + "%" + "sc" + "&" + str(a.text) + "%%%"
                        if "%" in j[0][7]:
                            mycursor.execute("UPDATE freelancers SET score= \"%s\" WHERE user_id= \"%s\"" % ("%" + str(
                                "{:.1f}".format(
                                    (float(j[0][7].replace("%", "").split("/")[0]) + int(a.text)) / 2)) + "/5%",
                                                                                                             user_id_2))
                        else:
                            mycursor.execute("UPDATE freelancers SET score= \"%s\" WHERE user_id= \"%s\"" % (
                            str("{:.1f}".format(
                                (float(j[0][7].replace("%", "").split("/")[0]) + int(a.text)) / 2)) + "/5", user_id_2))


                    else:
                        m = m + "%%%"
                        await bot.send_message(user_id, "لغو شد", reply_markup=ReplyKeyboardRemove(all))

                else:
                    m = m + "%%%"

                n += m

            mycursor.execute("UPDATE ads SET intermediation= \"%s\" WHERE ad_number= \"%s\"" % (n, ad_number))

        except Exception as e:
            pass

    elif call.data[:7] == "start_2":
        user_id = call.from_user.id
        user_name = call.from_user.username
        first_name = call.from_user.first_name
        message_id = call.message.message_id
        ad_number = call.data.split("%")[1]
        mark = InlineKeyboardMarkup([
            [InlineKeyboardButton("پی وی", url=f"https://t.me/{user_name}")],
            [InlineKeyboardButton("واسطه گری", callback_data="selection" + "%" + str(ad_number) + "%" + str(user_id))]
        ])
        mark_2 = InlineKeyboardMarkup([
            [InlineKeyboardButton("پشتیبانی", url="https://t.me/onprojsup")]
        ])
        i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
        i = mycursor.fetchall()

        try:

            if user_name == None:
                a = ""
                a = a[0]
            mycursor.execute("UPDATE users SET user_name= \"%s\",first_name= \"%s\" WHERE user_id= \"%s\"" % (
            user_name, "", user_id))
            mycursor.execute("UPDATE freelancers SET user_name= \"%s\",first_name= \"%s\" WHERE user_id= \"%s\"" % (
            user_name, "", user_id))
            await bot.get_chat_member("@onproj", user_id)

            for m in i[0][8].split("%%%")[:-1]:
                if str(user_id) == m.split("%")[0].replace("$$$", "").replace("$1$", "").replace("$2$", "").replace(
                        "$3$", ""):
                    offer_text = m.split("%")[1]
                    offer_cost = m.split("%")[2]

            j = mycursor.execute("SELECT * FROM freelancers WHERE user_id= \"%s\"" % (user_id))
            j = mycursor.fetchall()

            if "%" in j[0][7]:
                l = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (i[0][1]))
                l = mycursor.fetchall()
                if len(l) == 0:
                    un = i[0][1]
                else:
                    un = "@" + l[0][1]
                b = await bot.edit_message_text(user_id, message_id, f"""
<strong>پیشنهاد با موفقیت ثبت شد 🤝</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

<strong>Budget : {i[0][6]}
offer : {offer_cost}</strong>
""")
                await bot.send_message(user_id, f"""
فریلنسر عزیز میتونی با ثبت کردن اطلاعاتت در بات ما :

🚀 رزومه خودت رو هم کنار پیشنهاد برای کارفرما بفرستی
🚀 و همچنین آگهی هایی که مربوط به حرفه شماست رو از طریق بات دریافت کنید

<strong>/freelancer با استفاده از</strong>
""", reply_markup=ReplyKeyboardRemove(all))
                k = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                k = mycursor.fetchall()
                if k[0][1][0] == "@":
                    a = "None"
                else:
                    a = await bot.send_message(i[0][1], f"""
📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🤝 @{user_name}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}</strong>
""", reply_markup=mark)
                    a = a.message_id

            else:
                l = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (i[0][1]))
                l = mycursor.fetchall()
                if len(l) == 0:
                    un = i[0][1]
                else:
                    un = "@" + l[0][1]
                b = await bot.edit_message_text(user_id, message_id, f"""
<strong>پیشنهاد با موفقیت ثبت شد 🤝</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

📋 {j[0][5].split("%")[0]}

Linkedin : {j[0][6]}
Online Project Score : {j[0][7].replace("%", "")}

<strong>Budget : {i[0][6]}
offer : {offer_cost}</strong>
""", reply_markup=mark_2)
                K = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                K = mycursor.fetchall()
                if K[0][1][0] == "@":
                    a = "None"
                else:
                    a = await bot.send_message(i[0][1], f"""
📌 {i[0][5].split("%")[0]}

📝 {offer_text}

📋 {j[0][5].split("%")[0]}

Linkedin : {j[0][6]}
Online Project Score : {j[0][7].replace("%", "")}

🤝 @{user_name}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}</strong>
""", reply_markup=mark)
                    a = a.message_id

            j = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
            j = mycursor.fetchall()
            z = ""
            for m in j[0][8].split("%%%")[:-1]:
                if str(user_id) == m.split("%")[0].replace("$$$", "").replace("$1$", "").replace("$2$", "").replace(
                        "$3$", ""):
                    n = m.replace(m.split("%")[0], m.split("%")[0] + "!") + "%" + str(a) + "%" + str(
                        b.message_id) + "%%%"
                else:
                    n = m + "%%%"
                z += n
            if a == "None":
                mycursor.execute("UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % ("$$$" + z, ad_number))
            else:
                mycursor.execute("UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (z, ad_number))

        except Exception as e:
            mark = InlineKeyboardMarkup([
                [InlineKeyboardButton("تایید یوزرنیم", callback_data=call.data)]
            ])
            mark_2 = InlineKeyboardMarkup([
                [InlineKeyboardButton("عضویت", url="https://t.me/onproj")],
                [InlineKeyboardButton("تایید عضویت", callback_data=call.data)]
            ])

            if str(e) == "local variable 'offer_text' referenced before assignment":
                await bot.delete_messages(chat_id="me", message_ids=message_id)

            try:
                if str(e) == "string index out of range":
                    await bot.edit_message_text(user_id, message_id, "لطفا یوزرنیم برای اکانتت بزار", reply_markup=mark)
                elif str(
                        e) == 'Telegram says: [400 USER_NOT_PARTICIPANT] - The user is not a member of this chat (caused by "channels.GetParticipant")':
                    await bot.edit_message_text(user_id, message_id,
                                                "کاربر گرامی برای استفاده از بات لازمه اول تو کانال عضو باشی 🤝",
                                                reply_markup=mark_2)
            except Exception as e:
                pass

    elif call.data[:7] == "start_3":
        user_id = call.from_user.id
        user_name = call.from_user.username
        if user_name == None:
            user_name = ""
        first_name = call.from_user.first_name
        message_id = call.message.message_id
        ad_number = call.data.split("%")[1]
        mark = InlineKeyboardMarkup([
            [InlineKeyboardButton("واگذاری", callback_data="assignment" + "%" + ad_number)],
            [InlineKeyboardButton("پشتیبانی", url="https://t.me/onprojsup")]
        ])
        i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
        i = mycursor.fetchall()

        try:

            if user_name == "":
                a = ""
                a = a[0]
            mycursor.execute("UPDATE users SET user_name= \"%s\",first_name= \"%s\" WHERE user_id= \"%s\"" % (
            user_name, "", user_id))
            await bot.get_chat_member("@onproj", user_id)

            if str(user_id) == i[0][1] or "@" + user_name == i[0][1]:
                if i[0][5].split("%")[2] == "None":

                    if "FiNiShEd" in i[0][5]:
                        a = await bot.edit_message_text(i[0][1], message_id, f"""
📌 {i[0][5].split("%")[0]}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}</strong>
""")
                    else:
                        a = await bot.edit_message_text(i[0][1], message_id, f"""
📌 {i[0][5].split("%")[0]}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}</strong>
""", reply_markup=mark)

                    mycursor.execute(
                        "UPDATE ads SET user_id = \"%s\",ad= \"%s\",freelancer= \"%s\" WHERE ad_number= \"%s\"" % (
                        str(user_id),
                        i[0][5].replace("None", str(a.message_id)).replace(str(i[0][5].split("%")[1]), "None"),
                        i[0][8].replace("$$$", "").replace("$1$", "").replace("$2$", "").replace("$3$", "").replace(
                            "!%%%", "%%%"), str(i[0][0])))
                    i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                    i = mycursor.fetchall()

                    for m in i[0][8].split("%%%")[:-1]:

                        try:
                            a = m.split("%")[0].replace("!", "")
                            b = m.split("%")[1]
                            c = m.split("%")[2]
                            j = mycursor.execute("SELECT * FROM freelancers WHERE user_id= \"%s\"" % (a))
                            j = mycursor.fetchall()
                            mark_2 = InlineKeyboardMarkup([
                                [InlineKeyboardButton("پی وی", url=f"https://t.me/{user_name}")],
                                [InlineKeyboardButton("واسطه گری",
                                                      callback_data="selection" + "%" + (ad_number) + "%" + str(
                                                          user_id))]
                            ])
                            if "%" in j[0][7]:
                                d = await bot.send_message(user_id, f"""
📌 {i[0][5].split("%")[0]}

📝 {b}

📋 {j[0][5].split("%")[0]}

🤝 @{j[0][1]}
Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}
offer : {c}</strong>
""", reply_markup=mark_2)
                            else:
                                d = await bot.send_message(user_id, f"""
📌 {i[0][5].split("%")[0]}

📝 {b}

📋 {j[0][5].split("%")[0]}

Linkedin : {j[0][6]}
Online Project Score : {j[0][7].replace("%", "")}

🤝 @{j[0][1]}
Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}
offer : {c}</strong>
""", reply_markup=mark_2)
                            mycursor.execute("UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (
                            i[0][8].replace(m, m.replace("None", str(d.message_id))), ad_number))

                        except Exception as e:
                            pass

                else:
                    await bot.delete_messages(chat_id="me", message_ids=message_id)

            else:
                await bot.send_message(user_id, "لطفا از منو استفاده کن", reply_markup=ReplyKeyboardRemove(all))

        except Exception as e:
            mark = InlineKeyboardMarkup([
                [InlineKeyboardButton("تایید یوزرنیم", callback_data=call.data)]
            ])
            mark_2 = InlineKeyboardMarkup([
                [InlineKeyboardButton("عضویت", url="https://t.me/onproj")],
                [InlineKeyboardButton("تایید عضویت", callback_data=call.data)]
            ])

            try:
                if str(e) == "string index out of range":
                    await bot.edit_message_text(user_id, message_id, "لطفا یوزرنیم برای اکانتت بزار", reply_markup=mark)
                elif str(
                        e) == 'Telegram says: [400 USER_NOT_PARTICIPANT] - The user is not a member of this chat (caused by "channels.GetParticipant")':
                    await bot.edit_message_text(user_id, message_id,
                                                "کاربر گرامی برای استفاده از بات لازمه اول تو کانال عضو باشی 🤝",
                                                reply_markup=mark_2)
            except Exception as e:
                pass

    elif call.data[:6] == "new_ad":
        user_id = call.from_user.id
        user_name = call.from_user.username
        first_name = call.from_user.first_name
        message_id = call.message.message_id
        ad_number = call.data.split("%")[1]
        i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
        i = mycursor.fetchall()

        try:

            if user_name == None:
                a = ""
                a = a[0]
            mycursor.execute("UPDATE users SET user_name= \"%s\",first_name= \"%s\" WHERE user_id= \"%s\"" % (
            user_name, "", user_id))
            await bot.get_chat_member("@onproj", user_id)

            if "فوری" in i[0][5]:
                cost = 12000
                cost_2 = "12,000"
            else:
                cost = 6000
                cost_2 = "6,000"
            mark = InlineKeyboardMarkup([
                [InlineKeyboardButton("پرداخت",
                                      url=f"https://onproj.ir/zp/request/{cost}/{ad_number.replace('&', '111111111101111111111')}")]
            ])

            x = await bot.edit_message_text(user_id, message_id, ".")
            await bot.edit_message_text(user_id, x.message_id, "..")
            await bot.edit_message_text(user_id, x.message_id, "...")
            a = await bot.edit_message_text(user_id, x.message_id, f"""
<strong>آگهی با موفقیت ثبت شد 🤝</strong>

📌 {i[0][5].split("%")[0]}

Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
Bot Cost : {cost_2} T</strong>
""", reply_markup=mark)

            mycursor.execute("UPDATE ads SET ad= \"%s\" WHERE ad_number= \"%s\"" % (
            i[0][5] + "%" + "None" + "%" + str(a.message_id), ad_number))

        except Exception as e:
            mark = InlineKeyboardMarkup([
                [InlineKeyboardButton("تایید یوزرنیم", callback_data=call.data)]
            ])
            mark_2 = InlineKeyboardMarkup([
                [InlineKeyboardButton("عضویت", url="https://t.me/onproj")],
                [InlineKeyboardButton("تایید عضویت", callback_data=call.data)]
            ])

            try:
                if str(e) == "string index out of range":
                    a = await bot.edit_message_text(user_id, message_id, "لطفا یوزرنیم برای اکانتت بزار",
                                                    reply_markup=mark)
                elif str(
                        e) == 'Telegram says: [400 USER_NOT_PARTICIPANT] - The user is not a member of this chat (caused by "channels.GetParticipant")':
                    a = await bot.edit_message_text(user_id, message_id,
                                                    "کاربر گرامی برای استفاده از بات لازمه اول تو کانال عضو باشی 🤝",
                                                    reply_markup=mark_2)
            except Exception as e:
                pass

    elif call.data[:11] == "freelancers":
        user_id = call.from_user.id
        user_name = call.from_user.username
        first_name = call.from_user.first_name
        message_id = call.message.message_id
        mark = InlineKeyboardMarkup([
            [InlineKeyboardButton("ویرایش", callback_data="freelancers_edit")]
        ])
        i = mycursor.execute("SELECT * FROM freelancers WHERE user_id= \"%s\"" % (user_id))
        i = mycursor.fetchall()

        try:

            if user_name == None:
                a = ""
                a = a[0]
            mycursor.execute("UPDATE users SET user_name= \"%s\",first_name= \"%s\" WHERE user_id= \"%s\"" % (
            user_name, "", user_id))
            mycursor.execute("UPDATE freelancers SET user_name= \"%s\",first_name= \"%s\" WHERE user_id= \"%s\"" % (
            user_name, "", user_id))
            await bot.get_chat_member("@onproj", user_id)

            a = await bot.edit_message_text(user_id, message_id, f"""
<strong>اطلاعات ثبت شد 🤝</strong>

📋 {i[0][5].split("%")[0]}

Linkedin : {i[0][6]}
Online Project Score : {i[0][7].replace("%", "")}
""", reply_markup=mark)

            mycursor.execute("UPDATE freelancers SET explanation= \"%s\",score= \"%s\" WHERE user_id= \"%s\"" % (
            i[0][5].replace(i[0][5].split("%")[1], str(a.message_id)), i[0][7].replace("%", ""), user_id))

        except Exception as e:
            mark = InlineKeyboardMarkup([
                [InlineKeyboardButton("تایید یوزرنیم", callback_data=call.data)]
            ])
            mark_2 = InlineKeyboardMarkup([
                [InlineKeyboardButton("عضویت", url="https://t.me/onproj")],
                [InlineKeyboardButton("تایید عضویت", callback_data=call.data)]
            ])

            try:
                if str(e) == "string index out of range":
                    a = await bot.edit_message_text(user_id, message_id, "لطفا یوزرنیم برای اکانتت بزار",
                                                    reply_markup=mark)
                elif str(
                        e) == 'Telegram says: [400 USER_NOT_PARTICIPANT] - The user is not a member of this chat (caused by "channels.GetParticipant")':
                    a = await bot.edit_message_text(user_id, message_id,
                                                    "کاربر گرامی برای استفاده از بات لازمه اول تو کانال عضو باشی 🤝",
                                                    reply_markup=mark_2)
            except Exception as e:
                pass


# start...........#
async def start(client, message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    date = jdatetime.datetime.now()

    try:
        mycursor.execute("INSERT INTO users VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (user_id, "", "", "", date))
        await bot.send_message(user_id, f"""
سلام <strong>{first_name}</strong> 👋
به بات <strong>پروژه آنلاین | Online Project</strong> خوش اومدی

برای ادامه میتونی از دستورات زیر یا از Menu استفاده کنی :

/new_ad - ثبت آگهی درسی، کاری و استخدامی
/freelancer - انجام دهنده
/ads - آگهی های ثبت شده
/offers - پیشنهادات فرستاده شده به کارفرمایان
""", reply_markup=ReplyKeyboardRemove(all))

    except Exception as e:
        await bot.send_message(user_id, "لطفا از منو استفاده کن", reply_markup=ReplyKeyboardRemove(all))


# start_2..........#
async def start_2(client, message, text):
    try:
        user_id = message.from_user.id
        user_name = message.from_user.username
        if user_name == None:
            user_name = ""
        first_name = message.from_user.first_name
        date = jdatetime.datetime.now()
        ad_number = text.replace("/start 2", "").replace("111111111101111111111", "&")
        i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
        i = mycursor.fetchall()
        try:
            message_id = message.message_id
            text = message.text
        except:
            message_id = message.message.message_id
            text = text
            await bot.edit_message_text(user_id, message_id, f"""
📌 {i[0][5].split("%")[0]}

<strong>Budget : {i[0][6]}</strong>
""")
        mark = InlineKeyboardMarkup([
            [InlineKeyboardButton("پی وی", url=f"https://t.me/{user_name}")],
            [InlineKeyboardButton("واسطه گری", callback_data="selection" + "%" + ad_number + "%" + str(user_id))]
        ])
        mark_2 = InlineKeyboardMarkup([
            [InlineKeyboardButton("پشتیبانی", url="https://t.me/onprojsup")]
        ])

        if len(i) == 0:
            await bot.send_message(user_id, "لطفا از منو استفاده کن", reply_markup=ReplyKeyboardRemove(all))

        else:

            try:
                mycursor.execute(
                    "INSERT INTO users VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (user_id, "", "", "", date))
                mycursor.execute(
                    "INSERT INTO freelancers VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (
                    user_id, "", "", "", "", "", "", "%0/5%", date))
            except Exception as e:
                try:
                    mycursor.execute(
                        "INSERT INTO freelancers VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (
                        user_id, "", "", "", "", "", "", "%0/5%", date))
                except Exception as e:
                    pass

            if i[0][8] == "":
                z = "YES"

            else:
                for m in i[0][8].split("%%%")[:-1]:
                    if str(user_id) + "!" == m.split("%")[0].replace("$$$", "").replace("$1$", "").replace("$2$",
                                                                                                           "").replace(
                            "$3$", ""):
                        z = "NO"
                        await bot.send_message(user_id, "قبلا برای این آگهی درخواست فرستادی 🙂")
                        break
                    elif str(user_id) == m.split("%")[0]:
                        z = "YES"
                        x = ""
                        for m in i[0][8].split("%%%")[:-1]:
                            if str(user_id) == m.split("%")[0].replace("$$$", "").replace("$1$", "").replace("$2$",
                                                                                                             "").replace(
                                    "$3$", ""):
                                n = ""
                            else:
                                n = m + "%%%"
                            x += n
                        mycursor.execute("UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (x, ad_number))
                        break
                    else:
                        z = "YES"

            if z == "YES":

                if "FiNiShEd" in i[0][5]:
                    await bot.send_message(user_id, "آگهی واگذار شده", reply_markup=ReplyKeyboardRemove(all))

                elif "FiNiShEd" not in i[0][5]:

                    if str(user_id) == i[0][1] or "@" + user_name == i[0][1]:
                        await bot.send_message(user_id, "آگهی خودته که")

                    else:
                        i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                        i = mycursor.fetchall()
                        mycursor.execute("UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (
                        i[0][8] + str(user_id) + "%%%", ad_number))

                        while True:
                            try:
                                a = await bot.ask(user_id, f"""
فریلنسر عزیز خیلی ممنون از همکاری شما 🤝
🖋 لطفا برای ارسال پیشنهاد به کارفرما توضیحاتتون رو بنویسید :

📌 {i[0][5].split("%")[0]}

<strong>Budget : {i[0][6]}</strong>

/Cancel - لغو
""", reply_markup=ReplyKeyboardRemove(all))
                                if a.text == "/Cancel":
                                    j = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                                    j = mycursor.fetchall()
                                    z = ""
                                    for m in j[0][8].split("%%%")[:-1]:
                                        if str(user_id) == m.split("%")[0].replace("$$$", "").replace("$1$",
                                                                                                      "").replace("$2$",
                                                                                                                  "").replace(
                                                "$3$", ""):
                                            n = ""
                                        else:
                                            n = m + "%%%"
                                        z += n
                                    mycursor.execute(
                                        "UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (z, ad_number))
                                    await bot.send_message(user_id, "لغو شد", reply_markup=ReplyKeyboardRemove(all))
                                    break
                                elif len(a.text) < 20:
                                    await bot.send_message(user_id, "متنت خیلی کمه",
                                                           reply_markup=ReplyKeyboardRemove(all))
                                else:
                                    x = ["None", "FiNiShEd", "Paid Intermediation", "Posted Ad", "Paid Ad", "💰", "📌",
                                         "👋🏻", "❌", "⭕️", "✅", "🇮🇷", "⚠️", "❕", "⛔️", "❤️", "⬅️", "‼️", "@", "^", "*",
                                         "$", "!", "&", "%", "#", "/"]
                                    z = "YES"
                                    for m in x:
                                        if m in a.text:
                                            await bot.send_message(user_id,
                                                                   f"استفاده از کلمه یا حرف <strong>{m}</strong> مجاز نیست",
                                                                   reply_markup=ReplyKeyboardRemove(all))
                                            z = "NO"
                                    if z == "YES":
                                        break
                            except Exception as e:
                                await bot.send_message(user_id, "لطفا پیشنهادتون رو به صورت متن بدون استیکر بنویسید",
                                                       reply_markup=ReplyKeyboardRemove(all))

                        if a.text != "/Cancel":
                            j = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                            j = mycursor.fetchall()
                            z = ""
                            for m in j[0][8].split("%%%")[:-1]:
                                if str(user_id) == m.split("%")[0].replace("$$$", "").replace("$1$", "").replace("$2$",
                                                                                                                 "").replace(
                                        "$3$", ""):
                                    n = m + "%" + a.text + "%%%"
                                else:
                                    n = m + "%%%"
                                z += n
                            mycursor.execute(
                                "UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (z, ad_number))

                            while True:
                                b = await bot.ask(user_id, """
🖍 حالا قیمت پیشنهادیت رو به تومان بنویس : 

📋 نمونه : 50000
📋 نمونه : 50000-100000
📋 نمونه : توافقی (/None)

/Cancel - لغو
""", reply_markup=ReplyKeyboardRemove(all))
                                try:
                                    if b.text == "/Cancel":
                                        j = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                                        j = mycursor.fetchall()
                                        z = ""
                                        for m in j[0][8].split("%%%")[:-1]:
                                            if str(user_id) == m.split("%")[0].replace("$$$", "").replace("$1$",
                                                                                                          "").replace(
                                                    "$2$", "").replace("$3$", ""):
                                                n = ""
                                            else:
                                                n = m + "%%%"
                                            z += n
                                        mycursor.execute("UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (
                                        z, ad_number))
                                        await bot.send_message(user_id, "لغو شد", reply_markup=ReplyKeyboardRemove(all))
                                        break
                                    elif b.text == "/None":
                                        offer = "..."
                                        break
                                    elif "-" in b.text:
                                        x = b.text.split("-")
                                        if 100000000 >= int(x[0]) >= 10000 and 100000000 >= int(x[1]) >= 10000:
                                            if int(x[0]) > int(x[1]):
                                                y = {"۰": "0", "۱": "1", "۲": "2", "۳": "3", "۴": "4", "۵": "5",
                                                     "۶": "6", "۷": "7", "۸": "8", "۹": "9"}
                                                z = ""
                                                for m in str(x[0]):
                                                    if m in "۰۱۲۳۴۵۶۷۸۹":
                                                        z += y[m]
                                                    else:
                                                        z += m
                                                if 4 <= len(z) <= 6:
                                                    m = z[:-3] + ',' + z[-3:]
                                                elif 7 <= len(z) <= 9:
                                                    m = z[:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                                                elif 10 <= len(z) <= 12:
                                                    m = z[:-9] + ',' + z[-9:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                                                z = ""
                                                for n in str(x[1]):
                                                    if n in "۰۱۲۳۴۵۶۷۸۹":
                                                        z += y[n]
                                                    else:
                                                        z += n
                                                if 4 <= len(z) <= 6:
                                                    n = z[:-3] + ',' + z[-3:]
                                                elif 7 <= len(z) <= 9:
                                                    n = z[:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                                                elif 10 <= len(z) <= 12:
                                                    n = z[:-9] + ',' + z[-9:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                                                offer = m + " T - " + n + " T"
                                                break
                                            else:
                                                await bot.send_message(user_id, "فرمت درست نیست",
                                                                       reply_markup=ReplyKeyboardRemove(all))
                                        else:
                                            await bot.send_message(user_id, "خارج از محدوده",
                                                                   reply_markup=ReplyKeyboardRemove(all))
                                    else:
                                        if 100000000 >= int(b.text) >= 10000:
                                            x = {"۰": "0", "۱": "1", "۲": "2", "۳": "3", "۴": "4", "۵": "5", "۶": "6",
                                                 "۷": "7", "۸": "8", "۹": "9"}
                                            z = ""
                                            for m in str(b.text):
                                                if m in "۰۱۲۳۴۵۶۷۸۹":
                                                    z += x[m]
                                                else:
                                                    z += m
                                            if 4 <= len(z) <= 6:
                                                m = z[:-3] + ',' + z[-3:]
                                            elif 7 <= len(z) <= 9:
                                                m = z[:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                                            elif 10 <= len(z) <= 12:
                                                m = z[:-9] + ',' + z[-9:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                                            offer = m + " T"
                                            break
                                        else:
                                            await bot.send_message(user_id, "خارج از محدوده",
                                                                   reply_markup=ReplyKeyboardRemove(all))
                                except Exception as e:
                                    await bot.send_message(user_id, "فرمت درست نیست",
                                                           reply_markup=ReplyKeyboardRemove(all))

                            if b.text != "/Cancel":
                                j = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                                j = mycursor.fetchall()
                                z = ""
                                for m in j[0][8].split("%%%")[:-1]:
                                    if str(user_id) == m.split("%")[0].replace("$$$", "").replace("$1$", "").replace(
                                            "$2$", "").replace("$3$", ""):
                                        n = m + "%" + offer + "%%%"
                                    else:
                                        n = m + "%%%"
                                    z += n
                                mycursor.execute(
                                    "UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (z, ad_number))

                                try:

                                    if user_name == "":
                                        a = ""
                                        a = a[0]
                                    mycursor.execute(
                                        "UPDATE users SET user_name= \"%s\",first_name= \"%s\" WHERE user_id= \"%s\"" % (
                                        user_name, "", user_id))
                                    mycursor.execute(
                                        "UPDATE freelancers SET user_name= \"%s\",first_name= \"%s\" WHERE user_id= \"%s\"" % (
                                        user_name, "", user_id))
                                    await bot.get_chat_member("@onproj", user_id)

                                    j = mycursor.execute("SELECT * FROM freelancers WHERE user_id= \"%s\"" % (user_id))
                                    j = mycursor.fetchall()

                                    if "%" in j[0][7]:
                                        l = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (i[0][1]))
                                        l = mycursor.fetchall()
                                        if len(l) == 0:
                                            un = i[0][1]
                                        else:
                                            un = "@" + l[0][1]
                                        b = await bot.send_message(user_id, f"""
<strong>پیشنهاد با موفقیت ثبت شد 🤝</strong>

📌 {i[0][5].split("%")[0]}

📝 {a.text}

<strong>Budget : {i[0][6]}
offer : {offer}</strong>
""", reply_markup=mark_2)
                                        await bot.send_message(user_id, f"""
فریلنسر عزیز میتونی با ثبت کردن اطلاعاتت در بات ما :

🚀 رزومه خودت رو هم کنار پیشنهاد برای کارفرما بفرستی
🚀 و همچنین آگهی هایی که مربوط به حرفه شماست رو از طریق بات دریافت کنید

<strong>/freelancer با استفاده از</strong>
""", reply_markup=ReplyKeyboardRemove(all))
                                        k = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                                        k = mycursor.fetchall()
                                        if k[0][1][0] == "@":
                                            a = "None"
                                        else:
                                            a = await bot.send_message(i[0][1], f"""
📌 {i[0][5].split("%")[0]}

📝 {a.text}

🤝 @{user_name}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer}</strong>
""", reply_markup=mark)
                                            a = a.message_id

                                    else:
                                        l = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (i[0][1]))
                                        l = mycursor.fetchall()
                                        if len(l) == 0:
                                            un = i[0][1]
                                        else:
                                            un = "@" + l[0][1]
                                        b = await bot.send_message(user_id, f"""
<strong>پیشنهاد با موفقیت ثبت شد 🤝</strong>

📌 {i[0][5].split("%")[0]}

📝 {a.text}

📋 {j[0][5].split("%")[0]}

Linkedin : {j[0][6]}
Online Project Score : {j[0][7].replace("%", "")}

<strong>Budget : {i[0][6]}
offer : {offer}</strong>
""", reply_markup=mark_2)
                                        k = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                                        k = mycursor.fetchall()
                                        if k[0][1][0] == "@":
                                            a = "None"
                                        else:
                                            a = await bot.send_message(i[0][1], f"""
📌 {i[0][5].split("%")[0]}

📝 {a.text}

📋 {j[0][5].split("%")[0]}

Linkedin : {j[0][6]}
Online Project Score : {j[0][7].replace("%", "")}

🤝 @{user_name}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer}</strong>
""", reply_markup=mark)
                                            a = a.message_id

                                    j = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                                    j = mycursor.fetchall()
                                    z = ""
                                    for m in j[0][8].split("%%%")[:-1]:
                                        if str(user_id) == m.split("%")[0].replace("$$$", "").replace("$1$",
                                                                                                      "").replace("$2$",
                                                                                                                  "").replace(
                                                "$3$", ""):
                                            n = m.replace(m.split("%")[0], m.split("%")[0] + "!") + "%" + str(
                                                a) + "%" + str(b.message_id) + "%%%"
                                        else:
                                            n = m + "%%%"
                                        z += n
                                    if a == "None":
                                        mycursor.execute("UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (
                                        "$$$" + z, ad_number))
                                    else:
                                        mycursor.execute("UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (
                                        z, ad_number))

                                except Exception as e:
                                    if text[:8] != "/start 2":
                                        mark = InlineKeyboardMarkup([
                                            [InlineKeyboardButton("تایید یوزرنیم", callback_data="start_2" + "%" + str(
                                                ad_number) + "%" + str(message_id))]
                                        ])
                                        mark_2 = InlineKeyboardMarkup([
                                            [InlineKeyboardButton("عضویت", url="https://t.me/onproj")],
                                            [InlineKeyboardButton("تایید عضویت", callback_data="start_2" + "%" + str(
                                                ad_number) + "%" + str(message_id))]
                                        ])
                                    else:
                                        mark = InlineKeyboardMarkup([
                                            [InlineKeyboardButton("تایید یوزرنیم",
                                                                  callback_data="start_2" + "%" + str(ad_number))]
                                        ])
                                        mark_2 = InlineKeyboardMarkup([
                                            [InlineKeyboardButton("عضویت", url="https://t.me/onproj")],
                                            [InlineKeyboardButton("تایید عضویت",
                                                                  callback_data="start_2" + "%" + str(ad_number))]
                                        ])
                                    if str(e) == "string index out of range":
                                        await bot.send_message(user_id, "لطفا یوزرنیم برای اکانتت بزار",
                                                               reply_markup=mark)
                                    elif str(
                                            e) == 'Telegram says: [400 USER_NOT_PARTICIPANT] - The user is not a member of this chat (caused by "channels.GetParticipant")':
                                        await bot.send_message(user_id,
                                                               "کاربر گرامی برای استفاده از بات لازمه اول تو کانال عضو باشی 🤝",
                                                               reply_markup=mark_2)

    except Exception as e:
        pass


# start_3..........#
async def start_3(client, message):
    try:
        user_id = message.from_user.id
        user_name = message.from_user.username
        if user_name == None:
            user_name = ""
        first_name = message.from_user.first_name
        text = message.text
        date = jdatetime.datetime.now()
        ad_number = text.replace("/start 3", "").replace("111111111101111111111", "&")
        mark = InlineKeyboardMarkup([
            [InlineKeyboardButton("پشتیبانی", url="https://t.me/onprojsup")]
        ])
        mark_2 = InlineKeyboardMarkup([
            [InlineKeyboardButton("واگذاری", callback_data="assignment" + "%" + ad_number)],
            [InlineKeyboardButton("پشتیبانی", url="https://t.me/onprojsup")]
        ])
        i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
        i = mycursor.fetchall()

        try:
            mycursor.execute(
                "INSERT INTO users VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (user_id, "", "", "", date))
        except Exception as e:
            pass

        try:

            if user_name == "":
                a = ""
                a = a[0]
            mycursor.execute("UPDATE users SET user_name= \"%s\",first_name= \"%s\" WHERE user_id= \"%s\"" % (
            user_name, "", user_id))
            await bot.get_chat_member("@onproj", user_id)

            if str(user_id) == i[0][1] or "@" + user_name == i[0][1]:

                if i[0][5].split("%")[2] == "None":

                    if "FiNiShEd" in i[0][5]:
                        a = await bot.send_message(i[0][1], f"""
📌 {i[0][5].split("%")[0]}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}</strong>
""", reply_markup=mark)

                    else:
                        a = await bot.send_message(i[0][1], f"""
📌 {i[0][5].split("%")[0]}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}</strong>
""", reply_markup=mark_2)

                    mycursor.execute(
                        "UPDATE ads SET user_id = \"%s\",ad= \"%s\",freelancer= \"%s\" WHERE ad_number= \"%s\"" % (
                        str(user_id),
                        i[0][5].replace("None", str(a.message_id)).replace(str(i[0][5].split("%")[1]), "None"),
                        i[0][8].replace("$$$", "").replace("$1$", "").replace("$2$", "").replace("$3$", "").replace(
                            "!%%%", "%%%"), str(i[0][0])))
                    i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                    i = mycursor.fetchall()

                    for m in i[0][8].split("%%%")[:-1]:

                        try:
                            a = m.split("%")[0].replace("!", "")
                            b = m.split("%")[1]
                            c = m.split("%")[2]
                            j = mycursor.execute("SELECT * FROM freelancers WHERE user_id= \"%s\"" % (a))
                            j = mycursor.fetchall()
                            mark_2 = InlineKeyboardMarkup([
                                [InlineKeyboardButton("پی وی", url=f"https://t.me/{user_name}")],
                                [InlineKeyboardButton("واسطه گری",
                                                      callback_data="selection" + "%" + ad_number + "%" + str(a))]
                            ])
                            if "%" in j[0][7]:
                                d = await bot.send_message(user_id, f"""
📌 {i[0][5].split("%")[0]}

📝 {b}

🤝 @{j[0][1]}
Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}
offer : {c}</strong>
""", reply_markup=mark_2)
                            else:
                                d = await bot.send_message(user_id, f"""
📌 {i[0][5].split("%")[0]}

📝 {b}

📋 {j[0][5].split("%")[0]}

Linkedin : {j[0][6]}
Online Project Score : {j[0][7].replace("%", "")}

🤝 @{j[0][1]}
Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}
offer : {c}</strong>
""", reply_markup=mark_2)
                            mycursor.execute("UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (
                            i[0][8].replace(m, m.replace("None", str(d.message_id))), ad_number))

                        except Exception as e:
                            pass

                else:
                    await bot.send_message(user_id, "لطفا از منو استفاده کن")

            else:
                await bot.send_message(user_id, "لطفا از منو استفاده کن")

        except Exception as e:
            mark = InlineKeyboardMarkup([
                [InlineKeyboardButton("تایید یوزرنیم", callback_data="start_3" + "%" + str(ad_number))]
            ])
            mark_2 = InlineKeyboardMarkup([
                [InlineKeyboardButton("عضویت", url="https://t.me/onproj")],
                [InlineKeyboardButton("تایید عضویت", callback_data="start_3" + "%" + str(ad_number))]
            ])
            if str(e) == "string index out of range":
                await bot.send_message(user_id, "لطفا یوزرنیم برای اکانتت بزار", reply_markup=mark)
            elif str(
                    e) == 'Telegram says: [400 USER_NOT_PARTICIPANT] - The user is not a member of this chat (caused by "channels.GetParticipant")':
                await bot.send_message(user_id, "کاربر گرامی برای استفاده از بات لازمه اول تو کانال عضو باشی 🤝",
                                       reply_markup=mark_2)

    except Exception as e:
        pass


# new_ad..........#
async def new_ad(client, message):
    try:
        user_id = message.from_user.id
        user_name = message.from_user.username
        first_name = message.from_user.first_name
        date = jdatetime.datetime.now()
        i = mycursor.execute("SELECT * FROM ads WHERE user_id= \"%s\"" % (user_id))
        i = mycursor.fetchall()
        ad_number = str(user_id) + "&" + str(len(i) + 1)
        mark = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton("درسی")],
            [KeyboardButton("کاری")],
            [KeyboardButton("استخدامی")],
            [KeyboardButton("لغو")]
        ], resize_keyboard=True, one_time_keyboard=True)

        mycursor.execute(
            "INSERT INTO ads VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" %
            (ad_number, user_id, "we", "", "", "", "", "unpaid", "", "", date))

        a = await bot.ask(user_id, "انتخاب کنید", reply_markup=mark)

        if a.text == "درسی":
            x = "رشته"
            mark = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton("دانش آموز"), KeyboardButton("دانشجو")],
                [KeyboardButton("لغو")]
            ], resize_keyboard=True, one_time_keyboard=True)
            mycursor.execute("UPDATE ads SET type= \"%s\" WHERE ad_number= \"%s\"" % (a.text, ad_number))
            a = await bot.ask(user_id, "انتخاب کنید", reply_markup=mark)
            if a.text == "دانشجو":
                type = "درسی-دانشجو"
                a = ["فنی و مهندسی ", "پزشکی", "علوم انسانی ", "زبان خارجه", "ادبیات", "علوم پایه", "علوم اجتماعی",
                     "مقاله و پژوهش"]
                mark = InlineKeyboardMarkup([
                    [InlineKeyboardButton(a[2], callback_data="s" + "%" + ad_number + "%" + a[2]),
                     InlineKeyboardButton(a[1], callback_data="s" + "%" + ad_number + "%" + a[1]),
                     InlineKeyboardButton(a[0], callback_data="s" + "%" + ad_number + "%" + a[0])],
                    [InlineKeyboardButton(a[5], callback_data="s" + "%" + ad_number + "%" + a[5]),
                     InlineKeyboardButton(a[4], callback_data="s" + "%" + ad_number + "%" + a[4]),
                     InlineKeyboardButton(a[3], callback_data="s" + "%" + ad_number + "%" + a[3])],
                    [InlineKeyboardButton(a[7], callback_data="s" + "%" + ad_number + "%" + a[7]),
                     InlineKeyboardButton(a[6], callback_data="s" + "%" + ad_number + "%" + a[6])]
                ])
            elif a.text == "دانش آموز":
                type = "درسی-دانش آموز"
                b = ["هفتم", "هشتم", "نهم", "متوسطه اول", "ریاضی فیزیک", "علوم تجربی", "علوم انسانی", "فنی و حرفه ای",
                     "کار و دانش", "معارف اسلامی", "متوسطه دوم"]
                mark = InlineKeyboardMarkup([
                    [InlineKeyboardButton(b[3], callback_data=" ")],
                    [InlineKeyboardButton(b[2], callback_data="s" + "%" + ad_number + "%" + b[2]),
                     InlineKeyboardButton(b[1], callback_data="s" + "%" + ad_number + "%" + b[1]),
                     InlineKeyboardButton(b[0], callback_data="s" + "%" + ad_number + "%" + b[0])],
                    [InlineKeyboardButton(b[10], callback_data=" ")],
                    [InlineKeyboardButton(b[6], callback_data="s" + "%" + ad_number + "%" + b[6]),
                     InlineKeyboardButton(b[5], callback_data="s" + "%" + ad_number + "%" + b[5]),
                     InlineKeyboardButton(b[4], callback_data="s" + "%" + ad_number + "%" + b[4])],
                    [InlineKeyboardButton(b[9], callback_data="s" + "%" + ad_number + "%" + b[9]),
                     InlineKeyboardButton(b[8], callback_data="s" + "%" + ad_number + "%" + b[8]),
                     InlineKeyboardButton(b[7], callback_data="s" + "%" + ad_number + "%" + b[7])]
                ])
            else:
                type = "لغو"
                mycursor.execute("DELETE FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                await bot.send_message(user_id, "ثبت آگهی لغو شد", reply_markup=ReplyKeyboardRemove(all))

        elif a.text == "کاری" or a.text == "استخدامی":
            x = "مهارت"
            type = a.text
            c = ["وبسایت", "موبایل", "برنامه نویسی", "سئو و بازاریابی", "نرم افزار", "سخت افزار", "علم داده",
                 "امنیت و شبکه", "هوش مصنوعی", "ویندوز و آفیس", "اپلیکیشن", "سرور", "آی تی و برنامه نویسی",
                 "تبلیغات", "لوگو/پوستر", "فوتوشاپ", "سه بعدی", "رابط کاربری", "انیمیشن", "طراحی قالب",
                 "خدمات ویدئویی و ویرایش عکس", "طراحی و نقاشی", "طراحی و گرافیک",
                 "کامپیوتر", "مکانیک", "برق", "عمران ", "شیمی و پلیمر", "بیومکانیک", "اتوماسیون", "طراحی صنعتی",
                 "صنایع", "مکاترونیک", "الکترونیک", "معماری", "نفت و دریا", "نقشه کشی", "مدیریت", "فنی و مهندسی",
                 "تولید محتوا", "ترجمه", "نگارش/گزارش", "مقاله", "وبلاگ", "تایپ", "نویسندگی", "پژوهش", "کپی رایتینگ",
                 "زیرنویس", "دوبله", "ادمین", "محتوا و ترجمه"]
            mark = InlineKeyboardMarkup([
                [InlineKeyboardButton(c[12], callback_data=" ")],
                [InlineKeyboardButton(c[2], callback_data="s" + "%" + ad_number + "%" + c[2]),
                 InlineKeyboardButton(c[1], callback_data="s" + "%" + ad_number + "%" + c[1]),
                 InlineKeyboardButton(c[0], callback_data="s" + "%" + ad_number + "%" + c[0])],
                [InlineKeyboardButton(c[5], callback_data="s" + "%" + ad_number + "%" + c[5]),
                 InlineKeyboardButton(c[4], callback_data="s" + "%" + ad_number + "%" + c[4]),
                 InlineKeyboardButton(c[3], callback_data="s" + "%" + ad_number + "%" + c[3])],
                [InlineKeyboardButton(c[8], callback_data="s" + "%" + ad_number + "%" + c[8]),
                 InlineKeyboardButton(c[7], callback_data="s" + "%" + ad_number + "%" + c[7]),
                 InlineKeyboardButton(c[6], callback_data="s" + "%" + ad_number + "%" + c[6])],
                [InlineKeyboardButton(c[11], callback_data="s" + "%" + ad_number + "%" + c[11]),
                 InlineKeyboardButton(c[10], callback_data="s" + "%" + ad_number + "%" + c[10]),
                 InlineKeyboardButton(c[9], callback_data="s" + "%" + ad_number + "%" + c[9])],
                [InlineKeyboardButton(c[22], callback_data=" ")],
                [InlineKeyboardButton(c[15], callback_data="s" + "%" + ad_number + "%" + c[15]),
                 InlineKeyboardButton(c[14], callback_data="s" + "%" + ad_number + "%" + c[14]),
                 InlineKeyboardButton(c[13], callback_data="s" + "%" + ad_number + "%" + c[13])],
                [InlineKeyboardButton(c[18], callback_data="s" + "%" + ad_number + "%" + c[18]),
                 InlineKeyboardButton(c[17], callback_data="s" + "%" + ad_number + "%" + c[17]),
                 InlineKeyboardButton(c[16], callback_data="s" + "%" + ad_number + "%" + c[16])],
                [InlineKeyboardButton(c[21], callback_data="s" + "%" + ad_number + "%" + c[21]),
                 InlineKeyboardButton(c[20], callback_data="s" + "%" + ad_number + "%" + c[20]),
                 InlineKeyboardButton(c[19], callback_data="s" + "%" + ad_number + "%" + c[19])],
                [InlineKeyboardButton(c[38], callback_data=" ")],
                [InlineKeyboardButton(c[25], callback_data="s" + "%" + ad_number + "%" + c[25]),
                 InlineKeyboardButton(c[24], callback_data="s" + "%" + ad_number + "%" + c[24]),
                 InlineKeyboardButton(c[23], callback_data="s" + "%" + ad_number + "%" + c[23])],
                [InlineKeyboardButton(c[28], callback_data="s" + "%" + ad_number + "%" + c[28]),
                 InlineKeyboardButton(c[27], callback_data="s" + "%" + ad_number + "%" + c[27]),
                 InlineKeyboardButton(c[26], callback_data="s" + "%" + ad_number + "%" + c[26])],
                [InlineKeyboardButton(c[31], callback_data="s" + "%" + ad_number + "%" + c[31]),
                 InlineKeyboardButton(c[30], callback_data="s" + "%" + ad_number + "%" + c[30]),
                 InlineKeyboardButton(c[29], callback_data="s" + "%" + ad_number + "%" + c[29])],
                [InlineKeyboardButton(c[34], callback_data="s" + "%" + ad_number + "%" + c[34]),
                 InlineKeyboardButton(c[33], callback_data="s" + "%" + ad_number + "%" + c[33]),
                 InlineKeyboardButton(c[32], callback_data="s" + "%" + ad_number + "%" + c[32])],
                [InlineKeyboardButton(c[37], callback_data="s" + "%" + ad_number + "%" + c[37]),
                 InlineKeyboardButton(c[36], callback_data="s" + "%" + ad_number + "%" + c[36]),
                 InlineKeyboardButton(c[35], callback_data="s" + "%" + ad_number + "%" + c[35])],
                [InlineKeyboardButton(c[51], callback_data=" ")],
                [InlineKeyboardButton(c[41], callback_data="s" + "%" + ad_number + "%" + c[41]),
                 InlineKeyboardButton(c[40], callback_data="s" + "%" + ad_number + "%" + c[40]),
                 InlineKeyboardButton(c[39], callback_data="s" + "%" + ad_number + "%" + c[39])],
                [InlineKeyboardButton(c[44], callback_data="s" + "%" + ad_number + "%" + c[44]),
                 InlineKeyboardButton(c[43], callback_data="s" + "%" + ad_number + "%" + c[43]),
                 InlineKeyboardButton(c[42], callback_data="s" + "%" + ad_number + "%" + c[42])],
                [InlineKeyboardButton(c[47], callback_data="s" + "%" + ad_number + "%" + c[47]),
                 InlineKeyboardButton(c[46], callback_data="s" + "%" + ad_number + "%" + c[46]),
                 InlineKeyboardButton(c[45], callback_data="s" + "%" + ad_number + "%" + c[45])],
                [InlineKeyboardButton(c[50], callback_data="s" + "%" + ad_number + "%" + c[50]),
                 InlineKeyboardButton(c[49], callback_data="s" + "%" + ad_number + "%" + c[49]),
                 InlineKeyboardButton(c[48], callback_data="s" + "%" + ad_number + "%" + c[48])]
            ])

        else:
            type = "لغو"
            mycursor.execute("DELETE FROM ads WHERE ad_number= \"%s\"" % (ad_number))
            await bot.send_message(user_id, "ثبت آگهی لغو شد", reply_markup=ReplyKeyboardRemove(all))

        if type != "لغو":
            await bot.send_message(user_id, "انتخاب کنید", reply_markup=mark)
            b = await bot.ask(user_id, f"""
🔗 لطفا {x} مورد نیازت رو انتخاب کن

🖍 اگر {x} مورد نیازت در لیست قرار نداره ، تایپش کن :

/Cancel - لغو
""", reply_markup=ReplyKeyboardRemove(all))
            mycursor.execute("UPDATE ads SET type= \"%s\" WHERE ad_number= \"%s\"" % (type, ad_number))

            if b.text == "/Cancel":
                await bot.send_message(user_id, "ثبت آگهی لغو شد", reply_markup=ReplyKeyboardRemove(all))
                mycursor.execute("DELETE FROM ads WHERE ad_number= \"%s\"" % (ad_number))

            if b.text != "/Cancel":
                mycursor.execute(
                    "UPDATE ads SET skill= \"%s\" WHERE ad_number= \"%s\"" % ("%" + b.text + "%", ad_number))
                await new_ad_2(ad_number, user_id, user_name, first_name)

    except Exception as e:
        pass


async def new_ad_2(ad_number, user_id, user_name, first_name):
    try:
        await bot.send_message(user_id, """
⚖️ قوانین و مقررات درج آگهی ⚖️

🖋 درج آگهی امتحان و پروپزال و پایان نامه اکیداً ممنوع است

🖋 آگهی شما باید منطبق با عرف و حفظ شئونات باشد و از استفاده کلمات توهین آمیز جدا خودداری کنید

🖋 استفاده از هرگونه لینک و موارد تبلیغاتی در آگهی ممنوع میباشد ( برای ثبت تبلیغات به @onprojad مراجعه فرمایید )     
""", reply_markup=ReplyKeyboardRemove(all))

        while True:
            try:
                c = await bot.ask(user_id, """
🖍 حالا متن آگهیت رو اینجا برامون بنویس : 

📋 نمونه : به یک نفر مسلط به فیزیک عمومی ۱ جهت رفع اشکال نیازمندم

/Cancel - لغو
""", reply_markup=ReplyKeyboardRemove(all))
                if c.text == "/Cancel":
                    await bot.send_message(user_id, "ثبت آگهی لغو شد", reply_markup=ReplyKeyboardRemove(all))
                    mycursor.execute("DELETE FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                    break
                elif len(c.text) < 20:
                    await bot.send_message(user_id, "متنت خیلی کمه", reply_markup=ReplyKeyboardRemove(all))
                else:
                    x = ["None", "FiNiShEd", "Paid Intermediation", "Posted Ad", "Paid Ad", "💰", "📌", "👋🏻", "❌", "⭕️",
                         "✅", "🇮🇷", "⚠️", "❕", "⛔️", "❤️", "⬅️", "‼️", "@", "^", "*", "$", "!", "&", "%", "#", "/"]
                    for m in x:
                        if m in c.text:
                            await bot.send_message(user_id, f"استفاده از کلمه یا حرف <strong>{m}</strong> مجاز نیست",
                                                   reply_markup=ReplyKeyboardRemove(all))
                            c.text = "NO"
                    if "فوری" in c.text:
                        cost = 12000
                        cost_2 = "12,000"
                        mycursor.execute("UPDATE ads SET ad_type= \"%s\",ad= \"%s\" WHERE ad_number= \"%s\"" % (
                        "we I", c.text, ad_number))
                        break
                    elif c.text != "NO":
                        cost = 6000
                        cost_2 = "6,000"
                        mycursor.execute("UPDATE ads SET ad= \"%s\" WHERE ad_number= \"%s\"" % (c.text, ad_number))
                        break
            except Exception as e:
                await bot.send_message(user_id, "لطفا آگهی تون رو به صورت متن بدون استیکر بنویسید",
                                       reply_markup=ReplyKeyboardRemove(all))

        if c.text != "/Cancel":
            while True:
                d = await bot.ask(user_id, """
🖍 حالا قیمت پیشنهادیت رو به تومان بنویس : 

📋 نمونه : 50000
📋 نمونه : 50000-100000
📋 نمونه : توافقی (/None)

/Cancel - لغو
""", reply_markup=ReplyKeyboardRemove(all))
                try:
                    if d.text == "/Cancel":
                        await bot.send_message(user_id, "ثبت آگهی لغو شد", reply_markup=ReplyKeyboardRemove(all))
                        mycursor.execute("DELETE FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                        break
                    elif d.text == "/None":
                        budget = "..."
                        break
                    elif "-" in d.text:
                        x = d.text.split("-")
                        if 100000000 >= int(x[0]) >= 10000 and 100000000 >= int(x[1]) >= 10000:
                            if int(x[0]) > int(x[1]):
                                y = {"۰": "0", "۱": "1", "۲": "2", "۳": "3", "۴": "4", "۵": "5", "۶": "6", "۷": "7",
                                     "۸": "8", "۹": "9"}
                                z = ""
                                for m in str(x[0]):
                                    if m in "۰۱۲۳۴۵۶۷۸۹":
                                        z += y[m]
                                    else:
                                        z += m
                                if 4 <= len(z) <= 6:
                                    m = z[:-3] + ',' + z[-3:]
                                elif 7 <= len(z) <= 9:
                                    m = z[:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                                elif 10 <= len(z) <= 12:
                                    m = z[:-9] + ',' + z[-9:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                                z = ""
                                for n in str(x[1]):
                                    if n in "۰۱۲۳۴۵۶۷۸۹":
                                        z += y[n]
                                    else:
                                        z += n
                                if 4 <= len(z) <= 6:
                                    n = z[:-3] + ',' + z[-3:]
                                elif 7 <= len(z) <= 9:
                                    n = z[:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                                elif 10 <= len(z) <= 12:
                                    n = z[:-9] + ',' + z[-9:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                                budget = m + " T - " + n + " T"
                                break
                            else:
                                await bot.send_message(user_id, "فرمت درست نیست")
                        else:
                            await bot.send_message(user_id, "خارج از محدوده")
                    else:
                        if 100000000 >= int(d.text) >= 10000:
                            x = {"۰": "0", "۱": "1", "۲": "2", "۳": "3", "۴": "4", "۵": "5", "۶": "6", "۷": "7",
                                 "۸": "8", "۹": "9"}
                            z = ""
                            for m in str(d.text):
                                if m in "۰۱۲۳۴۵۶۷۸۹":
                                    z += x[m]
                                else:
                                    z += m
                            if 4 <= len(z) <= 6:
                                m = z[:-3] + ',' + z[-3:]
                            elif 7 <= len(z) <= 9:
                                m = z[:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                            elif 10 <= len(z) <= 12:
                                m = z[:-9] + ',' + z[-9:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                            budget = m + " T"
                            break
                        else:
                            await bot.send_message(user_id, "خارج از محدوده")
                except Exception as e:
                    await bot.send_message(user_id, "فرمت درست نیست")

            if d.text != "/Cancel":
                i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                i = mycursor.fetchall()
                mark = InlineKeyboardMarkup([
                    [InlineKeyboardButton("پرداخت",
                                          url=f"https://onproj.ir/zp/request/{cost}/{ad_number.replace('&', '111111111101111111111')}")]
                ])
                mycursor.execute("UPDATE ads SET budget= \"%s\" WHERE ad_number= \"%s\"" % (budget, ad_number))

                try:

                    if user_name == None:
                        a = ""
                        a = a[0]
                    mycursor.execute("UPDATE users SET user_name= \"%s\",first_name= \"%s\" WHERE user_id= \"%s\"" % (
                    user_name, "", user_id))
                    await bot.get_chat_member("@onproj", user_id)

                    x = await bot.send_message(user_id, ".")
                    await bot.edit_message_text(user_id, x.message_id, "..")
                    await bot.edit_message_text(user_id, x.message_id, "...")
                    e = await bot.edit_message_text(user_id, x.message_id, f"""
<strong>آگهی با موفقیت ثبت شد 🤝</strong>

📌 {c.text}

Ad Number : <code>{ad_number}</code>

<strong>Budget : {budget}
Bot Cost : {cost_2} T</strong>
""", reply_markup=mark)

                    mycursor.execute("UPDATE ads SET ad= \"%s\" WHERE ad_number= \"%s\"" % (
                    i[0][5] + "%" + "None" + "%" + str(e.message_id), ad_number))

                except Exception as e:
                    mark = InlineKeyboardMarkup([
                        [InlineKeyboardButton("تایید یوزرنیم", callback_data="new_ad" + "%" + ad_number)]
                    ])
                    mark_2 = InlineKeyboardMarkup([
                        [InlineKeyboardButton("عضویت", url="https://t.me/onproj")],
                        [InlineKeyboardButton("تایید عضویت", callback_data="new_ad" + "%" + ad_number)]
                    ])
                    if str(e) == "string index out of range":
                        e = await bot.send_message(user_id, "لطفا یوزرنیم برای اکانتت بزار", reply_markup=mark)
                    elif str(
                            e) == 'Telegram says: [400 USER_NOT_PARTICIPANT] - The user is not a member of this chat (caused by "channels.GetParticipant")':
                        e = await bot.send_message(user_id,
                                                   "کاربر گرامی برای استفاده از بات لازمه اول تو کانال عضو باشی 🤝",
                                                   reply_markup=mark_2)

    except Exception as e:
        pass


# freelancers.....#
async def freelancers(client, message):
    try:
        user_id = message.from_user.id
        user_name = message.from_user.username
        first_name = message.from_user.first_name
        mark = InlineKeyboardMarkup([
            [InlineKeyboardButton("ویرایش", callback_data="freelancers_edit")]
        ])

        try:
            mycursor.execute(
                "INSERT INTO freelancers VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (
                user_id, "", "", "", "", "", "", "%0/5%", jdatetime.datetime.now()))
            await freelancers_2(user_id, user_name, first_name, "نوع فریلنسریتو انتخاب کن")
        except Exception as e:
            i = mycursor.execute("SELECT * FROM freelancers WHERE user_id= \"%s\"" % (user_id))
            i = mycursor.fetchall()
            try:
                await bot.delete_messages(chat_id="me", message_ids=int(i[0][5].split("%")[1]))
            except Exception as e:
                pass

            if "%" not in i[0][7]:
                a = await bot.send_message(user_id, f"""
    📋 {i[0][5].split("%")[0]}

    Linkedin : {i[0][6]}
    Online Project Score : {i[0][7].replace("%", "")}
    """, reply_markup=mark)
                mycursor.execute("UPDATE freelancers SET explanation= \"%s\" WHERE user_id= \"%s\"" % (
                i[0][5].replace(i[0][5].split("%")[1], str(a.message_id)), user_id))
            else:
                mycursor.execute(
                    "UPDATE freelancers SET type= \"%s\",skill= \"%s\",explanation= \"%s\",linkedin= \"%s\" WHERE user_id= \"%s\"" % (
                    "", "", "", "", user_id))
                await freelancers_2(user_id, user_name, first_name, "نوع فریلنسریتو انتخاب کن")

    except Exception as e:
        pass


async def freelancers_2(user_id, user_name, first_name, text):
    try:
        a = ["دانشجویی", "دانش_آموزی", "فریلنسر_درسی", "فریلنسر_کاری", "فریلنسر_استخدامی"]
        b = ["فنی و مهندسی ", "پزشکی", "علوم انسانی ", "زبان خارجه", "ادبیات", "علوم پایه", "علوم اجتماعی",
             "مقاله و پژوهش"]
        c = ["هفتم", "هشتم", "نهم", "متوسطه اول", "ریاضی فیزیک", "علوم تجربی", "علوم انسانی", "فنی و حرفه ای",
             "کار و دانش", "معارف اسلامی", "متوسطه دوم"]
        d = ["وبسایت", "موبایل", "برنامه نویسی", "سئو و بازاریابی", "نرم افزار", "سخت افزار", "علم داده",
             "امنیت و شبکه", "هوش مصنوعی", "ویندوز و آفیس", "اپلیکیشن", "سرور", "آی تی و برنامه نویسی",
             "تبلیغات", "لوگو/پوستر", "فوتوشاپ", "سه بعدی", "رابط کاربری", "انیمیشن", "طراحی قالب", "خدمات ویدئویی",
             "طراحی و نقاشی", "طراحی و گرافیک",
             "کامپیوتر", "مکانیک", "برق", "عمران ", "شیمی و پلیمر", "بیومکانیک", "اتوماسیون", "طراحی صنعتی", "صنایع",
             "مکاترونیک", "الکترونیک", "معماری", "نفت و دریا", "نقشه کشی", "مدیریت", "فنی و مهندسی",
             "تولید محتوا", "ترجمه", "نگارش/گزارش", "مقاله", "وبلاگ", "تایپ", "نویسندگی", "پژوهش", "کپی رایتینگ",
             "زیرنویس", "دوبله", "ادمین", "محتوا و ترجمه"]
        mark = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton("دانشجویی")],
            [KeyboardButton("دانش آموزی")],
            [KeyboardButton("کاری")],
            [KeyboardButton("استخدامی")],
            [KeyboardButton("لغو")]
        ], resize_keyboard=True, one_time_keyboard=True)
        دانشجویی = InlineKeyboardMarkup([
            [InlineKeyboardButton(b[2], callback_data="freelancers" + "%" + b[2]),
             InlineKeyboardButton(b[1], callback_data="freelancers" + "%" + b[1]),
             InlineKeyboardButton(b[0], callback_data="freelancers" + "%" + b[0])],
            [InlineKeyboardButton(b[5], callback_data="freelancers" + "%" + b[5]),
             InlineKeyboardButton(b[4], callback_data="freelancers" + "%" + b[4]),
             InlineKeyboardButton(b[3], callback_data="freelancers" + "%" + b[3])],
            [InlineKeyboardButton(b[7], callback_data="freelancers" + "%" + b[7]),
             InlineKeyboardButton(b[6], callback_data="freelancers" + "%" + b[6])]
        ])
        دانش_آموزی = InlineKeyboardMarkup([
            [InlineKeyboardButton(c[3], callback_data=" ")],
            [InlineKeyboardButton(c[2], callback_data="freelancers" + "%" + c[2]),
             InlineKeyboardButton(c[1], callback_data="freelancers" + "%" + c[1]),
             InlineKeyboardButton(c[0], callback_data="freelancers" + "%" + c[0])],
            [InlineKeyboardButton(c[10], callback_data=" ")],
            [InlineKeyboardButton(c[6], callback_data="freelancers" + "%" + c[6]),
             InlineKeyboardButton(c[5], callback_data="freelancers" + "%" + c[5]),
             InlineKeyboardButton(c[4], callback_data="freelancers" + "%" + c[4])],
            [InlineKeyboardButton(c[9], callback_data="freelancers" + "%" + c[9]),
             InlineKeyboardButton(c[8], callback_data="freelancers" + "%" + c[8]),
             InlineKeyboardButton(c[7], callback_data="freelancers" + "%" + c[7])]
        ])
        فریلنسر_کاری = InlineKeyboardMarkup([
            [InlineKeyboardButton(d[12], callback_data=" ")],
            [InlineKeyboardButton(d[2], callback_data="freelancers" + "%" + d[2]),
             InlineKeyboardButton(d[1], callback_data="freelancers" + "%" + d[1]),
             InlineKeyboardButton(d[0], callback_data="freelancers" + "%" + d[0])],
            [InlineKeyboardButton(d[5], callback_data="freelancers" + "%" + d[5]),
             InlineKeyboardButton(d[4], callback_data="freelancers" + "%" + d[4]),
             InlineKeyboardButton(d[3], callback_data="freelancers" + "%" + d[3])],
            [InlineKeyboardButton(d[8], callback_data="freelancers" + "%" + d[8]),
             InlineKeyboardButton(d[7], callback_data="freelancers" + "%" + d[7]),
             InlineKeyboardButton(d[6], callback_data="freelancers" + "%" + d[6])],
            [InlineKeyboardButton(d[11], callback_data="freelancers" + "%" + d[11]),
             InlineKeyboardButton(d[10], callback_data="freelancers" + "%" + d[10]),
             InlineKeyboardButton(d[9], callback_data="freelancers" + "%" + d[9])],
            [InlineKeyboardButton(d[22], callback_data=" ")],
            [InlineKeyboardButton(d[15], callback_data="freelancers" + "%" + d[15]),
             InlineKeyboardButton(d[14], callback_data="freelancers" + "%" + d[14]),
             InlineKeyboardButton(d[13], callback_data="freelancers" + "%" + d[13])],
            [InlineKeyboardButton(d[18], callback_data="freelancers" + "%" + d[18]),
             InlineKeyboardButton(d[17], callback_data="freelancers" + "%" + d[17]),
             InlineKeyboardButton(d[16], callback_data="freelancers" + "%" + d[16])],
            [InlineKeyboardButton(d[21], callback_data="freelancers" + "%" + d[21]),
             InlineKeyboardButton(d[20], callback_data="freelancers" + "%" + d[20]),
             InlineKeyboardButton(d[19], callback_data="freelancers" + "%" + d[19])],
            [InlineKeyboardButton(d[38], callback_data=" ")],
            [InlineKeyboardButton(d[25], callback_data="freelancers" + "%" + d[25]),
             InlineKeyboardButton(d[24], callback_data="freelancers" + "%" + d[24]),
             InlineKeyboardButton(d[23], callback_data="freelancers" + "%" + d[23])],
            [InlineKeyboardButton(d[28], callback_data="freelancers" + "%" + d[28]),
             InlineKeyboardButton(d[27], callback_data="freelancers" + "%" + d[27]),
             InlineKeyboardButton(d[26], callback_data="freelancers" + "%" + d[26])],
            [InlineKeyboardButton(d[31], callback_data="freelancers" + "%" + d[31]),
             InlineKeyboardButton(d[30], callback_data="freelancers" + "%" + d[30]),
             InlineKeyboardButton(d[29], callback_data="freelancers" + "%" + d[29])],
            [InlineKeyboardButton(d[34], callback_data="freelancers" + "%" + d[34]),
             InlineKeyboardButton(d[33], callback_data="freelancers" + "%" + d[33]),
             InlineKeyboardButton(d[32], callback_data="freelancers" + "%" + d[32])],
            [InlineKeyboardButton(d[37], callback_data="freelancers" + "%" + d[37]),
             InlineKeyboardButton(d[36], callback_data="freelancers" + "%" + d[36]),
             InlineKeyboardButton(d[35], callback_data="freelancers" + "%" + d[35])],
            [InlineKeyboardButton(d[51], callback_data=" ")],
            [InlineKeyboardButton(d[41], callback_data="freelancers" + "%" + d[41]),
             InlineKeyboardButton(d[40], callback_data="freelancers" + "%" + d[40]),
             InlineKeyboardButton(d[39], callback_data="freelancers" + "%" + d[39])],
            [InlineKeyboardButton(d[44], callback_data="freelancers" + "%" + d[44]),
             InlineKeyboardButton(d[43], callback_data="freelancers" + "%" + d[43]),
             InlineKeyboardButton(d[42], callback_data="freelancers" + "%" + d[42])],
            [InlineKeyboardButton(d[47], callback_data="freelancers" + "%" + d[47]),
             InlineKeyboardButton(d[46], callback_data="freelancers" + "%" + d[46]),
             InlineKeyboardButton(d[45], callback_data="freelancers" + "%" + d[45])],
            [InlineKeyboardButton(d[50], callback_data="freelancers" + "%" + d[50]),
             InlineKeyboardButton(d[49], callback_data="freelancers" + "%" + d[49]),
             InlineKeyboardButton(d[48], callback_data="freelancers" + "%" + d[48])]
        ])
        فریلنسر_استخدامی = InlineKeyboardMarkup([
            [InlineKeyboardButton(d[12], callback_data=" ")],
            [InlineKeyboardButton(d[2], callback_data="freelancers" + "%" + d[2]),
             InlineKeyboardButton(d[1], callback_data="freelancers" + "%" + d[1]),
             InlineKeyboardButton(d[0], callback_data="freelancers" + "%" + d[0])],
            [InlineKeyboardButton(d[5], callback_data="freelancers" + "%" + d[5]),
             InlineKeyboardButton(d[4], callback_data="freelancers" + "%" + d[4]),
             InlineKeyboardButton(d[3], callback_data="freelancers" + "%" + d[3])],
            [InlineKeyboardButton(d[8], callback_data="freelancers" + "%" + d[8]),
             InlineKeyboardButton(d[7], callback_data="freelancers" + "%" + d[7]),
             InlineKeyboardButton(d[6], callback_data="freelancers" + "%" + d[6])],
            [InlineKeyboardButton(d[11], callback_data="freelancers" + "%" + d[11]),
             InlineKeyboardButton(d[10], callback_data="freelancers" + "%" + d[10]),
             InlineKeyboardButton(d[9], callback_data="freelancers" + "%" + d[9])],
            [InlineKeyboardButton(d[22], callback_data=" ")],
            [InlineKeyboardButton(d[15], callback_data="freelancers" + "%" + d[15]),
             InlineKeyboardButton(d[14], callback_data="freelancers" + "%" + d[14]),
             InlineKeyboardButton(d[13], callback_data="freelancers" + "%" + d[13])],
            [InlineKeyboardButton(d[18], callback_data="freelancers" + "%" + d[18]),
             InlineKeyboardButton(d[17], callback_data="freelancers" + "%" + d[17]),
             InlineKeyboardButton(d[16], callback_data="freelancers" + "%" + d[16])],
            [InlineKeyboardButton(d[21], callback_data="freelancers" + "%" + d[21]),
             InlineKeyboardButton(d[20], callback_data="freelancers" + "%" + d[20]),
             InlineKeyboardButton(d[19], callback_data="freelancers" + "%" + d[19])],
            [InlineKeyboardButton(d[38], callback_data=" ")],
            [InlineKeyboardButton(d[25], callback_data="freelancers" + "%" + d[25]),
             InlineKeyboardButton(d[24], callback_data="freelancers" + "%" + d[24]),
             InlineKeyboardButton(d[23], callback_data="freelancers" + "%" + d[23])],
            [InlineKeyboardButton(d[28], callback_data="freelancers" + "%" + d[28]),
             InlineKeyboardButton(d[27], callback_data="freelancers" + "%" + d[27]),
             InlineKeyboardButton(d[26], callback_data="freelancers" + "%" + d[26])],
            [InlineKeyboardButton(d[31], callback_data="freelancers" + "%" + d[31]),
             InlineKeyboardButton(d[30], callback_data="freelancers" + "%" + d[30]),
             InlineKeyboardButton(d[29], callback_data="freelancers" + "%" + d[29])],
            [InlineKeyboardButton(d[34], callback_data="freelancers" + "%" + d[34]),
             InlineKeyboardButton(d[33], callback_data="freelancers" + "%" + d[33]),
             InlineKeyboardButton(d[32], callback_data="freelancers" + "%" + d[32])],
            [InlineKeyboardButton(d[37], callback_data="freelancers" + "%" + d[37]),
             InlineKeyboardButton(d[36], callback_data="freelancers" + "%" + d[36]),
             InlineKeyboardButton(d[35], callback_data="freelancers" + "%" + d[35])],
            [InlineKeyboardButton(d[51], callback_data=" ")],
            [InlineKeyboardButton(d[41], callback_data="freelancers" + "%" + d[41]),
             InlineKeyboardButton(d[40], callback_data="freelancers" + "%" + d[40]),
             InlineKeyboardButton(d[39], callback_data="freelancers" + "%" + d[39])],
            [InlineKeyboardButton(d[44], callback_data="freelancers" + "%" + d[44]),
             InlineKeyboardButton(d[43], callback_data="freelancers" + "%" + d[43]),
             InlineKeyboardButton(d[42], callback_data="freelancers" + "%" + d[42])],
            [InlineKeyboardButton(d[47], callback_data="freelancers" + "%" + d[47]),
             InlineKeyboardButton(d[46], callback_data="freelancers" + "%" + d[46]),
             InlineKeyboardButton(d[45], callback_data="freelancers" + "%" + d[45])],
            [InlineKeyboardButton(d[50], callback_data="freelancers" + "%" + d[50]),
             InlineKeyboardButton(d[49], callback_data="freelancers" + "%" + d[49]),
             InlineKeyboardButton(d[48], callback_data="freelancers" + "%" + d[48])]
        ])

        a = await bot.ask(user_id, text, reply_markup=mark)

        if a.text != "لغو":
            mycursor.execute("UPDATE freelancers SET type= \"%s\" WHERE user_id= \"%s\"" % (a.text, user_id))
            if a.text == "دانشجویی":
                mark = دانشجویی
                x = "رشتت"
            elif a.text == "دانش آموزی":
                mark = دانش_آموزی
                x = "رشتت"
            elif a.text == "کاری":
                mark = فریلنسر_کاری
                x = "مهارتت"
            elif a.text == "استخدامی":
                mark = فریلنسر_استخدامی
                x = "مهارتت"
            else:
                x = "NO"
                await bot.send_message(user_id, "ثبت اطلاعات لغو شد", reply_markup=ReplyKeyboardRemove(all))
                mycursor.execute(
                    "UPDATE freelancers SET type= \"%s\",skill= \"%s\",explanation= \"%s\",linkedin= \"%s\" WHERE user_id= \"%s\"" % (
                    "", "", "", "", user_id))
            if x != "NO":
                await bot.send_message(user_id, "انتخاب کنید", reply_markup=mark)
                b = await bot.ask(user_id, f"""
🔗 لطفا {x} رو انتخاب کن

🖍 اگر {x} در لیست قرار نداره ، تایپش کن :

/Cancel - لغو
""", reply_markup=ReplyKeyboardRemove(all))
                if b.text == "/Cancel":
                    await bot.send_message(user_id, "ثبت اطلاعات لغو شد", reply_markup=ReplyKeyboardRemove(all))
                    mycursor.execute(
                        "UPDATE freelancers SET type= \"%s\",skill= \"%s\",explanation= \"%s\",linkedin= \"%s\" WHERE user_id= \"%s\"" % (
                        "", "", "", "", user_id))
                elif b.text != "/Cancel":
                    mycursor.execute(
                        "UPDATE freelancers SET skill= \"%s\" WHERE user_id= \"%s\"" % ("%" + b.text + "%", user_id))
                    await freelancers_3(user_id, user_name, first_name, b.text)

        else:
            await bot.send_message(user_id, "ثبت اطلاعات لغو شد", reply_markup=ReplyKeyboardRemove(all))
            mycursor.execute(
                "UPDATE freelancers SET type= \"%s\",skill= \"%s\",explanation= \"%s\",linkedin= \"%s\" WHERE user_id= \"%s\"" % (
                "", "", "", "", user_id))

    except Exception as e:
        pass


async def freelancers_3(user_id, user_name, first_name, b):
    try:
        mark = InlineKeyboardMarkup([
            [InlineKeyboardButton("ویرایش", callback_data="freelancers_edit")]
        ])

        while True:
            try:
                c = await bot.ask(user_id, """
🖍 لطفا رزومه خودت ، مهارت ها و تخصص هایی که داری و تحصیلات و سابقه کاری خودتو بنویس تا وقتی پیشنهاد به کارفرما میفرستی رزومت هم فرستاده بشه :

📋 پ.ن : از نوشتن هرگونه لینک و آیدی در رزومه خودداری کن
در صورت مشاهده لینک و آیدی در رزومه ، آیدی شما به بلک لیست فریلنسرها اضافه میشه و دیگه فرصت فعالیت به عنوان فریلنسر با این آیدی رو نخواهی داشت

/Cancel - لغو
""", reply_markup=ReplyKeyboardRemove(all))
                if c.text == "/Cancel":
                    await bot.send_message(user_id, "ثبت اطلاعات لغو شد", reply_markup=ReplyKeyboardRemove(all))
                    mycursor.execute(
                        "UPDATE freelancers SET type= \"%s\",skill= \"%s\",explanation= \"%s\",linkedin= \"%s\" WHERE user_id= \"%s\"" % (
                        "", "", "", "", user_id))
                    break
                elif len(c.text) < 20:
                    await bot.send_message(user_id, "متنت خیلی کمه", reply_markup=ReplyKeyboardRemove(all))
                else:
                    x = ["None", "FiNiShEd", "Paid Intermediation", "Posted Ad", "Paid Ad", "💰", "📌", "👋🏻", "❌", "⭕️",
                         "✅", "🇮🇷", "⚠️", "❕", "⛔️", "❤️", "⬅️", "‼️", "@", "^", "*", "$", "!", "&", "%", "#", "/"]
                    for m in x:
                        if m in c.text:
                            await bot.send_message(user_id, f"استفاده از کلمه یا حرف <strong>{m}</strong> مجاز نیست",
                                                   reply_markup=ReplyKeyboardRemove(all))
                            c.text = "NO"
                    if c.text != "NO":
                        break
            except Exception as e:
                await bot.send_message(user_id, "لطفا از متن بدون استیکر استفاده کنید",
                                       reply_markup=ReplyKeyboardRemove(all))

        if c.text != "/Cancel":
            mycursor.execute("UPDATE freelancers SET explanation= \"%s\" WHERE user_id= \"%s\"" % (c.text, user_id))
            while True:
                try:
                    d = await bot.ask(user_id, """
🖍 در صورت تمایل جهت تقویت اعتبار رزومه حرفه ای خود میتونی لینک پروفایل لینکدیتو رو ارسال کنی تا در رزومه نمایشی شما ثبت بشه :

📋 نمونه : https://www.linkedin.com/in/example
📋 نمونه : ندارم (/None)

/Cancel - لغو
""", reply_markup=ReplyKeyboardRemove(all))
                    if d.text == "/Cancel":
                        await bot.send_message(user_id, "ثبت اطلاعات لغو شد", reply_markup=ReplyKeyboardRemove(all))
                        mycursor.execute(
                            "UPDATE freelancers SET type= \"%s\",skill= \"%s\",explanation= \"%s\",linkedin= \"%s\" WHERE user_id= \"%s\"" % (
                            "", "", "", "", user_id))
                        break
                    elif d.text == "/None":
                        d.text = "..."
                        break
                    elif d.text[:28] == "https://www.linkedin.com/in/":
                        break
                    else:
                        await bot.send_message(user_id, "فرمت درست نیست", reply_markup=ReplyKeyboardRemove(all))
                except Exception as e:
                    await bot.send_message(user_id, "فرمت درست نیست", reply_markup=ReplyKeyboardRemove(all))

            if d.text != "/Cancel":
                mycursor.execute("UPDATE freelancers SET linkedin= \"%s\" WHERE user_id= \"%s\"" % (d.text, user_id))
                i = mycursor.execute("SELECT * FROM freelancers WHERE user_id= \"%s\"" % (user_id))
                i = mycursor.fetchall()

                try:

                    if user_name == None:
                        a = ""
                        a = a[0]
                    mycursor.execute("UPDATE users SET user_name= \"%s\",first_name= \"%s\" WHERE user_id= \"%s\"" % (
                    user_name, "", user_id))
                    mycursor.execute(
                        "UPDATE freelancers SET user_name= \"%s\",first_name= \"%s\" WHERE user_id= \"%s\"" % (
                        user_name, "", user_id))
                    await bot.get_chat_member("@onproj", user_id)

                    e = await bot.send_message(user_id, f"""
<strong>اطلاعات ثبت شد 🤝</strong>

📋 {i[0][5]}

Linkedin : {i[0][6]}
Online Project Score : {i[0][7].replace("%", "")}
""", reply_markup=mark)

                    mycursor.execute(
                        "UPDATE freelancers SET explanation= \"%s\",score= \"%s\" WHERE user_id= \"%s\"" % (
                        i[0][5] + "%" + str(e.message_id), i[0][7].replace("%", ""), user_id))

                except Exception as e:
                    mark = InlineKeyboardMarkup([
                        [InlineKeyboardButton("تایید یوزرنیم", callback_data="freelancers")]
                    ])
                    mark_2 = InlineKeyboardMarkup([
                        [InlineKeyboardButton("عضویت", url="https://t.me/onproj")],
                        [InlineKeyboardButton("تایید عضویت", callback_data="freelancers")]
                    ])
                    if str(e) == "string index out of range":
                        e = await bot.send_message(user_id, "لطفا یوزرنیم برای اکانتت بزار", reply_markup=mark)
                    elif str(
                            e) == 'Telegram says: [400 USER_NOT_PARTICIPANT] - The user is not a member of this chat (caused by "channels.GetParticipant")':
                        e = await bot.send_message(user_id,
                                                   "کاربر گرامی برای استفاده از بات لازمه اول تو کانال عضو باشی 🤝",
                                                   reply_markup=mark_2)
                    mycursor.execute("UPDATE freelancers SET explanation= \"%s\" WHERE user_id= \"%s\"" % (
                    i[0][5] + "%" + str(e.message_id), user_id))

    except Exception as e:
        pass


# ads.............#
async def ads(client, message):
    try:
        user_id = message.from_user.id
        i = mycursor.execute(
            "SELECT * FROM ads WHERE user_id= \"%s\" AND ad LIKE \'%s\' ORDER BY date ASC" % (str(user_id), '%%None%%'))
        i = mycursor.fetchall()
        z = []
        m = -1

        if len(i) == 0:
            a = "None"

        elif len(i) % 2 == 0:
            while m >= -len(i):
                a = [KeyboardButton("📌 " + i[m - 1][5].split("%")[0][:20] + " / " + i[m - 1][0]),
                     KeyboardButton("📌 " + i[m][5].split("%")[0][:20] + " / " + i[m][0])]
                m -= 2
                z.append(a)
            z.append([KeyboardButton("لغو")])
            mark = ReplyKeyboardMarkup(keyboard=z, resize_keyboard=True, one_time_keyboard=True)
            a = await bot.ask(user_id, "انتخاب کنید", reply_markup=mark)
            a = a.text

        elif len(i) % 2 != 0:
            while m > -len(i):
                a = [KeyboardButton("📌 " + i[m - 1][5].split("%")[0][:20] + " / " + i[m - 1][0]),
                     KeyboardButton("📌 " + i[m][5].split("%")[0][:20] + " / " + i[m][0])]
                m -= 2
                z.append(a)
            z.append([KeyboardButton("📌 " + i[0][5].split("%")[0][:20] + " / " + i[0][0])])
            z.append([KeyboardButton("لغو")])
            mark = ReplyKeyboardMarkup(keyboard=z, resize_keyboard=True, one_time_keyboard=True)
            a = await bot.ask(user_id, "انتخاب کنید", reply_markup=mark)
            a = a.text

        if a != "None" and a != "لغو":

            try:
                ad_number = a.split(" / ")[1]
                i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                i = mycursor.fetchall()
                message_id = i[0][5].split("%")[2]
                if i[0][2] == "we I":
                    cost = 12000
                    cost_2 = "12,000"
                else:
                    cost = 6000
                    cost_2 = "6,000"
                mark = InlineKeyboardMarkup([
                    [InlineKeyboardButton("پشتیبانی", url="https://t.me/onprojsup")]
                ])
                mark_2 = InlineKeyboardMarkup([
                    [InlineKeyboardButton("واگذاری", callback_data="assignment" + "%" + ad_number)],
                    [InlineKeyboardButton("پشتیبانی", url="https://t.me/onprojsup")]
                ])
                mark_3 = InlineKeyboardMarkup([
                    [InlineKeyboardButton("پرداخت",
                                          url=f"https://onproj.ir/zp/request/{cost}/{ad_number.replace('&', '111111111101111111111')}")]
                ])

                await bot.delete_messages(chat_id="me", message_ids=int(message_id))

                if "FiNiShEd" in i[0][5]:
                    await bot.send_message(user_id, "تایید شد", reply_markup=ReplyKeyboardRemove(all))
                    a = await bot.send_message(user_id, f"""
<strong>واگذاری شد</strong>

📌 {i[0][5].split("%")[0]}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}</strong>
""", reply_markup=mark)

                elif i[0][7] == "paid":
                    await bot.send_message(user_id, "تایید شد", reply_markup=ReplyKeyboardRemove(all))
                    a = await bot.send_message(user_id, f"""
📌 {i[0][5].split("%")[0]}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}</strong>
""", reply_markup=mark_2)

                elif i[0][7] == "pai":
                    a = await bot.send_message(user_id, f"""
<strong>در حال بررسی ...</strong>

📌 {i[0][5].split("%")[0]}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}</strong>
""", reply_markup=ReplyKeyboardRemove(all))

                else:
                    await bot.send_message(user_id, "تایید شد", reply_markup=ReplyKeyboardRemove(all))
                    a = await bot.send_message(user_id, f"""
📌 {i[0][5].split("%")[0]}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}
Bot Cost : {cost_2} T</strong>
""", reply_markup=mark_3)

                mycursor.execute("UPDATE ads SET ad= \"%s\" WHERE ad_number= \"%s\"" % (
                i[0][5].replace(i[0][5].split("%")[2], str(a.message_id)), ad_number))

                if i[0][8] != "":

                    for m in i[0][8].split("%%%")[:-1]:
                        try:
                            user_id_2 = m.split("%")[0].replace("!", "")
                            offer_text = m.split("%")[1]
                            offer_cost = m.split("%")[2]
                            message_id = m.split("%")[3]
                            i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                            i = mycursor.fetchall()
                            j = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (i[0][1]))
                            j = mycursor.fetchall()
                            k = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (user_id_2))
                            k = mycursor.fetchall()
                            l = mycursor.execute("SELECT * FROM freelancers WHERE user_id= \"%s\"" % (user_id_2))
                            l = mycursor.fetchall()
                            if m.split("%")[-1] != "FiNiShEd":
                                mark = InlineKeyboardMarkup([
                                    [InlineKeyboardButton("پی وی", url=f"https://t.me/{k[0][1]}")],
                                    [InlineKeyboardButton("واسطه گری",
                                                          callback_data="selection" + "%" + (ad_number) + "%" + str(
                                                              user_id_2))]
                                ])
                            else:
                                mark = InlineKeyboardMarkup([
                                    [InlineKeyboardButton("پی وی", url=f"https://t.me/{k[0][1]}")]
                                ])

                            await bot.delete_messages(chat_id="me", message_ids=int(message_id))

                            if "%" in l[0][7]:
                                a = await bot.send_message(i[0][1], f"""
📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}</strong>
""", reply_markup=mark)
                            else:
                                a = await bot.send_message(i[0][1], f"""
📌 {i[0][5].split("%")[0]}

📝 {offer_text}

📋 {l[0][5].split("%")[0]}

Linkedin : {l[0][6]}
Online Project Score : {l[0][7].replace("%", "")}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}</strong>
""", reply_markup=mark)

                            mycursor.execute("UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (
                            i[0][8].replace(m.split("%")[3], str(a.message_id)), ad_number))

                        except Exception as e:
                            pass

                if i[0][9] != "":

                    for m in i[0][9].split("%%%")[1:-1]:

                        try:
                            user_id_2 = m.split("%")[0]
                            o = m.split("%")[1]
                            p = m.split("%")[2]
                            message_id = m.split("%")[3]
                            i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                            i = mycursor.fetchall()
                            j = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (user_id))
                            j = mycursor.fetchall()
                            k = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (user_id_2))
                            k = mycursor.fetchall()

                            total_cost = int(p.replace(" T", "").replace(",", "")) + 3000
                            y = {"۰": "0", "۱": "1", "۲": "2", "۳": "3", "۴": "4", "۵": "5", "۶": "6", "۷": "7",
                                 "۸": "8", "۹": "9"}
                            z = ""
                            for x in str(total_cost):
                                if x in "۰۱۲۳۴۵۶۷۸۹":
                                    z += y[x]
                                else:
                                    z += x
                            if 4 <= len(z) <= 6:
                                x = z[:-3] + ',' + z[-3:]
                            elif 7 <= len(z) <= 9:
                                x = z[:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                            elif 10 <= len(z) <= 12:
                                x = z[:-9] + ',' + z[-9:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                            total_cost = x + " T"

                            for x in i[0][8].split("%%%")[:-1]:
                                if str(user_id_2) + "!" == x.split("%")[0]:
                                    offer_text = x.split("%")[1]
                                    offer_cost = x.split("%")[2]

                            await bot.delete_messages(chat_id="me", message_ids=int(message_id))

                            if len(m.split("%")) == 4:
                                mark = InlineKeyboardMarkup([
                                    [InlineKeyboardButton("تایید",
                                                          callback_data="emac" + "%" + ad_number + "%" + user_id_2)]
                                ])
                                a = await bot.send_message(user_id, f"""
📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}
Bot Cost : 3,000 T
Total Cost : {total_cost}</strong>
""", reply_markup=mark)

                            elif len(m.split("%")) == 6:
                                a = await bot.send_message(user_id, f"""
<strong>در انتظار تایید فریلنسر</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}
Bot Cost : 3,000 T
Total Cost : {total_cost}</strong>
""")

                            elif len(m.split("%")) == 7:
                                mark = InlineKeyboardMarkup([
                                    [InlineKeyboardButton("پرداخت",
                                                          url=f"https://onproj.ir/zp/request/{int(p.replace(',', '').replace(' T', '')) + 3000}/{ad_number.replace('&', '111111111101111111111')}111111111101111111111{user_id_2}")]
                                ])
                                if "!" in m.split("%")[6][-1]:
                                    a = await bot.send_message(user_id, f"""
<strong>پرداخت</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}
Bot Cost : 3,000 T
Total Cost : {total_cost}</strong>
""", reply_markup=mark)
                                else:
                                    a = await bot.send_message(user_id, f"""
<strong>در انتظار انجام پروژه توسط فریلنسر</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""")

                            elif len(m.split("%")) == 8:
                                mark = InlineKeyboardMarkup([
                                    [InlineKeyboardButton("تایید پروژه",
                                                          callback_data="emco" + "%" + ad_number + "%" + k[0][0])],
                                    [InlineKeyboardButton("ارجاع به داوری",
                                                          callback_data="emca" + "%" + ad_number + "%" + k[0][0])]
                                ])
                                a = await bot.send_message(user_id, f"""
<strong>تایید Vs ارجاع</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark)

                            elif len(m.split("%")) == 9:
                                mark = InlineKeyboardMarkup([
                                    [InlineKeyboardButton("امتیاز به فریلنسر",
                                                          callback_data="score" + "%" + ad_number + "%" + user_id_2)]
                                ])
                                mark_2 = InlineKeyboardMarkup([
                                    [InlineKeyboardButton("داوری", url="https://t.me/+A3SrS37IE702NzI0")]
                                ])
                                if m.split("%")[8] == "emco":
                                    a = await bot.send_message(user_id, f"""
<strong>لطفا از 0 تا 5 به عملکرد فریلنسر امتیاز بدید</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark)
                                elif m.split("%")[8] == "emca":
                                    a = await bot.send_message(user_id, f"""
<strong>داوری</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark_2)

                            elif len(m.split("%")) == 10:
                                mark_2 = InlineKeyboardMarkup([
                                    [InlineKeyboardButton("امتیاز به فریلنسر",
                                                          callback_data="score" + "%" + ad_number + "%" + user_id_2)]
                                ])
                                if m.split("%")[9][:2] == "re":
                                    if m.split("%")[9].split("&")[1].split("-")[0] == "0":
                                        x = "FiNiShEd"
                                        mark = ReplyKeyboardRemove(all)
                                    else:
                                        x = "لطفا شماره کارتتون رو برای واریز بنویسید"
                                        mark = InlineKeyboardMarkup([
                                            [InlineKeyboardButton("شماره کارت",
                                                                  callback_data="shebae" + "%" + ad_number + "%" + user_id_2)]
                                        ])
                                    a = await bot.send_message(user_id, f"""
<strong>{x}

⚠️ {m.split("%")[9].split("&")[0][2:]}</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark)
                                elif m.split("%")[9][:2] == "fr":
                                    a = await bot.send_message(user_id, f"""
<strong>لطفا از 0 تا 5 به عملکرد فریلنسر امتیاز بدید</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark_2)
                                else:
                                    a = await bot.send_message(user_id, f"""
<strong>FiNiShEd</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""")

                            elif len(m.split("%")) == 11:
                                if m.split("%")[9][:2] == "re":
                                    if m.split("%")[9].split("&")[1].split("-")[0] == "0":
                                        x = "FiNiShEd"
                                        mark = ReplyKeyboardRemove(all)
                                    else:
                                        x = "لطفا شماره کارتتون رو برای واریز بنویسید"
                                        mark = InlineKeyboardMarkup([
                                            [InlineKeyboardButton("شماره کارت",
                                                                  callback_data="shebae" + "%" + ad_number + "%" + user_id_2)]
                                        ])
                                    if m.split("%")[10][:2] == "em":
                                        a = await bot.send_message(user_id, f"""
<strong>FiNiShEd

⚠️ {m.split("%")[9].split("&")[0][2:]}</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""")
                                    elif m.split("%")[10][:2] == "fr":
                                        a = await bot.send_message(user_id, f"""
<strong>{x}

⚠️ {m.split("%")[9].split("&")[0][2:]}</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark)
                                else:
                                    a = await bot.send_message(user_id, f"""
<strong>FiNiShEd</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""")

                            elif len(m.split("%")) == 12:
                                a = await bot.send_message(user_id, f"""
<strong>FiNiShEd

⚠️ {m.split("%")[9].split("&")[0][2:]}</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""")

                            mycursor.execute("UPDATE ads SET intermediation= \"%s\" WHERE ad_number= \"%s\"" % (
                            i[0][9].replace(m.split("%")[3], str(a.message_id)), ad_number))

                        except Exception as e:
                            pass

            except Exception as e:
                await bot.send_message(user_id, "لغو شد", reply_markup=ReplyKeyboardRemove(all))

        elif a == "None":
            await bot.send_message(user_id, "لیستی ساخته نشده", reply_markup=ReplyKeyboardRemove(all))

        elif a == "لغو":
            await bot.send_message(user_id, "لغو شد", reply_markup=ReplyKeyboardRemove(all))

    except Exception as e:
        pass


# offers..........#
async def offers(client, message):
    try:
        user_id_2 = message.from_user.id
        i = mycursor.execute(
            "SELECT * FROM ads WHERE freelancer LIKE \'%s\' ORDER BY date ASC" % ('%' + str(user_id_2) + "!" + '%'))
        i = mycursor.fetchall()
        z = []
        m = -1

        if len(i) == 0:
            a = "None"

        elif len(i) % 2 == 0:
            while m >= -len(i):
                for x in i[m][8].split("%%%")[:-1]:
                    if str(user_id_2) + "!" == x.split("%")[0].replace("$$$", "").replace("$1$", "").replace("$2$",
                                                                                                             "").replace(
                            "$3$", ""):
                        offer_text = x.split("%")[1]
                        offer_cost = x.split("%")[2]
                for x in i[m - 1][8].split("%%%")[:-1]:
                    if str(user_id_2) + "!" == x.split("%")[0].replace("$$$", "").replace("$1$", "").replace("$2$",
                                                                                                             "").replace(
                            "$3$", ""):
                        offer_text_2 = x.split("%")[1]
                        offer_cost_2 = x.split("%")[2]
                a = [KeyboardButton("📝 " + offer_text_2[:20] + " / " + i[m - 1][0]),
                     KeyboardButton("📝 " + offer_text[:20] + " / " + i[m][0])]
                m -= 2
                z.append(a)
            z.append([KeyboardButton("لغو")])
            mark = ReplyKeyboardMarkup(keyboard=z, resize_keyboard=True, one_time_keyboard=True)
            a = await bot.ask(user_id_2, "انتخاب کنید", reply_markup=mark)
            a = a.text

        elif len(i) % 2 != 0:
            while m > -len(i):
                for x in i[m][8].split("%%%")[:-1]:
                    if str(user_id_2) + "!" == x.split("%")[0].replace("$$$", "").replace("$1$", "").replace("$2$",
                                                                                                             "").replace(
                            "$3$", ""):
                        offer_text = x.split("%")[1]
                        offer_cost = x.split("%")[2]
                for x in i[m - 1][8].split("%%%")[:-1]:
                    if str(user_id_2) + "!" == x.split("%")[0].replace("$$$", "").replace("$1$", "").replace("$2$",
                                                                                                             "").replace(
                            "$3$", ""):
                        offer_text_2 = x.split("%")[1]
                        offer_cost_2 = x.split("%")[2]
                a = [KeyboardButton("📝 " + offer_text_2[:20] + " / " + i[m - 1][0]),
                     KeyboardButton("📝 " + offer_text[:20] + " / " + i[m][0])]
                m -= 2
                z.append(a)
            for x in i[0][8].split("%%%")[:-1]:
                if str(user_id_2) + "!" == x.split("%")[0].replace("$$$", "").replace("$1$", "").replace("$2$",
                                                                                                         "").replace(
                        "$3$", ""):
                    offer_text_3 = x.split("%")[1]
                    offer_cost_3 = x.split("%")[2]
            z.append([KeyboardButton("📝 " + offer_text_3[:20] + " / " + i[0][0])])
            z.append([KeyboardButton("لغو")])
            mark = ReplyKeyboardMarkup(keyboard=z, resize_keyboard=True, one_time_keyboard=True)
            a = await bot.ask(user_id_2, "انتخاب کنید", reply_markup=mark)
            a = a.text

        if a != "None" and a != "لغو":

            try:
                ad_number = a.split(" / ")[1]
                i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
                i = mycursor.fetchall()
                j = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (i[0][1]))
                j = mycursor.fetchall()
                k = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (str(user_id_2)))
                k = mycursor.fetchall()

                for x in i[0][8].split("%%%")[:-1]:

                    try:
                        if str(user_id_2) + "!" == x.split("%")[0].replace("$$$", "").replace("$1$", "").replace("$2$",
                                                                                                                 "").replace(
                                "$3$", ""):
                            offer_text = x.split("%")[1]
                            offer_cost = x.split("%")[2]
                            message_id = x.split("%")[4].replace("!", "")
                            await bot.delete_messages(chat_id="me", message_ids=int(message_id))
                            l = mycursor.execute("SELECT * FROM freelancers WHERE user_id= \"%s\"" % (str(user_id_2)))
                            l = mycursor.fetchall()
                            mark = InlineKeyboardMarkup([
                                [InlineKeyboardButton("پشتیبانی", url="https://t.me/onprojsup")]
                            ])
                            await bot.send_message(user_id_2, "تایید شد", reply_markup=ReplyKeyboardRemove(all))
                            if "%" in l[0][7]:
                                a = await bot.send_message(user_id_2, f"""
📌 {i[0][5].split("%")[0]}

📝 {offer_text}

Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}</strong>
""", reply_markup=mark)
                            else:
                                a = await bot.send_message(user_id_2, f"""
📌 {i[0][5].split("%")[0]}

📝 {offer_text}

📋 {l[0][5].split("%")[0]}

Linkedin : {l[0][6]}
Online Project Score : {l[0][7].replace("%", "")}

Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}</strong>
""", reply_markup=mark)
                            mycursor.execute("UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (
                            i[0][8].replace(x.split("%")[4].replace("!", ""), str(a.message_id)), ad_number))

                    except Exception as e:
                        pass

                for m in i[0][9].split("%%%")[:-1]:

                    try:
                        if str(user_id_2) == m.split("%")[0]:
                            o = m.split("%")[1]
                            p = m.split("%")[2]
                            message_id_2 = m.split("%")[4]

                            total_cost = int(p.replace(" T", "").replace(",", "")) + 3000
                            y = {"۰": "0", "۱": "1", "۲": "2", "۳": "3", "۴": "4", "۵": "5", "۶": "6", "۷": "7",
                                 "۸": "8", "۹": "9"}
                            z = ""
                            for x in str(total_cost):
                                if x in "۰۱۲۳۴۵۶۷۸۹":
                                    z += y[x]
                                else:
                                    z += x
                            if 4 <= len(z) <= 6:
                                x = z[:-3] + ',' + z[-3:]
                            elif 7 <= len(z) <= 9:
                                x = z[:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                            elif 10 <= len(z) <= 12:
                                x = z[:-9] + ',' + z[-9:-6] + ',' + z[-6:-3] + ',' + z[-3:]
                            total_cost = x + " T"

                            await bot.delete_messages(chat_id="me", message_ids=int(message_id_2))

                            if len(m.split("%")) == 6:
                                mark = InlineKeyboardMarkup([
                                    [InlineKeyboardButton("تایید", callback_data="frac" + "%" + ad_number + "%" + str(
                                        user_id_2))]
                                ])
                                a = await bot.send_message(user_id_2, f"""
📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}
Bot Cost : 3,000 T</strong>
""", reply_markup=mark)

                            elif len(m.split("%")) == 7:
                                mark = InlineKeyboardMarkup([
                                    [InlineKeyboardButton("پروژه رو انجام دادم",
                                                          callback_data="frco" + "%" + ad_number + "%" + k[0][0])]
                                ])
                                if m.split("%")[6][-1] == "!":
                                    a = await bot.send_message(user_id_2, f"""
<strong>در انتظار پرداخت کارفرما</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}
Bot Cost : 3,000 T</strong>
""")
                                else:
                                    a = await bot.send_message(user_id_2, f"""
📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark)

                            elif len(m.split("%")) == 8:
                                a = await bot.send_message(user_id_2, f"""
<strong>در انتظار تایید پروژه توسط کارفرما</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""")

                            elif len(m.split("%")) == 9:
                                mark = InlineKeyboardMarkup([
                                    [InlineKeyboardButton("شماره کارت",
                                                          callback_data="sheba" + "%" + ad_number + "%" + str(
                                                              user_id_2))]
                                ])
                                mark_2 = InlineKeyboardMarkup([
                                    [InlineKeyboardButton("داوری", url="https://t.me/+A3SrS37IE702NzI0")]
                                ])
                                if m.split("%")[8] == "emco":
                                    a = await bot.send_message(user_id_2, f"""
<strong>لطفا شماره کارتتون رو برای واریز بنویسید</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark)
                                elif m.split("%")[8] == "emca":
                                    a = await bot.send_message(user_id_2, f"""
<strong>داوری</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark_2)

                            elif len(m.split("%")) == 10:
                                mark_2 = InlineKeyboardMarkup([
                                    [InlineKeyboardButton("شماره کارت",
                                                          callback_data="sheba" + "%" + ad_number + "%" + str(
                                                              user_id_2))]
                                ])
                                if m.split("%")[9][:2] == "re":
                                    if m.split("%")[9].split("&")[1].split("-")[1] == "0":
                                        x = "FiNiShEd"
                                        mark = ReplyKeyboardRemove(all)
                                    else:
                                        x = "لطفا شماره کارتتون رو برای واریز بنویسید"
                                        mark = InlineKeyboardMarkup([
                                            [InlineKeyboardButton("شماره کارت",
                                                                  callback_data="shebaf" + "%" + ad_number + "%" + str(
                                                                      user_id_2))]
                                        ])
                                    a = await bot.send_message(user_id_2, f"""
<strong>{x}

⚠️ {m.split("%")[9].split("&")[0][2:]}</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark)
                                elif m.split("%")[9][:2] == "fr":
                                    a = await bot.send_message(user_id_2, f"""
<strong>FiNiShEd</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""")
                                else:
                                    a = await bot.send_message(user_id_2, f"""
<strong>لطفا شماره کارتتون رو برای واریز بنویسید</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark_2)

                            elif len(m.split("%")) == 11:
                                mark_2 = InlineKeyboardMarkup([
                                    [InlineKeyboardButton("شماره کارت",
                                                          callback_data="sheba" + "%" + ad_number + "%" + str(
                                                              user_id_2))]
                                ])
                                if m.split("%")[9][:2] == "re":
                                    if m.split("%")[9].split("&")[1].split("-")[1] == "0":
                                        x = "FiNiShEd"
                                        mark = ReplyKeyboardRemove(all)
                                    else:
                                        x = "لطفا شماره کارتتون رو برای واریز بنویسید"
                                        mark = InlineKeyboardMarkup([
                                            [InlineKeyboardButton("شماره کارت",
                                                                  callback_data="shebaf" + "%" + ad_number + "%" + str(
                                                                      user_id_2))]
                                        ])
                                    if m.split("%")[10][:2] == "em":
                                        a = await bot.send_message(user_id_2, f"""
<strong>{x}

⚠️ {m.split("%")[9].split("&")[0][2:]}</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark)
                                    elif m.split("%")[10][:2] == "fr":
                                        a = await bot.send_message(user_id_2, f"""
<strong>FiNiShEd

⚠️ {m.split("%")[9].split("&")[0][2:]}</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""")
                                else:
                                    a = await bot.send_message(user_id_2, f"""
<strong>FiNiShEd</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""")

                            elif len(m.split("%")) == 12:
                                a = await bot.send_message(user_id_2, f"""
<strong>FiNiShEd

⚠️ {m.split("%")[9].split("&")[0][2:]}</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""")

                            mycursor.execute("UPDATE ads SET intermediation= \"%s\" WHERE ad_number= \"%s\"" % (
                            i[0][9].replace(m.split("%")[4], str(a.message_id)), ad_number))

                    except Exception as e:
                        pass

            except Exception as e:
                await bot.send_message(user_id_2, "لغو شد", reply_markup=ReplyKeyboardRemove(all))

        elif a == "None":
            await bot.send_message(user_id_2, "پیشنهادی برای انجام آگهی نفرستادی",
                                   reply_markup=ReplyKeyboardRemove(all))

        elif a == "لغو":
            await bot.send_message(user_id_2, "لغو شد", reply_markup=ReplyKeyboardRemove(all))

    except Exception as e:
        pass


# Refereeing......#
async def Refereeing(client, message):
    try:
        user_id = message.from_user.id
        user_id_2 = message.text.split("&")[2]
        ad_number = message.text.split("&")[0] + "&" + message.text.split("&")[1]
        i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
        i = mycursor.fetchall()
        j = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (i[0][1]))
        j = mycursor.fetchall()
        k = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (user_id_2))
        k = mycursor.fetchall()
        mark = InlineKeyboardMarkup([
            [InlineKeyboardButton("شماره کارت", callback_data="shebae" + "%" + ad_number + "%" + user_id_2)]
        ])
        mark_2 = InlineKeyboardMarkup([
            [InlineKeyboardButton("شماره کارت", callback_data="shebaf" + "%" + ad_number + "%" + user_id_2)]
        ])

        for m in i[0][8].split("%%%")[:-1]:
            if str(user_id_2) + "!" == m.split("%")[0]:
                offer_text = m.split("%")[1]
                offer_cost = m.split("%")[2]

        a = await bot.ask(user_id, f"""
نظر داوری : 

/cancel
""", reply_markup=ReplyKeyboardRemove(all))

        if a.text != "/cancel":
            b = await bot.ask(user_id, f"""
هزینه : (em-fr)

📋 نمونه : 50000-100000

/cancel
""", reply_markup=ReplyKeyboardRemove(all))

            if b.text != "/cancel":
                n = i[0][9].split("%%%")[0] + "%%%"
                for m in i[0][9].split("%%%")[1:-1]:
                    if str(user_id_2) == m.split("%")[0]:
                        o = m.split("%")[1]
                        p = m.split("%")[2]
                        message_id = m.split("%")[3]
                        message_id_2 = m.split("%")[4]

                        if b.text.split("-")[0] != "0":
                            await bot.edit_message_text(i[0][1], int(message_id), f"""
<strong>لطفا شماره کارتتون رو برای واریز بنویسید

{a.text}</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark)

                        else:
                            await bot.edit_message_text(i[0][1], int(message_id), f"""
<strong>FiNiShEd

{a.text}</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""")

                        if b.text.split("-")[1] != "0":
                            await bot.edit_message_text(user_id_2, int(message_id_2), f"""
<strong>لطفا شماره کارتتون رو برای واریز بنویسید

{a.text}</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark_2)

                        else:
                            await bot.edit_message_text(user_id_2, int(message_id_2), f"""
<strong>FiNiShEd

{a.text}</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""")

                        await bot.send_message(user_id, "تایید شد", reply_markup=ReplyKeyboardRemove(all))
                        m = m + "%" + "re" + a.text + "&" + b.text + "%%%"

                    else:
                        m = m + "%%%"

                    n += m

                mycursor.execute("UPDATE ads SET intermediation= \"%s\" WHERE ad_number= \"%s\"" % (n, ad_number))

            else:
                await bot.send_message(user_id, "لغو شد", reply_markup=ReplyKeyboardRemove(all))

        else:
            await bot.send_message(user_id, "لغو شد", reply_markup=ReplyKeyboardRemove(all))

    except Exception as e:
        pass


# profile.........#
"""async def profile(client,message):
    user_id= message.from_user.id"""

# s...............#
'''async def s(client,message):
    user_id= message.from_user.id
    date= jdatetime.datetime.now()
    #T
    a= mycursor.execute("SELECT ad_number FROM ads WHERE DAY(date)= DAY(\'%s\')"%(date))
    a= mycursor.fetchall()
    b= mycursor.execute(f"SELECT ad_number FROM ads WHERE ad_type= \'we\' AND DAY(date)= DAY(\'%s\')"%(date))
    b= mycursor.fetchall()
    c= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'ws\' AND DAY(date)= DAY(\'%s\')"%(date))
    c= mycursor.fetchall()
    d= mycursor.execute("SELECT ad_number FROM ads WHERE situation= \'unpaid\' AND DAY(date)= DAY(\'%s\')"%(date))
    d= mycursor.fetchall()
    e= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'we\' AND situation= \'unpaid\' AND DAY(date)= DAY(\'%s\')"%(date))
    e= mycursor.fetchall()
    f= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'ws\' AND situation= \'unpaid\' AND DAY(date)= DAY(\'%s\')"%(date))
    f= mycursor.fetchall()
    g= mycursor.execute("SELECT ad_number FROM ads WHERE situation= \'paid\' AND DAY(date)= DAY(\'%s\')"%(date))
    g= mycursor.fetchall()
    h= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'we\' AND situation= \'paid\' AND DAY(date)= DAY(\'%s\')"%(date))
    h= mycursor.fetchall()
    i= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'ws\' AND situation= \'paid\' AND DAY(date)= DAY(\'%s\')"%(date))
    i= mycursor.fetchall()
    #W
    j= mycursor.execute("SELECT ad_number FROM ads WHERE WEEK(date)= WEEK(\'%s\')"%(date))
    j= mycursor.fetchall()
    k= mycursor.execute(f"SELECT ad_number FROM ads WHERE ad_type= \'we\' AND WEEK(date)= WEEK(\'%s\')"%(date))
    k= mycursor.fetchall()
    l= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'ws\' AND WEEK(date)= WEEK(\'%s\')"%(date))
    l= mycursor.fetchall()
    m= mycursor.execute("SELECT ad_number FROM ads WHERE situation= \'unpaid\' AND WEEK(date)= WEEK(\'%s\')"%(date))
    m= mycursor.fetchall()
    n= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'we\' AND situation= \'unpaid\' AND WEEK(date)= WEEK(\'%s\')"%(date))
    n= mycursor.fetchall()
    o= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'ws\' AND situation= \'unpaid\' AND WEEK(date)= WEEK(\'%s\')"%(date))
    o= mycursor.fetchall()
    p= mycursor.execute("SELECT ad_number FROM ads WHERE situation= \'paid\' AND WEEK(date)= WEEK(\'%s\')"%(date))
    p= mycursor.fetchall()
    q= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'we\' AND situation= \'paid\' AND WEEK(date)= WEEK(\'%s\')"%(date))
    q= mycursor.fetchall()
    r= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'ws\' AND situation= \'paid\' AND WEEK(date)= WEEK(\'%s\')"%(date))
    r= mycursor.fetchall()
    #M
    s= mycursor.execute("SELECT ad_number FROM ads WHERE MONTH(date)= MONTH(\'%s\')"%(date))
    s= mycursor.fetchall()
    t= mycursor.execute(f"SELECT ad_number FROM ads WHERE ad_type= \'we\' AND MONTH(date)= MONTH(\'%s\')"%(date))
    t= mycursor.fetchall()
    u= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'ws\' AND MONTH(date)= MONTH(\'%s\')"%(date))
    u= mycursor.fetchall()
    v= mycursor.execute("SELECT ad_number FROM ads WHERE situation= \'unpaid\' AND MONTH(date)= MONTH(\'%s\')"%(date))
    v= mycursor.fetchall()
    w= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'we\' AND situation= \'unpaid\' AND MONTH(date)= MONTH(\'%s\')"%(date))
    w= mycursor.fetchall()
    x= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'ws\' AND situation= \'unpaid\' AND MONTH(date)= MONTH(\'%s\')"%(date))
    x= mycursor.fetchall()
    y= mycursor.execute("SELECT ad_number FROM ads WHERE situation= \'paid\' AND MONTH(date)= MONTH(\'%s\')"%(date))
    y= mycursor.fetchall()
    z= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'we\' AND situation= \'paid\' AND MONTH(date)= MONTH(\'%s\')"%(date))
    z= mycursor.fetchall()
    a2= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'ws\' AND situation= \'paid\' AND MONTH(date)= MONTH(\'%s\')"%(date))
    a2= mycursor.fetchall()
    #Y
    b2= mycursor.execute("SELECT ad_number FROM ads WHERE YEAR(date)= YEAR(\'%s\')"%(date))
    b2= mycursor.fetchall()
    c2= mycursor.execute(f"SELECT ad_number FROM ads WHERE ad_type= \'we\' AND YEAR(date)= YEAR(\'%s\')"%(date))
    c2= mycursor.fetchall()
    d2= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'ws\' AND YEAR(date)= YEAR(\'%s\')"%(date))
    d2= mycursor.fetchall()
    e2= mycursor.execute("SELECT ad_number FROM ads WHERE situation= \'unpaid\' AND YEAR(date)= YEAR(\'%s\')"%(date))
    e2= mycursor.fetchall()
    f2= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'we\' AND situation= \'unpaid\' AND YEAR(date)= YEAR(\'%s\')"%(date))
    f2= mycursor.fetchall()
    g2= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'ws\' AND situation= \'unpaid\' AND YEAR(date)= YEAR(\'%s\')"%(date))
    g2= mycursor.fetchall()
    h2= mycursor.execute("SELECT ad_number FROM ads WHERE situation= \'paid\' AND YEAR(date)= YEAR(\'%s\')"%(date))
    h2= mycursor.fetchall()
    i2= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'we\' AND situation= \'paid\' AND YEAR(date)= YEAR(\'%s\')"%(date))
    i2= mycursor.fetchall()
    j2= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'ws\' AND situation= \'paid\' AND YEAR(date)= YEAR(\'%s\')"%(date))
    j2= mycursor.fetchall()
    #A
    k2= mycursor.execute("SELECT ad_number FROM ads")
    k2= mycursor.fetchall()
    l2= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'we\'")
    l2= mycursor.fetchall()
    m2= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'ws\'")
    m2= mycursor.fetchall()
    n2= mycursor.execute("SELECT ad_number FROM ads WHERE situation= 'unpaid'")
    n2= mycursor.fetchall()
    o2= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'we\' AND situation= \'unpaid\'")
    o2= mycursor.fetchall()
    p2= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'ws\' AND situation= \'unpaid\'")
    p2= mycursor.fetchall()
    q2= mycursor.execute("SELECT ad_number FROM ads WHERE situation LIKE 'paid'")
    q2= mycursor.fetchall()
    r2= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'we\' AND situation= \'paid\'")
    r2= mycursor.fetchall()
    s2= mycursor.execute("SELECT ad_number FROM ads WHERE ad_type= \'ws\' AND situation= \'paid\'")
    s2= mycursor.fetchall()
    await bot.ask(user_id,f"""
Statistics

Today
ads: {len(a)} (We {len(b)} - Ws {len(c)})
Unpaid ads: {len(d)} (We {len(e)} - Ws {len(f)})
Paid ads: {len(g)} (We {len(h)} - Ws {len(i)})
intermediation: 

Week
ads: {len(j)} (We {len(k)} - Ws {len(l)})
Unpaid ads: {len(m)} (We {len(n)} - Ws {len(o)})
Paid ads: {len(p)} (We {len(q)} - Ws {len(r)})
intermediation: 

Month
ads: {len(s)} (We {len(t)} - Ws {len(u)})
Unpaid ads: {len(v)} (We {len(w)} - Ws {len(x)})
Paid ads: {len(y)} (We {len(z)} - Ws {len(a2)})
intermediation: 

Year
ads: {len(b2)} (We {len(c2)} - Ws {len(d2)})
Unpaid ads: {len(e2)} (We {len(f2)} - Ws {len(g2)})
Paid ads: {len(h2)} (We {len(i2)} - Ws {len(j2)})
intermediation: 

All
ads: {len(k2)} (We {len(l2)} - Ws {len(m2)})
Unpaid ads: {len(n2)} (We {len(o2)} - Ws {len(p2)})
Paid ads: {len(q2)} (We {len(r2)} - Ws {len(s2)})
intermediation: 
""",reply_markup= ReplyKeyboardRemove(all))'''


# main............#
@bot.on_message(filters.private)
async def main(client, message):
    try:
        user_id = message.from_user.id
        text = message.text

        if text == "/start":
            await start(client, message)
        elif text[:8] == "/start 2":
            await start_2(client, message, text)
        elif text[:8] == "/start 3":
            await start_3(client, message)
        elif text == "/new_ad":
            await new_ad(client, message)
        elif text == "/freelancer":
            await freelancers(client, message)
        elif text == "/ads":
            await ads(client, message)
        elif text == "/offers":
            await offers(client, message)
        elif len(text.split("&")) == 3:
            if user_id == 1845389925:
                await Refereeing(client, message)
        elif text == ".":
            if user_id == 1845389925:
                await bot.send_message(user_id, "تایید شد", reply_markup=ReplyKeyboardRemove(all))
                mycursor.execute(
                    "INSERT INTO ads VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" %
                    ("$", " ", " ", " ", " ", "%*" + "$" + "*%", " ", " ", " ", " ", jdatetime.datetime.now()))
            else:
                await bot.send_message(user_id, "لطفا از منو استفاده کن", reply_markup=ReplyKeyboardRemove(all))
        elif text == "a" or text == "b":
            if user_id == 1845389925:
                await bot.send_message(user_id, "تایید شد", reply_markup=ReplyKeyboardRemove(all))
                mycursor.execute(
                    "INSERT INTO ads VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" %
                    (text, " ", " ", " ", " ", "%*" + text + "*%", " ", " ", " ", " ", jdatetime.datetime.now()))
            else:
                await bot.send_message(user_id, "لطفا از منو استفاده کن", reply_markup=ReplyKeyboardRemove(all))
                # elif text== "/profile":
            # await profile(client,message)
        # elif text== "/s":
        # await s(client,message)
        else:
            await bot.send_message(user_id, "لطفا از منو استفاده کن", reply_markup=ReplyKeyboardRemove(all))

    except Exception as e:
        pass


@bot.on_message(filters.chat(-1001531714907))
async def main_2(client, message):
    try:
        text = message.text

        if "Paid Ad" in text:
            a = text.split("Ad Number : ")
            i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (a[1]))
            i = mycursor.fetchall()
            await bot.edit_message_text(i[0][1], int(i[0][5].split("%")[2]), f"""
<strong>در حال بررسی ...</strong>

📌 {i[0][5].split("%")[0]}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}</strong>
""")

        if "Posted Ad" in text:
            a = text.split("Ad Number : ")
            i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (a[1]))
            i = mycursor.fetchall()
            j = mycursor.execute("SELECT * FROM freelancers WHERE skill= \"%s\" ORDER BY date ASC" % (i[0][4]))
            j = mycursor.fetchall()
            mark = InlineKeyboardMarkup([
                [InlineKeyboardButton("واگذاری", callback_data="assignment" + "%" + i[0][0])],
                [InlineKeyboardButton("پشتیبانی", url="https://t.me/onprojsup")]
            ])
            mark_2 = InlineKeyboardMarkup([
                [InlineKeyboardButton("انجام این پروژه", callback_data="dtp" + "%" + a[1])]
            ])

            await bot.edit_message_text(i[0][1], int(i[0][5].split("%")[2]), f"""
📌 {i[0][5].split("%")[0]}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}</strong>
""", reply_markup=mark)

            for m in range(0, len(j)):
                try:
                    if j[m][0] != i[0][1]:
                        if "%" not in j[m][7]:
                            await bot.send_message(j[m][0], f"""
📌 {i[0][5].split("%")[0]}

💰Budget : {i[0][6]}
""", reply_markup=mark_2)
                except Exception as e:
                    pass

        elif "Paid Intermediation" in text:
            ad_number = text.split("Ad Number : ")[1].split("Budget : ")[0].strip()
            user_name_2 = text.split("🤝 ")[1].split("Ad Number : ")[0].replace("@", "").strip()
            i = mycursor.execute("SELECT * FROM ads WHERE ad_number= \"%s\"" % (ad_number))
            i = mycursor.fetchall()
            j = mycursor.execute("SELECT * FROM users WHERE user_id= \"%s\"" % (i[0][1]))
            j = mycursor.fetchall()
            k = mycursor.execute("SELECT * FROM users WHERE user_name= \"%s\"" % (user_name_2))
            k = mycursor.fetchall()
            mark = InlineKeyboardMarkup([
                [InlineKeyboardButton("پروژه رو انجام دادم", callback_data="frco" + "%" + ad_number + "%" + k[0][0])]
            ])

            z = i[0][9].split("%%%")[0] + "%%%"
            for m in i[0][9].split("%%%")[1:-1]:
                if k[0][0] == m.split("%")[0]:
                    o = m.split("%")[1]
                    p = m.split("%")[2]
                    message_id = m.split("%")[3]
                    message_id_2 = m.split("%")[4]
                    z += m.replace("*!*", "").replace("***", "").replace("!", "") + "%%%"
                else:
                    z += m + "%%%"

            for m in i[0][8].split("%%%")[:-1]:
                if k[0][0] + "!" == m.split("%")[0]:
                    offer_text = m.split("%")[1]
                    offer_cost = m.split("%")[2]

            await bot.edit_message_text(i[0][1], int(message_id), f"""
<strong>در انتظار انجام پروژه توسط فریلنسر</strong>

📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{k[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""")
            await bot.edit_message_text(k[0][0], int(message_id_2), f"""
📌 {i[0][5].split("%")[0]}

📝 {offer_text}

🔖 {o}

🤝 @{j[0][1]}
Ad Number : <code>{ad_number}</code>

<strong>Budget : {i[0][6]}
offer : {offer_cost}
Agreed Cost : {p}</strong>
""", reply_markup=mark)

            mycursor.execute("UPDATE ads SET intermediation= \"%s\" WHERE ad_number= \"%s\"" % (z, i[0][0]))

    except Exception as e:
        pass


@bot.on_message(filters.chat("@onproj"))
async def main_3(client, message):
    try:
        text = message.text

        if "%" in text:
            message_id = message.message_id
            i = mycursor.execute(f"SELECT * FROM ads WHERE ad LIKE '%{message_id}%'")
            i = mycursor.fetchall()
            mark = InlineKeyboardMarkup([
                [InlineKeyboardButton("ادیت", callback_data="Correction" + "%" + i[0][0])]
            ])
            mark_2 = InlineKeyboardMarkup([
                [InlineKeyboardButton("انجام این پروژه",
                                      url=f"https://telegram.me/onprojbot?start={'2' + i[0][0].replace('&', '111111111101111111111')}")]
            ])

            if "@" not in i[0][1]:

                try:
                    await bot_22.start()
                    await bot_22.edit_message_text("@onproj", message_id, f"""
📌 Ad returned by admin
""")
                    await bot_22.stop()
                except Exception as e:
                    await bot_2.start()
                    await bot_2.edit_message_text("@onproj", message_id, f"""
📌 Ad returned by admin
""")
                    await bot_2.stop()

                a = await bot.ask(1845389925, f"""
🖍 متن برا ادیت :

📌 {i[0][5].split("%")[0]}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}</strong>
""", reply_markup=ReplyKeyboardRemove(all))

                await bot.send_message(1845389925, """
تایید شد
""", reply_markup=ReplyKeyboardRemove(all))

                await bot.send_message(i[0][1], f"""
<strong>آگهی توسط ادمین رد شد

⚠️ {a.text}</strong>

🖍 لطفا متن آگهی خود را ادیت کنید :

📌 {i[0][5].split("%")[0]}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}</strong>
""", reply_markup=mark)

            else:
                await bot_2.start()
                await bot_2.edit_message_text("@onproj", message_id, f"""
📌 {i[0][5].split("%")[0]}

💰Budget : {i[0][6]}

bot : @onprojbot
Channel : @onproj
""", reply_markup=mark_2)
                await bot_2.stop()

        elif text == "📌 Ad returned by admin":
            pass

        else:

            if "📌 " not in text:
                a = ""
                a = a[0]

            try:
                message_id = message.message_id
                text = text.split("💰")[0].replace("📌 ", "").strip()
                i = mycursor.execute(f"SELECT * FROM ads WHERE ad LIKE '%{message_id}%'")
                i = mycursor.fetchall()
                mark = InlineKeyboardMarkup([
                    [InlineKeyboardButton("پشتیبانی", url="https://t.me/onprojsup")]
                ])
                mark_2 = InlineKeyboardMarkup([
                    [InlineKeyboardButton("واگذاری", callback_data="assignment" + "%" + i[0][0])],
                    [InlineKeyboardButton("پشتیبانی", url="https://t.me/onprojsup")]
                ])

                if "FiNiShEd" in i[0][5] and i[0][5].split("%")[2] != "None":
                    await bot.edit_message_text(i[0][1], int(i[0][5].split("%")[2]), f"""
<strong>واگذاری شد</strong>

📌 {text}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}</strong>
""", reply_markup=mark)

                elif "FiNiShEd" not in i[0][5] and i[0][5].split("%")[2] != "None":
                    await bot.edit_message_text(i[0][1], int(i[0][5].split("%")[2]), f"""
📌 {text}

Ad Number : <code>{i[0][0]}</code>

<strong>Budget : {i[0][6]}</strong>
""", reply_markup=mark_2)

                mycursor.execute("UPDATE ads SET ad= \"%s\" WHERE ad_number= \"%s\"" % (
                i[0][5].replace(i[0][5].split("%")[0], text), i[0][0]))

            except Exception as e:
                pass

    except Exception as e:

        try:
            if message.pinned_message.message_id:
                pass

        except Exception as e:
            user_id = message.chat.id
            if user_id == -1001748468339:
                user_id = 1845389925
            mark = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton("Effectless")],
                [KeyboardButton("3")],
                [KeyboardButton("6")],
                [KeyboardButton("9")],
                [KeyboardButton("12")],
                [KeyboardButton("15")]
            ], resize_keyboard=True, one_time_keyboard=True)
            i = mycursor.execute("SELECT * FROM ads WHERE ad LIKE \'%s\'" % ('%%*%'))
            i = mycursor.fetchall()

            if len(i) == 0:
                i = mycursor.execute("SELECT * FROM ads WHERE situation= \"%s\" ORDER BY date DESC" % ("paid"))
                i = mycursor.fetchall()
                date = i[0][10] + timedelta(minutes=9)
                date = date.strftime("%Y-%m-%d %H:%M:%S")
                a = await bot.ask(user_id, f"TiMe ✅\n\nNeXt Ad {date}", reply_markup=mark)

                try:
                    date = jdatetime.datetime.now() + timedelta(minutes=int(a.text))
                    date = date.strftime("%Y-%m-%d %H:%M:%S")
                    await bot.send_message(user_id, f"Accepted\n\nNeXt Ad {date}",
                                           reply_markup=ReplyKeyboardRemove(all))
                    mycursor.execute(
                        "INSERT INTO ads VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" %
                        (" ", " ", " ", " ", " ", "%*" + date + "*%", " ", " ", " ", " ", jdatetime.datetime.now()))

                except Exception as e:
                    i = mycursor.execute("SELECT * FROM ads WHERE situation= \"%s\" ORDER BY date DESC" % ("paid"))
                    i = mycursor.fetchall()
                    date = i[0][10] + timedelta(minutes=9)
                    date = date.strftime("%Y-%m-%d %H:%M:%S")
                    await bot.send_message(user_id, f"Accepted\n\nNeXt Ad {date}",
                                           reply_markup=ReplyKeyboardRemove(all))

            else:
                date = i[0][5].replace("%", "").replace("*", "")
                await bot.send_message(user_id, f"TiMe ❌\n\nNeXt Ad {date}", reply_markup=ReplyKeyboardRemove(all))


mycursor.close
mydb.close
bot.run()
