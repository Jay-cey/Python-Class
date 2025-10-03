class CourseRegistration:
    def __init__(self, db):
        self.db = db

    def register_course(self, matric, course_id):
        self.db.execute("INSERT INTO courses_registered (matric, course_id) VALUES (%s, %s)", (matric, course_id))
        return True

    def get_courses(self, matric):
        # return self.db.fetch_all("SELECT course_code FROM courses_registered WHERE matric=%s", (matric))
        return self.db.fetch_all("SELECT c.course_code, c.course_name, c.units FROM courses_registered cr JOIN courses c ON cr.course_id = c.course_id WHERE cr.matric = %s", (matric,))
    
    def get_course_list(self):
        return self.db.execute("SELECT * FROM courses")