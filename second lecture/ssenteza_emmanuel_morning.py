# Day 2 - Recess

"""
 if statement:
 If statement is used to execute a block of code based on a certain condition if true
 multiple if staements can be created with the use of elif 
 Example:
if constion true::
    do something in this block
elif someother condition true:
    do something in this block
else:
    if all false then do something in this final block
'''

'''
 Loops
 The for loop:
 The for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects.
 It executes the block of code until when the sequence is finished
 Example:
for item in list:
    code block executed for each item in the list

# while loop:
 The while loop is used to repeatedly execute a block of code as long as a certain condition is true.
 and stops the loop if condition is false
 Example:
while condition:
    do something for as long as condition is true

# break statement:
 The break statement is used to exit the current loop, even if the loop condition is still true.
 We used break statement to terminate a loop based on a certain condition.

 Example:
while condition:
    if condition_true:
        break

# continue statement:
 The continue statement is used to skip the current iteration of a loop and move to the next iteration.
 Use it to bypass the loop condition

  Example:
for item in sequence:
    if condition_true:
        continue to the next iteration
   

# pass statement:
 The pass statement is a placeholder that is used when a statement is required syntactically but you don't want to perform any action.
 Example:
def some_function():
    pass
     code block will be empty, but the function is syntactically correct

# try-except statement:
 The try-except statement is used to handle exceptions that may occur during the execution of code.
 catch blocks are used to handle exceptions thus preventing the program from crashing.

 Example:
try:
     code that may raise an exception
except SomeException:
     code executed if any Exception is raised
except AnotherException:
    #code executed if AnotherException is raised
else:
     code executed if no exceptions are raised
finally:
     code executed regardless of whether an exception occurred or not
"""


# Exercise 1
# Prompting  a student to enter their mental health rating
print("Welcome to the Student Mental Health Survey")

responses = []

num_students = int(input("Enter the number of students: "))

for i in range(1, num_students + 1):
    response = input(
        f"Student {i}, please rate your mental health on a scale of 1-10: ")
    responses.append(response)

print("\n--- Survey Results ---")
for i, response in enumerate(responses):
    print(f"Student {i + 1}: {response}")
