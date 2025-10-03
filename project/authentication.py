class Auth:
    def __init__(self, db):
        self.db = db

    def register(self, name, email, level, password):
        matric = self.generate_matric()
        self.db.execute("INSERT INTO students (name, email, password, matric, level) VALUES (%s, %s, %s, %s, %s)", 
                        (name, email, password, matric, level))
        return matric

    def login(self, email, password):
        student = self.db.fetch_one("SELECT * FROM students WHERE email=%s AND password=%s", (email, password))
        if student is not None: return student

    def generate_matric(self):
        import random
        return "MAT" + str(random.randint(1000, 9999))
