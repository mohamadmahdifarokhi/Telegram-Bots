from datetime import timedelta
from os import close
import re
from pyrogram import *
from pyrogram.methods.messages import edit_message_text
from pyrogram.types import *
import mysql.connector
from pyrogram.types.inline_mode import inline_query, inline_query_result, inline_query_result_article
from pyrogram.types.messages_and_media import message
import pyromod.listen
import jdatetime

bot= Client(session_name= "spender mom",
             api_id= 0,
             api_hash= "",
             bot_token= "5055888415:AAE8l1RqDq7o2U3cNVuFgFDr2cMez8ubKS0")

mydb= mysql.connector.connect(
host= "localhost",
user= "root",
password= "",
database= "spender_mom")
mycursor= mydb.cursor()

#..........answer........#

@bot.on_inline_query()
def answer(client, inline_query):
    user_id= inline_query.from_user.id
    text= inline_query.query
    mycursor.execute("SELECT * FROM lists WHERE user_id= %d ORDER BY date ASC"%(user_id))
    i= mycursor.fetchall()

    if text=='':
        inline_query.answer(results= [InlineQueryResultArticle(title= i[-1][1].replace('/*/*/'+str(user_id),''),input_message_content= InputTextMessageContent(i[-1][5]),
        description= i[-1][2],thumb_url= 'https://i.imgur.com/JyxrStE.png',reply_markup= InlineKeyboardMarkup([
        [InlineKeyboardButton('add',i[-1][1])]
        ]))],cache_time= 1)

    else:
        for j in range(-1,-len(i)-1,-1):
            name_list= i[j][1].split('/*/*/')[0]
            if text== name_list[:len(text)]:
                inline_query.answer(results= [InlineQueryResultArticle(title= name_list,input_message_content= InputTextMessageContent(i[j][5]),
                description= i[j][2],thumb_url= 'https://i.imgur.com/JyxrStE.png',reply_markup= InlineKeyboardMarkup([
                [InlineKeyboardButton('add',i[j][1])]
                ]))],cache_time= 1)

#..........call..........#

