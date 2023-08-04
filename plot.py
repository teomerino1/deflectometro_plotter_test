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
        # self.go_to_config = go_to_config
        #############
        # self.go_to_plot_2_from_plot_1 = go_to_plot_2_from_plot_1
        #############
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

            second_plot_frame = Frame(self.root)
            self.second_plot_frame = second_plot_frame

            columns = ("columna1", "columna2", "columna3", "columna4","columna5","columna6")  # Especifica los nombres de las columnas

            self.table = Treeview(second_plot_frame, columns=columns, show='headings')
            
            # Configurar el número de filas y columnas
            second_plot_frame.grid_rowconfigure(0, weight=1)
            second_plot_frame.grid_rowconfigure(1, weight=1)
            second_plot_frame.grid_rowconfigure(2, weight=1)
            second_plot_frame.grid_rowconfigure(3, weight=1)
            second_plot_frame.grid_rowconfigure(4, weight=1)
            second_plot_frame.grid_columnconfigure(0, weight=1)
            second_plot_frame.grid_columnconfigure(1, weight=1)
            second_plot_frame.grid_columnconfigure(2, weight=1)
            second_plot_frame.grid_columnconfigure(3, weight=1)
        
            title = Label(second_plot_frame, text="Plantilla general de resultados estadisticos",font=(None, 25)) 
            self.title = title
            
            # temperatura = Label(second_plot_frame, text= "Temperatura: %s"%(view.temp))
            # self.temperatura = temperatura

            # muestras = Label(second_plot_frame, text="Muestras: %s"%(view.grupos))
            # self.muestras = muestras 

            # grupos = Label(second_plot_frame, text="Grupos: %s"%(view.muestras))
            # self.grupos = grupos 

            atras = Button(second_plot_frame, text="Atras", command=self.go_to_config)
            self.atras = atras 

            next = Button(second_plot_frame,text="Next",command=self.go_to_plot_2_from_plot_1)
            self.next = next

            self.Table = table.Table(self.second_plot_frame) # instancia de tabla

            self.Graphs = graphs.Graphs(self.second_plot_frame) # instancia DEL GRAFICO PRINCIPAL QUE VA A SER BARRAS

        if(a == 1):

            self.second_plot_frame.grid(ipadx=10, ipady=5)
            self.title.grid(row = 0, column = 0, columnspan = 1,sticky="nw")
            # self.temperatura.grid(row=1, column=0, sticky="nw")
            # self.muestras.grid(row=1, column=1 ,sticky="nw")
            # self.grupos.grid(row=2, column=0, sticky="nw")
            self.atras.grid(row=3, column=0, sticky="nw")
            self.next.grid(row=4, column=0,sticky="nw")
            
    def generar_pdf(self):
    # Crear el objeto canvas
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

    
   


