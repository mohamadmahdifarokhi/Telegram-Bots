from pyrogram import *
import mysql.connector

bot_33= Client(session_name="online_project_33",
            api_id= 0,
            api_hash= "")

mydb= mysql.connector.connect(
host= "localhost",
user= "root",
password= "",
database= "online_project")
mycursor= mydb.cursor()

'''mydb= mysql.connector.connect(
host= "localhost",
user= "onprojir_mt",
password= "3910844000lte000",
database= "onprojir_onproj")
mycursor= mydb.cursor()'''

@bot_33.on_message(filters.private)
async def main(client,message):
    text= message.text

    if text== ".":

        try:
            user_id= message.from_user.id
            user_name= message.from_user.username
            i= mycursor.execute("SELECT * FROM ads WHERE user_id= \"%s\" ORDER BY date DESC"%("@"+user_name))
            i= mycursor.fetchall()

            a= "NO"

            for m in range (0,len(i)):
                if "FiNiShEd" not in i[m][5]:
                    a= "YES"
                    mycursor.execute("UPDATE ads SET ad= \"%s\",user_id= \"%s\" WHERE ad_number= \"%s\""%(i[m][5]+"%"+"!FiNiShEd",str(user_id),i[m][0]))

            if a== "YES":
                await bot_33.send_message(user_id,"تایید شد")

        except Exception as e:
            pass

mycursor.close
mydb.close
bot_33.run()

