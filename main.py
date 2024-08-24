

# Simple print
print("Hello, World!")

# Print multiple values
print("The sum of 5 + 10 is:", 5 + 10)

# Custom separator and end
print("Hello", "World", sep=", ", end="!")
# Key Points:

# Debugging: Print statements are often used to check values of variables during code execution.
# Formatting: You can control the format and layout of printed text using sep, end, and string formatting (e.g., f-Strings).
# 2. Strings
# Purpose
# Single-line strings
single_quote_string = 'Hello, World!'
double_quote_string = "Hello, World!"

# Multi-line strings
multi_line_string = '''This is
a multi-line
string.'''

# Concatenation
greeting = "Hello" + " " + "World!"

# Repetition
echo = "Echo! " * 3

# Slicing
substring = greeting[0:5]  # Outputs: 'Hello'
# String Methods:


# Convert to upper case
print(greeting.upper())  # Outputs: HELLO WORLD!

# Find a substring
position = greeting.find("World")  # Outputs: 6
Key Points:


 # 3. f-Strings

name = "Alice"
age = 30
greeting = f"My name is {name} and I am {age} years old."

# Using expressions inside f-Strings
calculation = f"5 + 10 = {5 + 10}"

# 4. Operators

# Operators are symbols that perform operations on variables and values. Python supports various types of operators.

# Types of Operators:

# Arithmetic Operators:

"""+: Addition
-: Subtraction
*: Multiplication
/: Division (results in a float)
//: Floor Division (results in an integer)
%: Modulus (remainder of division)
**: Exponentiation"""


a = 10
b = 3
print(a + b)  # Outputs: 13
print(a // b)  # Outputs: 3
print(a % b)  # Outputs: 1
Comparison Operators:

"""==: Equal to
!=: Not equal to
>: Greater than
<: Less than
>=: Greater than or equal to
<=: Less than or equal to"""


x = 5
y = 10
print(x == y)  # Outputs: False
print(x < y)  # Outputs: True
Logical Operators:

"""and: Returns True if both statements are true.
or: Returns True if at least one statement is true.
not: Reverses the result, returns False if the result is true."""


a = True
b = False
print(a and b)  # Outputs: False
print(a or b)  # Outputs: True
print(not a)  # Outputs: False

# 5. Lists & Tuples
Lists:


my_list = [1, 2, 3, "apple", "banana"]
Operations:


# Accessing elements
print(my_list[0])  # Outputs: 1

# Modifying elements
my_list[1] = "orange"
print(my_list)  # Outputs: [1, "orange", 3, "apple", "banana"]

# List methods
my_list.append("cherry")
print(my_list)  # Outputs: [1, "orange", 3, "apple", "banana", "cherry"]
# Tuples:


my_tuple = (1, 2, 3, "red", "green")
Operations:


# Accessing elements
print(my_tuple[0])  # Outputs: 1

# Tuples are immutable
# my_tuple[1] = "blue"  # This will raise an error


# Lists: Use lists when you need a sequence that can change.
# Tuples: Use tuples for fixed sequences that should not change.
# 6. Loops (for and while)
# For Loops:

# Purpose: for loops are used to iterate over a sequence (like a list, tuple, string, or range).
for item in sequence:
    # Code block to execute


fruits : list[str]= ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


while condition:
    # Code block to execute


count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1



# 7. Input Handling

user_input = input("Prompt message")

# Asking for user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello, {name}! You are {age} years old.")

#  8. Functions

def function_name(parameters):
    # Code block to execute
    return value

def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)  # Outputs: Hello, Alice!
#  Function Parameters:

# Positional Arguments: Standard arguments passed to a function.
# Keyword Arguments: Arguments passed with a key-value pair.

def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Outputs: 8
