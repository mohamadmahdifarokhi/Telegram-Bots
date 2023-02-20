import re
import time
from abc import ABC
from datetime import datetime

import jdatetime
from pyrogram import *
import psycopg2
import psycopg2.extras
from psycopg2._psycopg import connection, cursor
import pyromod.listen
from pyrogram import *
from pyrogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, \
    KeyboardButton

bot = Client(name="vpn",
             api_id=0,
             api_hash="",
             bot_token="")


class DBModel(ABC):
    TABLE: str
    PK: str

    def __str__(self) -> str:
        return f"<{self.__class__.__name__} {vars(self)}>"


class DBManager:
    HOST = "localhost"
    USER = "postgres"
    PORT = 5432
    PASSWORD = "1381"

    def __init__(self, database, user=USER, host=HOST, port=PORT, password=PASSWORD) -> None:
        self.database = database
        self.user = user
        self.host = host
        self.port = port
        self.password = password
        self.conn: connection = \
            psycopg2.connect(dbname=self.database, user=self.user, host=self.host, port=self.port, password=password)

    def __del__(self):
        self.conn.close()

    def __get_cursor(self) -> cursor:
        return self.conn.cursor()

    def create(self, model_instance: DBModel):
        with self.conn:
            assert isinstance(model_instance, DBModel)
            curs = self.__get_cursor()
            model_vars = vars(model_instance)
            model_fields_str = []
            for i in model_vars.keys():
                if i[0] == "_":
                    model_fields_str.append(i[1:])
                else:
                    model_fields_str.append(i)
            model_fields_str = ",".join(
                model_fields_str)
            model_values_str = ",".join(["%s"] * len(model_vars))
            model_values_tuple = tuple(model_vars.values())
            with curs:
                a = curs.execute(
                    f"""INSERT INTO {model_instance.TABLE}({model_fields_str}) VALUES ({model_values_str})
                     RETURNING ID;""", model_values_tuple)
                res = curs.fetchone()
                return res

    def read_user(self, model_class: type, col: str, value: int):
        assert issubclass(model_class, DBModel)
        with self.conn:
            curs = self.__get_cursor()
            with curs:
                curs.execute(f"""SELECT * FROM {model_class.TABLE} WHERE {col} = '{value}' """)
                res = curs.fetchall()
                return res

    def read_order(self, model_class: type, order_id: int):
        assert issubclass(model_class, DBModel)
        with self.conn:
            curs = self.__get_cursor()
            with curs:
                curs.execute(f"""SELECT * FROM {model_class.TABLE} WHERE id = '{order_id}' """)
                res = curs.fetchall()
                return res

    def read_all(self, model_class: type):
        assert issubclass(model_class, DBModel)
        with self.conn:
            curs = self.__get_cursor()
            with curs:
                curs.execute(f"""SELECT * FROM {model_class.TABLE}""")
                res = curs.fetchall()
                return res

    def read_one(self, model_class: type, col: str, value: str):
        assert issubclass(model_class, DBModel)
        with self.conn:
            curs = self.__get_cursor()
            with curs:
                curs.execute(f"""SELECT * FROM {model_class.TABLE} WHERE {col} = '{value}' """)
                res = curs.fetchone()
                return res

    def read_all_one(self, model_class: type, col: str, value: str):
        assert issubclass(model_class, DBModel)
        with self.conn:
            curs = self.__get_cursor()
            with curs:
                curs.execute(f"""SELECT * FROM {model_class.TABLE} WHERE {col} = '{value}' """)
                res = curs.fetchall()
                return res

    def update_order_mi(self, model_class: type, order_id: int, mi: int):
        assert issubclass(model_class, DBModel)
        with self.conn:
            curs = self.__get_cursor()
            with curs:
                curs.execute(f"""UPDATE {model_class.TABLE} SET message_id = '{mi}' WHERE id = '{order_id}' """)
                # res = curs.fetchall()
                # return res

    def delete(self, model_instance: DBModel, pk: str):
        assert issubclass(model_instance, DBModel)
        with self.conn:
            curs = self.__get_cursor()
            with curs:
                curs.execute(f"""DELETE FROM {model_instance.TABLE} WHERE {model_instance.PK} = '{pk}'""")


db = DBManager(database="v2ray")


