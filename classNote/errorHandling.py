# Error Handling
# Exceptions are events that occur which alter the flow of a program
# Three keywords for catching exceptions -- Try, Except, Finally(optional)... for try and except, else is optional
# try to avoid using except bare/alone 
# you can have as many except as possible under one try 

# num = int(input("Enter a number >>> "))
# print(num)

# try:
#     num = int(input("Enter a number >>> "))
#     print(num)
# except ValueError:
#     print("Invalid input, value must be a number")


def ent_app():
    try:
        name = input('Enter your name >>> ').strip()
        if not name or any(any_letter.isdigit() for any_letter in name):
            raise ValueError('Name should not contain a digit or be empty')
        
        age = input('Enter your age >>> ').strip()
        if not age.isdigit() or int(age) <= 0:
            raise ValueError('Age should be digit greater than zero nd cannot be empty')
        
        age = int(age)
        pass_code = '1234'
        access_code = input('Enter your access code >> ').strip()
        if access_code != pass_code:
            raise PermissionError('Incorrect access code.')
        
        print(f"\nWelcome {name}, age {age}! you have successfully entered.")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except PermissionError as pe:
        print(f"Access Denied: {pe}")

ent_app()

# Module and Library

# A module is a file that consists of a reusable code, created using the .py extension

# Regular Expressions are key shortuts/shorthands. A sequence of charcters that from pattern of search

import re
# $ ==endswith 