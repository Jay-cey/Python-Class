"""
Basics syntax of python programming
    Python syntax is designed to bbe clean, readable and plain. Pythonn syntax is case sensitive.
Variables : stores values temporarily in memory
Indentation
    Indentation is paramount
Data types
Naming conventions
Type Conversions
    Tuples can be created without the use of parenthesis '()'
Python Operators
"""

# variable
name = "Jeremy"
Name = "Jeremiah"
print(Name); print(name)

# naming conventions
"""
Pascal
camelCase
snake_case
"""

# Pascal
NameOfStudents = "Jay", "Ray"
# camel
nameOfStudents = "Emmanuel", "Stephen"
# snake
name_of_students = "Marvellous", "Marvelous"
print(NameOfStudents)
print(nameOfStudents)
print(name_of_students)

num1 = int("33")
num2 = 32

print(num1 + num2)
class_register = ("Emmanuel", "Ajayi")
class_register = ["Emmanuel", "Ajayi", 76, True, 101.0]
print(type(class_register[4]))
class_register = {"name" : "Ajayi", "age" : 76, "is tall": True, "account balance" : 101.1}
print(type(class_register["is tall"]))
class_register = { 5, 6, 8, 4, 2}
print(class_register)
# sets are generally unordered, but when working with integers, they are arranged in ascending order

fname = 'Daniel'
lname = 'Jobs'
course = 'Data Science'
welcome_note = 'You are welcome to python class'
print(fname + lname + 'You are welcome to python class' + course + 'option')
print(fname, lname, 'You are welcome to python class', course, 'option')
print(f"{fname} {lname}, You are welcome to python class {course} option.")

# assignment
# read on other methods of concatenation and include two examples each


# Operators
'''
Types of operators
** Arithmetic operators (+, -, *, /, //, %, **)
** Logical operators (and, or, not)
** Membership operators (in, not in)
** Assignment operators (=, ==, +=, -=, *=)
** Comparison operators (<, >, <=, >=)


The NOT operator is going to return true when the value is 0
OR either of the conditions must be true
AND both of the conditions must be true
NOT __0, "", true
'''

val1 = 1
val2 = 2
answer = val1 / val2
print(answer)
answer = val1 // val2
print(answer)
answer = val1 % val2
print(answer)

# if val1 > 3 and val2 == 2:
if val1 > 3 or val2 == 2:
    print("This is true")
# print("This is false")

print(not "")

list_of_item = ["Mongo", "Postgres", "Redis", "rubby"]
if "mango" in list_of_item :
    print("You are correct")


count = 0
name = input(" Enter your name >>> ")
for i in name:
    count += 1
    print(f"{i} is character {count}")