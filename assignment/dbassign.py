import pymysql as pyms

class Database_Operations:
    connectionStatus = False
    def __init__(self, table, db, connection=connectionStatus):
        self.db = db
        self.table = table
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


    def createDB(self):
        self.cursor.execute(f"CREATE DATABASE {self.db.upper()}")
        self.con_sql.commit()

    def show(self):
        self.cursor.execute("SHOW DATABASES")
        for db in self.cursor:
            print(db)

    def createTable(self):
        self.cursor.execute(f"USE {self.db.upper()}")
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table}(std_id INT(3), full_name VARCHAR(20), email VARCHAR(50), gender VARCHAR(6), level VARCHAR(5))")
        # self.con_sql.commit()
        print("Table created successfully")

    def create(self):
        self.cursor.execute(f"SHOW COLUMNS FROM {self.table}")
        for col in self.cursor:
            print(col)

    def close_cursor(self):
        if self.cursor:
            self.cursor.close()

    def close_connection(self):
        if self.con_sql:
            self.con_sql.close()

if __name__ == '__main__':    
    collegedb = Database_Operations(table="college_record", db="collegeDB")
    collegedb.initialize_db()
    # try:
    collegedb.createDB()
    # except:
        # print("Database already exists")
    collegedb.connect_db()
    collegedb.show()
