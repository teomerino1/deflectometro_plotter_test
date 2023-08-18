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
        self.label_der=None
        self.label_izq=None

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

            self.table = Treeview(self.second_plot_frame, columns=columns, show='headings')
            
            atras = ttk.Button(self.second_plot_frame, text="Atras", command=self.go_to_config,style="TButton")
            self.atras=atras

            next = ttk.Button(self.second_plot_frame,text="Next",command=self.go_to_plot_2_from_plot_1,style="TButton")
            self.next = next

            self.Table = table.Table(self.second_plot_frame) 
            self.Graphs = graphs.Graphs(self.second_plot_frame) 

            label_der = Label(self.second_plot_frame, text="Huella Externa (DERECHA)", font=("Helvetica", 22, "bold"))
            self.label_der=label_der

            label_izq = Label(self.second_plot_frame, text="Huella Interna (IZQUIERDA)", font=("Helvetica", 22, "bold"))
            self.label_izq=label_izq

        if(a == 1):
            self.second_plot_frame.grid()  
            self.atras.grid(row=0, column=0,pady=(0,20),sticky=NW)
            self.next.grid(row=0, column=1,padx=(500,0),pady=(0,20))
            self.label_der.grid(row=1, column=0,padx=(320,0), pady=0)
            self.label_izq.grid(row=1, column=1,padx=(0,150))
            
            
    def generar_pdf(self):
        # self.Table.donwload_table()
        self.Graphs.donwload_graphs()
        
    def get_prog_max(self):
        return self.Graphs.get_max()
    
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

    
   


