import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("250x220")
window.configure(bg="violet")

frame = tk.Frame(window, bg="violet", padx=10, pady=10)
frame.grid(row=0, column=0)

result = tk.Label(frame,text="Result will appear here", bg="white", width=30, pady=5, padx=10)

result.grid(row=0, column=0, columnspan=2, pady=10)
num1_label = tk.Label(frame, text="Enter 1st Number:")
num1_label.grid(row=1, column=0)

num1_entry = tk.Entry(frame, width=13)
num1_entry.grid(row=1, column=1, padx=5)

num2_label = tk.Label(frame, text="Enter 2nd Number:")
num2_label.grid(row=2, column=0, pady=5)

num2_entry = tk.Entry(frame, width=13)
num2_entry.grid(row=2, column=1, pady=5)

def add():
    n1 = int(num1_entry.get())
    n2 = int(num2_entry.get())
    result.config(text="The sum of " + str(n1) + " + " + str(n2) + " is " + str(n1+n2) + ".")

def subtract():
    n1 = int(num1_entry.get())
    n2 = int(num2_entry.get())
    result.config(text="The difference of " + str(n1) + "-" + str(n2) + " is " + str(n1-n2)+ ".")

def multiply():
    n1 = int(num1_entry.get())
    n2 = int(num2_entry.get())
    result.config(text="The product of " + str(n1) + " * " + str(n2) + " is " + str(n1*n2)+ ".")

def divide():
    n1 = int(num1_entry.get())
    n2 = int(num2_entry.get())
    result.config(text="The quotient of " + str(n1) + " / " + str(n2) + " is " + str(n1/n2)+ ".")

add_btn = tk.Button(frame, text="Add", command=add)
add_btn.grid(row=3, column=0, pady=10)

sub_btn = tk.Button(frame, text="Subtract", command=subtract)
sub_btn.grid(row=3, column=1)

mul_btn = tk.Button(frame, text="Multiply", command=multiply)
mul_btn.grid(row=4, column=0)

div_btn = tk.Button(frame, text="Division", command=divide)
div_btn.grid(row=4, column=1)

window.mainloop()