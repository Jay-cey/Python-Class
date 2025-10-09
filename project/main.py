import pymysql as pyms
from getpass import getpass
import re

# -------------------------
# Import all classes here
import authentication
import coursereg
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

    # Admin table
    connect.createTable("admin(id INT(3) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), email VARCHAR(50), password VARCHAR(15), matric VARCHAR(7) UNIQUE NOT NULL)")

    # Payments table
    connect.createTable("payments(serial_number INT(5) AUTO_INCREMENT PRIMARY KEY, matric VARCHAR(7), amount DECIMAL(10,2), semester VARCHAR(10), academic_year INT, payment_date DATE, FOREIGN KEY (matric) REFERENCES students(matric))")

    # Courses table
    connect.createTable("courses(course_id INT AUTO_INCREMENT PRIMARY KEY, course_code VARCHAR(10) NOT NULL UNIQUE, course_name VARCHAR(60) NOT NULL, units INT, semester VARCHAR(10), academic_year INT, level INT)")

    # Courses registered
    connect.createTable("courses_registered(id INT AUTO_INCREMENT PRIMARY KEY, matric VARCHAR(7), course_id INT, semester VARCHAR(10), academic_year INT, registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, status VARCHAR(20) DEFAULT 'registered', FOREIGN KEY (matric) REFERENCES students(matric), FOREIGN KEY (course_id) REFERENCES courses(course_id), UNIQUE(matric, course_id, semester, academic_year))")

    # Questions
    connect.createTable("questions(id INT AUTO_INCREMENT PRIMARY KEY, course_code VARCHAR(10), question TEXT, answer VARCHAR(2), option_a TEXT, option_b TEXT, option_c TEXT, option_d TEXT, FOREIGN KEY (course_code) REFERENCES courses(course_code))")

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
    # global auth
    auth = authentication.Auth(db)
    payment = Payment.Payment(db)
    course_reg = coursereg.CourseRegistration(db)
    student_reg = StudentRegister.StudentRegister(db)
    quiz = Quiz.Quiz(db)

    semester = "Rain"
    academic_year = 2024

    # 3. Main menu loop
    while True:
        print("\n=== School Management Portal ===")
        print("1. Register")
        print("2. Login")
        print("3. Login as admin")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            register(auth)

        elif choice == "2":
            login(auth, payment, course_reg, student_reg, quiz, semester, academic_year)

        elif choice == "3":
            semester, academic_year = login_admin(auth, quiz, student_reg, semester, academic_year)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")

    # conn.close()
    connect.close_cursor()
    connect.close_connection()

def check_name(name):
    if re.match(r'^[A-Za-z]{2,20}$', name): return True

def register(auth):
    """Collect student details, store info in database and auto-generate a matric number"""
    try:

        while True:
            fname = input("Enter first name: ").strip().capitalize()
            if check_name(fname):
                break
            print(" Invalid first name. Use only letters (2-20 characters)")
        
        
        while True:
            lname = input("Enter last name: ").strip().capitalize()
            if check_name(lname):
                break
            print(" Invalid last name. Use only letters (2-20 characters)")
        
        
        while True:
            email = input("Enter email: ").lower().strip()
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                break
            print(" Invalid email format. Please try again")
        
        
        while True:
            try:
                level = int(input("Enter your level e.g 100: ").strip())
                if level in [100, 200, 300, 400, 500]:
                    break
                print(" Invalid level. Choose from: 100, 200, 300, 400, 500")
            except ValueError:
                print(" Please enter a valid number")
        

        while True:
            password = getpass("Enter password (min 8 characters): ")
            if len(password) < 8:
                print(" Password must be at least 8 characters")
                continue
            
            confirm_password = getpass("Confirm your password: ")
            if password == confirm_password:
                name = f"{fname} {lname}"
                matric = auth.register(name, email, level, password)
                print(f" Registration successful! Your Matric Number: {matric}")
                return
            else:
                print(" Passwords do not match. Please try again")
    
    except KeyboardInterrupt:
        print("\n⚠️ Registration cancelled")
    # except Exception as e:
    #     print(f" An error occurred: {e}")

def login(auth, payment, course_reg, student_reg, quiz, semester, academic_year):
    """Login with info provided found in database"""
    email = input("Enter email: ")
    password = getpass("Enter password: ")
    student = auth.login(email, password)
    if student:
        print(" Login successful!")
        matric = student[4]
        student_menu(auth, payment, course_reg, student_reg, quiz, matric, semester, academic_year)
    else:
        print(" Invalid login.")
        req = input("Do you wish to try again? Y/N :   ").lower().strip()
        if req in ["yes", "y"]:
            login(auth, payment, course_reg, student_reg, quiz, semester, academic_year)
        else:
            # print(" Invalid Input.")
            main()