class User(DBModel):
    TABLE = 'users'
    PK = 'id'

    def __init__(self, user_id: int, user_name: str, date: jdatetime.datetime):
        self.user_id = user_id
        self.user_name = user_name
        self.date = date
        db.create(self)


class Order(DBModel):
    TABLE = 'orders'
    PK = 'id'

    def __init__(self, user_id: int, server_id: int,
                 price: int, month: int, expiration_date: jdatetime.datetime,
                 date: jdatetime.datetime, pay: bool = None, status: bool = None):
        self.user_id = user_id
        self.server_id = server_id
        self.price = price
        self.month = month
        self.expiration_date = expiration_date
        self.date = date
        self.pay = pay
        self.status = status
        dba = db.create(self)

        self.id = dba[0]

    def get_id(self):
        return self.id


class Server(DBModel):
    TABLE = 'servers'
    PK = 'id'

    def __init__(self, name: str, price: int, month: int, date: jdatetime.datetime):
        self.name = name
        self.price = price
        self.month = month
        self.date = date
        db.create(self)


mark = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton("سرویس ها"), KeyboardButton("خرید سرویس")],
    [KeyboardButton("تعرفه ها"), KeyboardButton("راهنمای اتصال")],
    [KeyboardButton("پشتیبانی")],
], resize_keyboard=True)


@bot.on_callback_query()
async def answer(client, call):
    if call.data == "membership":
        user_id = call.from_user.id
        user_name = call.from_user.username
        first_name = call.from_user.first_name
        message_id = call.message.id

        try:
            await bot.get_chat_member("@tahrimgozarchannel", user_id)
            if db.read_one(User, "user_id", user_id):
                await bot.edit_message_text(user_id, message_id, 'عضویت تایید شد برای ادامه از منو استفاده کنید 🤝')
            else:
                mark = ReplyKeyboardMarkup(keyboard=[
                    [KeyboardButton("سرویس ها"), KeyboardButton("خرید سرویس")],
                    [KeyboardButton("تعرفه ها"), KeyboardButton("راهنمای اتصال")],
                    [KeyboardButton("پشتیبانی")],
                ], resize_keyboard=True)
                await bot.edit_message_text(user_id, message_id, f"""
    سلام <strong>{first_name}</strong> 👋
    به بات <strong>VPN CLUB</strong> خوش اومدی

    برای ادامه میتونی از دکمه های زیر استفاده کنی :

    """, reply_markup=mark)
                User(user_id, user_name, jdatetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))



        except:
            pass

    elif "protocol" in call.data:
        user_id = call.from_user.id
        user_name = call.from_user.username
        first_name = call.from_user.first_name
        message_id = call.message.id
        server_id = call.data.split("-")[1]

        protocols = db.read_all_one(Protocol, "server_id", server_id)

        prs = []
        for protocol in protocols:
            print(protocol)
            prs.append([InlineKeyboardButton(f"{protocol[2]} - {protocol[3]}G - {protocol[4]}T",
                                             callback_data=f"pay-{protocol[0]}")])

        print(prs)
        mark = InlineKeyboardMarkup(prs)

        print(user_id, message_id)
        await bot.edit_message_text(user_id, message_id, "پروتکلی که میخواین رو انتخاب کنید",
                                    reply_markup=mark)

    elif "month" in call.data:
        server_name = call.data.split("-")[1]
        user_id = call.from_user.id
        user_name = call.from_user.username
        first_name = call.from_user.first_name
        message_id = call.message.id

        servers = db.read_all_one(Server, 'name', server_name)

        months = []
        for server in servers:
            months.append([InlineKeyboardButton(f"{server[2]} ماه ", callback_data=f"protocol-{server[0]}")])

        mark = InlineKeyboardMarkup(months)

        await bot.edit_message_text(user_id, message_id, "مدت زمان سرویس رو انتخاب کنید",
                                    reply_markup=mark)

    elif "pay" in call.data:
        protocol_id = call.data.split("-")[1]
        user_id = call.from_user.id
        user_name = call.from_user.username
        first_name = call.from_user.first_name
        message_id = call.message.id
        date = jdatetime.datetime.now()

        mark = InlineKeyboardMarkup([
            [InlineKeyboardButton("پرداخت", url='www.google.com')],
        ])

        user = db.read_one(User, 'user_id', user_id)
        protocol = db.read_one(Protocol, 'id', protocol_id)
        server = db.read_one(Server, 'id', protocol[1])
        print(protocol)
        await bot.edit_message_text(user_id, message_id, f"""
فاکتور پرداخت شما :

پروتکل : {protocol[2]}
حجم سرویس : {protocol[3]}   گیگ
مدت سرویس : {server[2]} ماه
شماره پیگیری : <code>{protocol[0]}</code>

مبلغ سرویس : {protocol[4]} تومان
""",
                                    reply_markup=mark)

        end_date = date + jdatetime.timedelta(days=server[2] * 30)

        Order(user[0], protocol[0], protocol[3], protocol[4], message_id,
              date.strftime("%Y-%m-%d %H:%M:%S"),
              end_date.strftime("%Y-%m-%d %H:%M:%S"), None, None)


    elif "extension" in call.data:
        user_id = call.from_user.id
        user_name = call.from_user.username
        first_name = call.from_user.first_name
        message_id = call.message.id
        order_id = call.data.split("-")[1]

        mark = InlineKeyboardMarkup([
            [InlineKeyboardButton("پرداخت", url='www.google.com')],
        ])

        # user = db.read_one(User, 'user_id', user_id)
        order = db.read_all_one(Order, "id", order_id)[0]

        print(order)

        protocol = db.read_one(Protocol, 'id', order[2])

        day = str(order[-1] - order[-2] - jdatetime.timedelta(days=1)).split(" ")[0]

        await bot.edit_message_text(user_id, message_id, f"""
تمدید سرویس :

پروتکل : {protocol[2]}
حجم سرویس :{protocol[3]}گیگ
مدت سرویس : {day} روز
شماره پیگیری : <code>{protocol[0]}</code>

مبلغ سرویس : {protocol[4]} تومان
""",
                                    reply_markup=mark)


