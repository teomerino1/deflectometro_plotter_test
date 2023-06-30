import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Crear el Treeview
tree = ttk.Treeview(root)
tree.pack(side="left", fill="y")

# Crear el Scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")

# Configurar el Scrollbar para controlar el Treeview
tree.configure(yscrollcommand=scrollbar.set)

# Añadir elementos al Treeview
for i in range(50):
    tree.insert("", "end", text=f"Item {i}")

root.mainloop()






