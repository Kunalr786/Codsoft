import tkinter as tk

def add_task():
    task = new_task_textbox.get()
    tasks_listbox.insert(tk.END, task)
    new_task_textbox.delete(0, tk.END)

def delete_task():
    selected_task = tasks_listbox.curselection()
    for index in reversed(selected_task):
        tasks_listbox.delete(index)

window = tk.Tk()
window.title("To-Do List")

tasks_listbox = tk.Listbox(window, height=10, width=50)
tasks_listbox.pack(pady=20)

new_task_textbox = tk.Entry(window, width=50)
new_task_textbox.pack()

add_task_button = tk.Button(window, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

delete_task_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_task_button.pack(pady=5)

window.mainloop()