# Error handling in python 
# try and except statement used to catch exceptions

# a = [1,2,4]

'''
try:
    print(a[3])
except:
    print("there was an error in code")
'''
# catching specific exception 

'''
a = 1
b = "name"
try:
    print(b[30])
    c = a + b
except IndexError:
    print("there was an error in code")
except TypeError:
    print("Invalid type input")

'''

# Try with else clause

'''
a = 1
b = "name"
try:
    c = a + b
    print(f"I am very okay {c}")
except IndexError:
    print("there was an error in code")
except TypeError:
    print("Invalid type input")
else:
    print("The else block will be executed")
'''

# try with finally block 

'''
a = 1
b = 4
try:
    c = a + b
    print(f"I am very okay {c}")
except IndexError:
    print("there was an error in code")
except TypeError:
    print("Invalid type input")
else:
    print("no error")
finally:
    print("finally block printed")

'''

# raise an error 


# a = 1
# b = "emma"
# try:
#     c = a + b
#     print(f"I am very okay {c}")
# except TypeError:
#     print("Invalid type input")
# else:
#     print("no error")
# finally:
#     print("finally block printed")
#     raise IndexError
