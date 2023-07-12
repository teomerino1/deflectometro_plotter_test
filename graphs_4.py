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

        self.show_deflexiones_gmean_graph()

    
    def deflexiones_gmean_graph(self,row, column, columnspan,title):
        
        figure = Figure(figsize=(7, 7), dpi=100)

        sub_figure=figure.add_subplot(211)

        sub_figure.set_title(title)

        sub_figure.set_xlim(0,20)

        sub_figure.set_ylim(0,100)

        sub_figure.bar([], [], width = 3, linewidth=0)

        sub_figure.grid(axis='both',linestyle='dotted')

        bar = FigureCanvasTkAgg(figure,self.frame)

        bar_widget = bar.get_tk_widget()

        bar_widget.grid(row = row, column = column, columnspan = columnspan)

        return figure, bar, bar_widget
    

    def show_deflexiones_gmean_graph(self):

        self.figure_defl_mean_r, self.defl_mean_r, self.defl_mean_widget_l = self.deflexiones_gmean_graph(3,0,1,"Informe estadistico: Lado Izquierdo")

        self.figure_defl_mean_l, self.defl_mean_l, self.defl_mean_widget_l = self.deflexiones_gmean_graph(3,1,1,"Informe estadístico: Lado Derecho")