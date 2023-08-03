from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
# Clase donde se inicializa y actualiza la tabla

class Table():
    def __init__(self, frame):
        self.table = None
        self.frame=frame
        self.show(frame)
        self.original_table_height = None
          

    # Metodo que inserta valores en el diccionario
    # TODO -> Falta compensar los valores con respecto a la temperatura
    def insert(self, dict_r, dict_l):

        last_index_r = dict_r['Grupo'][len(dict_r['Grupo'])-1] # ultimo valor del array
        last_defl_mean_r = dict_r['Defl.'][len(dict_r['Defl.'])-1] # ultimo valor del array
        last_radio_mean_r = dict_r['Radio'][len(dict_r['Radio'])-1] # ultimo valor del array
        last_rd_r = dict_r['R*D'][len(dict_r['R*D'])-1] # ultimo valor del array
        last_r_d_r = dict_r['D/R'][len(dict_r['D/R'])-1] # ultimo valor del array

        last_index_l = dict_l['Grupo'][len(dict_l['Grupo'])-1] # ultimo valor del array
        last_defl_mean_l = dict_l['Defl.'][len(dict_l['Defl.'])-1] # ultimo valor del array
        last_radio_mean_l = dict_l['Radio'][len(dict_l['Radio'])-1] # ultimo valor del array
        last_rd_l = dict_l['R*D'][len(dict_l['R*D'])-1] # ultimo valor del array
        last_r_d_l = dict_l['D/R'][len(dict_l['D/R'])-1] # ultimo valor del array


        self.table.insert('', END, values = (
            last_index_r,
            last_radio_mean_r, 
            last_defl_mean_r,
            last_rd_r, 
            last_r_d_r, 
            last_index_l, 
            last_radio_mean_l,
            last_defl_mean_l, 
            last_rd_l, 
            last_r_d_l
            )) 


    def show(self,frame):
        columns = ("groups_r", "radio_r", "defl_r", "r_d_r", "r/d_r","groups_l", "radio_l", "defl_l", "r_d_l", "r/d_l")
        
        # Crear el Treeview
        self.table = Treeview(self.frame, columns=columns, show='headings')

        self.table.grid(row=3, column=0, columnspan=3)

        # Configurar el alto del Treeview
        self.table.configure(height=7)

        # Crear el Scrollbar
        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.table.yview)
        scrollbar.grid(row=3, column=4, sticky="ns")
        
        self.table.configure(yscrollcommand=scrollbar.set)

        # Configurar encabezados y columnas del Treeview
        headers = [
            ("groups_r", "Groups R"),
            ("radio_r", "Radio"),
            ("defl_r", "Defl."),
            ("r_d_r", "R*D"),
            ("r/d_r", "R/D"),
            ("groups_l", "Groups L"),
            ("radio_l", "Radio"),
            ("defl_l", "Defl."),
            ("r_d_l", "R*D"),
            ("r/d_l", "R/D")
        ]
        for column, header in headers:
            self.table.heading(column, text=header)
            self.table.column(column, anchor=CENTER, width=100)

  
    def clear_table(self):
        # Elimina todos los elementos de la tabla
        self.table.delete(*self.table.get_children())

    def reset(self):
        # Agrega aquí cualquier otra lógica específica para reiniciar la tabla
        # Si tienes algún estado inicial para la tabla, puedes restaurarlo aquí
        self.clear_table()
        # Agrega aquí cualquier otro proceso que necesites realizar para reiniciar la tabla
        self.show(self)

