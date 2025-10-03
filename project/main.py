import pymysql as pyms
from getpass import getpass

# -------------------------
# Import all classes here
import authentication as Auth
import coursereg as CourseRegistration
import payment as Payment
import quiz as Quiz
import studentreg as StudentRegister
import dbassign as ConnectDB
# -------------------------

def main():
    db = "collegedb"
    connect = ConnectDB.Database_operations(db)
    connect.connect_db()
    # connect.show()
    # Students table
    connect.createTable("students(std_id INT(3) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), email VARCHAR(50), password VARCHAR(15), matric VARCHAR(7) UNIQUE NOT NULL, level INT)")

    # Payments table
    connect.createTable("payments(serial_number INT(5) AUTO_INCREMENT PRIMARY KEY, matric VARCHAR(7), amount DECIMAL(10,2), semester VARCHAR(10), academic_year INT, payment_date DATE, FOREIGN KEY (matric) REFERENCES students(matric))")

    # Courses table
    connect.createTable("courses(course_id INT AUTO_INCREMENT PRIMARY KEY, course_code VARCHAR(10) NOT NULL UNIQUE, course_name VARCHAR(60) NOT NULL, units INT, semester VARCHAR(10), academic_year INT, level INT)")

    # Courses registered
    connect.createTable("courses_registered(id INT AUTO_INCREMENT PRIMARY KEY, matric VARCHAR(7), course_id INT, semester VARCHAR(10), academic_year INT, registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, status VARCHAR(20) DEFAULT 'registered', FOREIGN KEY (matric) REFERENCES students(matric), FOREIGN KEY (course_id) REFERENCES courses(course_id), UNIQUE(matric, course_id, semester, academic_year))")

    # Questions
    connect.createTable("questions(id INT AUTO_INCREMENT PRIMARY KEY, course_code VARCHAR(10), question TEXT, answer VARCHAR(255), FOREIGN KEY (course_code) REFERENCES courses(course_code))")

    # Results table - tracks quiz scores per semester (for retakes)
    connect.createTable("results(id INT AUTO_INCREMENT PRIMARY KEY, matric VARCHAR(7), course_code VARCHAR(10), score INT, semester VARCHAR(10), academic_year INT, attempt_date DATETIME, FOREIGN KEY (matric) REFERENCES students(matric), FOREIGN KEY (course_code) REFERENCES courses(course_code))")
    # 1. Connect to MySQL
       
    # conn = pyms.connect(
    #     host="127.0.0.1",
    #     user="root",
    #     password="Cxerrexc22.",
    #     database="collegedb"
    # )
    db = connect

    # 2. Initialize classes
    auth = Auth.Auth(db)
    payment = Payment.Payment(db)
    course_reg = CourseRegistration.CourseRegistration(db)
    student_reg = StudentRegister.StudentRegister(db)
    quiz = Quiz.Quiz(db)

    # 3. Main menu loop
    while True:
        print("\n=== School Management Portal ===")
        print("1. Register")
        print("2. Login")
        print("3. Login as admin")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter full name: ").strip()
            email = input("Enter email: ").lower().strip()
            level = int(input("Enter your level e.g 100:  "))
            while True:
                password = getpass("Enter password: ")
                confirm_password = input("Confirm your password")
                if password == confirm_password:
                    matric = auth.register(name, email, level, password)
                    print(f"✅ Registration successful! Your Matric Number: {matric}")
                    break
                else:
                    print("❌ Passwords do not match")

        elif choice == "2":
            email = input("Enter email: ")
            password = getpass("Enter password: ")
            student = auth.login(email, password)
            if student:
                print("✅ Login successful!")
                matric = student[4]
                student_menu(auth, payment, course_reg, student_reg, quiz, matric)
            else:
                print("❌ Invalid login")

        elif choice == "4":
            print("👋 Goodbye!")
            break

        else:
            print("Invalid option, try again.")

    # conn.close()
    connect.close_cursor()
    connect.close_connection()

def register_courses(matric, course_reg):
    """Register Courses with matric number and course Id"""
    print(f"\nCourse List:")
    for c in course_reg.get_course_list():
        print(f"ID: {c[0]}. Code: {c[1]:8} Name: {c[2]:40} Units: {c[3]}")
    course_id = input("\nEnter course IDs separated with comma ',' from above list: ")
    course_list = course_id.strip().split(',')
    for item in course_list:
        if item != " ":
            try:
                item = int(item)
                course_reg.register_course(matric, item)
            except ValueError:
                print("IDs must be numbers. Seperated by commas if multiple.")
                register_courses(matric, course_reg)
        else:
            print("Input cannot be empty")
            register_courses(matric, course_reg)
    print("✅ Course registered")

def check_courses(matric, course_reg):
    """Check the list of courses registered"""
    courses = course_reg.get_courses(matric)
    print("\n 📚 Your Courses:")
    total_units = 0
    for course in courses:
        print(f"\t{course[0]:10} - {course[1]:40} ({course[2]} units)")
        total_units += course[2]
    print(f"\nTotal Units: {total_units}")

def all_students(student_reg):
    students = student_reg.list_students()
    print("\n 👥 All Students:")
    print(f" {'S/N':3}  {'Full Name':30} {'Email':30} {'Matric':8} {'Level'}")
    for s in students:
        print(f"{s[0]:3}.  {s[1]:30} {s[2]:30} {s[3]:8} {s[4]}l")

def student_menu(auth, payment, course_reg, student_reg, quiz, matric):
    while True:
        print(f"\n=== Student Dashboard ({matric}) ===")
        print("1. Make Payment")
        print("2. Register Course")
        print("3. View My Courses")
        print("4. View All Students")
        print("5. Take Quiz")
        print("6. Check Result & Grade")
        print("7. Logout")

        sub_choice = input("Enter choice: ").strip()

        if sub_choice == "1":
            amount = float(input("Enter payment amount: ").strip())
            if amount == 10000.0:
                payment.make_payment(matric, amount)
                print("✅ Payment successful")
            else:
                print("❌ Payment Error: Please ensure your payment is exactly $10,000")

        elif sub_choice == "2":
            register_courses(matric, course_reg)

        elif sub_choice == "3":
            check_courses(matric, course_reg)

        elif sub_choice == "4":
            all_students(student_reg)

        elif sub_choice == "5":
            semester = "Rain"
            academic_year = 2024
            course_code = input("Enter course code for quiz: ").strip().upper()
            score = quiz.take_quiz(matric, course_code, semester, academic_year)
            print(f"✅ Quiz completed. Score = {score}")

        elif sub_choice == "6":
            course_code = input("Enter course code: ").strip().upper()
            grade = quiz.get_grade(matric, course_code)
            if grade:
                print(f"📊 Your grade for {course_code} is {grade}")

        elif sub_choice == "7":
            print("🔒 Logging out...")
            break

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
