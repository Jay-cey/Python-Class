class CourseRegistration:
    def __init__(self, db):
        self.db = db

    def register_course(self, matric, course_id):
        self.db.execute("INSERT INTO courses_registered (matric, course_id) VALUES (%s, %s)", (matric, course_id))
        return True
    
    def add_course_db(self, course_code, course_name, units, semester, academic_year, level):
        self.db.execute("INSERT INTO courses (course_code, course_name, units, semester, academic_year, level) VALUES (%s, %s, %s, %s, %s, %s)", (course_code, course_name, units, semester, academic_year, level))
    
    def get_all_courses(self, matric):
        # return self.db.fetch_all("SELECT course_code FROM courses_registered WHERE matric=%s", (matric))
        return self.db.fetch_all("SELECT c.course_code, c.course_name, c.units FROM courses_registered cr JOIN courses c ON cr.course_id = c.course_id WHERE cr.matric = %s", (matric,))

    def get_courses(self, matric, semester, academic_year):
        # return self.db.fetch_all("SELECT course_code kFROM courses_registered WHERE matric=%s", (matric))
        return self.db.fetch_all("SELECT c.course_code, c.course_name, c.units FROM courses_registered cr JOIN courses c ON cr.course_id = c.course_id WHERE cr.matric = %s AND cr.semester = %s AND cr.academic_year = %s", (matric, semester, academic_year))
    
    def get_course_list(self, semester, academic_year):
        return self.db.execute("SELECT * FROM courses WHERE semester=%s AND academic_year=%s", (semester, academic_year))