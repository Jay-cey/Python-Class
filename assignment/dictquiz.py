user_database = []
login_state = True
questions_and_answers = {
    "What is the capital of England? ": {
        "options": ("a. Auckland", "b. Paris", "c. London", "d. Berlin"),
        "answer": "c"
    },
    "What is 2 + 2? ": {
        "options": ("a. 4", "b. 22", "c. 5", "d. 3"),
        "answer": "a"
    },
    "What is the largest planet in our solar system? ": {
        "options": ("a. Mars", "b. Saturn", "c. Venus", "d. Jupiter"),
        "answer": "d"
    },
    "Who wrote 'Romeo and Juliet'? ": {
        "options": ("a. Charles Dickens", "b. Mark Twain", "c. William Shakespeare", "d. Jane Austen"),
        "answer": "c"
    },
    "What is the boiling point of water in Celsius? ": {
        "options": ("a. 90°C", "b. 100°C", "c. 110°C", "d. 120°C"),
        "answer": "b"
    }
}

while True:
    fname = input("\n enter your first name >>> ").lower().strip()
    lname = input("\n enter your last name >>> ").lower().strip()
    email = input("\n enter your email >>> ").lower().strip()
    at_index = email.find("@")
    dot_com_index = email.find(".com")
    part_b4_at = email[:at_index + 1]
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
    passwd = input(" enter your password, must be longer than 8 characters >>> ")
    confirm_passwd = input(" confirm password >>> ")
    if len(passwd) >= 8:
        if passwd == confirm_passwd:
            user_database.append([fname, lname, email, passwd])
            print("Registration Successful")
            break
        else:
            print("Password must match")
            continue
    else:
        print("Password length must be 8 or longer")


while login_state:
    login_email = input("\n enter your email >>> ").lower().strip()
    at_index = login_email.find("@")
    dot_com_index = login_email.find(".com")
    part_b4_at = login_email[:at_index + 1]
    part_after_at_before_dot_com = login_email[at_index + 1 : dot_com_index]

    if "@" in login_email and login_email.endswith(".com"):
        if part_after_at_before_dot_com:
            login_password = input(" enter your password >>> ")
            for user in user_database:
                if login_password in user and login_email in user:
                    print(f"Login Successful. You are welcome back, {fname.capitalize()} {lname.capitalize()}.")
                    take_quiz = input("Do you want to take a quiz? (yes/no) >>> ").lower().strip()
                    while True:
                        if take_quiz in ["yes", "y", "no", "n"]:
                            break
                        else:
                            take_quiz = input("Invalid input. Please enter 'yes' or 'no' >>> ").lower().strip()
                    if take_quiz in ["yes", "y"]:
                        score = 0
                        for question in questions_and_answers:
                            a, b, c, d = questions_and_answers[question]["options"]
                            answer = questions_and_answers[question]["answer"]
                            ans = input(f"\n {question} \n {a} {b} {c} {d} \n\t >>> ").strip().lower()
                            if ans in ["a", "b", "c", "d"] and ans == answer:
                                score += 1
                        print(f"{fname.capitalize()}, your total score is {score}/{len(questions_and_answers)}")
                    login_state = False
                    break
                else:
                    print("Invalid Username or Password")
                    continue    
        else:
            print("invalid email!")
            continue
    else:
        print("invalid email! your email must have '@' and should end with '.com'")
        continue

