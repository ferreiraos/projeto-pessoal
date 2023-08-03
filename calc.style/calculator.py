import tkinter as tk

def button_click(event):
    current_text = display_var.get()
    button_text = event.widget.cget("text")
    if button_text == "=":
        try:
            result = eval(current_text)
            expression_label.config(text=current_text)
            result_label.config(text=result)
        except Exception as e:
            expression_label.config(text=current_text)
            result_label.config(text="Erro")
    elif button_text == "C":
        display_var.set("")
        expression_label.config(text="")
        result_label.config(text="")
    else:
        display_var.set(current_text + button_text)

root = tk.Tk()
root.title("Calculadora")
root.configure(bg="black")

expression_label = tk.Label(root, text="", font="Helvetica 14 bold", bg="black", fg="white")
expression_label.grid(row=0, column=0, columnspan=4)

display_var = tk.StringVar()
display_var.set("")

display = tk.Entry(root, textvar=display_var, font="Helvetica 20 bold", bd=10, insertwidth=4, width=15, justify="right", bg="black", fg="white")
display.grid(row=1, column=0, columnspan=4)

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+"),
]

for row_idx, row in enumerate(buttons):
    for col_idx, button_text in enumerate(row):
        button = tk.Button(root, text=button_text, font="Helvetica 18 bold", padx=20, pady=20, bg="black", fg="gold")
        button.grid(row=row_idx+2, column=col_idx)
        button.bind("<Button-1>", button_click)

result_label = tk.Label(root, text="", font="Helvetica 14 bold", bg="black", fg="white")
result_label.grid(row=len(buttons)+2, column=0, columnspan=4)

root.mainloop()
