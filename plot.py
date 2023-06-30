from tkinter import *
from tkinter.ttk import Label, Frame, Button, Scrollbar
import view
import table
import graphs
from tkinter.ttk import Treeview
import tkinter as tk
from tkinter import ttk


# Clase correspondiente a la vista encargada de mostrar los datos y graficos

class Plot():
    def __init__(self,root,plot_callback):

        self.root = root
        self.main_plot_frame = None
        self.second_plot_frame = None
        self.plot_callback = plot_callback

        self.Table = None
        self.Graphs = None

    # Metodo que elimina todo lo que muestra la pagina
    def close(self):
        self.second_plot_frame.destroy()

    # def show(self):
    #     columns = ("columna1", "columna2", "columna3", "columna4", "columna5", "columna6")
    #     second_plot_frame = tk.Frame(self.root)
    #     second_plot_frame.grid(ipadx=10, ipady=5)
    #     self.second_plot_frame = second_plot_frame
    #     title = tk.Label(second_plot_frame, text="Plantilla general de resultados estadisticos", font=(None, 15))
    #     title.grid(row=0, column=0, columnspan=1, sticky="nw")

    #     Label(second_plot_frame, text="Temperatura: %s" % (view.temp)).grid(column=0, row=1, sticky="nw")
    #     Label(second_plot_frame, text="Grupos: %s" % (view.muestras)).grid(column=1, row=1, sticky="nw")
    #     Label(second_plot_frame, text="Muestras: %s" % (view.grupos)).grid(column=2, row=1, sticky="nw")

        

    #     # self.table = ttk.Treeview(second_plot_frame, columns=columns, show='headings')
    #     # self.table.grid(row=2, column=0, columnspan=3, sticky="nsew")

    #     self.Table = table.Table(self.second_plot_frame) # instancia de tabla

    #     # self.add_scrollbar()

    #     # self.Graphs = graphs.Graphs(self.second_plot_frame) # instancia DEL GRAFICO PRINCIPAL QUE VA A SER BARRAS

    #     # tk.Button(second_plot_frame, text="Atras", command=self.plot_callback).grid(column=0, row=3, sticky="nw")
    #     Button(second_plot_frame, text="Atras", command=self.plot_callback).grid(column=0, row=3,sticky="nw")

    def show(self):

        columns = ("columna1", "columna2", "columna3", "columna4","columna5","columna6")  # Especifica los nombres de las columnas
        second_plot_frame = Frame(self.root)
        self.table = Treeview(second_plot_frame, columns=columns, show='headings')
       
        second_plot_frame.grid(ipadx=10, ipady=5)
        self.second_plot_frame = second_plot_frame
        title = Label(second_plot_frame, text="Plantilla general de resultados estadisticos",font=(None, 15)) 
        title.grid(row = 0, column = 0,columnspan = 1,sticky="nw")
        

        Label(second_plot_frame, text= "Temperatura: %s"%(view.temp)).grid(column=0, row=1,sticky="nw")
        Label(second_plot_frame, text="Grupos: %s"%(view.muestras)).grid(column=1, row=1,sticky="nw")
        Label(second_plot_frame, text="Muestras: %s"%(view.grupos)).grid(column=2, row=1,sticky="nw")

        self.Table = table.Table(self.second_plot_frame) # instancia de tabla

        self.Graphs = graphs.Graphs(self.second_plot_frame) # instancia DEL GRAFICO PRINCIPAL QUE VA A SER BARRAS

        Button(second_plot_frame, text="Atras", command=self.plot_callback).grid(column=0, row=3,sticky="nw")

        
       

    # Metodo que recibe los datos nuevos y manda a actualizar estructuras y plots
    def new_group_data_plot(self,dict_r, dict_l):
        self.Table.insert(dict_r, dict_l)
        # self.Graphs.update_gmean(dict_r, dict_l)
        # self.update_data(dict_r, dict_l)
    
    def update_bar_plot(self, defl_left_right_dict):
        self.Graphs.update_bar(defl_left_right_dict)

    def add_scrollbar(self):
        scrollbar = ttk.Scrollbar(self.second_plot_frame, orient="vertical", command=self.table.yview)
        scrollbar.grid(row=2, column=3, sticky="ns")
        self.table.configure(yscrollcommand=scrollbar.set)


