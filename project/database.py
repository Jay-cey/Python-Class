class Database:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()

    def execute(self, query, params=None): 
        self.cursor.execute(query, params or [])
        self.conn.commit()
        return self.cursor

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params or [])
        return self.cursor.fetchone()

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params or [])
        return self.cursor.fetchall()