@bot.on_callback_query()
async def answerr(client,callback_query):
    if 'confirmation'== callback_query.data[-12:]:
        name= callback_query.data[:-12]
        name_list= callback_query.data[:-12].split('/*/*/')[0]
        user_id= callback_query.data[:-12].split('/*/*/')[1]
        message_id= callback_query.message.message_id
        mycursor.execute("SELECT * FROM lists WHERE name= \'%s\'"%(name))
        i= mycursor.fetchall()
        mark= InlineKeyboardMarkup([
        [InlineKeyboardButton('Send',switch_inline_query= name_list)],
        [InlineKeyboardButton('complete',name+'complete')]
        ])
        await bot.edit_message_text(i[0][0],message_id,i[0][5],reply_markup= mark)
        mycursor.execute("UPDATE lists SET  inline_message_id= \'%s\' WHERE name= \'%s\'"%(str(message_id)+' ',name))

    elif 'complete'== callback_query.data[-8:]:
            name= callback_query.data[:-8]
            name_list= name.split('/*/*/')[0]
            user_id_list= name.split('/*/*/')[1]
            message_id= callback_query.message.message_id
            mycursor.execute("SELECT * FROM lists WHERE name= \'%s\'"%(name))
            i= mycursor.fetchall()
            if i[0][7]== str(message_id)+' ':
                pass
            else:
                for j in i[0][7].split(' ')[1:-1]:
                    await bot.edit_inline_caption(j,i[0][5])
                await bot.edit_message_text(user_id_list,message_id,i[0][5])
                mycursor.execute("UPDATE lists SET  user_id= \'%s\' WHERE name= \'%s\'"%(i[0][0]+'complete',name))
                bot_cost= int(5000/len(i[0][6].split(' ')[:-1]))
                total_cost= int(i[0][3])+int(bot_cost)
                mark= InlineKeyboardMarkup([
                [InlineKeyboardButton('Payment',url= 'https://translate.google.com')]
                ])
                mycursor.execute("SELECT * FROM user WHERE user_id= \'%d\'"%(int(user_id_list)))
                iii= mycursor.fetchall()
                s=[]
                for k in (i[0][3],bot_cost,total_cost):
                    if  4 <=len(str(k))<= 6:
                        costt= str(k)[:-3]+','+str(k)[-3:]
                    elif  7 <=len(str(k))<= 9:
                        costt= str(k)[:-6]+','+str(k)[-6:-3]+','+str(k)[-3:]
                    elif  10 <=len(k)<= 12:
                        costt= str(k)[:-9]+','+str(k)[-9:-6]+','+str(k)[-6:-3]+','+str(k)[-3:]
                    s.append(costt)
                for j in i[0][6].split(' ')[:-1]:
                    await bot.send_message(int(j.split('@')[0]),f'''
List: {i[0][1].split('/*/*/')[0]}
List Owner: {iii[0][1]}
Cost: {s[0]} T
Bot Cost: {s[1]} T

Total Cost: {s[2]} T
''',reply_markup= mark)

    else:
        inline_message_id= callback_query.inline_message_id
        name= callback_query.data
        user_id_list= callback_query.data.split('/*/*/')[1]
        user_id= callback_query.from_user.id
        first_name= callback_query.from_user.first_name
        user_name= callback_query.from_user.username
         
        mycursor.execute("SELECT * FROM user WHERE user_id= \'%d\'"%(user_id))
        i= mycursor.fetchall()
        if len(i)!=0:
            mycursor.execute("SELECT inline_message_id FROM lists WHERE name= \'%s\'"%(name))
            i= mycursor.fetchall()
            if inline_message_id not in i[0][0] :
                mycursor.execute("UPDATE lists SET  inline_message_id = \'%s\' WHERE name = \'%s\'"%(i[0][0]+inline_message_id+' ',name))
            user_id= callback_query.from_user.id
            name_list= callback_query.data.split('/*/*/')[0]
            user_id_list= callback_query.data.split('/*/*/')[1]
            inline_message_id= callback_query.inline_message_id
            mycursor.execute("SELECT * FROM lists WHERE name= \'%s\'"%(name))
            i= mycursor.fetchall()
            if str(user_id)!= str(user_id_list) and 'complete' not in i[0][0] and str(user_id)+'@'+user_name+' ' not in i[0][6]:
                mycursor.execute("UPDATE lists SET  membership = \'%s\' WHERE name = \'%s\'"%(i[0][6]+str(user_id)+'@'+user_name+' ',name))
                mycursor.execute("SELECT membership FROM lists WHERE name= \'%s\'"%(name))
                ii= mycursor.fetchall()
                user= ii[0][0].split(' ')
                z= ''
                for j in range(0,len(user)-1):
                    a= '@'+user[j].split('@')[1]+' '
                    z+= a
                if  4 <=len(str(i[0][3]))<= 6:
                    costt= str(i[0][3])[:-3]+','+str(i[0][3])[-3:]
                elif  7 <=len(str(i[0][3]))<= 9:
                    costt= str(i[0][3])[:-6]+','+str(i[0][3])[-6:-3]+','+str(i[0][3])[-3:]
                elif  10 <=len(str(i[0][3]))<= 12:
                    costt= str(i[0][3])[:-9]+','+str(i[0][3])[-9:-6]+','+str(i[0][3])[-6:-3]+','+str(i[0][3])[-3:]
                mycursor.execute("UPDATE lists SET  list = \'%s\' WHERE name = \'%s\'"%(f'''
{name_list}

{i[0][2]}

برای عضویت اول بات رو استارت کن 
@spendermombot

{z}

cost {costt} T
''',name))
                mycursor.execute("SELECT * FROM lists WHERE name= \'%s\'"%(name))
                i= mycursor.fetchall()
                for j in i[0][7].split(' ')[1:-1]:
                    await bot.edit_inline_caption(j,i[0][5],reply_markup= InlineKeyboardMarkup([
                    [InlineKeyboardButton('add',name)]
                    ]))
                mark= InlineKeyboardMarkup([
                [InlineKeyboardButton('Send',switch_inline_query= name_list )],
                [InlineKeyboardButton('complete',name+'complete')]
                ])
                await bot.edit_message_text(user_id_list,int(i[0][7].split(' ')[0]),i[0][5],reply_markup= mark)

            else:
               pass
        else:
            pass
