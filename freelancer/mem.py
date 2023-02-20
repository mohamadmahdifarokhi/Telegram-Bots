from pyrogram import *
from pyrogram.types import *
import pyromod.listen
import mysql.connector
import time
import schedule
import jdatetime
from datetime import timedelta,datetime

bot= Client(session_name= "sup",
            api_id=0,
            api_hash="")

'''bot= Client(session_name= "me",
            api_id= 0,
            api_hash= "")'''

mydb= mysql.connector.connect(
host= "localhost",
user= "root",
password= "",
database= "mem")
mycursor= mydb.cursor()

'''a= ""

count= 0
for i in a.split("\n"):
    count+= 1
    print(count)
    try:
        mycursor.execute("INSERT INTO user VALUES(\"%s\")"%(i.split(" @")[1].replace(" ","").replace(".","")))
    except Exception as e:
        print(count)
        print(e)
        pass'''

def job():
    with bot:
        count=0
        for i in bot.iter_chat_members('@divar_e_daneshjoo',limit= 100000):

            if i.user.status== "recently" and i.user.username!= None:
                try:
                    mycursor.execute("INSERT INTO user VALUES(\"%s\")"%(i.user.username))
                    bot.send_message(i.user.username,f"""
سلام ما تیم پروژه آنلاین هستیم

خوشحال میشیم دعوت مارو به چنل بپذیرید 🙏 

🟢 مزایای چنل برای فریلنسرها :

🚀 ذخیره رزومه فریلنسر در بات و ارسال اون به همراه پیام درخواست انجام پروژه به کارفرما

🚀 ارسال آگهی های مربوط به مهارت های انتخابی شما از طریق بات

🚀 استفاده از واسطه گری خودکار

🚀 امنیت در پرداخت

برای ثبت اطلاعاتتون می تونید وارد بات بشید و دستور freelancer/ رو بزنید

لطفا ما رو به دوستانتون هم معرفی کنید ❤️

bot : @onprojbot
Channel : @onproj
""")
                    ''' bot.forward_messages(
                        chat_id= i.user.username,
                        from_chat_id= -1001748468339,
                        message_ids= 9638
                        )'''
                    count+=1
                except Exception as e:
                    print(e)
                    if e== '''Telegram says: [400 PEER_FLOOD] - The method can't be used because your account is currently limited (caused by "messages.SendMessage")''':
                        break
                if count== 1:
                    break


schedule.every(1).seconds.do(job)
count=0
while 1:
    count+= 1
    '''print(count)'''
    schedule.run_pending()
    time.sleep(10)