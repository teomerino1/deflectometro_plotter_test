from tkinter import *
import tkinter as tk
from tkinter.ttk import Label, Frame, Button, Scrollbar, Treeview
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_pdf import FigureCanvasPdf
import io
import PyPDF2


# Clase donde se inicializan y actualizan los graficos

class Graphs4():
    def __init__(self, frame):
        self.frame = frame
        self.figure_defl_mean_r = None
        self.defl_mean_r = None
        self.defl_mean_widget_l = None
        self.figure_defl_mean_l = None 
        self.defl_mean_l = None 
        self.defl_mean_widget_l = None
        self.rad_mean_l_data=[]
        self.rad_mean_r_data=[]
        self.indexes=[] 

        self.show()

    def show(self):

        self.show_defl_radios_graph()

    
    def deflexiones_radios_graph(self,row, column, columnspan,title):
        
        figure = Figure(figsize=(7, 7), dpi=100)
        sub_figure=figure.add_subplot(211)
        sub_figure.set_title(title)
        sub_figure.set_xlim(0,20)
        sub_figure.set_ylim(0,100)
        sub_figure.set_xlabel("Radio")
        sub_figure.set_ylabel("Defl.")
        sub_figure.bar([], [], width = 3, linewidth=0)
        sub_figure.grid(axis='both',linestyle='dotted')

        bar = FigureCanvasTkAgg(figure,self.frame)
        bar_widget = bar.get_tk_widget()
        bar_widget.grid(row = row, column = column, columnspan = columnspan)
        return figure, bar, bar_widget
    
    def update_deflexiones_radios_graph(self, dict_r, dict_l,grupos):

        self.rad_mean_r_data.extend(dict_r['Radio'][-1:])
        self.rad_mean_l_data.extend(dict_l['Radio'][-1:])
        # self.indexes=list(range(1,len(self.rad_mean_l_data)+1))
        self.indexes = [x * grupos for x in range(1, len(self.rad_mean_l_data)+1)]

        self.figure_defl_mean_l.clear()
        self.figure_defl_mean_r.clear()
        
        subfigure_izq=self.figure_defl_mean_l.add_subplot(211)
        subfigure_der=self.figure_defl_mean_r.add_subplot(211)

        subfigure_der.set_xlim(min(self.indexes)-50, max(self.indexes)+50)
        subfigure_izq.set_xlim(min(self.indexes)-50, max(self.indexes)+50)
        subfigure_der.set_ylim(0,400)
        subfigure_izq.set_ylim(0,400)

        subfigure_izq.scatter(self.indexes,self.rad_mean_l_data, color = 'r')
        subfigure_der.scatter(self.indexes, self.rad_mean_r_data, color = 'r')
        
        subfigure_izq.grid(axis='both',linestyle='dotted')
        subfigure_der.grid(axis='both',linestyle='dotted')

        subfigure_izq.set_xlabel("Radio")
        subfigure_izq.set_ylabel("Defl")
        subfigure_der.set_xlabel("Radio")
        subfigure_der.set_ylabel("Defl")

        subfigure_izq.set_title("Informe estadistico: Lado Izquierdo")
        subfigure_der.set_title("Informe estadistico: Lado Derecho")

        self.figure_defl_mean_l.canvas.draw_idle()
        self.figure_defl_mean_r.canvas.draw_idle()
    

    def show_defl_radios_graph(self):

        self.figure_defl_mean_r, self.defl_mean_r, self.defl_mean_widget_r = self.deflexiones_radios_graph(3,0,1,"Informe estadistico: Lado Izquierdo")
        self.figure_defl_mean_l, self.defl_mean_l, self.defl_mean_widget_l = self.deflexiones_radios_graph(3,1,1,"Informe estadístico: Lado Derecho")

    def download_graphs4(self):

        buffer_r = io.BytesIO()
        figure_canvas_pdf_r = FigureCanvasPdf(self.figure_defl_mean_r.figure)
        figure_canvas_pdf_r.print_pdf(buffer_r)
        buffer_r.seek(0)

        # Generar PDF para self.figure_bar_l
        buffer_l = io.BytesIO()
        figure_canvas_pdf_l = FigureCanvasPdf(self.figure_defl_mean_l.figure)
        figure_canvas_pdf_l.print_pdf(buffer_l)
        buffer_l.seek(0)

        # Combinar los PDFs en un solo documento
        pdf_writer = PyPDF2.PdfWriter()
        
        # Agregar el PDF de self.figure_bar_r al escritor
        pdf_writer.append(fileobj=buffer_r)

        # Agregar el PDF de self.figure_bar_l al escritor
        pdf_writer.append(fileobj=buffer_l)

        # Guardar el PDF combinado en un archivo
        with open('Informe_estadistico.pdf', 'wb') as f:
            pdf_writer.write(f)

        # Cerrar los buffers
        buffer_r.close()
        buffer_l.close()