#..........start.........#

async def start(client, message):
    user_id= message.from_user.id
    user_name= message.from_user.username
    first_name= message.from_user.first_name
    date= jdatetime.datetime.now()

    try:
        mycursor.execute("INSERT INTO user VALUES (\'%d\',\'%s\',\'%s\',\'%s\')"%(user_id,'@'+user_name,first_name,jdatetime.datetime.now()))
    except:
        pass

    await bot.send_message(user_id,f"سلام {first_name}")

#..........new_list......#

async def new_list(client, message):
    user_id= message.from_user.id
    mark= ReplyKeyboardMarkup(keyboard= [
        [KeyboardButton("لغو")]
        ],resize_keyboard= True)

    count= 0  
    while True:
        count+= 1
        if count== 1:
            await bot.send_message(user_id,'اسم لیست (4.1)')
            name= await bot.ask(user_id,'پ.ن: تکراری نباشه',reply_markup= mark)
            mycursor.execute("SELECT * FROM lists WHERE name= \'%s\'"%(name.text+'/*/*/'+str(user_id)))
            i= mycursor.fetchall()
            if name.text== 'لغو':
                break
            elif len(i)== 0:
                if '/*/*/'+str(user_id) in name.text:
                    await bot.send_message(user_id,'اسم لیست مورد تایید نیست')
                else:
                    break
            else:
                await bot.send_message(user_id,'اسم لیست تکراریه')
        else:
            name= await bot.ask(user_id,'دوباره امتحان کن',reply_markup= mark)
            mycursor.execute("SELECT * FROM lists WHERE name= \'%s\'"%(name.text+'/*/*/'+str(user_id)))
            i= mycursor.fetchall()
            if name.text== 'لغو':
                break
            elif len(i)== 0:
                if '/*/*/'+str(user_id) in name.text:
                    await bot.send_message(user_id,'اسم لیست مورد تایید نیست')
                else:
                    break
            else:
                await bot.send_message(user_id,'اسم لیست تکراریه')
    
    if name.text!= 'لغو':
        description= await bot.ask(user_id,'توضیحات (4.2)',reply_markup= mark)

        count= 0 
        if description.text!= 'لغو':
            while True:
                count+= 1
                if count== 1:
                    try:
                        await bot.send_message(user_id,'سهم هر فرد به تومان (4.3)')
                        cost= await bot.ask(user_id,'نمونه: 50000',reply_markup= mark)
                        if cost.text== 'لغو':
                            break
                        elif cost.text== '/None':
                            break
                        elif 1000000000>int(cost.text)>10000:
                            break
                        elif 1000000000<int(cost.text):
                            await bot.send_message(user_id,'بیشتر از حد مجاز')
                        elif int(cost.text)<10000:
                            await bot.send_message(user_id,'کمتر از حد مجاز')
                    except:
                        await bot.send_message(user_id,'درست نیست')
                else:
                    try:
                        cost= await bot.ask(user_id,'دوباره امتحان کن',reply_markup= mark)
                        if cost.text== 'لغو':
                            break
                        elif cost.text== '/None':
                            break
                        elif 1000000000>int(cost.text)>10000:
                            break
                        elif 1000000000<int(cost.text):
                            await bot.send_message(user_id,'بیشتر از حد مجاز')
                        elif int(cost.text)<10000:
                            await bot.send_message(user_id,'کمتر از حد مجاز')
                    except:
                        await bot.send_message(user_id,'درست نیست')
            if  4 <=len(cost.text)<= 6:
                costt= cost.text[:-3]+','+cost.text[-3:]
            elif  7 <=len(cost.text)<= 9:
                costt= cost.text[:-6]+','+cost.text[-6:-3]+','+cost.text[-3:]
            elif  10 <=len(cost.text)<= 12:
                costt= cost.text[:-9]+','+cost.text[-9:-6]+','+cost.text[-6:-3]+','+cost.text[-3:]

            if cost.text!= 'لغو':
                count= 0 
                while True:
                    count+= 1
                    if count== 1:
                        await bot.send_message(user_id,'شماره کارت (4.4)')   
                        account_number= await bot.ask(user_id,'نمونه: 1234-1234-1234-1234',reply_markup= mark)
                        if account_number.text== 'لغو':  
                            break
                        else:
                            a= account_number.text.split('-')
                            count_2= 0
                            for i in a:
                                if len(i)== 4:
                                    count_2+= 1
                            if count_2== 4:
                                break
                            else:
                                await bot.send_message(user_id,'درست نیست')
                    else:
                        account_number= await bot.ask(user_id,'دوباره امتحان کن',reply_markup= mark)          
                        if account_number.text== 'لغو':
                            break
                        else:
                            a= account_number.text.split('-')
                            count_2= 0
                            for i in a:
                                if len(i)== 4:
                                    count_2+= 1
                            if count_2== 4:
                                break
                            else:
                                await bot.send_message(user_id,'درست نیست')
                if account_number.text!= 'لغو':
                    if cost.text!= '/None':
                        list= f'''
{name.text}

{description.text}

برای عضویت اول بات رو استارت کن 
@spendermombot

cost {costt} T
'''

                    mycursor.execute("INSERT INTO lists VALUES(\"%d\",\"%s\",\"%s\",\"%d\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")"
                    %(user_id,name.text+'/*/*/'+str(user_id),description.text,int(cost.text),account_number.text,
                    list,'','',jdatetime.datetime.now()))
                    await bot.send_message(user_id,f'''
Card Number : {account_number.text}
Card Number Name : ...
''',reply_markup= InlineKeyboardMarkup([[InlineKeyboardButton('confirmation',f'{name.text}/*/*/{str(user_id)}confirmation')]]))

