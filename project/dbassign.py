import pymysql as pyms

class Database_operations:
    connectionStatus = False
    def __init__(self, db, connection=connectionStatus):
        self.db = db
        # self.table = table
        self.connection = connection
        self.con_sql = None
        self.cursor = None

    def initialize_db(self):
        self.con_sql = pyms.connect(host = "127.0.0.1", user="root", password="",)
        self.cursor = self.con_sql.cursor()

    def connect_db(self):
        self.connection = True
        self.con_sql = pyms.connect(host = "127.0.0.1", user="root", password="", db=self.db)
        self.cursor = self.con_sql.cursor()
        print(f"Connection to {self.db} is successful")

    def createDB(self):
        self.cursor.execute(f"CREATE DATABASE {self.db.upper()}")
        self.con_sql.commit()

    def show(self):
        self.cursor.execute("SHOW DATABASES")
        for db in self.cursor:
            print(db)
    
    def execute(self, query, params=None): 
        self.cursor.execute(query, params or [])
        self.con_sql.commit()
        return self.cursor
    
    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params or [])
        return self.cursor.fetchone()

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params or [])
        return self.cursor.fetchall()

    def createTable(self, table):
        self.cursor.execute(f"USE {self.db.upper()}")
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table}")
        self.con_sql.commit()
        print("Table created successfully")

    # def create(self):
    #     self.cursor.execute(f"SHOW COLUMNS FROM {self.table}")
    #     for col in self.cursor:
    #         print(col)

    def cursor(self):
        return self.cursor

    def close_cursor(self):
        if self.cursor:
            self.cursor.close()

    def close_connection(self):
        if self.con_sql:
            self.con_sql.close()
