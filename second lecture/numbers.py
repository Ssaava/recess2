# converting a float to a float
num = 3.4
print(complex(num))

# coverting a float to an integer
# casting is about assigning a data type to a variable

print("Integer: ", int(num))

# Casting in python
h = int(20)  # h is 20
a = int("8")  # a is 8
print(type(a))

# Strings
name = "Emmanuel"
print(name)

# Multiline strings
words = """
Hello world 
How is the going 
How is Uganda the Pearl of Africa
"""
print(words)

# Strings as arrays
print(words[34], " is the 34th character in the string")

# Exercise on Strings
# one: use the len() to determine length of the String
print(len(words))

# two: use  for loop with strings
for i in range(len(words)):
    print(words[i])

# three: give an example of slicing a String
print(words[2:20])

# how to modify the String
# print(words.upper())
# print(words.lower())

# Remove white spaces from the String
b = "After noon"
print(b.strip())

# String concatination can be done with the + symbol or the join method
a = "Emma"
b = "nuel"
print(a + b)
c = a.join(b)
print(c)


# Booleans in Python
# Booleans are a data type in Python that represent truth values.
# Booleans are often used in conditional statements to control the flow of the program.

# Examples
# Useing comparison operators like <, >, ==, <=, >=, != to evaluate conditions
# Combining conditions using logical operators like: logical and, logical or,  logical not

# Exercise
# Use boolean values and conditions to control program flow.
b = True  # this is the boolean value that we using for this while loop
i = 0
while b:
    if (i == 5):
        print(f"The number of times has reached {i}")
        b = False
    i += 1
