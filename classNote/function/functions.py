'''
Function Basics
Defining and calling functions
Parameters and argument
return statements
Local and global scope
Parameter Types
Positional and keyword arguments
Default parameters
*args and **kwargs
Built-in Functions
map, filter, zip, enumerate
sorted, reversed, any, all
len, sum, min, max
'''
import time

# function is a block of code that carries out a particular type
# Built-in functions, User defined functions
# Function declaration, definition, and invoking

each_student = {}
student_register = []
def register():
    name = input("Register \n enter your name >>> ").lower().strip()
    while True:
        email = input("\n enter your email >>> ").lower().strip()
        for student in student_register:
            if email == student['email']:
                print("User already exists. Please try logging in or use a different email.")
            home_page()
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
            break
        else:
            print("Password must match")
            continue
    each_student.update(name=name, email=email, passwd=passwd)
    student_register.append(each_student)
    login()
    # print(each_student)


def login():
    print("Login")
    count = 3
    while True:
        # count += 3
        email = input("Enter your email >>> ").lower().strip()
        password = input("Enter your password >>> ")
        if student_register == []:
            print("No registered users found. Please register first.")
            home_page()
        for students in student_register:
            if email == students['email'] and password == students['passwd']:
                print(f"Login Successful \n Welcome {students['name']}!!!")
                break
            else:
                count -= 1
                print(f"invalid input: try again... you have {count} attempts left")
                if count == 0:
                    print(f"invalid input: you have exceeded your attempts. Try again after 30 seconds")
                    time.sleep(30)
                    login()
        # break

def about():
    print("This is python class and we are currently in week five. \n You can join the next cohort")

def contact_us():
    print("This is python class and we are currently in week five. \n call the class rep for more information")

def home_page():
    print("""
            1. Login
            2. Register
            3. About
            4. Contact
            5. Exit
        """)
    user_inp = input("options >>> ")
    if user_inp == "1":
        login()
    elif user_inp == "2":
        register()
    elif user_inp == "3":
        about()
    elif user_inp == "4":
        contact_us()
    elif user_inp == "5":
        exit()
    else:
        print("invalid input")

while True:
    home_page()
                    

# register()

# use time module, 30 minutes
# check if user already exists, output "user already exists"
# fix login