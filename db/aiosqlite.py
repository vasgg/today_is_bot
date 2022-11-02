import aiosqlite


class Database:
    """
    Класс для работы с базой данных
    """

    def __init__(self, path_to_db='db/today_is.db'):
        self.path_to_db = path_to_db

    @property
    async def connection(self):
        """
        Метод класса который совершает подключение к бд
        :return: объект подключения к бд
        """

        return await aiosqlite.connect(self.path_to_db)

    async def execute(self, sql: str, params: tuple = None, fetchone=False,
                      fetchall=False, commit=False):
        """
        Метод класса выполняющий sql запросы
        :param sql: запрос на языке sql
        :param params: параметры, вставляемые в запрос
        :param fetchone: параметр, определяющий возвращать ли одну строку
        :param fetchall: параметр, определяющий возвращать все строки
        :param commit: параметр, определяющий делать ли запись в бд
        :return: данные бд
        """

        if not params:
            params = tuple()
        connection = await self.connection
        await connection.set_trace_callback(logger)
        cursor = await connection.cursor()
        await cursor.execute(sql, params)
        data = None

        if commit:
            await connection.commit()
        if fetchone:
            data = await cursor.fetchone()
        if fetchall:
            data = await cursor.fetchall()
        await cursor.close()
        await connection.close()
        return data

    async def create_table_users(self):
        """
        Метод, создающий таблицу Users
        """

        sql = """
        CREATE TABLE IF NOT EXISTS Users(
        user_ID int NOT NULL PRIMARY KEY,
        username TEXT,
        current_timezone INT
        );
        """

        await self.execute(sql, commit=True)

    async def create_table_records(self):
        """
        Метод, создающий таблицу Records
        """

        sql = '''CREATE TABLE IF NOT EXISTS Records(
            event_name TEXT,
            event_timestamp TEXT,
            user_ID INTEGER NOT NULL,
            FOREIGN KEY (user_ID)
               REFERENCES Users (user_ID)
        );'''

        # await self.execute(sql2, commit=True)
        await self.execute(sql, commit=True)
        # logger (sql executing bla bla bla)

    async def select_all_users(self):
        """
        Метод возвращающий список с данными всей таблицы
        :return: данные таблицы Users
        """

        sql = "SELECT * FROM Users"
        result = await self.execute(sql, fetchall=True)
        return result

    async def check_user(self, user_ID):
        sql = f"SELECT * FROM Users WHERE User_ID={user_ID}"
        result = await self.execute(sql, fetchall=True)
        print(result)
        if len(result) > 0:
            return True
        else:
            return False

    async def add_user(self, user_ID, username, current_timezone):
        params = (user_ID, username, current_timezone)
        sql = f'INSERT INTO Users(user_ID, username, current_timezone) VALUES (?, ?, ?)'
        await self.execute(sql, params=params, commit=True)

    async def registration_record(self, event_timestamp, event_name, user_ID):
        params = (event_timestamp, event_name, user_ID)
        sql = f'INSERT INTO Records(event_timestamp, event_name, user_ID) VALUES (?, ?, ?)'
        await self.execute(sql, params=params, commit=True)

    async def user_rowid(self, user_ID):
        sql = f'SELECT ROWID from Users WHERE User_ID={user_ID}'
        result = await self.execute(sql, fetchone=True)
        return result[0]

    async def user_timezone(self, user_ID):
        sql = f'SELECT current_timezone FROM Users WHERE User_ID={user_ID}'
        result = await self.execute(sql, fetchone=True)
        return result[0]

    async def registration_date(self, user_ID):
        sql = f'SELECT event_timestamp from Records WHERE User_ID={user_ID}'
        result = await self.execute(sql, fetchone=True)
        return result[0]

    async def update_timezone(self, current_timezone, user_ID):
        params = (current_timezone, )
        sql = f'UPDATE Users(current_timezone) SET VALUES (?, ) WHERE user_ID={user_ID}'
        await self.execute(sql, params=params, commit=True)


def logger(statement):
    """
    Функция для визуализации работы бд
    :param statement: текущая выполняемая задача бд
    """

    print(f"""
--------------------------------------------------------------------
Executing:
{statement}
____________________________________________________________________
""")
