import tkinter as tk
from tkinter import messagebox

class TaskListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")
        
        self.tasks = []
        
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill="both", expand=True)
        
        self.title_label = tk.Label(self.canvas, text="Lista de Tarefas", font=("Helvetica", 16, "bold"), bg="white")
        self.title_label.pack(pady=10)
        
        self.task_entry = tk.Entry(self.canvas, font=("Helvetica", 12), bg="white", fg="black")
        self.task_entry.pack(padx=20, pady=10, fill="both")
        self.task_entry.bind("<Return>", self.add_task_enter)  # Associar evento "Return" à função
        
        self.add_button = tk.Button(self.canvas, text="Adicionar Tarefa", command=self.add_task, font=("Helvetica", 12), bg="black", fg="gold")
        self.add_button.pack(pady=5)
        
        self.task_listbox = tk.Listbox(self.canvas, font=("Helvetica", 12), bg="white", fg="black", selectbackground="black", selectforeground="gold")
        self.task_listbox.pack(padx=20, pady=10, fill="both", expand=True)
        
        self.remove_button = tk.Button(self.canvas, text="Remover Selecionada", command=self.remove_selected_task, font=("Helvetica", 12), bg="black", fg="gold")
        self.remove_button.pack(pady=5)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, "end")
    
    def add_task_enter(self, event):  # Função para adicionar tarefa com Enter
        self.add_task()
    
    def remove_selected_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_task_listbox()
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, "end")
        for task in self.tasks:
            self.task_listbox.insert("end", task)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Lista de Tarefas")
    root.geometry("400x500")  # Defina a largura e a altura desejadas
    
    app = TaskListApp(root)
    root.mainloop()
