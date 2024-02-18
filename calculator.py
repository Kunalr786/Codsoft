import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def display_password():
    length = int(entry.get())
    password = generate_password(length)
    messagebox.showinfo("Generated Password", "Your generated password is: " + password)

root = tk.Tk()
root.title("Password Generator")

label = tk.Label(root, text="Enter the desired length of the password:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Generate Password", command=display_password)
button.pack()

root.mainloop()