#..........lists.........#

async def lists(client, message):
    user_id= message.from_user.id 
    text= message.text
    mycursor.execute("SELECT * FROM lists WHERE user_id= \'%s\' ORDER BY date ASC"%(user_id))
    i= mycursor.fetchall()
    z= []
    j= -1

    if len(i)== 0:
        await bot.send_message(user_id,"لیستی ساخته نشده")

    elif len(i)%2== 0:
        while j>=-len(i):
            a= [KeyboardButton(i[j-1][1].split('/*/*/')[0]),KeyboardButton(i[j][1].split('/*/*/')[0])]
            j-= 2
            z.append(a)
        mark= ReplyKeyboardMarkup(keyboard= z,resize_keyboard= True)
        await bot.send_message(user_id,"انتخاب کنید",reply_markup= mark)

    elif len(i)%2!= 0:
        while j>-len(i):
            a= [KeyboardButton(i[j-1][1].split('/*/*/')[0]),KeyboardButton(i[j][1].split('/*/*/')[0])]
            j-= 2
            z.append(a)
        z.append([KeyboardButton(i[0][1].split('/*/*/')[0])])
        mark= ReplyKeyboardMarkup(keyboard= z,resize_keyboard= True)
        await bot.send_message(user_id,"انتخاب کنید",reply_markup= mark)

#..........ins...........#

async def ins(client, message):
    pass

#..........que...........#

async def que(client, message):
    pass

#..........sup...........#

async def sup(client, message):
    pass

#..........mainp.........#

@bot.on_message()
async def main(client, message):
    user_id= message.from_user.id
    text= message.text

    if text== "/start":
        await start(client, message)

    elif text== "/new_list":
        await new_list(client, message)

    elif text== "/lists":
        await lists(client, message)

    elif text== "/instruction":
        await ins(client, message)

    elif text== "/questions":
        await que(client, message)

    elif text== "/support":
        await sup(client, message)

    else:
        await bot.send_message(user_id,'لطفا از منو استفاده کن')

mycursor.close
mydb.close
bot.run()