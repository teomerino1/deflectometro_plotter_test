from tkinter import *
from tkinter.ttk import Treeview

# Clase donde se inicializa y actualiza la tabla

class Table():
    def __init__(self, frame):
        self.table = None
        self.show(frame)
          

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


        print("Last_index_r",last_index_r)
        print("last_defl_mean_r" ,last_defl_mean_r)
        print("last_radio_mean_r",last_radio_mean_r)
        print("last_rd_r",last_rd_r)
    


        self.table.insert('', END, values = (
            last_index_r,
            last_defl_mean_r, 
            last_radio_mean_r, 
            last_rd_r, 
            last_r_d_r, 
            last_index_l, 
            last_defl_mean_l, 
            last_radio_mean_l, 
            last_rd_l, 
            last_r_d_l
            )) 

    # Metodo que inicializa la tabla
    def show(self, frame):
            columns = ("groups_r", "radio_r", "defl_r", "r_d_r", "r/d_r","groups_l", "radio_l", "defl_l", "r_d_l", "r/d_l")

            self.table = Treeview(frame, columns=columns, show='headings')

            # frame.config(width=100, height=10)

            # TODO -> distinguir de alguna manera si las mediciones son de izquierda o derecha
            self.table.heading("groups_r", text="Groups")
            self.table.heading("radio_r", text="Radio")
            self.table.heading("defl_r", text="Defl.")
            self.table.heading("r_d_r", text="R*D")
            self.table.heading("r/d_r", text="R/D")

            self.table.heading("groups_l", text="Groups")
            self.table.heading("radio_l", text="Radio")
            self.table.heading("defl_l", text="Defl.")
            self.table.heading("r_d_l", text="R*D")
            self.table.heading("r/d_l", text="R/D")

            self.table.column("groups_r", anchor=CENTER,width=100)
            self.table.column("radio_r", anchor=CENTER, width=100)
            self.table.column("defl_r", anchor=CENTER, width=100)
            self.table.column("r_d_r", anchor=CENTER, width=100)
            self.table.column("r/d_r", anchor=CENTER, width=100)

            self.table.column("groups_l", anchor=CENTER,width=100)
            self.table.column("radio_l", anchor=CENTER, width=100)
            self.table.column("defl_l", anchor=CENTER, width=100)
            self.table.column("r_d_l", anchor=CENTER, width=100)
            self.table.column("r/d_l", anchor=CENTER, width=100)

            self.table.grid(row = 3, column = 0,columnspan = 3)

            # TODO -> quizas es mejor hacer dos tablas distintas, una para la derecha y otra para la izquierda
            # self.table_r = Treeview(frame, columns=columns, show='headings')
            # self.table_l = Treeview(frame, columns=columns, show='headings')
            
            # self.table_r.heading("groups_r", text="Groups")
            # self.table_r.heading("radio_r", text="Radio")
            # self.table_r.heading("defl_r", text="Defl.")
            # self.table_r.heading("r_d_r", text="R*D")
            # self.table_r.heading("r/d_r", text="R/D")

            # self.table_l.heading("groups_l", text="Groups")
            # self.table_l.heading("radio_l", text="Radio")
            # self.table_l.heading("defl_l", text="Defl.")
            # self.table_l.heading("r_d_l", text="R*D")
            # self.table_l.heading("r/d_l", text="R/D")

            # self.table_r.column("groups_r", anchor=CENTER)
            # self.table_r.column("radio_r", anchor=CENTER)
            # self.table_r.column("defl_r", anchor=CENTER)
            # self.table_r.column("r_d_r", anchor=CENTER)
            # self.table_r.column("r/d_r", anchor=CENTER)

            # self.table_l.column("groups_l", anchor=CENTER)
            # self.table_l.column("radio_l", anchor=CENTER)
            # self.table_l.column("defl_l", anchor=CENTER)
            # self.table_l.column("r_d_l", anchor=CENTER)
            # self.table_l.column("r/d_l", anchor=CENTER)

            # self.table_r.grid(row = 3, column = 0,columnspan = 3)
            # self.table_l.grid(row = 4, column = 0,columnspan = 3)