from tkinter import *
from tkinter.ttk import Label, Frame, Button, Scrollbar
import view
import table
import graphs
from tkinter.ttk import Treeview
import tkinter as tk
from tkinter import ttk

from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk


# Clase correspondiente a la vista encargada de mostrar los datos y graficos

class Plot():
    def __init__(self,root,go_to_config, go_to_plot_2_from_plot_1):

        self.root = root
        self.main_plot_frame = None
        self.second_plot_frame = None
        self.go_to_config = go_to_config
        #############
        self.go_to_plot_2_from_plot_1 = go_to_plot_2_from_plot_1
        #############
        self.Table = None
        self.Graphs = None

    # Metodo que elimina todo lo que muestra la pagina
    def close(self):
        self.second_plot_frame.grid_forget()
        # self.second_plot_frame.destroy()

    def show(self,a):

        if(a==0):
            columns = ("columna1", "columna2", "columna3", "columna4","columna5","columna6")  # Especifica los nombres de las columnas
            second_plot_frame = Frame(self.root)
            second_plot_frame.grid(ipadx=10, ipady=5)
            self.table = Treeview(second_plot_frame, columns=columns, show='headings')
            
            # Configurar el número de filas y columnas
            second_plot_frame.grid_rowconfigure(0, weight=1)
            second_plot_frame.grid_rowconfigure(1, weight=1)
            second_plot_frame.grid_rowconfigure(2, weight=1)
            second_plot_frame.grid_rowconfigure(3, weight=1)
            second_plot_frame.grid_rowconfigure(4, weight=1)
            second_plot_frame.grid_rowconfigure(5, weight=1)
            second_plot_frame.grid_rowconfigure(6, weight=1)
            second_plot_frame.grid_rowconfigure(7, weight=1)
            second_plot_frame.grid_rowconfigure(8, weight=1)
            # config_frame.grid_rowconfigure(4, weight=1)
            second_plot_frame.grid_columnconfigure(0, weight=1)
            second_plot_frame.grid_columnconfigure(1, weight=1)
            second_plot_frame.grid_columnconfigure(2, weight=1)
            second_plot_frame.grid_columnconfigure(3, weight=1)
        
            self.second_plot_frame = second_plot_frame

            
            title = Label(second_plot_frame, text="Plantilla general de resultados estadisticos",font=(None, 25)) 
            title.grid(row = 0, column = 0, columnspan = 1,sticky="nw")
            
            temperatura = Label(second_plot_frame, text= "Temperatura: %s"%(view.temp))
            temperatura.grid(row=1, column=0, sticky="nw")

            muestras = Label(second_plot_frame, text="Muestras: %s"%(view.grupos))
            muestras.grid(row=1, column=1 ,sticky="nw")

            grupos = Label(second_plot_frame, text="Grupos: %s"%(view.muestras))
            grupos.grid(row=2, column=0, sticky="nw")

            atras = Button(second_plot_frame, text="Atras", command=self.go_to_config)
            atras.grid(row=3, column=0, sticky="nw")

            next= Button(second_plot_frame,text="Next",command=self.go_to_plot_2_from_plot_1)
            next.grid(row=4, column=0,sticky="nw")

            self.Table = table.Table(self.second_plot_frame) # instancia de tabla

            self.Graphs = graphs.Graphs(self.second_plot_frame,plot_number=1) # instancia DEL GRAFICO PRINCIPAL QUE VA A SER BARRAS

        if(a==1):

            self.second_plot_frame.grid(ipadx=10, ipady=5)
            
        # scrollbar = Scrollbar(second_plot_frame, orient="vertical", command=self.table.yview)
        # scrollbar.grid(row=0, column=2, rowspan=7, sticky="ns")
        # self.table.configure(yscrollcommand=scrollbar.set)

    
    def grid_plot1(self):

        self.second_plot_frame.grid(ipadx=10, ipady=5)

    def update_bar_plot(self, defl_left_right_dict):
        self.Graphs.update_bar(defl_left_right_dict)

    # Metodo que recibe los datos nuevos y manda a actualizar estructuras y plots
    def new_group_data_plot(self,dict_r, dict_l):
        self.Table.insert(dict_r, dict_l)
        # self.Graphs.update_gmean(dict_r, dict_l)
        # self.update_data(dict_r, dict_l)
    
   

    # def add_scrollbar(self):
    #     scrollbar = ttk.Scrollbar(self.second_plot_frame, orient="vertical", command=self.table.yview)
    #     scrollbar.grid(row=2, column=3, sticky="ns")
    #     self.table.configure(yscrollcommand=scrollbar.set)


