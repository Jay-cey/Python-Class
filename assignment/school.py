import time
# A school management system
all_students = []  # This will hold all student profiles
# each_student = {}  # This will hold individual student details
all_quizzes = []  # This will hold all quizzes/exams
payment_status = []
payment_records = []
# quiz_results = []
login_status = False
profile_update_status = False
questions_and_answers = (
        ("What is the capital of England? ", ("a) Auckland","b) Paris", "c) London", "d) Berlin"), "c"),
        ("What is 2 + 2? ", ("a) 4", "b) 22", "c) 5", "d) 3"), "a"),
        ("What is the largest planet in our solar system? ", ("a) Mars", "b) Saturn", "c) Venus", "d) Jupiter"), "d"),
        ("Who wrote 'Romeo and Juliet'? ", ("a) Charles Dickens", "b) Mark Twain", "c) William Shakespeare", "d) Jane Austen"), "c"),
        ("What is the boiling point of water in Celsius? ", ("a) 90°C", "b) 100°C", "c) 110°C", "d) 120°C"), "b")
    )

print("School Management System")

def create_student_profile():
    while True:
        name = input("Register \n enter your name >>> ").lower().strip()
        email = input("\n enter your email >>> ").lower().strip()
        for student in all_students:
            if email == student['email']:
                print("User already exists. Please try logging in or use a different email.")
            home()
        at_index = email.find("@")
        dot_com_index = email.find(".com")
        # part_b4_at = email[:at_index + 1]
        part_after_at_before_dot_com = email[at_index + 1 : dot_com_index]
        if "@" in email and email.endswith(".com"):
            if part_after_at_before_dot_com:
                break
            else:
                print("invalid email! your email must have '@' and should end with '.com'")
                continue
        else:
            print("invalid email! your email must have '@' and should end with '.com'")
            continue

    while True:
        passwd = input(" enter your password >>> ")
        confirm_passwd = input(" confirm password >>> ")
        if passwd == confirm_passwd:
            print("Registration Successful")
            global matriculation_number
            matriculation_number = 250000 + len(all_students) + 1
            print(f"Your matriculation number is {matriculation_number}")
            break
        else:
            print("Password must match")
            continue
    each_student = {"name":name, "email":email, "passwd":passwd, "matric_number":matriculation_number}
    all_students.append(each_student)
    login()
    return
    # print(each_student)

def login():
    print("Login")
    count = 3
    while True:
        # count += 3
        email = input("Enter your email >>> ").lower().strip()
        password = input("Enter your password >>> ")
        if all_students == []:
            print("No registered users found. Please register first.")
            home()
        for student in all_students:
            if email == student['email'] and password == student['passwd']:
                global login_status
                login_status = True
                global logged_in_student
                logged_in_student = student
                print(f"Login Successful \n Welcome {student['name']}!!!")
                home()
                break
            else:
                count -= 1
                print(f"invalid input: try again... you have {count} attempts left")
                if count == 0:
                    print(f"invalid input: you have exceeded your attempts. Try again after 30 seconds")
                    time.sleep(30)
                    login()
                    return
        # break


def view_student_profiles():
    print("Viewing your student profile...")
    for student in all_students:
        if student["matric_number"] == matriculation_number:
            # print(student['name'].capitalize(), student['email'])
            print(f"Name: {student['name'].capitalize()}\nEmail: {student['email']}\nMatriculation Number: {student['matric_number']}")
            if 'age' in student:
                print(f"Age: {student['age']} \nAddress: {student['address']} \nPhone Number: {student['phone_number']}")
            return
    print("No profile found.")
    # Placeholder for actual implementation

def update_student_profile():
    global age, address, phone_number
    age = input("Enter your age >>> ").strip()
    address = input("Enter your address >>> ").strip()
    phone_number = input("Enter your phone number >>> ").strip()
    for student in all_students:
        if student["matric_number"] == matriculation_number:
            student.update(age=age, address=address, phone_number=phone_number)
            print("Profile updated successfully.")
            global profile_update_status
            profile_update_status = True
            return

def delete_student_profile():
    print("Deleting a student profile...")
    # Placeholder for actual implementation

def pay_fees():

    print("Processing fee payment...")
    # Placeholder for actual implementation

def see_payment_history():
    print("Viewing payment history...")
    # Placeholder for actual implementation

def register_for_quizzes():
    global register_status
    register_status = True
    if profile_update_status:
        print("You have successfully registered for the quiz...")
    else:
        print("Please update your profile before registering for the quiz.")
        update_student_profile()

def take_quizzes():
    if register_status and login_status:
        print(f"Welcome to quizzes/exams... {logged_in_student["name"].capitalize()}")
        take_quiz = input("Do you want to take a quiz? (yes/no) >>> ").lower().strip()
        if take_quiz in ["yes", "y"]:
            score = 0
            for question, option, answer in questions_and_answers:
                a, b, c, d = option
                ans = input(f"\n {question} \n {a} {b} {c} {d} \n\t >>> ").strip().lower()
                if ans in ["a", "b", "c", "d"] and ans == answer:
                    score += 1
            logged_in_student.update(score=score)
            print(f"{logged_in_student['name'].capitalize()}, your total score is {score}/{len(questions_and_answers)}")
        elif take_quiz in ["no", "n"]:
            print("You chose not to take the quiz. Returning to home.")
            home()
    else:
        print("You are not logged in. Please log in to take the quiz")
        login()

def view_results():
    print("Viewing results...")
    # Placeholder for actual implementation

def first_page():
    print("Welcome to the School Management System")
    while True:
        print("""\nMenu:
              1. Create Student Profile
              2. Login
              3. Exit
              """)
        choice = input("Please select an option (1-3): ").strip()
        if choice == '1':
            create_student_profile()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break

def home():
    print("Welcome to the School Management System")
    while True:
        print("""\nMenu:
              1. View Student Profiles
              2. Update Student Profile
              3. Delete Student Profile
              4. Pay Fees
              5. See Payment History
              6. Register for quizzes/Exams
              7. Take Quizzes/Exams
              8. View Results
              9. Exit
              """)
        choice = input("Please select an option (1-10): ").strip()
        if choice == '1':
            view_student_profiles()
        elif choice == '2':
            update_student_profile()
        elif choice == '3':
            delete_student_profile()
        elif choice == '4':
            pay_fees()
        elif choice == '5':
            see_payment_history()
        elif choice == '6':
            register_for_quizzes()
        elif choice == '7':
            take_quizzes()
        elif choice == '8':
            view_results()
        elif choice == '9':
            print("Exiting the system. Goodbye!")
            break

first_page()