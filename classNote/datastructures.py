# list data type
names_of_students = ["Joshua", "Steven", "Emmanuel", 1, 4, 9, 6, 7.8, 8.5, True, False]
'''
# Methods
print(type(names_of_students))
print(len(names_of_students))
print(names_of_students[::2])

# Update at index
names_of_students[2] = "Ajayi"
'''

'''
names_of_students.append("Steven")
names_of_students.append(["Steven", "Precious"]) #adds list[] in list
names_of_students.insert(3, "Marvellous") #inserts at index
names_of_students.insert(5, ["Jeremiah", "Ibukun", "Marvelous", "Peter"]) # inserts list[] at index 5
names_of_students.extend(["Jeremiah", "Ibukun", "Marvelous", "Peter"])
names_of_students.reverse() # Reverse list item order
'''

# name = "Jeremiah".split()
# new_name = name.reverse()
# name = " ".join(new_name)
# print(name)
print(names_of_students)