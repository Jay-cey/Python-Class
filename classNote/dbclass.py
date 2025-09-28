import pymysql as pyms
import time


con_sql = pyms.connect(host = "127.0.0.1", user="root", password="Cxerrexc22.", db="studentsDB")
print("Connection Successful")

# create cursor after connection. It travels baack and forth to the database...
my_cursor = con_sql.cursor()

# conventionally write query in uppercase
# my_cursor.execute("CREATE DATABASE studentsDB")
# print("db created successfully")
# DB can only be created once

# include DB into connection =>>>>> line 4

# Create a table in DB using the cursor
# my_cursor.execute("CREATE TABLE student_record(std_id INT(3), full_name VARCHAR(20), email VARCHAR(50), gender VARCHAR(6), level VARCHAR(5))")
# print("Table created successfully")
# you cannot add space or hyphen.
# The number "3" in INT ()>>> the max figure range and in this case 999
# Comma "," signifies the end of a column
# DB must have at least a column
# The VARCHAR limits the number of character collected

# my_cursor.execute("SHOW DATABASES")
#show all databases

# for db in my_cursor:
    # print(db)
# my_cursor.close()
# close db to make efficient use of resources

# my_cursor.execute("SHOW COLUMNS FROM student_record")
# for col in my_cursor:
#     print(col)
# my_cursor.close
# Show all columns in DB

# my_query="ALTER TABLE student_record MODIFY full_name VARCHAR(25) AFTER email"
my_query="ALTER TABLE student_record MODIFY email VARCHAR(50) AFTER full_name"
my_cursor.execute(my_query)
# Modify table by moving the fullname column to the position after email    

# my_query=("ALTER TABLE student_record CHANGE std_id student_id INT(5) PRIMARY KEY AUTO_INCREMENT")
# my_cursor.execute(my_query)
# print("ID changed successfully")

# my_query=("ALTER TABLE student_record ADD phone_num VARCHAR(11) UNIQUE")
# Unique ==> "Constraint", all entries must be unique, no dupicates allowed
# Add ==> append column
# my_cursor.execute(my_query)
# print("Phone num added successfully")
# my_query =  "ALTER TABLE student_record DROP gender"
# my_cursor.execute(my_query)
# print("Gender dropped successfully")


# populate table
# my_query = "INSERT INTO student_record (email, full_name, level, phone_num) VALUES(%s,%s,%s,%s)"
# val = ("batman@gmail.com", "Bruce Wayne", "500l", "+167757898")
# my_cursor.execute(my_query, val)
# con_sql.commit()
# print(my_cursor.rowcount,"records inserted successfully")

# with more data 
# num = 2
# for i in range (num):
#     Full_name =  input("enter your full name ===> ")
#     email = input("Enter your email ===> ")
#     level = input("ENter your level >>> ")
#     Phone_num = input("enter your phone num ===> ")
#     my_query = "INSERT INTO student_record (full_name, email, level, phone_num) VALUES(%s,%s,%s,%s)"
#     val = (Full_name, email, level, Phone_num)
#     my_cursor.execute(my_query, val)
#     con_sql.commit()
# print(f"{num} records inserted successfully")

# fetch data 
# my_query="SELECT * FROM student_record" #gets all data in database
# my_cursor.execute(my_query)
# for each in my_cursor:
#     print(each)

# my_query="SELECT * FROM student_record WHERE level=%s" #gets all matching set of values
# val = "300l",
# my_cursor.execute(my_query, val)
# for each in my_cursor:
#     print(each)

# my_query= "SELECT * FROM student_record WHERE full_name LIKE '%ade%'" # gets record matching the str "ADE"
# my_cursor.execute(my_query)
# myreg = my_cursor.fetchall() # gets all matches
# for each in myreg:
#     print(each)

# my_query = "SELECT full_name FROM student_record" # gets the list of the full_name
# my_cursor.execute(my_query)
# for each in my_cursor:
#     print(each)
# myreg = my_cursor.fetchone() # gets the first match in table
# print(myreg)



my_cursor.execute("SELECT full_name FROM student_record")
row_count = my_cursor.rowcount
print(f"NUMBER of rows in 'your_table_name': {row_count}")


o_email = input("Your old fullname : ")
n_email = input("Your new fullname : ")
my_query = "UPDAATE student_record SET email=%s WHERE email=%s"
val = (n_email, o_email)
my_cursor.execute(my_query, val)
my_cursor.execute(my_query, val)
con_sql.commit()
print(my_cursor.rowcount, "record update sucessful")


o_fullname = input("Your old fullname :  ")
n_fullname = input("Your new fullname :  ")
my_query = "UPDATE student_record SET full_name=%s WHERE full_name=%s"
val = n_fullname, o_fullname
my_cursor.execute(my_query, val)
con_sql.commit()
print(my_cursor.rowcount, "record update successful")

my_query = "UPDATE student_record SET level='500l', full_name='Charles Dickens' WHERE phome_num=%s"
val = "+187564323"
my_cursor.execute(my_query, val)
con_sql.commit()
print(my_cursor.rowcount, "record updated successfully")

my_query = "DELETE FROM student_record WHERE full_name='Charles Dickens'"
val = "tyt"
my_cursor.execute(my_query)
con_sql.commit()

# Drop database
# my_query = "DROP DATABASE studentDB"
# my_cursor.execute(my_query)


count = 0
while count < 3 :
    full_name = input("Enter your full name >>> ") 
    password = input("Enter your password >>> ")
    my_query = "SELECE full_name, password from registration_tb WHERE full_name=%s AND password=%s"
    val = (full_name, password)
    my_cursor.execute(my_query, val)
    reg = my_cursor.fetchon()
    if reg:
        print("logged in successful")
        break
    else:
        count += 1
        print(f"Invalid credentials! You have {3 - count} attempts left.")
        if count == 3:
            print("You have exceeded your limit try again after ten seconds")
            time.sleep(10)