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


"""
La clase Graphs corresponde a los objetos de los gráficos de deflexiones individuales.
Contiene todos los atributos correspondientes y la lógica de actualización de datos en la interfaz
"""
class Graphs():
    def __init__(self, frame):
        self.a=None
        self.frame = frame
        self.defl_r_data = []
        self.defl_l_data = []
        self.indexes = []
        self.flag=0
        self.cantidad_barras=500
        self.contador_graficos=0
        self.datos_actual=0
        self.data_selector=0
        self.figure_bar_l=None
        self.figure_bar_r=None
        self.bar_l=None
        self.bar_r=None
        self.bar_widget_l=None
        self.bar_widget_r=None
        self.show_bar_graph()
        
    """
    Esta función es la encargada de crear el gráfico de barras

    @return Los elementos que contiene el gráfico
    """
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
        
    """
    Este método se encarga de actualizar los datos a mostrar en los gráficos de deflexiones individuales.
    Guarda en 'dataset_der ' 'dataset_izq' los valores actuales de los arreglos en base al valor de 'contador_gráficos'

    Si los arreglos de datos que se están llenando son los mismos que se estan seleccionando con 'data_selector', los grafico en tiempo real

    Si se alcanza la cantidad de barras a mostrar (500) se incrementa el número de gráficos a mostrar y se crean arreglos nuevos

    @param: Los arreglos con los valores de deflexiones a graficar
    """
    def update_bar(self, defl_r,defl_l):

        dataset_der = getattr(self,f"defl_r_data_{self.contador_graficos}")
        dataset_izq = getattr(self,f"defl_l_data_{self.contador_graficos}")
        indexes=getattr(self,f"indexes_{self.contador_graficos}")

        dataset_der.extend(defl_r)
        dataset_izq.extend(defl_l)
        indexes=list(range(self.contador_graficos*self.cantidad_barras,self.contador_graficos*self.cantidad_barras+len(dataset_der)))

        # print("Len indexes UPDATE BAR:",len(indexes))
        # print("Len datos der UPDATE BAR:",len(dataset_izq))
        #Si el selector de datos es el actual, grafico en tiempo real
        if(self.contador_graficos==self.data_selector):
            self.graph_data(dataset_der,dataset_izq,indexes,limite=self.contador_graficos)
        #Si ya alcancé la cantidad de datos, incremento contador y creo arrays nuevos
        if(len(indexes)>=self.cantidad_barras):
            print("IDENTIFICO QUE TENGO QUE CREAR NEWS")
            self.contador_graficos+=1
            self.create_arrays()


    """
    Este método muestra los datos de deflexiones individuales que el usuario selecciona con los botones para avanzar o
    retroceder entre grupos de 500 datos.

    Si el usuario está parado en el gráfico de los datos que se están ploteando en tiempo real y quiere avanzar, no hace nada

    Solo va a graficar los datos en caso de que los arreglos existan y tengan datos

    @param step: El paso que el usuario quiere realizar:
                 1 para avanzar
                -1 para retroceder
    """
    def show_data(self,step):
        #Si estoy parado en el gráfico actual y quiero avanzar, no hago nada
        if(self.data_selector==self.contador_graficos and step==1):
            print("ESTOY EN EL ACTUAL. NO MUESTRO")
            print("CONTADOR GRAFICOS:",self.contador_graficos)
            print("DATA SELECTOR:",self.data_selector)
            return
        valor_anterior=self.data_selector
        self.data_selector += step

        #Si existen los arrays y además tienen datos los muestro. Si no, no.
        if hasattr(self, f"defl_r_data_{self.data_selector}") and len(getattr(self, f"defl_l_data_{self.data_selector}"))>0:
            print("MUESTRO")
            print("CONTADOR GRAFICOS:",self.contador_graficos)
            print("DATA SELECTOR:",self.data_selector)
            dataset_der = getattr(self, f"defl_r_data_{self.data_selector}")
            dataset_izq = getattr(self, f"defl_l_data_{self.data_selector}")
            indexes=list(range(self.data_selector*self.cantidad_barras,self.data_selector*self.cantidad_barras+len(dataset_der)))
            self.graph_data(dataset_der,dataset_izq,indexes,limite=self.data_selector)

        else:
            print("NO HAY PA MOSTRA")
            self.data_selector=valor_anterior
            print("CONTADOR GRAFICOS:",self.contador_graficos)
            print("DATA SELECTOR:",self.data_selector)

    """
    Este método grafica los datos que correspondan
    Es llamado para graficar datos en tiempo real, o para graficar el conjunto de 500 datos que el usuario seleccione

    @params: 
            dataset_der, dataset_izq: Los conjuntos de datos a graficar de deflexion derecha e izquierda
            indexes: El arreglo de datos del eje 'x'
            limite: El limite inferior del eje 'x'
    """
    def graph_data(self,dataset_der,dataset_izq,indexes,limite):

        self.figure_bar_r.clear()
        self.figure_bar_l.clear()

        subfigure_der = self.figure_bar_r.add_subplot(211)
        subfigure_izq = self.figure_bar_l.add_subplot(211)
        
        #Si los datasets ya tienen datos, los grafico. Puede pasar que existan pero todavia no tengan datos
        if(len(dataset_der) and len(dataset_izq)>0):
            subfigure_der.set_xlim(limite*self.cantidad_barras,limite*self.cantidad_barras+len(dataset_der))
            subfigure_izq.set_xlim(limite*self.cantidad_barras,limite*self.cantidad_barras+len(dataset_izq))

            subfigure_der.set_ylim(0,max(dataset_der)+1)
            subfigure_izq.set_ylim(0,max(dataset_izq)+1)
            # Grafica todos los datos almacenados
            subfigure_der.bar(indexes, dataset_der, width=1)
            subfigure_izq.bar(indexes, dataset_izq, width=1)

            subfigure_der.set_title("Deflexiones Derecha")
            subfigure_izq.set_title("Deflexiones Izquierda")

            subfigure_der.set_xlabel("nº")
            subfigure_izq.set_xlabel("nº")

            subfigure_der.set_ylabel("Deflexiones")
            subfigure_izq.set_ylabel("Deflexiones")
        
            subfigure_der.grid(axis='both',linestyle='dotted')
            subfigure_izq.grid(axis='both',linestyle='dotted')

            # Llama al método draw_idle() para actualizar la interfaz gráfica
            self.figure_bar_r.canvas.draw_idle()
            self.figure_bar_l.canvas.draw_idle()


    """
    Este método se encarga de crear los gráficos de barras y de crear los arrays al comienzo de la ejecución
    Es llamado una única vez cuando el programa se ejecuta y quedan listos los objetos para graficar las deflexiones
    """
    def show_bar_graph(self):
        self.figure_bar_l, self.bar_l, self.bar_widget_l = self.bar_graph(2, 0,"Deflexiones Izquierda")
        self.figure_bar_r, self.bar_r, self.bar_widget_r = self.bar_graph(2, 1,"Deflexiones Derecha")
        self.create_arrays()
 

    """
    Este método crea arrays dinámicamente a medida que se necesiten en la ejecución.
    Es llamado cada vez que se 'llenan' los arreglos con 500 datos y crea nuevos para continuar la ejecución con nuevos datos
    """
    def create_arrays(self): 
        new_defl_r_data = f"defl_r_data_{self.contador_graficos}"
        setattr(self, new_defl_r_data, [])
        new_defl_l_data = f"defl_l_data_{self.contador_graficos}"
        setattr(self, new_defl_l_data, [])
        new_indexes = f"indexes_{self.contador_graficos}"
        setattr(self, new_indexes, [])
        print("Creé los arrays:")

    """
    Este método devuelve el conjunto de indices actual
    """
    def get_indexes_actual(self):
        actual_indexes = f"indexes_{self.contador_graficos}"
        setattr(self, actual_indexes, [])
        return actual_indexes
    
    """
    Este método devuelve el dataset actual de deflexiones de lado izquierdo
    """
    def get_dataset_actual_izq(self):
        defl_l_data_actual = f"defl_l_data_{self.contador_graficos}"
        setattr(self, defl_l_data_actual, [])
        return defl_l_data_actual
    
    """
    Este método devuelve el dataset actual de deflexiones de lado derecho
    """
    def get_dataset_actual_der(self):
        defl_r_data_actual = f"defl_r_data_{self.contador_graficos}"
        setattr(self, defl_r_data_actual, [])
        return defl_r_data_actual    

    """
    Este método devuelve el array total derecho. Se utiliza para saber cuantos datos hay 
    """
    def get_array_total(self):
        data_total=[]
        for i in range(0,self.contador_graficos+1):
            data_total.extend(getattr(self, f"defl_r_data_{i}"))
        return data_total
    

    """
    Este método devuelve la cantidad de datos que tienen los arreglos.
    Se utiliza para determinar la 'progresiva final' en el PDF.
    """
    def get_max(self):
        data_total_actual=self.get_array_total()
        if(data_total_actual==[]):
            messagebox.showwarning("Aviso","No hay datos para mostrar en PDF")
        else:
            return len(data_total_actual)
    
    """
    Este método guarda las imágenes de los gráficos para poder insertarlas 
    en el PDF

    @params:
            numero_pagina: Determina el número de página en donde deben estar los gráficos
            graph_flag: Si es 1, se guardan los gráficos con las deflexiones totales de todos los datos
                        Si es 0, se guardan los gráficos con las deflexiones parciales de datos
    """
    def donwload_graphs(self,numero_pagina,graph_flag):
        
        figure_bar_r = Figure(figsize=(7,6), dpi=100,facecolor='#F6F4F2')
        figure_bar_l = Figure(figsize=(7,6), dpi=100,facecolor='#F6F4F2')
        subfigure_der_aux=figure_bar_r.add_subplot(211)
        subfigure_izq_aux=figure_bar_l.add_subplot(211)

        #Si la flag de grafico completo es 1
        if(graph_flag==1):

            data_total_der=[]
            data_total_izq=[]
            #Recorro todos los arrays creados y guardo los valores
            for i in range(0,self.contador_graficos+1):
                data_total_der.extend(getattr(self, f"defl_r_data_{i}"))
                data_total_izq.extend(getattr(self, f"defl_l_data_{i}"))

            indexes=list(range(1,len(data_total_der)+1))

            subfigure_der_aux.set_ylim(0,max(data_total_der)+1)
            subfigure_izq_aux.set_ylim(0,max(data_total_izq)+1)

            subfigure_der_aux.bar(indexes, data_total_der, width=1)
            subfigure_izq_aux.bar(indexes, data_total_izq, width=1)
            
        else:
            #Obtengo los graficos con datos parciales
            data_parcial_der=(getattr(self, f"defl_r_data_{self.data_selector}"))
            data_parcial_izq=(getattr(self, f"defl_l_data_{self.data_selector}"))

            indexes=list(range(self.data_selector*self.cantidad_barras,self.data_selector*self.cantidad_barras+len(data_parcial_der)))

            subfigure_der_aux.set_ylim(0,max(data_parcial_der)+1)
            subfigure_izq_aux.set_ylim(0,max(data_parcial_izq)+1)

            subfigure_der_aux.set_xlim(self.data_selector*self.cantidad_barras,self.data_selector*self.cantidad_barras+len(data_parcial_der))
            subfigure_izq_aux.set_xlim(self.data_selector*self.cantidad_barras,self.data_selector*self.cantidad_barras+len(data_parcial_izq))

            subfigure_der_aux.bar(indexes, data_parcial_der, width=1)
            subfigure_izq_aux.bar(indexes, data_parcial_izq, width=1)

            
        subfigure_der_aux.set_title("Derecha")
        subfigure_izq_aux.set_title("Izquierda")

        subfigure_der_aux.set_xlabel("nº")
        subfigure_izq_aux.set_xlabel("nº")
        
        subfigure_der_aux.set_ylabel("Deflexiones")
        subfigure_izq_aux.set_ylabel("Deflexiones")

        figure_bar_l.savefig('figure_bar_l.png', bbox_inches='tight')
        figure_bar_r.savefig('figure_bar_r.png', bbox_inches='tight')

        ancho_pagina,alto_pagina=A4
        centro_x = ancho_pagina / 2

        output_pdf = 'defl_individuales.pdf'
        c = canvas.Canvas(output_pdf, pagesize=A4)
    
        c.drawImage('header2.png', 25, 773, width=585, height=60)
        c.drawImage('image.png', 0, 0, width=600, height=120)
        c.drawImage('figure_bar_l.png', 40, 150, width=500, height=280)
        c.drawImage('figure_bar_r.png', 40, 450,width=500, height=280)
        c.drawString(centro_x-1, 125, f"{numero_pagina+1}")
                    
        c.save()
        os.remove('figure_bar_l.png')
        os.remove('figure_bar_r.png')



       