def login_admin(auth, quiz, student_reg, semester, academic_year):
    """Login admin provided info is found in table"""
    email = input("Enter email: ")
    password = getpass("Enter password: ")
    admin = auth.login_admin(email, password)
    if admin:
        print(" Login successful!")
        matric = admin[4]
        semester, academic_year = admin_menu(auth, quiz, student_reg, matric, semester, academic_year)
    else:
        print(" Invalid login.")
        req = input("Do you wish to try again? Y/N :   ").lower().strip()
        if req in ["yes", "y"]:
            login_admin(auth, quiz, student_reg, semester, academic_year)
        else:
            print(" Invalid Input.")
            main()
    return semester, academic_year
            
def register_courses(matric, course_reg, semester, academic_year):
    """Register Courses with matric number and course Id"""
    print(f"\nCourse List:")
    for c in course_reg.get_course_list(semester, academic_year):
        print(f"ID: {c[0]}. Code: {c[1]:8} Name: {c[2]:40} Units: {c[3]}")
    course_id = input("\nEnter course IDs separated with comma ',' from above list: ")
    course_list = course_id.strip().split(',')
    for item in course_list:
        if item.strip() != "":
            try:
                item = int(item)
                course_reg.register_course(matric, item)
            except ValueError:
                print("IDs must be numbers. Seperated by commas if multiple.")
                register_courses(matric, course_reg)
        else:
            print("Input cannot be empty")
            register_courses(matric, course_reg)
    print(" Course registered")

def pay_tuition(payment, matric, semester, academic_year):
    try:
        if payment.get_payment(matric, academic_year, semester):
            return print(f" Tution for {semester} semester, {academic_year} session has already been paid.")
        amount = float(input("Enter payment amount 10,000: ").strip().replace(",", ""))
        if amount == 10000.0:
            payment.make_payment(matric, amount, semester, academic_year)
            print(" Payment successful")
        else:
            print(" Payment Error: Please ensure your payment is exactly 10,000")
    except ValueError:
        print(" Payment Error: invalid input")

def check_courses(matric, course_reg, semester, academic_year):
    courses = course_reg.get_all_courses(matric, semester, academic_year)
    print("\n 📚 Your Courses:")
    total_units = 0
    for course in courses:
        print(f"\t{course[0]:10} - {course[1]:40} ({course[2]} units)")
        total_units += course[2]
    print(f"\nTotal Units: {total_units}")

def check_all_courses(matric, course_reg):
    courses = course_reg.get_all_courses(matric)
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

def admin_menu(auth, quiz, student_reg, matric, semester, academic_year):
    while True:
        print(f"\n=== Admin Dashboard ({matric})===")
        print(f"Current Session: {semester} {academic_year}")
        print(f"1. Create Database \n2. Create Table \n3. Set Session and Academic Year \n4. View all students \n5. Set Quiz Questions \n6. Add Courses \7. Logout")

        sub_choice = input("Enter choice: ").strip()

        if sub_choice == "1":
            pass

        elif sub_choice == "2":
            pass

        elif sub_choice == "3":
            sem = input("Set current semester. E.g Harmattan >>>  ").strip().capitalize()
            if sem in ["Harmattan", "Rain"]:
                semester = sem
                print(f"Semester set to: {semester}")
            else:
                print(" Invalid input")

            year = input("Set current academic year. E.g 2024 >>>  ").strip()
            if year.isdecimal() :
                academic_year = int(year)
                print(f"Academic Year set to: {academic_year}")
            else:
                print(" Invalid Year")
        
        elif sub_choice == "4":
            all_students(student_reg)

        elif sub_choice == "5":
            pass

        elif sub_choice == "6":
            pass

        elif sub_choice == "7":
            print("Logging Out ")
            break

        else:
            print("Invalid option, try again")

    return semester, academic_year

def student_menu(auth, payment, course_reg, student_reg, quiz, matric, semester, academic_year):
    while True:
        print(f"\n=== Student Dashboard ({matric}) ===")
        print(f"Current Session: {semester} {academic_year}")
        print("1. Make Payment")
        print("2. Register Course")
        print("3. View My Courses")
        # print("4. View All Students")
        print("4. Take Quiz")
        print("5. Check Result & Grade")
        print("6. Logout")

        sub_choice = input("Enter choice: ").strip()

        if sub_choice == "1":
            pay_tuition(payment, matric, semester, academic_year)

        elif sub_choice == "2":
            register_courses(matric, course_reg, semester, academic_year)

        elif sub_choice == "3":
            check_all_courses(matric, course_reg)

        elif sub_choice == "4":
            course_code = input("Enter course code for quiz: ").strip().upper()
            score = quiz.take_quiz(matric, course_code, semester, academic_year)
            print(f" Quiz completed. Score = {score}")

        elif sub_choice == "5":
            # course_code = input("Enter course code: ").strip().upper()

            score = quiz.get_grade(matric, semester, academic_year)
            if score:
                for i in score:
                    score = i[1]
                    grade = ""
                    if score >= 70: grade = "A"
                    elif score >= 60: grade = "B"
                    elif score >= 50: grade = "C"
                    elif score >= 45: grade = "D"
                    elif score >= 40: grade = "E"
                    else: grade = "F"
                    print(f"📊 Your grade for {i[0]} is {i[1]} {grade}")

        elif sub_choice == "6":
            print("Logging out...")
            break

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()