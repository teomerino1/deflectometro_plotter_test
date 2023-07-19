from tkinter import *
import tkinter as tk
from tkinter.ttk import Label, Frame, Button, Scrollbar, Treeview
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
    
    def update_deflexiones_radios_graph(self, dict_r, dict_l):

        self.figure_rad_mean_l, self.rad_mean_l, self.rad_mean_widget_l = self.deflexiones_radios_graph(3,0,1,"Informe estadistico: Lado Izquierdo")
        
        self.figure_rad_mean_l.clear()

        subfigure_izq=self.figure_rad_mean_l.add_subplot(211)

        subfigure_izq.set_xlabel("Radio")

        subfigure_izq.set_ylabel("Defl")

        subfigure_izq.set_xlim(0,20)

        # subfigure2.set_ylim(0,100)

        subfigure_izq.set_title("Informe estadistico: Lado Izquierdo")

        subfigure_izq.scatter(dict_l['Grupo'], dict_l['Radio'], color = 'r')

        subfigure_izq.grid(axis='both',linestyle='dotted')
    
        self.rad_mean_l.draw()


        self.figure_rad_mean_r, self.rad_mean_r, self.rad_mean_widget_r = self.deflexiones_radios_graph(3,1,1,"Informe estadistico: Lado Derecho")

        self.figure_rad_mean_r.clear()

        subfigure_der=self.figure_rad_mean_r.add_subplot(211)

        subfigure_der.set_xlabel("Radio")

        subfigure_der.set_ylabel("Defl")

        subfigure_der.set_xlim(0,20)

        # subfigure.set_ylim(0,100)

        subfigure_der.set_title("Informe estadistico: Lado Derecho")

        subfigure_der.scatter(dict_r['Grupo'], dict_r['Radio'], color = 'r')

        subfigure_der.grid(axis='both',linestyle='dotted')
        
        self.rad_mean_r.draw()


    def show_defl_radios_graph(self):

        self.figure_defl_mean_r, self.defl_mean_r, self.defl_mean_widget_l = self.deflexiones_radios_graph(3,0,1,"Informe estadistico: Lado Izquierdo")
        self.figure_defl_mean_l, self.defl_mean_l, self.defl_mean_widget_l = self.deflexiones_radios_graph(3,1,1,"Informe estadístico: Lado Derecho")