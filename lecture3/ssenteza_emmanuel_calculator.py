# import the tkinter library to add the GUI functionality
import tkinter as tk


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))


def button_clear():
    entry.delete(0, tk.END)

# function to carry out the functionarity of the equals button


def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# Create the main root
root = tk.Tk()
root.title("Calculator")

# Create an entry field
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for numbers and operators and also make a function call to capture user clicks
button_1 = tk.Button(root, text="1", padx=20, pady=10,
                     command=lambda: button_click(1), activebackground="#00b3e3")
button_2 = tk.Button(root, text="2", padx=20, pady=10,
                     command=lambda: button_click(2), activebackground="#00b3e3")
button_3 = tk.Button(root, text="3", padx=20, pady=10,
                     command=lambda: button_click(3), activebackground="#00b3e3")
button_4 = tk.Button(root, text="4", padx=20, pady=10,
                     command=lambda: button_click(4), activebackground="#00b3e3")
button_5 = tk.Button(root, text="5", padx=20, pady=10,
                     command=lambda: button_click(5), activebackground="#00b3e3")
button_6 = tk.Button(root, text="6", padx=20, pady=10,
                     command=lambda: button_click(6), activebackground="#00b3e3")
button_7 = tk.Button(root, text="7", padx=20, pady=10,
                     command=lambda: button_click(7), activebackground="#00b3e3")
button_8 = tk.Button(root, text="8", padx=20, pady=10,
                     command=lambda: button_click(8), activebackground="#00b3e3")
button_9 = tk.Button(root, text="9", padx=20, pady=10,
                     command=lambda: button_click(9), activebackground="#00b3e3")
button_0 = tk.Button(root, text="0", padx=20, pady=10,
                     command=lambda: button_click(0), activebackground="#00b3e3")

# The following lines of code will add the operators to the screen and call function to capture equal and clear buttons clicks
button_add = tk.Button(root, text="+", padx=20, pady=10,
                       command=lambda: button_click("+"), bg="#808080", activebackground="#00b3e3")
button_subtract = tk.Button(root, text="-", padx=20,
                            pady=10, command=lambda: button_click("-"), bg="#808080", activebackground="#00b3e3")
button_multiply = tk.Button(root, text="*", padx=20,
                            pady=10, command=lambda: button_click("*"), bg="#808080", activebackground="#00b3e3")
button_divide = tk.Button(root, text="/", padx=20,
                          pady=10, command=lambda: button_click("/"), bg="#808080", activebackground="#00b3e3")
button_clear = tk.Button(root, text="C", padx=20,
                         pady=10, command=button_clear, bg="#ff0000", activebackground="#00b3e3")
button_equal = tk.Button(root, text="=", padx=20,
                         pady=10, command=button_equal, bg="#808080", activebackground="#00b3e3")

# Position the buttons on the grid
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=1)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_clear.grid(row=4, column=0)
button_equal.grid(row=4, column=2)

# Start the main event loop
root.mainloop()
