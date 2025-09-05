# users = []
signup_email = input(" Enter your email: ")
signup_password = input(" Enter your password: ")

print(f"Thank you for signing up, {signup_email}!")

while True :
    print("Please login to continue.")
    login_email = input(" Enter your email to login: ")
    login_password = input(" Enter your password to login: ")
    if login_email == signup_email and login_password == signup_password:
        print(f"Welcome back, {login_email}!")
        break
    else:
        print("Login failed. Please check your email and password.")


