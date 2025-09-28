import os

my_file = open("example.txt", "r")
# print(my_file.read())
my_file.close()

# Opening a file from any directory (use double backslashes or raw string to avoid errors): Python treats a single backslash as an escape character, but using double backslashes (\\) or a raw string (r"path") correctly handles file paths

# file_path = r"C:\\Users\\HomePC\\Python\\assignment\\example2.txt"
file_path = r"C:/Users/HomePC/Python/assignment/example2.txt"
with open(file_path, "r") as file:
    print(file.read())

# Writing to a file overwrites existing content
with open("example.txt", "w") as file:
    file.write("This is the overwriting string")

# Appending to a file
with open("example.txt", "a") as file:
    file.write("\nNew content added")

# Creating a new file using "x" mode (throws error if the file already exists)
# if not os.path.exists("newfile.txt"):
#     with open("newfile.txt", "x") as file:
#         file.write("This is a new file created in py.")
# else:
#     print("File already exists")

# Opening a binary file in read modes
# with open(r"C:/Users/HomePC/Documents/Finals/confusion_matrix.png", "rb") as file:
#     data = file.read()
#     print("Binary file read successfully")

# with open(r"C:\\Users\\HomePC\\Documents\\Finals\\gesture_data.csv", "r") as file:
#     data = file.read()
#     print(data)

# reading and writing in update mode ('r+)
# with open("example.txt", 'r+') as file:
#     content = file.read() # Read the entire file content
#     file.seek(0, 2)
#     file.write("This mode is a special mode. I want to add more")
#     file.seek(0)
#     updated_content = file.read()
#     print(updated_content) 

# with open("example.txt", "r+") as files:
#     content = file.read()
#     file.write("\nAppending in r+ mode.")
#     file.seek(0)
#     updated_content = file.read()
#     print(updated_content)

# OS Interaction
print("Current working directory:", os.getcwd())

new_directory = "newfolder"
if not os.path.exists(new_directory):
    os.makedirs(new_directory)
    print("Directory created successfully.")
else:
    print("Directory already exists.")

try:
    with open(r'newfolder/new_file2.pdf', 'x') as file:
        file.write("This file is created inside the directory.")
        print("File created successfully")
except FileExistsError:
    print("File already exists")

file_path = os.path.join((new_directory, "example.txt"))
if not os.path.exists(file_path):
    with open(file_path, "w") as file:
        file.write("This file is created into the new directory")
    print("File created successfully")
else:
    print("File already exists")

os.chdir(new_directory)
print("New working directory:", os.getcwd())

def current_path():
    print("Current working directory before")
