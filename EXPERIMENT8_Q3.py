

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# ---------------- DATABASE ----------------
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS students")

cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    course TEXT,
    gender TEXT,
    date TEXT
)
""")
conn.commit()

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Student Registration System")
root.geometry("900x550")
root.resizable(False, False)
root.configure(bg="#1e1e2f")

# ---------------- VARIABLES ----------------
name_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
course_var = tk.StringVar()
gender_var = tk.StringVar()

# ---------------- FUNCTIONS ----------------
def show_frame(frame):
    frame.tkraise()

def clear_fields():
    name_var.set("")
    email_var.set("")
    phone_var.set("")
    course_var.set("")
    gender_var.set("")

def add_student():
    if (name_var.get() == "" or email_var.get() == "" or
        phone_var.get() == "" or course_var.get() == "" or
        gender_var.get() == ""):

        messagebox.showerror("Error", "All fields are required!")
        return

    cursor.execute(
        "INSERT INTO students (name,email,phone,course,gender,date) VALUES (?,?,?,?,?,?)",
        (
            name_var.get(),
            email_var.get(),
            phone_var.get(),
            course_var.get(),
            gender_var.get(),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )
    conn.commit()

    messagebox.showinfo("Success", "Student Registered Successfully!")
    clear_fields()

def show_students():
    tree.delete(*tree.get_children())

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", values=row)

def go_to_table():
    show_students()
    show_frame(frame2)

# ---------------- FRAMES ----------------
frame1 = tk.Frame(root, bg="#2b2d42")
frame2 = tk.Frame(root, bg="#2b2d42")

for frame in (frame1, frame2):
    frame.place(x=0, y=0, width=900, height=550)

# ---------------- PAGE 1 ----------------
tk.Label(frame1, text="Student Registration",
         font=("Segoe UI", 22, "bold"),
         bg="#2b2d42", fg="#edf2f4").pack(fill=tk.X, pady=15)

form = tk.Frame(frame1, bg="#edf2f4", bd=0)
form.place(x=250, y=90, width=400, height=360)

def field(label, var, y):
    tk.Label(form, text=label,
             font=("Segoe UI", 11, "bold"),
             bg="#edf2f4", fg="#2b2d42").place(x=20, y=y)
    tk.Entry(form, textvariable=var,
             font=("Segoe UI", 10),
             bd=1, relief="solid").place(x=20, y=y+25, width=350)

field("Name", name_var, 10)
field("Email", email_var, 70)
field("Phone", phone_var, 130)

tk.Label(form, text="Course", bg="#edf2f4",
         font=("Segoe UI", 11, "bold")).place(x=20, y=190)

ttk.Combobox(form, textvariable=course_var,
             values=["B.Tech", "BCA", "MCA", "MBA", "B.Sc"],
             state="readonly").place(x=20, y=215, width=350)

tk.Label(form, text="Gender", bg="#edf2f4",
         font=("Segoe UI", 11, "bold")).place(x=20, y=250)

ttk.Combobox(form, textvariable=gender_var,
             values=["Male", "Female", "Other"],
             state="readonly").place(x=20, y=275, width=350)

# Buttons
tk.Button(frame1, text="Submit",
          font=("Segoe UI", 11, "bold"),
          bg="#06d6a0", fg="white",
          activebackground="#05c091",
          command=add_student).place(x=300, y=470, width=120)

tk.Button(frame1, text="View Data",
          font=("Segoe UI", 11, "bold"),
          bg="#118ab2", fg="white",
          activebackground="#0f7aa0",
          command=go_to_table).place(x=450, y=470, width=120)

# ---------------- PAGE 2 ----------------
tk.Label(frame2, text="Registered Students",
         font=("Segoe UI", 22, "bold"),
         bg="#2b2d42", fg="#edf2f4").pack(fill=tk.X, pady=15)

table_frame = tk.Frame(frame2, bg="white")
table_frame.place(x=50, y=80, width=800, height=380)

scroll_x = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)

tree = ttk.Treeview(
    table_frame,
    columns=("ID", "Name", "Email", "Phone", "Course", "Gender", "Date"),
    xscrollcommand=scroll_x.set,
    yscrollcommand=scroll_y.set
)

scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

scroll_x.config(command=tree.xview)
scroll_y.config(command=tree.yview)

for col in ("ID", "Name", "Email", "Phone", "Course", "Gender", "Date"):
    tree.heading(col, text=col)
    tree.column(col, anchor=tk.CENTER, width=110)

tree["show"] = "headings"
tree.pack(fill=tk.BOTH, expand=1)

tk.Button(frame2, text="← Back",
          font=("Segoe UI", 11, "bold"),
          bg="#ef476f", fg="white",
          activebackground="#d43f5e",
          command=lambda: show_frame(frame1)).place(x=50, y=480, width=120)

# ---------------- START ----------------
show_frame(frame1)
root.mainloop()