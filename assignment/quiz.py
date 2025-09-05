user_database = []
login_state = True
questions_and_answers = (
        ("What is the capital of England? ", ("a) Auckland","b) Paris", "c) London", "d) Berlin"), "c"),
        ("What is 2 + 2? ", ("a) 4", "b) 22", "c) 5", "d) 3"), "a"),
        ("What is the largest planet in our solar system? ", ("a) Mars", "b) Saturn", "c) Venus", "d) Jupiter"), "d"),
        ("Who wrote 'Romeo and Juliet'? ", ("a) Charles Dickens", "b) Mark Twain", "c) William Shakespeare", "d) Jane Austen"), "c"),
        ("What is the boiling point of water in Celsius? ", ("a) 90°C", "b) 100°C", "c) 110°C", "d) 120°C"), "b")
    )

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
                    if take_quiz == "yes":
                        score = 0
                        for question, option, answer in questions_and_answers:
                            a, b, c, d = option
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




# take_quiz = input("Do you want to take a quiz? (yes/no) >>> ").lower().strip()
# if take_quiz == "yes":
#     score = 0
#     for question, option, answer in questions_and_answers:
#         a, b, c, d = option
#         ans = input(f"{question} \n {a} {b} {c} {d} \n\t >>> ")
#         if ans == answer:
#             score += 1
#     print(f"{fname.capitalize()} Your total score is {score}/{len(questions_and_answers)}")








# food_joint = (("McDonald's", "$20", "seattle"), ("Burger King", "$15", "bellevue", "Tigger"), ("Wendys", "$10", "redmond"))
# joint1, joint2, joint3 = food_joint
# # print(joint1)

# # for food, price, location in food_joint:
# #     print(food, "=>", )

# for food, *others in food_joint:
#     print(others)