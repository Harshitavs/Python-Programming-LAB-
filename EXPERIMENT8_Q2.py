from tkinter import *
import math

root = Tk()
root.title("Calculator")
root.geometry("600x450")


frame = Frame(root)
frame.pack(expand=True)


e = Entry(frame, width=30, borderwidth=5, font=("Arial", 18), justify="right")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def click(value):
    e.insert(END, value)

def clear():
    e.delete(0, END)

def equal():
    try:
        result = eval(e.get(), {"__builtins__": None}, {"math": math})
        e.delete(0, END)
        e.insert(0, result)
    except:
        e.delete(0, END)
        e.insert(0, "Error")

def sqrt(): e.insert(END, "math.sqrt(")
def factorial(): e.insert(END, "math.factorial(")
def sin(): e.insert(END, "math.sin(math.radians(")
def cos(): e.insert(END, "math.cos(math.radians(")
def tan(): e.insert(END, "math.tan(math.radians(")
def log(): e.insert(END, "math.log10(")
def pi(): e.insert(END, str(math.pi))

def open_bracket(): e.insert(END, "(")
def close_bracket(): e.insert(END, ")")


Button(frame, text='Sqrt', padx=18, pady=18, command=sqrt).grid(row=1, column=0, padx=3, pady=3)
Button(frame, text='pi', padx=18, pady=18, command=pi).grid(row=1, column=1, padx=3, pady=3)
Button(frame, text='**', padx=18, pady=18, command=lambda: click("**")).grid(row=1, column=2, padx=3, pady=3)
Button(frame, text='!', padx=18, pady=18, command=factorial).grid(row=1, column=3, padx=3, pady=3)
Button(frame, text='(', padx=18, pady=18, command=open_bracket).grid(row=1, column=4, padx=3, pady=3)

Button(frame, text='7', padx=20, pady=20, command=lambda: click("7")).grid(row=2, column=0, padx=3, pady=3)
Button(frame, text='8', padx=20, pady=20, command=lambda: click("8")).grid(row=2, column=1, padx=3, pady=3)
Button(frame, text='9', padx=20, pady=20, command=lambda: click("9")).grid(row=2, column=2, padx=3, pady=3)
Button(frame, text='/', padx=20, pady=20, command=lambda: click("/")).grid(row=2, column=3, padx=3, pady=3)
Button(frame, text=')', padx=20, pady=20, command=close_bracket).grid(row=2, column=4, padx=3, pady=3)

Button(frame, text='4', padx=20, pady=20, command=lambda: click("4")).grid(row=3, column=0, padx=3, pady=3)
Button(frame, text='5', padx=20, pady=20, command=lambda: click("5")).grid(row=3, column=1, padx=3, pady=3)
Button(frame, text='6', padx=20, pady=20, command=lambda: click("6")).grid(row=3, column=2, padx=3, pady=3)
Button(frame, text='*', padx=20, pady=20, command=lambda: click("*")).grid(row=3, column=3, padx=3, pady=3)
Button(frame, text='sin', padx=20, pady=20, command=sin).grid(row=3, column=4, padx=3, pady=3)

Button(frame, text='1', padx=20, pady=20, command=lambda: click("1")).grid(row=4, column=0, padx=3, pady=3)
Button(frame, text='2', padx=20, pady=20, command=lambda: click("2")).grid(row=4, column=1, padx=3, pady=3)
Button(frame, text='3', padx=20, pady=20, command=lambda: click("3")).grid(row=4, column=2, padx=3, pady=3)
Button(frame, text='+', padx=20, pady=20, command=lambda: click("+")).grid(row=4, column=3, padx=3, pady=3)
Button(frame, text='cos', padx=20, pady=20, command=cos).grid(row=4, column=4, padx=3, pady=3)


Button(frame, text='0', padx=20, pady=20, command=lambda: click("0"))\
.grid(row=5, column=0, padx=3, pady=3)

Button(frame, text='C', padx=20, pady=20, command=clear)\
.grid(row=5, column=1, padx=3, pady=3)

Button(frame, text='=', padx=20, pady=20, command=equal)\
.grid(row=5, column=2, padx=3, pady=3)

Button(frame, text='-', padx=20, pady=20, command=lambda: click("-"))\
.grid(row=5, column=3, padx=3, pady=3)

Button(frame, text='log', padx=20, pady=20, command=log)\
.grid(row=5, column=4, padx=3, pady=3)

root.mainloop()