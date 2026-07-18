from tkinter import messagebox
import tkinter as tk
import random
import string

# Function to generate password
def generate_password():
    length = length_entry.get()
    if length == "":
        messagebox.showerror("Error", "Please enter password length!")
        return
    if not length.isdigit():
        messagebox.showerror("Error", "Please enter numbers only!")
        return
    length = int(length)
    if length < 4:
        messagebox.showerror("Error", "Password length should be at least 4.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Success", "Password copied")

def clear_fields():
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

#Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x400")
root.resizable(False, False)

# Heading
title = tk.Label(root, text="Password Generator", font=("Arial", 20, "bold"))
title.pack(pady=20)

# Password Length
length_label = tk.Label(root, text="Enter Password Length:",font=("Arial", 12, "bold"))
length_label.pack()

length_entry = tk.Entry(root, font=("Arial", 12), width=20)
length_entry.pack(pady=10)

# Generate Button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

# Password Output
password_entry = tk.Entry(root, font=("Arial", 12), width=30)
password_entry.pack(pady=10)

# copy button
copy_btn = tk.Button(root, text="Copy Password", command=copy_password)
copy_btn.pack(pady=5)

# clear button
clear_btn = tk.Button(root, text="Clear", command=clear_fields)
clear_btn.pack(pady=5)

root.mainloop()