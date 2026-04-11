# Login & Signup System (Updated Colors)


import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- DATABASE ----------------
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Login & Signup System")
root.geometry("420x450")
root.resizable(False, False)
root.configure(bg="#f8f9fa")

# ---------------- FUNCTIONS ----------------
def show_frame(frame):
    frame.tkraise()

def clear_login():
    login_user.set("")
    login_pass.set("")

def clear_signup():
    signup_user.set("")
    signup_pass.set("")

def signup():
    username = signup_user.get()
    password = signup_pass.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()

        messagebox.showinfo("Success", "Account created successfully!")
        clear_signup()
        show_frame(login_frame)

    except:
        messagebox.showerror("Error", "Username already exists!")

def login():
    username = login_user.get()
    password = login_pass.get()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", f"Welcome {username}!")
        clear_login()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

def forgot_password():
    username = login_user.get()

    if username == "":
        messagebox.showerror("Error", "Enter username first!")
        return

    cursor.execute(
        "SELECT password FROM users WHERE username=?",
        (username,)
    )
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Password Found", f"Your password is: {result[0]}")
    else:
        messagebox.showerror("Error", "Username not found!")

# ---------------- FRAMES ----------------
login_frame = tk.Frame(root, bg="#f8f9fa")
signup_frame = tk.Frame(root, bg="#f8f9fa")

for frame in (login_frame, signup_frame):
    frame.place(x=0, y=0, width=420, height=450)

# ---------------- LOGIN PAGE ----------------
tk.Label(login_frame, text="🔐 Login",
         font=("Segoe UI", 22, "bold"),
         bg="#0f4c5c", fg="white", pady=10).pack(fill=tk.X)

card1 = tk.Frame(login_frame, bg="#e9ecef")
card1.place(x=40, y=90, width=340, height=260)

tk.Label(card1, text="Username",
         bg="#e9ecef").place(x=20, y=20)
login_user = tk.StringVar()
tk.Entry(card1, textvariable=login_user).place(x=20, y=50, width=300)

tk.Label(card1, text="Password",
         bg="#e9ecef").place(x=20, y=100)
login_pass = tk.StringVar()
tk.Entry(card1, textvariable=login_pass, show="*").place(x=20, y=130, width=300)

tk.Button(card1, text="Login",
          bg="#2ecc71", fg="white",
          width=18, command=login).place(x=80, y=170)

tk.Button(card1, text="Clear",
          bg="#f39c12", fg="white",
          width=10, command=clear_login).place(x=20, y=210)

tk.Button(card1, text="Forgot Password?",
          fg="#2980b9", bg="#e9ecef",
          bd=0, command=forgot_password).place(x=170, y=210)

tk.Button(login_frame, text="Go to Signup",
          bg="#3498db", fg="white",
          command=lambda: show_frame(signup_frame)).place(x=140, y=370)

# ---------------- SIGNUP PAGE ----------------
tk.Label(signup_frame, text="📝 Signup",
         font=("Segoe UI", 22, "bold"),
         bg="#0f4c5c", fg="white", pady=10).pack(fill=tk.X)

card2 = tk.Frame(signup_frame, bg="#e9ecef")
card2.place(x=40, y=90, width=340, height=260)

tk.Label(card2, text="Username",
         bg="#e9ecef").place(x=20, y=20)
signup_user = tk.StringVar()
tk.Entry(card2, textvariable=signup_user).place(x=20, y=50, width=300)

tk.Label(card2, text="Password",
         bg="#e9ecef").place(x=20, y=100)
signup_pass = tk.StringVar()
tk.Entry(card2, textvariable=signup_pass, show="*").place(x=20, y=130, width=300)

tk.Button(card2, text="Signup",
          bg="#2ecc71", fg="white",
          width=18, command=signup).place(x=80, y=170)

tk.Button(card2, text="Clear",
          bg="#f39c12", fg="white",
          width=10, command=clear_signup).place(x=20, y=210)

tk.Button(signup_frame, text="Back to Login",
          bg="#3498db", fg="white",
          command=lambda: show_frame(login_frame)).place(x=140, y=370)

# ---------------- START ----------------
show_frame(login_frame)
root.mainloop()