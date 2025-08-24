import tkinter as tk

root = tk.Tk()
root.title("Styled Calculator")
root.geometry("320x450")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

expression = ""


display = tk.Entry(root, font=("Arial", 24), bd=10, relief='flat', justify="right", bg="#ffffff", fg="#000000")
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, padx=10, pady=20, sticky="nsew")


button_style = {
    "font": ("Arial", 18),
    "bd": 0,
    "fg": "#333333",
    "bg": "#e6e6e6",
    "activebackground": "#cccccc",
    "width": 5,
    "height": 2
}

def press(num):
    global expression
    expression += str(num)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = result
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    action = lambda x=text: press(x) if x not in ['=', 'C'] else (calculate() if x == '=' else clear())
    tk.Button(root, text=text, command=action, **button_style).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")


for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()