class Quiz:
    def __init__(self, db):
        self.db = db

    def create_question(self, course_code, question, answer):
        self.db.execute("INSERT INTO questions (course_code, question, answer) VALUES (%s, %s, %s)",        (course_code, question, answer))

    def take_quiz(self, matric, course_code, semester, academic_year):
        import time
        questions = self.db.fetch_all("SELECT id, question, answer, option_a, option_b, option_c, option_d FROM questions WHERE course_code=%s", (course_code,))
        score = 0
        start = time.time()
        for q in questions:
            print(f"{q[1]}\na. {q[3]} b. {q[4]} c. {q[5]} d. {q[6]}")  # display question
            ans = input("Answer: ").strip().lower()
            if time.time() - start <= 30 and ans.strip().lower() == q[2].lower():
                score += 1
            else:
                break
        score = (score/len(questions)) * 100
        self.db.execute("INSERT INTO results (matric, course_code, score, semester, academic_year, attempt_date) VALUES (%s, %s, %s, %s, %s, NOW())", (matric, course_code, score, semester, academic_year))
        return score

    def get_grade(self, matric, semester, academic_year):
        try:
            result = self.db.fetch_all("SELECT course_code, score FROM results WHERE matric=%s AND semester=%s AND academic_year=%s", (matric, semester, academic_year))
            return result
        except TypeError:
            print(f"You have not taken the any quiz.")    