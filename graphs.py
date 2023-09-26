from tkinter import *
import tkinter as tk
from tkinter.ttk import Label, Frame, Button, Scrollbar, Treeview
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from reportlab.lib.pagesizes import letter,A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from matplotlib.backends.backend_pdf import FigureCanvasPdf
import io
import PyPDF2
from PyPDF2 import PdfWriter,PdfReader
import os
from tkinter import messagebox

# Clase donde se inicializan y actualizan los graficos

class Graphs():
    def __init__(self, frame):
        self.a=None
        self.frame = frame
        # Inicializa las listas para almacenar los datos
        self.defl_r_data = []
        self.defl_l_data = []
        self.indexes = []
        self.flag=0
        #CANTIDAD DE BARRAS A QUERER GRAFICAR!!!!!!!!!
        self.cantidad_barras=20
        #VARIABLE PARA INSTANCIAR NUEVOS ARRAY DE DATOS, POR EJEMPLO 'self.defl_l_data_1,self.defl_l_data_2'
        self.contador_graficos=0
        #VARIABLE PARA SABER QUÉ ARRAY DE DATOS ESTOY SELECCIONANDO.
        self.datos_actual=0

        self.figure_bar_l=None
        self.figure_bar_r=None
        self.bar_l=None
        self.bar_r=None
        self.bar_widget_l=None
        self.bar_widget_r=None
        self.show()
        


    def bar_graph(self, row, column,title):
        
        figure = Figure(figsize=(7,6), dpi=100,facecolor='#F6F4F2')
        sub_figure=figure.add_subplot(211)

        sub_figure.set_ylim(0,100)
        sub_figure.set_xlim(0,10)
        sub_figure.set_title(title)

        sub_figure.set_xlabel("nº grupo")
        sub_figure.set_ylabel("Deflexiones")

        sub_figure.bar([], [], width = 1, linewidth=0.1)
        sub_figure.grid(axis='both',linestyle='dotted')

        figure.subplots_adjust(bottom=0,top=0.94)
        
        bar = FigureCanvasTkAgg(figure,self.frame)
        
        bar_widget = bar.get_tk_widget()
        bar_widget.grid(row = row, column = column,padx=(0,0))
    
        return figure, bar, bar_widget
        
    def update_bar(self, defl_r,defl_l):

        #QUEDÉ ACÁ TRATANDO DE IMPLEMENTAR LA LÓGICA PARA ALTERNAR ENTRE CONJUNTOS DE DATOS DISTINTOS
        dataset_der = getattr(self,f"defl_r_data_{self.contador_graficos}")
        dataset_izq = getattr(self,f"defl_l_data_{self.contador_graficos}")
        indexes=getattr(self,f"indexes_{self.contador_graficos}")

        print("Contador graficos:",self.contador_graficos)
        print("Dataset der before extend:",dataset_der)
        dataset_der.extend(defl_r)
        dataset_izq.extend(defl_l)
        indexes=list(range(self.contador_graficos*self.cantidad_barras,self.contador_graficos*self.cantidad_barras+len(dataset_der)))
        print("Defl r parametro:",defl_r)
        print("Dataset der after extend:",dataset_der)
        print("Indexes:",indexes)

        self.figure_bar_r.clear()
        self.figure_bar_l.clear()

        subfigure_der = self.figure_bar_r.add_subplot(211)
        subfigure_izq = self.figure_bar_l.add_subplot(211)

        subfigure_der.set_ylim(0, (max(dataset_der)+1))
        subfigure_izq.set_ylim(0, (max(dataset_izq)+1))
        
        subfigure_der.set_xlim(self.contador_graficos*self.cantidad_barras,self.contador_graficos*self.cantidad_barras+len(dataset_der))
        subfigure_izq.set_xlim(self.contador_graficos*self.cantidad_barras,self.contador_graficos*self.cantidad_barras+len(dataset_der))

        # Grafica todos los datos almacenados
        subfigure_der.bar(indexes, dataset_der, width=1)
        subfigure_izq.bar(indexes, dataset_izq, width=1)

        subfigure_der.set_title("Deflexion Derecha")
        subfigure_izq.set_title("Deflexion Izquierda")

        subfigure_der.set_xlabel("nº grupo")
        subfigure_izq.set_xlabel("nº grupo")

        subfigure_der.set_ylabel("Deflexiones")
        subfigure_izq.set_ylabel("Deflexiones")
       
        subfigure_der.grid(axis='both',linestyle='dotted')
        subfigure_izq.grid(axis='both',linestyle='dotted')

         # Llama al método draw_idle() para actualizar la interfaz gráfica
        self.figure_bar_r.canvas.draw_idle()
        self.figure_bar_l.canvas.draw_idle()

        if(len(indexes)==self.cantidad_barras):
            print("Aca me doy cuenta que llegué a la cantidad de datos a mostrar")
            self.contador_graficos+=1
            self.create_arrays()


    def show_bar_graph(self):
        self.figure_bar_l, self.bar_l, self.bar_widget_l = self.bar_graph(2, 0,"Deflexion Izquierda")
        self.figure_bar_r, self.bar_r, self.bar_widget_r = self.bar_graph(2, 1,"Deflexion Derecha")
        ########################
        self.create_arrays()
        #######################

    def create_arrays(self): 
        new_defl_r_data = f"defl_r_data_{self.contador_graficos}"
        setattr(self, new_defl_r_data, [])
        new_defl_l_data = f"defl_l_data_{self.contador_graficos}"
        setattr(self, new_defl_l_data, [])
        new_indexes = f"indexes_{self.contador_graficos}"
        setattr(self, new_indexes, [])
        print("Creé los arrays:")
            
    def select_dataset(self, datos):
        self.datos_actual = datos

    def get_selected_dataset(self,datos):
        dataset_name = f"{datos}_{self.datos_actual}"
        return getattr(self, dataset_name)

    def show(self):
        self.show_bar_graph()

    def set_flag(self,flag):
        self.flag=flag

    def get_flag(self):
        return self.flag
    
    def get_max(self):
        if(self.defl_l_data==[]):
            messagebox.showwarning("Aviso","No hay datos para mostrar en PDF")
        else:
            return max(self.indexes)
    
    def donwload_graphs(self,numero_pagina):
       
        # Ajustar los límites para eliminar espacio en blanco
        if(self.defl_l_data==[] or self.defl_r_data==[]):
            return
        else:
            self.figure_bar_l.gca().set_ylim(0, (max(self.defl_l_data)+1))
            self.figure_bar_r.gca().set_ylim(0, (max(self.defl_r_data)+1))  # Ajustar límites en el eje y según tu necesidad
            self.figure_bar_l.savefig('figure_bar_l.png', bbox_inches='tight')
            self.figure_bar_r.savefig('figure_bar_r.png', bbox_inches='tight')

            ancho_pagina,alto_pagina=A4
            centro_x = ancho_pagina / 2

            output_pdf = 'defl_individuales.pdf'
            c = canvas.Canvas(output_pdf, pagesize=A4)
          
            c.drawImage('header2.png', 25, 773, width=575, height=60)
            c.drawImage('image.png', 0, 0, width=600, height=120)
            c.drawImage('figure_bar_l.png', 100, 200, width=383, height=230)
            c.drawImage('figure_bar_r.png', 100, 500,width=383, height=230)
            c.drawString(centro_x-1, 125, f"{numero_pagina+1}")
            
            
            c.save()
            os.remove('figure_bar_l.png')
            os.remove('figure_bar_r.png')







       

