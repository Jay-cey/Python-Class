fname = input("\n enter your first name >>> ").lower().strip()
lname = input("\n enter your last name >>> ").lower().strip()

while True:
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
    passwd = input(" enter your password >>> ")
    confirm_passwd = input(" confirm password >>> ")
    if passwd == confirm_passwd:
        print("Registration Successful")
        break
    else:
        print("Password must match")
        continue


while True:
    login_email = input("\n enter your email >>> ").lower().strip()
    at_index = login_email.find("@")
    dot_com_index = login_email.find(".com")
    part_b4_at = login_email[:at_index + 1]
    part_after_at_before_dot_com = login_email[at_index + 1 : dot_com_index]
    if "@" in login_email and login_email.endswith(".com"):
        if part_after_at_before_dot_com:
            login_password = input(" enter your password >>> ")
            if login_password == passwd and login_email == email:
                print(f"Login Successful. You are welcome back, {fname.capitalize()} {lname.capitalize()}.")
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
