class Quiz:
    def __init__(self, db):
        self.db = db

    def create_question(self, course_code, question, answer):
        self.db.execute("INSERT INTO questions (course_code, question, answer) VALUES (%s, %s, %s)",        (course_code, question, answer))

    def take_quiz(self, matric, course_code, semester, academic_year):
        import time
        questions = self.db.fetch_all("SELECT id, question, answer FROM questions WHERE course_code=%s", (course_code,))
        score = 0
        for q in questions:
            print(q[1])  # display question
            start = time.time()
            ans = input("Answer: ")
            if time.time() - start <= 30 and ans.strip().lower() == q[2].lower():
                score += 1
        self.db.execute("INSERT INTO results (matric, course_code, score, semester, academic_year, attempt_date) VALUES (%s, %s, %s, %s, %s, NOW())", (matric, course_code, score, semester, academic_year))
        return score

    def get_grade(self, matric, course_code):
        try:
            result = self.db.fetch_one("SELECT score FROM results WHERE matric=%s AND course_code=%s", (matric, course_code))
            score = result[0]
            if score >= 70: return "A"
            elif score >= 60: return "B"
            elif score >= 50: return "C"
            elif score >= 45: return "D"
            elif score >= 40: return "E"
            else: return "F"
        except TypeError:
            print(f"You have not taken the {course_code} quiz. Please type in a valid course code.")