import tkinter as tk
import random
import string

def generate_password():
    password_length = length_var.get()
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_digits = digits_var.get()
    include_special_chars = special_chars_var.get()

    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if not characters:
        result_label.config(text="Selecione pelo menos um tipo de caractere.")
        return

    password = []
    while len(password) < password_length:
        char = random.choice(characters)
        if len(password) >= 2 and char.isdigit() and password[-1].isdigit() and int(char) == int(password[-1]) + 1 == int(password[-2]) + 2:
            continue
        password.append(char)

    result_label.config(text=''.join(password))

# Configuração da interface gráfica
root = tk.Tk()
root.title("Gerador de Senhas")
root.geometry("400x400")
root.configure(bg="#F9F9F9")

header_label = tk.Label(root, text="Gerador de Senhas", font=("Arial", 24), bg="#F9F9F9")
header_label.pack(pady=20)

length_var = tk.IntVar()
length_label = tk.Label(root, text="Comprimento da senha:", font=("Arial", 14), bg="#F9F9F9")
length_label.pack()

length_scale = tk.Scale(root, from_=8, to=20, orient=tk.HORIZONTAL, variable=length_var, bg="#F9F9F9", bd=0, sliderlength=15, length=300)
length_scale.pack()

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(root, text="Incluir letras maiúsculas", variable=uppercase_var, font=("Arial", 12), bg="#F9F9F9")
uppercase_check.pack()

lowercase_var = tk.BooleanVar()
lowercase_check = tk.Checkbutton(root, text="Incluir letras minúsculas", variable=lowercase_var, font=("Arial", 12), bg="#F9F9F9")
lowercase_check.pack()

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(root, text="Incluir números", variable=digits_var, font=("Arial", 12), bg="#F9F9F9")
digits_check.pack()

special_chars_var = tk.BooleanVar()
special_chars_check = tk.Checkbutton(root, text="Incluir caracteres especiais", variable=special_chars_var, font=("Arial", 12), bg="#F9F9F9")
special_chars_check.pack()

generate_button = tk.Button(root, text="Gerar Senha", font=("Arial", 16), command=generate_password, bg="#0078D4", fg="white", activebackground="#005A9E", activeforeground="white")
generate_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#F9F9F9")
result_label.pack()

root.mainloop()

