from tkinter import *
import tkinter as tk
from tkinter.ttk import Label, Frame, Button, Scrollbar, Treeview
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from matplotlib.backends.backend_pdf import FigureCanvasPdf
import io
import PyPDF2


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
        self.show()
        

    # Grafico que corresponde a las deflexiones individuales
    def bar_graph(self, row, column, columnspan,title):
        
        figure = Figure(figsize=(6, 7), dpi=100)
        sub_figure=figure.add_subplot(211)

        sub_figure.set_ylim(0,100)
        sub_figure.set_xlim(0,10)
        sub_figure.set_title(title)

        sub_figure.set_xlabel("Nº grupo")
        sub_figure.set_ylabel("Deflexiones")

        sub_figure.bar([], [], width = 0.3, linewidth=0.1)
        sub_figure.grid(axis='both',linestyle='dotted')

        bar = FigureCanvasTkAgg(figure,self.frame)
        

        bar_widget = bar.get_tk_widget()
        bar_widget.grid(row = row, column = column, columnspan = columnspan)
        

        return figure, bar, bar_widget
        
    def update_bar(self, defl_r,defl_l):

        self.defl_r_data.extend(defl_r)
        self.defl_l_data.extend(defl_l)
        self.indexes = list(range(1,len(self.defl_r_data)+1))

        if(len(self.defl_r_data)==len(self.indexes)):
            print("Realizando calculos de deflexiones..")
        else:
            print("Indices NO iguales")

        self.figure_bar_r.clear()
        self.figure_bar_l.clear()

        subfigure_der = self.figure_bar_r.add_subplot(211)
        subfigure_izq = self.figure_bar_l.add_subplot(211)

        subfigure_der.set_ylim(0, (max(self.defl_r_data)+100))
        subfigure_izq.set_ylim(0, (max(self.defl_l_data)+100))
        
        subfigure_der.set_xlim(1, len(self.defl_r_data)+1)
        subfigure_izq.set_xlim(1, len(self.defl_l_data)+1)

        # Grafica todos los datos almacenados
        subfigure_der.bar(self.indexes, self.defl_r_data, width=0.8)
        subfigure_izq.bar(self.indexes, self.defl_l_data, width=0.8)

        subfigure_der.set_title("Deflexion Derecha")
        subfigure_izq.set_title("Deflexion Izquierda")

        subfigure_der.set_xlabel("Progresivas [metros]")
        subfigure_izq.set_xlabel("Progresivas [metros]")

        subfigure_der.set_ylabel("Deflexiones")
        subfigure_izq.set_ylabel("Deflexiones")
       
        subfigure_der.grid(axis='both',linestyle='dotted')
        subfigure_izq.grid(axis='both',linestyle='dotted')

         # Llama al método draw_idle() para actualizar la interfaz gráfica
        self.figure_bar_r.canvas.draw_idle()
        self.figure_bar_l.canvas.draw_idle()

    def show_bar_graph(self):
        
        self.figure_bar_l, self.bar_l, self.bar_widget_l = self.bar_graph(3, 1, 1,"Deflexion Izquierda")
        self.figure_bar_r, self.bar_r, self.bar_widget_r = self.bar_graph(3, 2, 1,"Deflexion Derecha") 

    def show(self):
        self.show_bar_graph()


    def set_flag(self,flag):
        self.flag=flag

    def get_flag(self):
        return self.flag
    
    def get_max(self):
        return max(self.defl_l_data)
    
    def donwload_graphs(self):
        print("Ejecuto PDF")

    # Generar PDF para self.figure_bar_r
        buffer_r = io.BytesIO()
        figure_canvas_pdf_r = FigureCanvasPdf(self.figure_bar_r.figure)
        figure_canvas_pdf_r.print_pdf(buffer_r)
        buffer_r.seek(0)

        # Generar PDF para self.figure_bar_l
        buffer_l = io.BytesIO()
        figure_canvas_pdf_l = FigureCanvasPdf(self.figure_bar_l.figure)
        figure_canvas_pdf_l.print_pdf(buffer_l)
        buffer_l.seek(0)

        # Combinar los PDFs en un solo documento
        pdf_writer = PyPDF2.PdfWriter()
        
        # Agregar el PDF de self.figure_bar_r al escritor
        pdf_writer.append(fileobj=buffer_r)

        # Agregar el PDF de self.figure_bar_l al escritor
        pdf_writer.append(fileobj=buffer_l)

        # Guardar el PDF combinado en un archivo
        with open('pdf2.pdf', 'wb') as f:
            pdf_writer.write(f)

        # Cerrar los buffers
        buffer_r.close()
        buffer_l.close()

