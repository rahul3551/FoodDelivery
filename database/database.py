# we will connect database here lets use sqlite for simplicity and we will create a class to handle database operations

import sqlite3
from abc import ABC, abstractmethod



class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    # @abstractmethod
    # def execute_query(self, query, params=None):
    #     pass

class SQLiteDatabase(DatabaseInterface):
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.create_table()

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection
    
    # def execute_query(self, query, params=None):
    #     if self.connection is None:
    #         raise Exception("Database not connected")
    #     cursor = self.connection.cursor()
    #     if params:
    #         cursor.execute(query, params)
    #     else:
    #         cursor.execute(query)
    #     return cursor

    def create_table(self):
        conn = self.connect()

        if conn is None:
            raise Exception("Database not connected")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        customer_type TEXT NOT NULL
        )
        """)


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS restaurants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        city TEXT NOT NULL
        )
        """)


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        restaurant_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        discount REAL NOT NULL,
        delivery_charge REAL NOT NULL,
        final_amount REAL NOT NULL,
        delivery_type TEXT NOT NULL,
        created_at TEXT NOT NULL
        )
        """)

        conn.commit()
        self.close()
    
    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None