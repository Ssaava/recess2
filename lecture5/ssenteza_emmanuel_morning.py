'''
lecture 5 morning session
1: regular expressions
2: generators and iterators 
3: decorators
4: content managers
5: multithreading and multprocessing 
'''

# 1: regular expressions
'''
\d: matches any digit (0-9)
\w: matches any alphanumeric character (a-z, A-Z, 0-9, and underscore)
\s: matches any whitespace character 
.: matches any character exceot a new line
*: matches zero or more occurences of the preceeding character or group
+: same as above but matches one or more occurences of the preceding character
?: same as above but matches zero or one occurences of the preceding character
[]: matches any character within the square brackets
[^ ]: matches any character not within the square brackets
^: matches the start of a line 
$: matches the end of a line 
'''

# matching and searching
# regex re.match() is the function used for matching
# regex re.match() is the function used for matching
# regex re.findall() is the function used for find all

# Example1 demonstrating regex to match password, match group words,
# match all numbers

import re
text = "Hello, my name is Emma. I am a programmer with 10 years of experience"

# match first word
match = re.search(r"\b\w+\b", text)
# if match:
#     print("Matches: ", match.group())

matches = re.findall(r"\b\d+\b", text)

# if matches:
# print("Matches: ", matches)

# Example2 validate email


def validateEmail(email):
    pattern = r'^[\w\.\-]+@[\w\.\-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False


# Usage
email = 'ssavaemma4@gmail.com'
email2 = 'ssavaemma4@gmail.com'

# print(validateEmail(email))
# print(validateEmail(email2))


# Generators and iterators
#  'yield' keyword is used for generator generator
# Iterator '__iter__', '__next__' iterator

def factorial(n):
    # return the factorial of a number
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


# Print factorial of 1 - 10
# for i in range(1, 10):
#     print(factorial(i))

# Example3
# generate a function that yields the square of unmbers from 1 - 10
def square():
    for i in range(1, 10):
        yield i ** 2


# create the iterator object to yield square of numbers from 1-10
square_iterator = square()

# print the first 5 sqaure of numbers from 1-10
for i in range(5):
    print(next(square_iterator))

# Decorators


def my_decorator(func):
    def inner():
        print("Thhis is my decorator")
        func()
    return inner


@my_decorator
def outer_decorator():
    print("Thhis is my outer decorator")


outer_decorator()
