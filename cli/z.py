from email import message
import imp
from pydoc import text
from pyrogram import Client,filters,types
from pyrogram.types import Message
from pyrogram.raw import functions
from pyrogram.types import *
import schedule
import time
import mysql.connector
from pyrogram.types.inline_mode import inline_query, inline_query_result, inline_query_result_article
import schedule
import time
import jdatetime
from datetime import timedelta,datetime
import imp

bot= Client(session_name="online_project",
            api_id= 0,
            api_hash= "")


'''@bot_444.on_message()
def test(client,m:Message):
    if m.text==".":
        first_name= m.from_user.first_name
        m.reply(f'سلامز {first_name}')'''

'''with bot:
    def job():
        print('a')
        bot.start()
        date= jdatetime.datetime.now().strftime("%H %M")
        bot.send(
        functions.account.UpdateProfile(
            about= date))
        bot.stop()'''



'''with bot:
    def g():
        bot.start()
        bot.send_message("@lllIIIIIlIIIIIlll","هزینه پیشنهادی")
g()'''
'''
with bot:
    bot.send(
        functions.account.UpdateProfile(
            first_name='Mt',
            last_name=''))'''
    
'''    mark= ReplyKeyboardMarkup(keyboard= [
        [KeyboardButton("لغو")]
        ],resize_keyboard= True)
    bot.send_message(1296441026,'123')'''
    
with bot:
    count=0
    for i in bot.iter_chat_members('@onlineprojchannel'):
        count+=1
        try:
            mycursor.execute("INSERT INTO user VALUES(\"%d\")"%(i.user.id))
            print(count)
        except:
            pass
      

chat_members = bot.get_chat_members("@onlineprojchannel",limit= 1000)

with bot:
    mycursor.execute("SELECT d FROM user")
    j= mycursor.fetchall()

    count=0
    for i in j:
        print(i[0],' ',count)
        count+=1
        
        bot.send(
            functions.channels.InviteToChannel(
            channel=bot.resolve_peer('@testchz'),
            users=[bot.resolve_peer(i[0])]))
        print(count)


'''
count=0
while 1:
    count+= 1
    print(count)
    schedule.run_pending()
    time.sleep(1)'''

bot_444.run()