import tkinter as tk


def click_button(value):
    current_text = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, current_text + str(value))


def clear_input():
    input_field.delete(0, tk.END)


def calculate():
    try:
        result = eval(input_field.get())
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, str(result))
    except Exception as e:
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, "Ошибка")


root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x500")

input_field = tk.Entry(root, font=("Arial", 24), justify="right")
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("=", 4, 2),
    ("+", 4, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(root,
                       text=text,
                       font=("Arial", 18),
                       command=lambda t=text: click_button(t)
                       if t != "=" else calculate())
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

clear_button = tk.Button(root,
                         text="C",
                         font=("Arial", 18),
                         command=clear_input)
clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
