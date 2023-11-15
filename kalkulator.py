import tkinter as tk

def button_click(value):
    current_text = display_data.get()
    display_data.set(current_text + str(value))

def clear_command():
    display_data.set("")

def calculate():
    try:
        result = eval(display_data.get())
        display_data.set(result)
    except Exception as e:
        display_data.set("Error")

root = tk.Tk()
root.title("Kalkulator")
root.resizable(0, 0)
root.config(background="black")

display_data = tk.StringVar()
display_data.set("")

display = tk.Label(root, width=15, height=2, textvariable=display_data, background="black", foreground="white")
display.grid(row=0, column=1)

clear = tk.Button(root, width=15, height=2, text="AC", command=clear_command, foreground="black", background="red")
clear.grid(row=4, column=0)

buttons = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9",
]

row_val = 1
col_val = 0

for button_text in buttons:
    button = tk.Button(root, width=15, height=2, text=button_text, command=lambda bt=button_text: button_click(bt),  foreground="white", background="grey")
    button.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1

# Corrected placement for the "0" button
button_0 = tk.Button(root, width=15, height=2, text="0", command=lambda bt="0": button_click(bt), foreground="white", background="grey")
button_0.grid(row=4, column=1)

operators = ["+", "-", "*", "/"]

row_val = 1
col_val = 3

for operator in operators:
    button = tk.Button(root, width=7, height=2, text=operator, command=lambda op=operator: button_click(op),background="darkorange", foreground="black")
    button.grid(row=row_val, column=col_val)
    row_val += 1


equal = tk.Button(root, width=15, height=2, text="=", command=calculate, foreground="black", background="green")
equal.grid(row=4, column=2)

root.mainloop()
