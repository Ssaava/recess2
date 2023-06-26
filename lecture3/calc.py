from tkinter import *
# import tkinter // this is also another way to import tkinter

root = Tk()
root.title("Ssenteza Emmanuel")
frame = Frame(root)
# Add the frame to the parent of the window
frame.pack()

# create the bottom frame and input buttons
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
button1 = Button(frame, text="1")
button1.pack(side=LEFT)
button2 = Button(frame, text="2")
button2.pack(side=LEFT)

button3 = Button(frame, text="3")
button3.pack(side=LEFT)
button4 = Button(frame, text="4")
button4.pack(side=LEFT)


# button5 = Button(root, text="5")
# button5.grid()
# button6 = Button(root, text="6")
# button6.grid()
# button7 = Button(root, text="7")
# button7.grid()
# button8 = Button(root, text="8")
# button8.grid()
# button9 = Button(root, text="9")
# button9.grid()

# button1 = tk.Button(root, text="1")
root.mainloop()
