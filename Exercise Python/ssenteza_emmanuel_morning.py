# Day7
# Context Manager
# this is an object that defines a tempolary context for a block of code
# Example1: we open a file and returnna context manager
# def open_file(filename):
#     # to open a file and return a contect manager instance
#     file = open(filename, "r")

#     def __enter__(): return file

#     def __exit__(self, exc_type, exc_value, exc_tb):
#         file.close()
#         return __enter__, __exit__


# with open_file("my_file.txt") as f:
#     contents = f.read()

# Example2 demonstrating a context manager using a time series
# import time


# class Timer:
#     def __enter__(self):
#         self.start_time = time.time()

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         end_time = time.time()
#         execution_time = end_time - self.start_time
#         print(f"The time for this execution {execution_time} seconds")


# with Timer():
#     # measure the execution time
#     time.sleep(2)


# Multithreading and multiprocessing
# techniques that can be used to improve performance of a pyhton program

# Multithreading: multithreads are created within a single process
# Example: multithreading
import time
import sqlite3
import threading


# def task(name):
#     print(f"Running task {name}")


# # create multiple threads
# threads = []
# for i in range(10):
#     t = threading.Thread(target=task, args=(f"Thread {i}",))
#     threads.append(t)
#     t.start()

# # wait for the threads to finish before it joins
# for t in threads:
#     t.join()

# Multiprocessing: this is a technique where multiple threads are created
# Example 4: Demonstrate use of multiprocessing
import multiprocessing


# def process_task(name):
#     print(f"Process task {name}")


# # #  Create a pool of processes
# pool = multiprocessing.Pool(processes=5)

# # # Submit multiple tasks to the pool
# for i in range(6):
#     pool.apply_async(process_task, args=(f"Process {i}",))

# # # Close the pool and wait for all processes to finish
# pool.close()
# pool.join()

# I get an endless loop when I run the code above I have failed to find out why

# Example5: multithreading and multiprocessing
# def task(name):
#     print(
#         f"Running task {name} on thread {threading.current_thread().name} with process {multiprocessing.current_process().name}")


# # create multiple threads to run
# threads = []
# for i in range(4):
#     t = threading.Thread(target=task, args=(f"Thread {i}",))
#     threads.append(t)
#     t.start()

# # wait for all threads to finish
# for t in threads:
#     t.join()


# Assignment A7:
# 1a) Show a context manager for file handling that automatically opens and closes a file.

class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):

        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


# Using the context manager
with FileHandler("emma.txt", "x") as file:
    print("Done")
    # The file will be automatically closed after this block

# b) Shows a context manager for managing a database connection.


class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()


with DatabaseConnection("database.db") as conn:
    print("Done")
    # The connection will be automatically closed after this block

# c) Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time.


def task(name, duration):
    print(f"Task {name} started.")
    time.sleep(duration)
    print(f"Task {name} finished.")


# Multithreading
threads = []
for i in range(3):
    t = threading.Thread(target=task, args=(f"Thread {i}", i+1))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Multiprocessing
processes = []
for i in range(3):
    p = multiprocessing.Process(target=task, args=(f"Process {i}", i+1))
    processes.append(p)
    p.start()

for p in processes:
    p.join()