async def start(client, message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    date = jdatetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Server("usa", 1, date)
    # Server("usa", 2, date)
    # Server("uk", 2, date)
    #
    # Protocol(3, "vmess", 20, 30000, date=date)
    # Protocol(3, "vless", 30, 50000, date=date)
    # Protocol(2, "vless", 40, 100000, date=date)

    try:
        try:
            user_name = message.from_user.username
        except:
            user_name = None

        User(user_id, user_name, jdatetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        await bot.send_message(user_id, f"""
سلام <strong>{first_name}</strong> 👋
به بات <strong>VPN CLUB</strong> خوش اومدی

برای ادامه میتونی از دکمه های زیر استفاده کنی :

""", reply_markup=mark)

    except Exception as e:
        await bot.send_message(user_id, "لطفا از منو استفاده کن")


async def buy(client, message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name

    try:
        # user = db.read_one(User, "user_id", user_id)

        # order = Order(user_id=user[0], start_date=jdatetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        servers = []
        server_names = []
        for server in db.read_all(Server):
            if server[1] not in server_names:
                server_names.append(server[1])
                servers.append([InlineKeyboardButton(server[1], callback_data=f"month-{server[1]}")])

        mark = InlineKeyboardMarkup(servers)

        await bot.send_message(user_id, "سرور مورد نظر رو انتخاب کنید",
                               reply_markup=mark)

    except Exception as e:
        await bot.send_message(user_id, "لطفا از منو استفاده کن")


async def services(client, message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name

    try:
        print('a')
        user = db.read_one(User, "user_id", user_id)

        orders = db.read_all_one(Order, "user_id", user[0])

        print(orders)

        if len(orders) != 0:
            print('sdf')
            ods = []
            for order in orders:
                print(order)

                if order[6] == True:
                    protocol = db.read_one(Protocol, "id", order[2])
                    server = db.read_one(Server, "id", protocol[1])
                    print(protocol)
                    ods.append([
                        InlineKeyboardButton(f"{protocol[2]}", callback_data='None'),
                        InlineKeyboardButton(f"{protocol[3]}G", callback_data='None'),
                        InlineKeyboardButton(f"{protocol[4]}T", callback_data='None'),
                        InlineKeyboardButton(f"{server[2]}M", callback_data='None'),
                        InlineKeyboardButton("فعال", callback_data='None')
                    ])

                elif order[6] == False:
                    protocol = db.read_one(Protocol, "id", order[2])
                    server = db.read_one(Server, "id", protocol[1])
                    ods.append([
                        InlineKeyboardButton(f"{protocol[2]}", callback_data='None'),
                        InlineKeyboardButton(f"{order[3]}G", callback_data='None'),
                        InlineKeyboardButton(f"{order[4]}T", callback_data='None'),
                        InlineKeyboardButton(f"{server[2]}M", callback_data='None'),
                        InlineKeyboardButton("تمدید", callback_data=f'extension-{order[0]}')
                    ])
                else:
                    pass

            print(ods)

            if len(ods) != 0:

                mark = InlineKeyboardMarkup(ods)

                await bot.send_message(user_id, "سرویس ها",
                                       reply_markup=mark)
            else:
                await bot.send_message(user_id, "شما سرویسی ندارید")

        else:
            await bot.send_message(user_id, "شما سرویسی ندارید")

    except Exception as e:
        print(e)
        await bot.send_message(user_id, "لطفا از منو استفاده کن")


async def guide(client, message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name

    try:
        await bot.send_message(user_id, """
ios :

napsternet : https://apps.apple.com/us/app/napsternetv/id1629465476
fairvpn : https://apps.apple.com/us/app/fair-vpn/id1533873488

android :

v2raying : https://play.google.com/store/apps/details?id=com.v2ray.ang&hl=en_US&gl=US
onclick : https://play.google.com/store/apps/details?id=earth.oneclick&hl=fa&gl=US

windows :

v2rayncore : https://github.com/v2fly/v2ray-core/releases/download/v4.31.0/v2ray-windows-64.zip
""", reply_markup=mark)

    except Exception as e:
        await bot.send_message(user_id, "لطفا از منو استفاده کن")


async def Tariffs(client, message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name

    try:

        servers = db.read_all(Server)

        t = ""
        for server in servers:
            text = f" سرور {server[1]}" + "\n" + f"{server[2]} ماهه"
            protocols = db.read_all_one(Protocol, 'server_id', server[0])
            for protocol in protocols:
                text += f"\n\n{protocol[2]} - {protocol[3]}G - {protocol[4]}T"

            if len(protocols) != 0:
                t += text
                t += "\n\n"

        await bot.send_message(user_id, t, reply_markup=mark)


    except Exception as e:
        print(e)
        await bot.send_message(user_id, "لطفا از منو استفاده کن")


async def support(client, message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name

    try:
        a = await bot.ask(user_id, "پیام خود را تایپ کنید")

        if a.text:
            a = await bot.send_message(user_id, "متن شما دریافت شد و به زودی پاسخ رو دریافت خواهید کرد")


    except Exception as e:
        await bot.send_message(user_id, "لطفا از منو استفاده کن")


@bot.on_message(filters.private)
async def main(client, message):
    try:
        user_id = message.from_user.id
        text = message.text

        try:

            await bot.get_chat_member("@vpnclubd", user_id)

            if text == "/start":
                await start(client, message)

            elif text == "خرید سرویس":
                await buy(client, message)

            elif text == "سرویس ها":
                await services(client, message)

            elif text == "راهنمای اتصال":
                await guide(client, message)

            elif text == "تعرفه ها":
                await Tariffs(client, message)

            elif text == "پشتیبانی":
                await support(client, message)

            else:
                await bot.send_message(user_id, "لطفا از منو استفاده کن")

        except Exception as e:
            print(e)
            mark = InlineKeyboardMarkup([
                [InlineKeyboardButton("عضویت", url="https://t.me/vpnclubd")],
                [InlineKeyboardButton("تایید عضویت", callback_data='membership')]
            ])

            await bot.send_message(user_id, "کاربر گرامی برای استفاده از بات لازمه اول تو کانال عضو باشی 🤝",
                                   reply_markup=mark)

    except Exception as e:
        print(e)
        await bot.send_message(user_id, "لطفا از منو استفاده کن")


@bot.on_message(filters.chat(-1001750696948))
async def main2(client, message):
    try:
        text = message.text

        if "Order Id" in text:
            pattern = re.compile(r'(Id)\s\W\s\d{1,4}\b')
            result = pattern.search(text)
            order_id = result.group(0).split(' : ')[-1]
            order = db.read_order(Order, order_id)
            user = db.read_user(User, 'id', order[0][1])

        await bot.edit_message_text(user[0][1], order[0][-2], "پرداخت شد")
    except Exception as e:
        print(e)
        pass


bot.run()
