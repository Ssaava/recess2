# # inheritance Examples

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating")


# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

#     def bark(self):
#         print(f"{self.name} is barking")


# class Cat(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

#     def meow(self):
#         print(f"{self.name} is meowing")

# # dog = Dog("Fido", "Lab")

# # multiple inheritance


# class Animals:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating")


# class Flayable:
#     def fly(self):
#         print(f"{self.name} is flying")


# class Bird(Animals, Flayable):
#     # this is where we show multiple inheritance
#     def __init__(self, name, wings):
#         super().__init__(name)
#         self.wings = wings

#     def display(self):
#         super().display(self)
#         print(f"{self.name} has {self.wings} wings")


# # create the bird object
# bird = Bird("Pigeon", 4)
# # bird.fly()
# # bird.display()

# # Method overriding


# class Animal:

#     def make_sound(self):
#         print(f"Animal is making sound")


# class Dog(Animal):
#     def make_sound(self):
#         print(f"Dog is barking")


# class Cat(Animal):
#     def make_sound(self):
#         print(f"Cat is meowing")


# def make_animal_sound(animal):
#     animal.make_sound()


# animal = Animal()
# dog = Dog()
# cat = Cat()
# make_animal_sound(cat)

# polymorphism allows yout o write code that can work with different objects

# exercise for today
# please sir kindly uncomment each section of the code to run it 
# 1 Express abstraction using calculating area of a circle and rectangle

'''
import math
class Area():
    def __init__(self,radius,width, length):
       
        self.__width = width
        self.__length = length
        self.__radius = radius
    def calculate_circle_area(self):
        area = math.pi * self.__radius**2
        return area

    def calculate_rectangle_area(self):
        area = self.__length * self.__width
        return area

length = 7
width = 3
radius = 5
area = Area(radius,width,length)

circle_area = area.calculate_circle_area()
print(f"The area of the circle with radius {radius} is: {circle_area:.2f}")


rectangle_area = area.calculate_rectangle_area()
print(f"The area of the rectangle with length {length} and width {width} is: {rectangle_area}")

'''

# 2 Create a receipt printing program with GUI interface,
# a more advanced detail earns you more points 
#
'''
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def print_receipt():
    # Get the values entered in the GUI fields
    customer_name = name_entry.get()
    item_name = item_entry.get()
    quantity = int(quantity_entry.get())
    price = float(price_entry.get())
    payment_method = payment_var.get()

    # Calculate total amount
    total_amount = quantity * price

    # Format the receipt with the provided options
    receipt = "Receipt\n"
    receipt += "--------------------------------\n"
    receipt += f"Customer Name: {customer_name}\n"
    receipt += f"Item: {item_name}\n"
    receipt += f"Quantity: {quantity}\n"
    receipt += f"Price: ${price:.2f}\n"
    receipt += f"Total Amount: ${total_amount:.2f}\n"
    receipt += f"Date: {datetime.now().strftime('%Y-%m-%d')}\n"
    receipt += f"Payment Method: {payment_method}\n"
    receipt += "--------------------------------"

    messagebox.showinfo("Receipt", receipt)

# Create the main window
window = tk.Tk()
window.title("Receipt Printing Program")

# Create and position the GUI elements using grid layout
name_label = tk.Label(window, text="Customer Name:")
name_label.grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

item_label = tk.Label(window, text="Item Name:")
item_label.grid(row=1, column=0, sticky="e")
item_entry = tk.Entry(window)
item_entry.grid(row=1, column=1)

quantity_label = tk.Label(window, text="Quantity:")
quantity_label.grid(row=2, column=0, sticky="e")
quantity_entry = tk.Entry(window)
quantity_entry.grid(row=2, column=1)

price_label = tk.Label(window, text="Price:")
price_label.grid(row=3, column=0, sticky="e")
price_entry = tk.Entry(window)
price_entry.grid(row=3, column=1)

payment_label = tk.Label(window, text="Payment Method:")
payment_label.grid(row=4, column=0, sticky="e")
payment_var = tk.StringVar(window)
payment_var.set("Cash")  # Default payment method
payment_option = tk.OptionMenu(window, payment_var, "Cash", "Credit Card", "Online Payment")
payment_option.grid(row=4, column=1)

print_button = tk.Button(window, text="Print Receipt", command=print_receipt)
print_button.grid(row=5, columnspan=2)

window.mainloop()

'''