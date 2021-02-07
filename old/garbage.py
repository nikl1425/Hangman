# Import all from lib
from tkinter import *
import tkinter as tk
from tkmacosx import Button


# Defining an instance of the tk object
window = tk.Tk()

# adding labels:
label = tk.Label(text="Welcome to ",
                 foreground='white',
                 background='black',
                 height=2)

# Start game button
button = Button(window, text='Start the Game!', bg='black', fg='white', borderless=1)

# Input from user
entry = Entry(fg='white', bg='black', width=10)
userInput = entry.get()



# Set width + height of window
frame = Frame(window, width=300, height=300)

# Apply to window
label.pack()
button.pack()
entry.pack()
frame.pack()


# initialize window
window.mainloop()