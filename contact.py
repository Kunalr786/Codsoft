import tkinter as tk
from tkinter import messagebox

# Contact information
contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    contacts[name] = (phone, email, address)
    messagebox.showinfo("Add Contact", "Contact added successfully!")

def view_contacts():
    contact_list = "\n".join(f"{name}: {phone}" for name, (phone, _, _) in contacts.items())
    messagebox.showinfo("View Contacts", contact_list)

def search_contact():
    name = name_entry.get()
    if name in contacts:
        phone, email, address = contacts[name]
        messagebox.showinfo("Search Contact", f"Name: {name}\nPhone: {phone}\nEmail: {email}\nAddress: {address}")
    else:
        messagebox.showinfo("Search Contact", "Contact not found!")

def update_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name in contacts:
        contacts[name] = (phone, email, address)
        messagebox.showinfo("Update Contact", "Contact updated successfully!")
    else:
        messagebox.showinfo("Update Contact", "Contact not found!")

def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Delete Contact", "Contact deleted successfully!")
    else:
        messagebox.showinfo("Delete Contact", "Contact not found!")

root = tk.Tk()
root.title("Contact Management System")

# User interface
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

view_button = tk.Button(root, text="View Contacts", command=view_contacts)
view_button.pack()

search_button = tk.Button(root, text="Search Contact", command=search_contact)
search_button.pack()

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()

root.mainloop()
