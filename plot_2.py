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

class Plot2():
    def __init__(self,root):

        self.root = root
        self.main_plot_frame = None
        self.second_plot_frame = None
        self.third_plot_frame = None
        # self.plot_2_callback = plot_2_callback

        self.Table = None
        self.Graphs = None

    # Metodo que elimina todo lo que muestra la pagina
    def close(self):
        self.third_plot_frame.destroy()

    def show(self):

        columns = ("columna1", "columna2", "columna3", "columna4","columna5","columna6")  # Especifica los nombres de las columnas
        second_plot_frame = Frame(self.root)
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
        second_plot_frame.grid(ipadx=10, ipady=5)
        self.second_plot_frame = second_plot_frame

        
        title = Label(second_plot_frame, text="Plantilla general de resultados estadisticos",font=(None, 15)) 
        title.grid(row = 0, column = 0, columnspan = 1,sticky="nw")
        
   


        
    
    

    # Metodo que recibe los datos nuevos y manda a actualizar estructuras y plots
    def new_group_data_plot(self,dict_r, dict_l):
        self.Table.insert(dict_r, dict_l)
        # self.Graphs.update_gmean(dict_r, dict_l)
        # self.update_data(dict_r, dict_l)
    
    def update_bar_plot(self, defl_left_right_dict):
        self.Graphs.update_bar(defl_left_right_dict)

    # def add_scrollbar(self):
    #     scrollbar = ttk.Scrollbar(self.second_plot_frame, orient="vertical", command=self.table.yview)
    #     scrollbar.grid(row=2, column=3, sticky="ns")
    #     self.table.configure(yscrollcommand=scrollbar.set)


