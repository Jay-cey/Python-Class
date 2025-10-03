class Payment:
    def __init__(self, db):
        self.db = db

    def make_payment(self, matric, amount):
        self.db.execute("INSERT INTO payments (matric, amount) VALUES (%s, %s)", (matric, amount))
        return True
