import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            name varchar(255),
            language varchar(5),
            phone varchar(255) NULL
            );
"""
        self.execute(sql, commit=True)
    
    

    def create_table_diabet(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Diabet (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            type varchar(255),
            age varchar(3) NULL,
            weight varchar(3) NULL,
            height varchar(3) NULL,
            start_illness varchar(10) NULL,
            start_insulin varchar(20) NULL,
            age_range varchar(255) NULL
            ); """
        self.execute(sql, commit=True)
    

    "create table obesity"
    def create_table_obesity(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Obesity (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            age varchar(3),
            weight varchar(3),
            height varchar(3),
            location varchar(255)
            ); """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())
    

    def add_user(self, id, name, language, phone=None):
        sql = "INSERT OR IGNORE INTO Users (id, Name, language, phone) VALUES (?, ?, ?,?)"
        self.execute(sql, parameters=(id, name, language, phone), commit=True)

    def select_user(self, user_id):
        sql = "SELECT name, language, phone FROM Users WHERE id = ?"
        return self.execute(sql, parameters=(user_id,),fetchone=True)
    
    def update_phone(self, id, phone):
        sql = "UPDATE Users SET phone = ? WHERE id = ?"
        self.execute(sql, parameters=(phone, id), commit=True)
    
    def select_lang(self, id):
        sql = "SELECT language FROM Users WHERE id = ?"
        return self.execute(sql, parameters=(id,), fetchone=True)[0]

    def update_lang(self, id, language):
        sql = "UPDATE Users SET language = ? WHERE id = ?"
        self.execute(sql, parameters=(language, id), commit=True)
    

    def select_user(self, id):
        sql = "SELECT * FROM Users WHERE id = ? "

        return self.execute(sql, parameters=(id,), fetchone=True)



    """
            Table Diabet:
    fields:
        type: varchar(255),
        age: varchar(3),
        weight: varchar(3),
        height: varchar(3),
        start_illness: varchar(10)
        start_insulin: varchar(20)
        age_range: varchar(255)


    create table for this
        """

    

    def add_diabet(self, id, user_id, type, age, weight= None, height= None, start_illness = None, start_insulin = None, age_range = None):
        sql = "INSERT OR IGNORE INTO Diabet (id, user_id, type, age, weight, height, start_illness, start_insulin, age_range)\
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.execute(sql, parameters=(id, user_id,type, age, weight, height, start_illness, start_insulin, age_range), commit=True)
    

    def select_diabet(self, id, user_id):
        sql = "SELECT type, age, weight, height, start_illness, start_insulin, age_range FROM Diabet WHERE id = ?, user_id = ?"
        return self.execute(sql, parameters=(id, user_id), fetchone=True)
    
    
    def add_obesity(self, user_id, id=None, age=None, weight=None, height=None, location=None):
        sql = "INSERT OR IGNORE INTO Obesity (id, user_id, age, weight, height, location)\
              VALUES (?, ?, ?, ?, ?)"
        self.execute(sql, parameters=(id, age, weight, height, location), commit=True)
    

    def select_obesity(self, id, user_id):
        sql = "SELECT age, weight, height, location FROM Obesity WHERE id = ?, user_id = ?"
        return self.execute(sql, parameters=(id, user_id), fetchone=True)