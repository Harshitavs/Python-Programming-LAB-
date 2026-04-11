# Create a GUI based task manager using Tkinter + SQLite

import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- DATABASE ----------------
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT,
    status TEXT
)
""")
conn.commit()

# ---------------- FUNCTIONS ----------------
def load_tasks():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT id, task, status FROM tasks")
    rows = cursor.fetchall()

    for index, row in enumerate(rows, start=1):
        task_text = f"{index}. {row[1]} ({row[2]})"
        listbox.insert(tk.END, task_text)

def add_task():
    task = entry.get()

    if task == "":
        messagebox.showerror("Error", "Task cannot be empty!")
        return

    cursor.execute("INSERT INTO tasks (task, status) VALUES (?, ?)", (task, "Pending"))
    conn.commit()

    entry.delete(0, tk.END)
    load_tasks()

def delete_task():
    try:
        selected = listbox.curselection()[0]
        cursor.execute("SELECT id FROM tasks")
        task_id = cursor.fetchall()[selected][0]

        cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        load_tasks()
    except:
        messagebox.showerror("Error", "Select a task first!")

def mark_complete():
    try:
        selected = listbox.curselection()[0]
        cursor.execute("SELECT id FROM tasks")
        task_id = cursor.fetchall()[selected][0]

        cursor.execute("UPDATE tasks SET status='Completed' WHERE id=?", (task_id,))
        conn.commit()
        load_tasks()
    except:
        messagebox.showerror("Error", "Select a task first!")

def edit_task():
    try:
        selected = listbox.curselection()[0]
        new_task = entry.get()

        if new_task == "":
            messagebox.showerror("Error", "Enter new task text!")
            return

        cursor.execute("SELECT id FROM tasks")
        task_id = cursor.fetchall()[selected][0]

        cursor.execute("UPDATE tasks SET task=? WHERE id=?", (new_task, task_id))
        conn.commit()

        entry.delete(0, tk.END)
        load_tasks()
    except:
        messagebox.showerror("Error", "Select a task to edit!")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Task Manager")
root.geometry("500x500")
root.configure(bg="#fdf6ec")

# Title
tk.Label(root, text="📝 Task Manager",
         font=("Calibri", 20, "bold"),
         bg="#6c5ce7", fg="white",
         pady=10).pack(fill=tk.X)

# Entry
entry = tk.Entry(root, font=("Calibri", 13), bd=2, relief="groove")
entry.pack(pady=12, padx=20, fill=tk.X)

# Buttons
btn_frame = tk.Frame(root, bg="#fdf6ec")
btn_frame.pack(pady=8)

tk.Button(btn_frame, text="Add Task", bg="#00b894", fg="white",
          width=12, command=add_task).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Edit Task", bg="#0984e3", fg="white",
          width=12, command=edit_task).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Delete Task", bg="#d63031", fg="white",
          width=12, command=delete_task).grid(row=1, column=0, padx=5, pady=5)

tk.Button(btn_frame, text="Mark Complete", bg="#fdcb6e", fg="black",
          width=12, command=mark_complete).grid(row=1, column=1, padx=5, pady=5)

# Listbox + Scrollbar
frame = tk.Frame(root)
frame.pack(pady=12, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(
    frame,
    font=("Calibri", 12),
    bg="white",
    selectbackground="#a29bfe",
    activestyle="none",
    yscrollcommand=scrollbar.set
)

listbox.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)

# Load tasks
load_tasks()

root.mainloop()