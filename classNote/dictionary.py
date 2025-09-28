# Dictionary

electronics = {
                "name" : "Television",
                "brand" : "LG", 
                "colour" : "Black", 
                "inches" : "75'"
            }
item = dict(name="telemundo", brand="Hisense", colour="Brown")

'''
print(type(electronics))
print(type(item))
print(len(electronics))

# how to access dict element
print(electronics["name"])
print(electronics.keys())
print(electronics.values())
print(electronics.items())

for each_key, each_value in electronics.items() :
    print(each_key, ":", each_value)
'''
# You can update multiple items a the same time
item.update(inches="65'")
electronics.update(inches="65'")
# print(electronics)
# print(f"{item = }")

# print(item.get("brand"))
# item.clear()
lecs = item.copy()
# print(f"{lecs = }")
item.pop("brand")
item.popitem()
# print(f"{item = }")


'''
student_register = {}
each_student=[]
numbering = 0
for each in range(3):
    numbering += 1
    name = input("enter your name >>> ")
    email = input("enter your email >>> ")
    passwd = input("enter your password >>> ")
    each_student.append((name, email, passwd))
    student_register[f"student{numbering}"]=each_student
    each_student=[]
# print(f"{student_register = }")
print(student_register)
'''

student_register = {}
each_student=[]
numbering = 0
for each in range(3):
    numbering += 1
    name = input("enter your name >>> ")
    email = input("enter your email >>> ")
    passwd = input("enter your password >>> ")
    student_register.update(name=name, email=email, passwd=passwd)
    each_student.append(student_register)
print(each_student)
