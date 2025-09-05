list_of_names = ['Tolu', 'Ibukun', 'Marvellous', "Joshua", "Peter", "Ajayi", 'Jeremiah', 'Steven', 'Emmanuel']
count = 0

# for each_name in list_of_names :
#     count+=1
#     if len(each_name) == 6:
#         continue
#     print(f"{count}. {each_name}")


# string and it's methods

#replacing character in a string
name = "Jeremiah"
print(name.capitalize())

# startswith, endswith, join, split, .join
name1 = "Jeremiah"
print(name.split('e'))
print(name.startswith("J"))
print(name.endswith("h"))
name2 = "Ogunleye"
print(", ".join((name1, name2)))

#getting index
name = "Ibukun"
new_name = name.index("k")
print(new_name)

#replacing character in a string
name = "Jeremiah"
print(name.replace("e", "i"))

# replacing item in a list
name = ["jeremiah", "Joshua", "Ibukun", "Mayowa"]
name[new_name] = "Jeremy"
print(name)

#strip of whitespace
name = "   Jerry"
name = name.strip()
print(name)
'''

'''
