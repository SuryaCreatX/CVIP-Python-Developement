import tkinter as tk

def on_button_click(event):
    current_text = result_var.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            result_var.set(result)
            save_calculation(current_text, result)
        except Exception as e:
            result_var.set("Error")
    elif button_text == "C":
        result_var.set("")
    else:
        result_var.set(current_text + button_text)

def save_calculation(expression, result):
    if len(calc_history) >= 5:
        calc_history.pop(0)
    calc_history.append((expression, result))
    update_calc_history()

def update_calc_history():
    calc_history_text.set("\n".join([f"{exp} = {res}" for exp, res in calc_history]))

root = tk.Tk()
root.title("My Basic Calculator") 

calculator_name_label = tk.Label(root, text="Welcome to My Basic Calculator!", font="Helvetica 16 bold")
calculator_name_label.grid(row=0, column=0, columnspan=4)

intro_text = "Perform calculations and see history below:"
intro_label = tk.Label(root, text=intro_text, font="Helvetica 12")
intro_label.grid(row=1, column=0, columnspan=4)

result_var = tk.StringVar()
result_var.set("")

result_entry = tk.Entry(root, textvariable=result_var, font="Helvetica 20 bold", justify="right")
result_entry.grid(row=2, column=0, columnspan=4)

calc_history = []
calc_history_text = tk.StringVar()
calc_history_label = tk.Label(root, textvariable=calc_history_text, font="Helvetica 12", anchor="w", justify="left")
calc_history_label.grid(row=3, column=0, columnspan=4, sticky="ew")

button_texts = [
    ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("/", 4, 3),
    ("4", 5, 0), ("5", 5, 1), ("6", 5, 2), ("*", 5, 3),
    ("1", 6, 0), ("2", 6, 1), ("3", 6, 2), ("-", 6, 3),
    ("0", 7, 0), (".", 7, 1), ("=", 7, 2), ("+", 7, 3),
    ("C", 8, 0)
]

for (text, row, col) in button_texts:
    button = tk.Button(root, text=text, padx=20, pady=20, font="Helvetica 15 bold")
    button.grid(row=row, column=col)
    button.bind("<Button-1>", on_button_click)

root.mainloop()
