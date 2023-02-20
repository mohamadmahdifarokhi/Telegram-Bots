from pyrogram import *
from pyrogram.types import *
from pyrogram.raw import functions
import pyromod.listen
import mysql.connector
import time
import schedule
import jdatetime
from datetime import timedelta,datetime

bot= Client(session_name="Time",
            api_id= 0,
            api_hash= "")

def job():
    with bot:
        date= jdatetime.datetime.now().strftime("%S")
        if date== "00":
            try:
                date= jdatetime.datetime.now().strftime("%H : %M")
                bot.send(
                functions.account.UpdateProfile(
                    about= date))
            except:
                pass

schedule.every(1).seconds.do(job)
count=0
while 1:
    count+= 1
    schedule.run_pending()
    time.sleep(1)