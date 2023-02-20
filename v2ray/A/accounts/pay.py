from abc import ABC
import jdatetime
import psycopg2
import psycopg2.extras
from psycopg2._psycopg import connection, cursor


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
                curs.execute(
                    f"""INSERT INTO {model_instance.TABLE}({model_fields_str}) VALUES ({model_values_str})
                     RETURNING ID;""", model_values_tuple)
                res = curs.fetchone()
                return res

    def read_order(self, model_class: type, order_id: int):
        assert issubclass(model_class, DBModel)
        with self.conn:
            curs = self.__get_cursor()
            with curs:
                curs.execute(f"""SELECT * FROM {model_class.TABLE} WHERE id = '{order_id}' """)
                res = curs.fetchall()
                return res

    def update_order(self, model_class: type, order_id: int, status: str):
        assert issubclass(model_class, DBModel)
        with self.conn:
            curs = self.__get_cursor()
            with curs:
                curs.execute(f"""UPDATE {model_class.TABLE} SET pay = '{status}' WHERE id = '{order_id}' """)
                # res = curs.fetchall()
                # return res

    def delete(self, model_instance: DBModel, pk: str):
        assert issubclass(model_instance, DBModel)
        with self.conn:
            curs = self.__get_cursor()
            with curs:
                curs.execute(f"""DELETE FROM {model_instance.TABLE} WHERE {model_instance.PK} = '{pk}'""")


db = DBManager(database="vpn")


class Order(DBModel):
    TABLE = 'orders'
    PK = 'id'

    def __init__(self, user_id: int, server_name: str, count: int, price: int, pay: bool,
                 date: jdatetime.datetime):
        self.user_id = user_id
        self.server_name = server_name
        self.count = count
        self.price = price
        self.pay = pay
        self.date = date
        dba = db.create(self)
        self.id = dba[0]

    def get_id(self):
        return self.id


def pay(order_id):
    a = db.update_order(Order, order_id, False)
