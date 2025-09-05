'''
Python provides a set of built-in data types that serve as the foundation for storing and manipulating different kinds of data. Understanding these data types is crucial for effective Python programming, as they determine what operations can be performed on the data and how the data is stored in memory.

Python's Data Type System

Python is dynamically typed, which means variable types are determined at runtime rather than during compilation. This allows variables to change types during program execution, providing flexibility but requiring careful handling to prevent runtime errors. Unlike statically typed languages, Python doesn't require explicit type declarations - the interpreter automatically infers the type based on the assigned value.

Python treats everything as objects, meaning there are no primitive data types in the traditional sense. All data values are objects with identity, type, and value properties. This object-oriented approach distinguishes Python from languages like Java or C++ that have primitive types.
'''

# Numeric Data Types

#  Integer (int)
# Integers represent whole numbers without decimal points. Python integers have unlimited precision, meaning they can represent arbitrarily large numbers.

x = 42
large_number = 1_000_000_000  # Underscores for readability
negative = -256

'''
Float (float)
Floating-point numbers represent real numbers with decimal points, accurate to approximately 15 decimal places.
'''
pi = 3.14159
scientific = 1.23e-4  # Scientific notation

'''
Complex (complex)
Complex numbers consist of real and imaginary parts, denoted with 'j' for the imaginary unit.
'''
z = 3 + 4j
real_part = z.real    # 3.0
imag_part = z.imag    # 4.0

'''
String (str)
Strings represent Unicode text data and are immutable sequences of characters. They can be created using single, double, or triple quotes.
'''
single_quote = 'Hello, World!'
double_quote = "Hello, World!"
triple_quote = """This is a
multiline string"""

'''
List (list)
Lists are ordered, mutable collections that can contain items of different data types. They support indexing, slicing, and various modification operations.
'''
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

'''
Tuple
Tuples are ordered, immutable sequences similar to lists but cannot be modified after creation[9][11]. They're useful for storing related data that shouldn't change.
'''
coordinates = (10.0, 20.0)
person = ("Alice", 30, "Engineer")

'''
Range
Range objects represent immutable sequences of numbers, commonly used in loops.
'''
numbers = range(5)      # 0, 1, 2, 3, 4
even_nums = range(2, 10, 2)  # 2, 4, 6, 8

'''
Dictionary (`dict`)
Dictionaries store key-value pairs and are mutable, unordered collections. Keys must be immutable types.
'''
student = {"name": "John", "age": 25, "grade": "A"}


'''
Set (set) and Frozen Set (frozenset)
Sets contain unique, unordered elements. Sets are mutable, while frozen sets are immutable.
'''
unique_numbers = {1, 2, 3, 4, 5}
immutable_set = frozenset([1, 2, 3])

'''
Boolean (`bool`)
Boolean values represent truth values: `True` or `False`. They're subclasses of integers where `True` equals 1 and `False` equals 0.
'''
is_valid = True
is_empty = False



'''
Mutability vs Immutability
Python data types are classified as either mutable or immutable:

Immutable Types
- Numbers (`int`, `float`, `complex`)
- Strings (`str`)
- Tuples (`tuple`)
- Frozen sets (`frozenset`)
- Bytes (`bytes`)
- Boolean (`bool`)
- None (`NoneType`)

Mutable Types
- Lists (`list`)
- Dictionaries (`dict`)
- Sets (`set`)
- Bytearrays (`bytearray`)

Immutable objects cannot be changed after creation, while mutable objects allow in-place modifications. This distinction affects memory usage, performance, and program behavior.
'''


# Type Checking and Conversion
'''
Checking Types
Python provides several ways to check object types:
'''
x = 42
print(type(x))           # <class 'int'>
print(isinstance(x, int)) # True

'''
Type Conversion
Python supports explicit type conversion between compatible types:
'''
x = "123"
y = int(x)      # Convert string to integer
z = float(y)    # Convert integer to float
s = str(z)      # Convert back to string

'''
Dynamic Typing Implications

Python's dynamic typing provides several advantages:
- Flexibility: Variables can change types during execution
- Rapid prototyping: Less boilerplate code for type declarations
- Simplified syntax: No need for explicit type declarations
- Enhanced productivity: Focus on logic rather than type management

Drawbacks:
- Runtime errors: Type mismatches discovered only during execution
- Debugging challenges: Harder to track type-related issues
- Performance overhead: Type checking happens at runtime

Understanding Python's data types is fundamental for writing efficient, maintainable code. The language's dynamic typing system provides flexibility while its rich set of built-in types offers powerful tools for data manipulation and storage across various programming scenarios.
 
'''
# Example usage of various data types
# Numeric types
a = 10          # int
b = 3.14        # float
c = 2 + 3j      # complex
print(f"Integer: {a}, Float: {b}, Complex: {c}")

# String type
name = "Alice"
greeting = f"Hello, {name}!"
print(greeting)
# List type
colors = ["red", "green", "blue"]
colors.append("yellow")
print("Colors:", colors)

# Tuple type
point = (5, 10)
print("Point coordinates:", point)
# Dictionary type
person = {"name": "Bob", "age": 30}
person["city"] = "New York"
print("Person info:", person)
# Set type
unique_items = {1, 2, 3, 4}
unique_items.add(5)
print("Unique items:", unique_items)
# Boolean type
is_active = True
print("Is active:", is_active)
# Range type
print("Range of numbers:", list(range(5)))