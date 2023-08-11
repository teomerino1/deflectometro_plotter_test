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
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader



# Clase correspondiente a la vista encargada de mostrar los datos y graficos

class Plot():
    def __init__(self,root,view_instance):

        self.root = root
        self.main_plot_frame = None
        self.second_plot_frame = None
        self.view_instance = view_instance
        self.title = None 
        self.temperatura = None 
        self.muestras = None 
        self.grupos = None 
        self.atras = None 
        self.next = None 
        self.Table = None
        self.Graphs = None

    # Metodo que elimina todo lo que muestra la pagina
    def close(self):
        self.second_plot_frame.grid_forget()
    
    def reset(self):
        self.second_plot_frame.destroy()
        self.show(0)

    def show(self,a):

        if(a == 0):

            width = self.root.winfo_screenwidth()
            height = self.root.winfo_screenheight()
            second_plot_frame = Frame(self.root,width=width,height=height)
            self.second_plot_frame = second_plot_frame
            
            columns = ("columna1", "columna2", "columna3", "columna4","columna5","columna6")  # Especifica los nombres de las columnas

            self.table = Treeview(second_plot_frame, columns=columns, show='headings')
            
            atras = Button(second_plot_frame, text="Atras", command=self.go_to_config)
            self.atras=atras

            next = Button(second_plot_frame,text="Next",command=self.go_to_plot_2_from_plot_1)
            self.next = next

            self.Table = table.Table(self.second_plot_frame) # instancia de tabla
            self.Graphs = graphs.Graphs(self.second_plot_frame) # insta ncia DEL GRAFICO PRINCIPAL QUE VA A SER BARRAS

        if(a == 1):

            # self.second_plot_frame.grid(ipadx=10, ipady=5,sticky="nwsew")
            self.second_plot_frame.grid(row=0, column=0, sticky="nsew")  
            # self.title.grid(row = 0, column = 0, columnspan = 1,sticky="nw")
            # self.temperatura.grid(row=1, column=0, sticky="nw")
            # self.muestras.grid(row=1, column=1 ,sticky="nw")
            # self.grupos.grid(row=2, column=0, sticky="nw")
            self.atras.grid(row=0, column=0, sticky="nw")
            self.next.grid(row=1, column=0,sticky="nw")
            
    def generar_pdf(self):
        self.Table.donwload_table()
        self.Graphs.donwload_graphs()
        

    def grid_plot1(self):
        self.second_plot_frame.grid(ipadx=10, ipady=5)

    def update_bar_plot(self, defl_r,defl_l):
        self.Graphs.update_bar(defl_r,defl_l)

    # Metodo que recibe los datos nuevos y manda a actualizar estructuras y plots
    def new_group_data_plot(self,dict_r, dict_l):
        self.Table.insert(dict_r, dict_l)

    def go_to_plot_2_from_plot_1(self):
        self.view_instance.enqueue_transition('go_to_plot_2_from_plot_1')
        
    def go_to_config(self):
        self.view_instance.enqueue_transition('go_to_config')

    def reset_table(self):
        self.Table.reset()

    
   


