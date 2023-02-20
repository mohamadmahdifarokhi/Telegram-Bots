# from glob import glob
# import os
import sqlite3

# import time
# import requests
# import subprocess
# import threading
# import schedule


# _max_allowed_connections = 3
# _user_last_id = 0
# _telegrambot_token = ''
# _telegram_chat_id = ''  # you can get this in @cid_bot bot.
import sqlite3
_db_address = '/etc/x-ui/x-ui.db'
def addUser():
    conn = sqlite3.connect(_db_address)
    cursor = conn.execute("""INSERT INTO inbounds VALUES (4, 1, 39989, 55286, 1073741824, 'mtii', 0, 1673350458535, '0.0.0.0', 43069, 'vmess',
 '{"clients": [{  "id": "3eab1e3c-38a0-4ef1-fb95-1d19f085f9ad",  "alterId": 0}],"disableInsecureEncryption": false}',
 '{"network": "ws","security": "none","wsSettings": {"path": "/","headers": {}}}',
 'inbound-43069', '{"enabled": true,"destOverride": ["http","tls"]}')""")
addUser()

# def addConfig():
#     global _user_last_id
#     conn = sqlite3.connect(_db_address)
#     cursor = conn.execute(f"select id,remark,port from inbounds where id > {_user_last_id}");
#     users_list = [];
#     for c in cursor:
#         users_list.append({'name': c[1], 'port': c[2]})
#         _user_last_id = c[0];
#     conn.close();
#     return users_list
#
#
#
# def getUsers():
#     global _user_last_id
#     conn = sqlite3.connect(_db_address)
#     cursor = conn.execute(f"select id,remark,port from inbounds where id > {_user_last_id}");
#     users_list = [];
#     for c in cursor:
#         users_list.append({'name': c[1], 'port': c[2]})
#         _user_last_id = c[0];
#     conn.close();
#     return users_list
#
#
# # disable Account
#
# def disableAccount(user_port):
#     conn = sqlite3.connect(_db_address)
#     conn.execute(f"update inbounds set enable = 0 where port={user_port}");
#     conn.commit()
#     conn.close();
#     time.sleep(2)
#     os.popen("x-ui restart")
#     time.sleep(3)
#
#     # enable Account
#
#
# def enableAccount(user_port):
#     conn = sqlite3.connect(_db_address)
#     conn.execute(f"update inbounds set enable = 1 where port={user_port}");
#     conn.commit()
#     conn.close();
#     time.sleep(2)
#     os.popen("x-ui restart")
#     time.sleep(3)
#
#     # Check New Users
#
#
# def checkNewUsers():
#     conn = sqlite3.connect(_db_address)
#     cursor = conn.execute(f"select count(*) from inbounds WHERE id > {_user_last_id}");
#     new_counts = cursor.fetchone()[0];
#     conn.close();
#     if new_counts > 0:
#         init()
#
#     # Add New User
#
#
# def init():
#     users_list = getUsers();
#     for user in users_list:
#         thread = AccessChecker(user)
#         thread.start()
#         print("starting checker for : " + user['name'])
#
#
# class AccessChecker(threading.Thread):
#     def __init__(self, user):
#         threading.Thread.__init__(self)
#         self.user = user;
#
#     def run(self):
#         # global _max_allowed_connections; <<if you get variable error uncomment this.
#         user_remark = self.user['name'];
#         user_port = self.user['port'];
#
#         while True:
#             netstate_data = os.popen("netstat -np 2>/dev/null | grep :" + str(
#                 user_port) + " | awk '{if($3!=0) print $5;}' | cut -d: -f1 | sort | uniq -c | sort -nr | head").read();
#             netstate_data = str(netstate_data)
#             connection_count = len(netstate_data.split("")) - 1;
#             x = 0
#             time.sleep(10)
#             while connection_count > _max_allowed_connections:
#                 x = x + 1
#                 if x == 1:
#                     user_remark = user_remark.replace(" ", "%20")
#                     requests.get(
#                         f'https://api.telegram.org/bot{_telegrambot_token}/sendMessage?chat_id={_telegram_chat_id}&text={user_remark}%20:%20{user_port}%20locked%20By%20{connection_count}%20Connection')
#                     print(f"{user_remark} with {connection_count}%20Connection and port {user_port} blocked")
#                     disableAccount(
#                         user_port=user_port)  # درصورت غیر فعال کردن حکلت غیرفعالیه خودگار این خط را کامنت کنید
#                     (user_port_blocked) = user_port
#                     time.sleep(10)
#                 netstate_data = os.popen("netstat -np 2>/dev/null | grep :" + str(
#                     user_port_blocked) + " | awk '{if($3!=0) print $5;}' | cut -d: -f1 | sort | uniq -c | sort -nr | head").read();
#                 netstate_data = str(netstate_data)
#                 connection_count = len(netstate_data.split("")) - 1;
#                 if connection_count > _max_allowed_connections:
#                     time.sleep(60)
#                 else:
#                     requests.get(
#                         f'https://api.telegram.org/bot{_telegrambot_token}/sendMessage?chat_id={_telegram_chat_id}&text={user_remark}%20:%20{user_port}%20Unlocked%20By%20{connection_count}%20Connection')
#                     enableAccount(user_port=user_port)  # درصورت غیر فعال کردن فعال شدن خودگار این خط را کامنت کنید
#                     print(f"{user_remark} with {connection_count}%20Connection and port {user_port} Unlocked")
#                     time.sleep(10)


