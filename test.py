from tkinter import *
from tkinter.ttk import Treeview

class MyTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabla de Mediciones")
        
        # columns = ("Grupos_r", "Radio_r", "Defl_r", "R*D_r", "R/D_r","Grupos_L", "Radio_L", "Defl_L", "R*D_L", "R/D_L")
        columns = ("Grupos_r", "Radio_r", "Defl_r", "R*D_r", "R/D_r", "Radio_L", "Defl_L", "R*D_L", "R/D_L")
        
        # Crear el Treeview
        self.table = Treeview(self.frame, columns=columns, show='headings')
        # self.table.grid(row=1, column=0, columnspan=3)
        self.table.grid(row=1, column=1,columnspan=2,pady=30)
        # Configurar el alto del Treeview
        self.table.configure(height=7)
        
        headers = [
            ("Grupos_r", "Grupos"),
            ("Radio_r", "Radio"),
            ("Defl_r", "Defl."),
            ("R*D_r", "R*D"),
            ("R/D_r", "D/R"),
            # ("Grupos_L", "Groups L"),
            ("Radio_L", "Radio"),
            ("Defl_L", "Defl."),
            ("R*D_L", "R*D"),
            ("R/D_L", "D/R")
        ]

if __name__ == "__main__":
    root = Tk()
    app = MyTableApp(root)
    root.mainloop()
