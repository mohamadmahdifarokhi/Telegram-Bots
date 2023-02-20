from pyrogram import *
from pyrogram.types import *
import pyromod.listen
import mysql.connector
import time
import schedule
import jdatetime
from datetime import timedelta, datetime

bot_2 = Client(session_name="online_project_2",
               api_id=0,
               api_hash="",
               bot_token="")

bot_3 = Client(session_name="online_project_3",
               api_hash="",
               bot_token="")

bot_4 = Client(session_name="online_project_4",
               api_hash="",
               bot_token="")

bot_5 = Client(session_name="online_project_5",
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


def job():
    try:
        with bot_3:
            with bot_2:

                i = mycursor.execute(
                    "SELECT * FROM ads WHERE ad_type LIKE 'ws%' AND ad LIKE '%!FiNiShEd%' ORDER BY date ASC")
                i = mycursor.fetchall()
                if len(i) != 0:
                    for m in range(0, len(i)):
                        bot_2.edit_message_text("@onproj", int(i[m][5].split("%")[3]), f"""
📌 {i[m][5].split("%")[0]}

💰Budget : {i[m][6]}

bot : @onprojbot
Channel : @onproj
""")
                        mycursor.execute("UPDATE ads SET ad= \"%s\" WHERE ad_number= \"%s\"" % (
                        i[m][5].replace("!FiNiShEd", "FiNiShEd"), i[m][0]))

                i = mycursor.execute("SELECT * FROM ads WHERE ad LIKE \'%s\' ORDER BY date ASC" % ('%*%'))
                i = mycursor.fetchall()
                date = jdatetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                x = date.split(" ")
                y = x[0].split("-")
                z = x[1].split(":")
                date = jdatetime.datetime(int(y[0]), int(y[1]), int(y[2]), int(z[0]), int(z[1]), int(z[2]))
                if len(i) != 0:
                    if "%*a*%" in i[0][5]:
                        mycursor.execute("DELETE FROM ads WHERE ad= \"%s\"" % ("%*a*%"))
                        bot_2.send_message(1845389925, "ON")
                    elif "$" in i[0][5]:
                        mycursor.execute("DELETE FROM ads WHERE ad= \"%s\"" % ("%*$*%"))
                        a = ""
                        a = a[0]
                    elif "%*b*%" in i[0][5]:
                        pass
                    else:
                        x = i[0][5].replace("%", "").replace("*", "").split(" ")
                        y = x[0].split("-")
                        z = x[1].split(":")
                        date_2 = jdatetime.datetime(int(y[0]), int(y[1]), int(y[2]), int(z[0]), int(z[1]), int(z[2]))
                        job_1_1(date, date_2, i)
                else:
                    j = mycursor.execute("SELECT * FROM ads WHERE situation= \"%s\" ORDER BY date DESC" % ("paid"))
                    j = mycursor.fetchall()
                    if len(j) != 0:
                        x = j[0][10].strftime("%Y-%m-%d %H:%M:%S").split(" ")
                        y = x[0].split("-")
                        z = x[1].split(":")
                        date_2 = jdatetime.datetime(int(y[0]), int(y[1]), int(y[2]), int(z[0]), int(z[1]), int(z[2]))
                        date_2 = date_2 + timedelta(minutes=22)
                    else:
                        date_2 = jdatetime.datetime.now() - timedelta(minutes=22)
                    job_1_1(date, date_2, i)

    except Exception as e:
        if str(e) == "string index out of range":
            a = ""
            a = a[0]


def job_1_1(date, date_2, i):
    z = "YES"

    try:

        # 1
        try:
            a = bot_3.get_history("@project_board", limit=100)

            for m in a:
                a = m.text
                message_id = str(m.message_id)

                try:
                    x = ["آگهی منقضی شده", "#انجام_دهنده", "None", "FiNiShEd", "Paid Intermediation", "Posted Ad",
                         "Paid Ad", "‼️", "💰", "📌", "👋🏻", "❌", "⭕️", "✅", "🇮🇷", "⚠️", "❕", "⛔️", "❤️", "⬅️", "‼️", "^",
                         "*", "$", "!", "&", "%", "#", "/"]
                    for n in x:
                        if n in a:
                            y = "NO"
                            break
                        else:
                            y = "YES"
                    if y == "YES":
                        if "🔻واگذار شد" in a:
                            a = a.replace("- - - - - - - - - - - - - -", "").replace("@project_board", "").replace(
                                "🔻واگذار شد", "").strip()
                            j = mycursor.execute("SELECT * FROM ads WHERE ad LIKE \'%s\' AND DAY(date)= DAY(\'%s\')" % (
                            '%' + message_id + '%', date))
                            j = mycursor.fetchall()
                            if len(j) != 0:
                                if "FiNiShEd" not in j[0][5] and j[0][5].split("%")[2] == "None":
                                    bot_2.edit_message_text("@onproj", int(j[0][5].split("%")[3]), f"""
📌 {j[0][5].split("%")[0]}

💰Budget : {j[0][6]}

bot : @onprojbot
Channel : @onproj
""")
                                    mycursor.execute("UPDATE ads SET ad= \"%s\" WHERE ad_number= \"%s\"" % (
                                    j[0][5] + "%" + "FiNiShEd", j[0][0]))

                        if z == "YES" and date >= date_2:
                            if "@project_board" in a:
                                if "فوری" in a:
                                    a = a.replace("فوری", "")
                                a = a.replace("- - - - - - - - - - - - - -", "").replace("@project_board", "").replace(
                                    "🆔 ", "").split("@")
                                a[0] = a[0].strip()
                                a[1] = a[1].strip()
                                j = mycursor.execute(
                                    "SELECT ad_number FROM ads WHERE ad_type= \"%s\" AND ad LIKE \'%s\' ORDER BY date DESC" % (
                                    "ws1", '%' + message_id + '%'))
                                j = mycursor.fetchall()
                                if len(j) == 0:
                                    j = mycursor.execute(
                                        "SELECT ad_number FROM ads WHERE ad LIKE \'%s\' ORDER BY date DESC" % (
                                                    a[0] + '%'))
                                    j = mycursor.fetchall()
                                    if len(j) == 0:
                                        j = mycursor.execute("SELECT * FROM ads WHERE ad_type LIKE 'ws%'")
                                        j = mycursor.fetchall()
                                        k = mycursor.execute("SELECT * FROM ads WHERE user_id= \"%s\"" % ("@" + a[1]))
                                        k = mycursor.fetchall()
                                        ad_number = str(len(j) + 1) + "&" + str(len(k) + 1)
                                        mark = InlineKeyboardMarkup([
                                            [InlineKeyboardButton("انجام این پروژه",
                                                                  url=f"https://telegram.me/onprojbot?start={'2' + str(len(j) + 1) + '111111111101111111111' + str(len(k) + 1)}")]
                                        ])
                                        mycursor.execute(
                                            "INSERT INTO ads VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" %
                                            (ad_number, "@" + a[1], "ws1", "", "", a[0],
                                             "...", "paid", "", "", date))
                                        b = bot_2.send_message("@onproj", f"""
📌 {a[0]}

💰Budget : ...

bot : @onprojbot
Channel : @onproj
""", reply_markup=mark)
                                        if len(i) != 0:
                                            mycursor.execute("DELETE FROM ads WHERE ad= \"%s\"" % (i[0][5]))
                                        ad = a[0] + "%" + str(m.message_id) + "%" + "None" + "%" + str(b.message_id)
                                        mycursor.execute(
                                            "UPDATE ads SET ad= \"%s\" WHERE ad_number= \"%s\"" % (ad, ad_number))
                                        '''print("111")'''
                                        z = "NO"
                                        break

                except Exception as e:
                    pass

        except Exception as e:
            pass

        # 2
        try:
            a = bot_3.get_history("@freelancer_job", limit=100)

            for m in a:
                a = m.text
                message_id = str(m.message_id)

                try:
                    x = ["آگهی منقضی شده", "#انجام_دهنده", "None", "FiNiShEd", "Paid Intermediation", "Posted Ad",
                         "Paid Ad", "‼️", "💰", "📌", "👋🏻", "❌", "⭕️", "✅", "🇮🇷", "⚠️", "❕", "⛔️", "❤️", "⬅️", "‼️", "^",
                         "*", "$", "!", "&", "%", "#", "/"]
                    for n in x:
                        if n in a:
                            y = "NO"
                            break
                        else:
                            y = "YES"
                    if y == "YES":
                        if "🔴 واگذار شد" in a:
                            a = a.replace("- - - - - - - - - - - - - -", "").replace("@freelancer_job", "").replace(
                                "🔴 واگذار شد", "").strip()
                            j = mycursor.execute("SELECT * FROM ads WHERE ad LIKE \'%s\' AND DAY(date)= DAY(\'%s\')" % (
                            '%' + message_id + '%', date))
                            j = mycursor.fetchall()
                            if len(j) != 0:
                                if "FiNiShEd" not in j[0][5] and j[0][5].split("%")[2] == "None":
                                    bot_2.edit_message_text("@onproj", int(j[0][5].split("%")[3]), f"""
📌 {j[0][5].split("%")[0]}

💰Budget : {j[0][6]}

bot : @onprojbot
Channel : @onproj
""")
                                    mycursor.execute("UPDATE ads SET ad= \"%s\" WHERE ad_number= \"%s\"" % (
                                    j[0][5] + "%" + "FiNiShEd", j[0][0]))

                        if z == "YES" and date >= date_2:
                            if "@freelancer_job" in a:
                                if "فوری" in a:
                                    a = a.replace("فوری", "")
                                a = a.replace("- - - - - - - - - - - - - -", "").replace("@freelancer_job", "").replace(
                                    "🆔 ", "").split("@")
                                a[0] = a[0].strip()
                                a[1] = a[1].strip()
                                j = mycursor.execute(
                                    "SELECT ad_number FROM ads WHERE ad_type= \"%s\" AND ad LIKE \'%s\' ORDER BY date DESC" % (
                                    "ws2", '%' + message_id + '%'))
                                j = mycursor.fetchall()
                                if len(j) == 0:
                                    j = mycursor.execute(
                                        "SELECT ad_number FROM ads WHERE ad LIKE \'%s\' ORDER BY date DESC" % (
                                                    a[0] + '%'))
                                    j = mycursor.fetchall()
                                    if len(j) == 0:
                                        j = mycursor.execute("SELECT * FROM ads WHERE ad_type LIKE 'ws%'")
                                        j = mycursor.fetchall()
                                        k = mycursor.execute("SELECT * FROM ads WHERE user_id= \"%s\"" % ("@" + a[1]))
                                        k = mycursor.fetchall()
                                        ad_number = str(len(j) + 1) + "&" + str(len(k) + 1)
                                        mark = InlineKeyboardMarkup([
                                            [InlineKeyboardButton("انجام این پروژه",
                                                                  url=f"https://telegram.me/onprojbot?start={'2' + str(len(j) + 1) + '111111111101111111111' + str(len(k) + 1)}")]
                                        ])
                                        mycursor.execute(
                                            "INSERT INTO ads VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" %
                                            (ad_number, "@" + a[1], "ws2", "", "", a[0],
                                             "...", "paid", "", "", date))
                                        b = bot_2.send_message("@onproj", f"""
📌 {a[0]}

💰Budget : ...

bot : @onprojbot
Channel : @onproj
""", reply_markup=mark)
                                        if len(i) != 0:
                                            mycursor.execute("DELETE FROM ads WHERE ad= \"%s\"" % (i[0][5]))
                                        ad = a[0] + "%" + str(m.message_id) + "%" + "None" + "%" + str(b.message_id)
                                        mycursor.execute(
                                            "UPDATE ads SET ad= \"%s\" WHERE ad_number= \"%s\"" % (ad, ad_number))
                                        '''print("222")'''
                                        z = "NO"
                                        break

                except Exception as e:
                    pass

        except Exception as e:
            pass

        # 3
        try:
            a = bot_3.get_history("@ProjectAcademy", limit=100)

            for m in a:
                a = m.text
                message_id = str(m.message_id)

                try:
                    x = ["آگهی منقضی شده", "#انجام_دهنده", "None", "FiNiShEd", "Paid Intermediation", "Posted Ad",
                         "Paid Ad", "‼️", "💰", "👋🏻", "❌", "⭕️", "✅", "🇮🇷", "⚠️", "❕", "⛔️", "❤️", "⬅️", "‼️", "^", "*",
                         "$", "!", "&", "%", "/"]
                    for n in x:
                        if n in a:
                            y = "NO"
                            break
                        else:
                            y = "YES"
                    if y == "YES":
                        if z == "YES" and date >= date_2:
                            if "@ProjectAcademy" in a:
                                if "فوری" in a:
                                    a = a.replace("فوری", "")
                                a = a.split("📌")[1].replace("----------------------", "").replace("@ProjectAcademy",
                                                                                                  "").replace("🌎 ",
                                                                                                              "").split(
                                    "@")
                                a[0] = a[0].strip()
                                a[1] = a[1].strip()
                                j = mycursor.execute(
                                    "SELECT ad_number FROM ads WHERE ad_type= \"%s\" AND ad LIKE \'%s\' ORDER BY date DESC" % (
                                    "ws3", '%' + message_id + '%'))
                                j = mycursor.fetchall()
                                if len(j) == 0:
                                    j = mycursor.execute(
                                        "SELECT ad_number FROM ads WHERE ad LIKE \'%s\' ORDER BY date DESC" % (
                                                    a[0] + '%'))
                                    j = mycursor.fetchall()
                                    if len(j) == 0:
                                        j = mycursor.execute("SELECT * FROM ads WHERE ad_type LIKE 'ws%'")
                                        j = mycursor.fetchall()
                                        k = mycursor.execute("SELECT * FROM ads WHERE user_id= \"%s\"" % ("@" + a[1]))
                                        k = mycursor.fetchall()
                                        ad_number = str(len(j) + 1) + "&" + str(len(k) + 1)
                                        mark = InlineKeyboardMarkup([
                                            [InlineKeyboardButton("انجام این پروژه",
                                                                  url=f"https://telegram.me/onprojbot?start={'2' + str(len(j) + 1) + '111111111101111111111' + str(len(k) + 1)}")]
                                        ])
                                        mycursor.execute(
                                            "INSERT INTO ads VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" %
                                            (ad_number, "@" + a[1], "ws3", "", "", a[0],
                                             "...", "paid", "", "", date))
                                        b = bot_2.send_message("@onproj", f"""
📌 {a[0]}

💰Budget : ...

bot : @onprojbot
Channel : @onproj
""", reply_markup=mark)
                                        if len(i) != 0:
                                            mycursor.execute("DELETE FROM ads WHERE ad= \"%s\"" % (i[0][5]))
                                        ad = a[0] + "%" + str(m.message_id) + "%" + "None" + "%" + str(b.message_id)
                                        mycursor.execute(
                                            "UPDATE ads SET ad= \"%s\" WHERE ad_number= \"%s\"" % (ad, ad_number))
                                        '''print("333")'''
                                        z = "NO"
                                        break

                except Exception as e:
                    pass

        except Exception as e:
            pass

    except Exception as e:
        pass


def job_2():
    try:
        i = mycursor.execute("SELECT * FROM ads WHERE freelancer LIKE '\$$$%\' ORDER BY date ASC")
        i = mycursor.fetchall()

        with bot_3:
            with bot_2:
                v = "YES"

                if len(i) != 0:

                    for m in range(0, len(i)):

                        try:

                            for n in ["$2$", "$3$"]:
                                if n in i[m][8]:
                                    z = "NO"
                                    break
                                else:
                                    z = "YES"

                            if z == "YES":
                                if "!%%%" not in i[m][8]:
                                    u = bot_3.send_message(i[m][1], f"""
سلام دوست عزیز برای ارتباط با انجام دهنده روی گزینه پی وی انجام دهنده بزنید 🤝

تا بتونید در صورت توافق ، از واسطه گری خودکار استفاده کنید جهت جلوگیری از کلاهبرداری 🙏

bot : @onprojbot
Channel : @onproj
""")

                                for n in i[m][8].split("%%%")[:-1]:

                                    try:
                                        if n[-1] != "!":
                                            a = n.split("%")[0].replace("$1$", "").replace("$$$", "").replace("!", "")
                                            b = n.split("%")[1]
                                            c = n.split("%")[2]
                                            mark = InlineKeyboardMarkup([
                                                [InlineKeyboardButton('پی وی انجام دهنده',
                                                                      url=f"https://telegram.me/onprojbot?start={'3' + i[0][0].replace('&', '111111111101111111111')}")]
                                            ])
                                            j = mycursor.execute(
                                                "SELECT * FROM freelancers WHERE user_id= \"%s\"" % (a))
                                            j = mycursor.fetchall()
                                            if "%" in j[0][7]:
                                                e = bot_2.send_message(-1001531714907, f"""
📌 {i[m][5].split("%")[0]}

📝 {b}

<strong>Offer : {c}</strong>
""", reply_markup=mark)
                                            else:
                                                e = bot_2.send_message(-1001531714907, f"""
📌 {i[m][5].split("%")[0]}

📝 {b}

📋 {j[0][5].split("%")[0]}

Linkedin : {j[0][6]}
Online Project Score : {j[0][7].replace("%", "")}

<strong>Offer : {c}</strong>
""", reply_markup=mark)
                                            bot_3.forward_messages(
                                                chat_id=i[m][1],
                                                from_chat_id=-1001531714907,
                                                message_ids=e.message_id
                                            )
                                            i = mycursor.execute(
                                                "SELECT * FROM ads WHERE ad_number= \"%s\"" % (i[m][0]))
                                            i = mycursor.fetchall()
                                            mycursor.execute(
                                                "UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (
                                                "$1$" + i[m][8].replace(n, n + "!").replace("$1$", "").replace("$$$",
                                                                                                               ""),
                                                i[m][0]))
                                            v = "NO"

                                    except Exception as e:
                                        if str(e) == 'Telegram says: [400 MESSAGE_ID_INVALID] - The message id is invalid (caused by "messages.ForwardMessages")':
                                            bot_3.delete_messages(chat_id="me", message_ids=int(u.message_id))

                        except Exception as e:
                            if len(i) != 0:
                                if "$1$" in i[m][8]:
                                    mycursor.execute("UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (
                                    i[m][8].replace("$1$", ""), i[m][0]))

        with bot_4:
            with bot_2:

                if v == "YES":

                    if len(i) != 0:

                        for m in range(0, len(i)):

                            try:

                                for n in ["$1$", "$3$"]:
                                    if n in i[m][8]:
                                        z = "NO"
                                        break
                                    else:
                                        z = "YES"

                                if z == "YES":

                                    if "!%%%" not in i[m][8]:
                                        u = bot_4.send_message(i[m][1], f"""
سلام دوست عزیز برای ارتباط با انجام دهنده روی گزینه پی وی انجام دهنده بزنید 🤝

تا بتونید در صورت توافق ، از واسطه گری خودکار استفاده کنید جهت جلوگیری از کلاهبرداری 🙏

bot : @onprojbot
Channel : @onproj
""")

                                    for n in i[m][8].split("%%%")[:-1]:

                                        try:
                                            if n[-1] != "!":
                                                a = n.split("%")[0].replace("$2$", "").replace("$$$", "").replace("!",
                                                                                                                  "")
                                                b = n.split("%")[1]
                                                c = n.split("%")[2]
                                                mark = InlineKeyboardMarkup([
                                                    [InlineKeyboardButton('پی وی انجام دهنده',
                                                                          url=f"https://telegram.me/onprojbot?start={'3' + i[0][0].replace('&', '111111111101111111111')}")]
                                                ])
                                                j = mycursor.execute(
                                                    "SELECT * FROM freelancers WHERE user_id= \"%s\"" % (a))
                                                j = mycursor.fetchall()
                                                if "%" in j[0][7]:
                                                    e = bot_2.send_message(-1001531714907, f"""
📌 {i[m][5].split("%")[0]}

📝 {b}

<strong>Offer : {c}</strong>
""", reply_markup=mark)
                                                else:
                                                    e = bot_2.send_message(-1001531714907, f"""
📌 {i[m][5].split("%")[0]}

📝 {b}

📋 {j[0][5].split("%")[0]}

Linkedin : {j[0][6]}
Online Project Score : {j[0][7].replace("%", "")}

<strong>Offer : {c}</strong>
""", reply_markup=mark)
                                                bot_4.forward_messages(
                                                    chat_id=i[m][1],
                                                    from_chat_id=-1001531714907,
                                                    message_ids=e.message_id
                                                )
                                                i = mycursor.execute(
                                                    "SELECT * FROM ads WHERE ad_number= \"%s\"" % (i[m][0]))
                                                i = mycursor.fetchall()
                                                mycursor.execute(
                                                    "UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (
                                                    "$2$" + i[m][8].replace(n, n + "!").replace("$2$", "").replace(
                                                        "$$$", ""), i[m][0]))
                                                v = "NO"

                                        except Exception as e:
                                            if str(e) == 'Telegram says: [400 MESSAGE_ID_INVALID] - The message id is invalid (caused by "messages.ForwardMessages")':
                                                bot_4.delete_messages(chat_id="me", message_ids=int(u.message_id))

                            except Exception as e:
                                if len(i) != 0:
                                    if "$2$" in i[m][8]:
                                        mycursor.execute("UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (
                                        i[m][8].replace("$2$", ""), i[m][0]))

        with bot_5:
            with bot_2:

                if v == "YES":

                    if len(i) != 0:

                        for m in range(0, len(i)):

                            try:

                                for n in ["$1$", "$2$"]:
                                    if n in i[m][8]:
                                        z = "NO"
                                        break
                                    else:
                                        z = "YES"

                                if z == "YES":

                                    if "!%%%" not in i[m][8]:
                                        u = bot_5.send_message(i[m][1], f"""
سلام دوست عزیز برای ارتباط با انجام دهنده روی گزینه پی وی انجام دهنده بزنید 🤝

تا بتونید در صورت توافق ، از واسطه گری خودکار استفاده کنید جهت جلوگیری از کلاهبرداری 🙏

bot : @onprojbot
Channel : @onproj
""")

                                    for n in i[m][8].split("$")[-1].split("%%%")[:-1]:

                                        try:
                                            if n[-1] != "!":
                                                a = n.split("%")[0].replace("$3$", "").replace("$$$", "").replace("!",
                                                                                                                  "")
                                                b = n.split("%")[1]
                                                c = n.split("%")[2]
                                                mark = InlineKeyboardMarkup([
                                                    [InlineKeyboardButton('پی وی انجام دهنده',
                                                                          url=f"https://telegram.me/onprojbot?start={'3' + i[0][0].replace('&', '111111111101111111111')}")]
                                                ])
                                                j = mycursor.execute(
                                                    "SELECT * FROM freelancers WHERE user_id= \"%s\"" % (a))
                                                j = mycursor.fetchall()
                                                if "%" in j[0][7]:
                                                    e = bot_2.send_message(-1001531714907, f"""
📌 {i[m][5].split("%")[0]}

📝 {b}

<strong>Offer : {c}</strong>
""", reply_markup=mark)
                                                else:
                                                    e = bot_2.send_message(-1001531714907, f"""
📌 {i[m][5].split("%")[0]}

📝 {b}

📋 {j[0][5].split("%")[0]}

Linkedin : {j[0][6]}
Online Project Score : {j[0][7].replace("%", "")}

<strong>Offer : {c}</strong>
""", reply_markup=mark)
                                                bot_5.forward_messages(
                                                    chat_id=i[m][1],
                                                    from_chat_id=-1001531714907,
                                                    message_ids=e.message_id
                                                )
                                                i = mycursor.execute(
                                                    "SELECT * FROM ads WHERE ad_number= \"%s\"" % (i[m][0]))
                                                i = mycursor.fetchall()
                                                mycursor.execute(
                                                    "UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (
                                                    "$3$" + i[m][8].replace(n, n + "!").replace("$3$", "").replace(
                                                        "$$$", ""), i[m][0]))

                                        except Exception as e:
                                            if str(e) == 'Telegram says: [400 MESSAGE_ID_INVALID] - The message id is invalid (caused by "messages.ForwardMessages")':
                                                bot_5.delete_messages(chat_id="me", message_ids=int(u.message_id))

                            except Exception as e:
                                if len(i) != 0:
                                    if "$3$" in i[m][8]:
                                        mycursor.execute("UPDATE ads SET freelancer= \"%s\" WHERE ad_number= \"%s\"" % (
                                        i[m][8].replace("$3$", ""), i[m][0]))

    except Exception as e:
        pass


schedule.every(1).seconds.do(job)
schedule.every(1).seconds.do(job_2)
count = 0
while 1:
    count += 1
    '''print(count)'''
    schedule.run_pending()
    time.sleep(15)