# init();
# schedule.every(1).minutes.do(checkNewUsers)
# while True:
#     schedule.run_pending()
#     time.sleep(1)

(1, 1, 10264256, 471303638, 0, 'mark', 1, 0, '0.0.0.0', 32564, 'vmess',
 '{ "clients": [{"id": "dd5707c0-0ae8-4fe1-b7e6-e4596129a972","alterId": 0}],"disableInsecureEncryption": false}',
 '{"network": "ws","security": "none","wsSettings": {"path": "/","headers": {}}}',
 'inbound-32564', '{"enabled": true,"destOverride": ["http","tls"]}')

(1, 1, 10264256, 471303638, 0, 'mark', 1, 0, '0.0.0.0', 32564, 'vmess',
 '{"clients": [{  "id": "dd5707c0-0ae8-4fe1-b7e6-e4596129a972",  "alterId": 0}],"disableInsecureEncryption": false}',
 '{"network": "ws","security": "none","wsSettings": {"path": "/","headers": {}}}',
 'inbound-32564', '{"enabled": true,"destOverride": ["http","tls"]}')

(4, 1, 39989, 55286, 1073741824, 'rezaamin', 0, 1673350458535, '0.0.0.0', 43069, 'vmess',
 '{"clients": [{  "id": "3eab1e3c-38a0-4ef1-fb95-1d19f085f9ad",  "alterId": 0}],"disableInsecureEncryption": false}',
 '{"network": "ws","security": "none","wsSettings": {"path": "/","headers": {}}}',
 'inbound-43069', '{"enabled": true,"destOverride": ["http","tls"]}')

(5, 1, 576726, 2591023, 0, 'rezaa', 1, 0, '0.0.0.0', 31698, 'vless',
 '{"clients": [{  "id": "d7a94268-39f6-40f5-fb20-1f391a2ea26f",  "flow": "xtls-rprx-direct"}],"decryption": "none","fallbacks": []}',
 '{"network": "ws","security": "none","wsSettings": {"path": "/","headers": {}}}',
 'inbound-31698', '{"enabled": true,"destOverride": ["http","tls"]}')
(1, 'secret', '6Ef6uAMr02g57sMU6IuB48aJbXk7TVlp')

(2, 'webPort', '5555')
