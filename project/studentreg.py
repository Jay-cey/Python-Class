class StudentRegister:
    def __init__(self, db):
        self.db = db

    def list_students(self):
        return self.db.fetch_all("SELECT std_id, name, email, matric, level FROM students")
