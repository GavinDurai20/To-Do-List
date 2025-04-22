import tkinter as tk
from tkinter import messagebox
import json
import os

FILENAME = "todo_list.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

# GUI Functions
def add_task():
    task = entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks(tasks)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
        tasks.pop(selected_index)
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def mark_complete():
    try:
        selected_index = listbox.curselection()[0]
        tasks[selected_index]["completed"] = True
        listbox.delete(selected_index)
        task_text = tasks[selected_index]["task"] + " ✅"
        listbox.insert(selected_index, task_text)
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")

# Initialize app
tasks = load_tasks()
root = tk.Tk()
root.title("To-Do List App")

# Entry box
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Buttons
frame = tk.Frame(root)
frame.pack()

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

complete_button = tk.Button(frame, text="Mark Complete", command=mark_complete)
complete_button.pack(side=tk.LEFT, padx=5)

# Task list
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Load existing tasks into the listbox
for task in tasks:
    text = task["task"] + (" ✅" if task["completed"] else "")
    listbox.insert(tk.END, text)

# Run the app
root.mainloop()
