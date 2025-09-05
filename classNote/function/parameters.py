# Parameters and argument
# return statements
# Local and global scope
# Parameter Types
# Positional and keyword arguments
# Default parameters
# *args and **kwargs


# Parametized function
num2 = 2
def square_num(num1): #Function takes in parameters
    global num3 # Makes local variable global
    num3 = 3
    result = num1 ** 2 + num2 ** 2 + num3 ** 2
    return result 
# print(square_num(10))# Function call takes in arguments


def square_num(num4): #Function takes in parameters
    result = num4 ** 2 + num2 ** 2 + num3 ** 2
    return result 
# print(square_num(7)) # Function call takes in arguments



# Keyword Arg means you're explicitly assigning the value to parameter names

def welcome_user(fname, m_name,  lname="Ade"): # Keyword argument can only come after using positional parameters first
    return f"Dear {lname}, {fname} {m_name} you are welcome to SQI Ogbomoso campus."
# print(welcome_user(lname="Ogunleye", m_name="Ola", fname="Jeremiah"))

# Arbitrary arguments **kwargs
def welcome( **name ):
    return f"Dear {name} you are welcome to SQI Ogbomoso campus."
# print(welcome(lname="Ogunleye", m_name="Ola", fname="Jeremiah"))

# Arbitrary arguments *args
def welcome( *name ):
    return f"Dear {name} you are welcome to SQI Ogbomoso campus."
# print(welcome("Ogunleye", "Ola", "Jeremiah"))

# print(sum([19, 2, 4, 5, 9]))

# Map
nums = [1, 2, 3, 4, 5, 6]
def square_num3(num):
    result = num * 2
    return result
# print(list(map(square_num3, nums)))

# Ennumerate
names = ("tolu", "bolu", "titi")
for index, name in enumerate(names):
    # print(index+1, name)
    # print(index+1, name)
    pass

def odd_even(num):
    if num % 2 == 0:
        return True
filtered_nums = filter(odd_even, nums)
# print(list(filtered_nums))

# zip
nums1 = [7, 8, 9, 10, 11, 12]
zipped = zip(nums, nums1)
# print(list(zipped))

# any
# none, 0, "", False are considered as False
# number other than 0, non empty string, non empty list, True are considered as True 
list1 = [0, "", False, 5, 8]
# print(any(list1))
# print(any(x > 10 for x in nums))

# all
# returns True if all elements in the iterable are true and if the iterable is empty
# returns False if any element in the iterable is false
# print(all(list1))
# print(all(x > 0 for x in nums))
# print(all(nums))

# sorted
# takes an iterable and returns a sorted list, by default in ascending order
unsorted_list = [5, 3, 6, 2, 8, 1, 4, 7]
# print(sorted(unsorted_list))
unsorted_words = ["banana", "apple", "orange", "grape"]
# print(sorted(unsorted_words))
# print(sorted(unsorted_words, key=len))
# print(sorted(unsorted_words, reverse=True))

# reversed
# returns a reversed iterator without modifying the original iterable
# print(list(reversed(unsorted_list)))
