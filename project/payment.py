class Payment:
    def __init__(self, db):
        self.db = db

    def make_payment(self, matric, amount, semester, academic_year):
        self.db.execute("INSERT INTO payments (matric, amount, semester, academic_year) VALUES (%s, %s, %s, %s)", (matric, amount, semester, academic_year))
        return True
    
    def get_payment(self, matric, academic_year, semester):
        paid = self.db.fetch_one("SELECT * FROM payments WHERE matric=%s AND academic_year=%s AND semester=%s", (matric, academic_year, semester))
        if paid: return True
