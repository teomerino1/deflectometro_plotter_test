from tkinter import *
import tkinter as tk
from tkinter.ttk import Label, Frame, Button, Scrollbar, Treeview
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Clase donde se inicializan y actualizan los graficos

class Graphs3():
    def __init__(self, frame,lado):

        self.frame = frame

        self.figure_defl_mean_r = None

        self.defl_mean_r = None

        self.defl_mean_widget_l = None

        self.figure_defl_mean_l = None 

        self.defl_mean_l = None 

        self.defl_mean_widget_l = None 

        self.show(lado)


    def show(self,lado):

        self.show_deflexiones_gmean_graph(lado)

    
    def deflexiones_gmean_graph(self,row, column, columnspan,title):
        
        figure = Figure(figsize=(7, 7), dpi=100)

        sub_figure=figure.add_subplot(211)
        sub_figure.set_title(title)

        # sub_figure.set_xlim(0,20)

        sub_figure.set_ylim(0,100)
        sub_figure.set_xlabel("Progresivas")
        sub_figure.set_ylabel("Deflexiones")

        sub_figure.bar([], [], width = 3, linewidth=0)
        sub_figure.grid(axis='both',linestyle='dotted')

        bar = FigureCanvasTkAgg(figure,self.frame)

        bar_widget = bar.get_tk_widget()

        bar_widget.grid(row = row, column = column, columnspan = columnspan)

        return figure, bar, bar_widget
    
    def update_deflexiones_gmean(self, dict_r, dict_l, defl_r_max, defl_l_max, defl_r_car, defl_l_car, lado):

        if(lado == "Izquierdo"):

            self.figure_rad_mean_l, self.rad_mean_l, self.rad_mean_widget_l = self.deflexiones_gmean_graph(3,1,1,"Deflexiones Izquierda")
            self.figure_rad_mean_l.clear()

            subfigure_izq = self.figure_rad_mean_l.add_subplot(211)
            subfigure_izq.set_title("Deflexiones Izquierda")
            # subfigure_izq.set_xlim(0,80)
            subfigure_izq.set_ylim(0,100)  
            subfigure_izq.set_xlabel("Progresivas")
            subfigure_izq.set_ylabel("Deflexiones")

            subfigure_izq.bar(dict_l['Grupo'], dict_l['Defl.'], color='red',width = 0.5, edgecolor='black')
            subfigure_izq.scatter(dict_l['Grupo'], defl_l_max)
            subfigure_izq.plot(dict_l['Grupo'], defl_l_car)
            subfigure_izq.grid(axis='both',linestyle='dotted')
        
            self.rad_mean_l.draw()

        if(lado == "Derecho"):

            self.figure_rad_mean_r, self.rad_mean_r, self.rad_mean_widget_r = self.deflexiones_gmean_graph(3,1,1,"Deflexiones Derecha")
            self.figure_rad_mean_r.clear()

            subfigure_der=self.figure_rad_mean_r.add_subplot(211)

            subfigure_der.set_title("Deflexiones Derecha")
            # subfigure_der.set_xlim(0,80)
            subfigure_der.set_ylim(0,100)
            subfigure_der.set_xlabel("Progresivas")
            subfigure_der.set_ylabel("Deflexiones")

            subfigure_der.bar(dict_r['Grupo'], dict_r['Defl.'], color='red',width = 0.5, edgecolor='black')
            subfigure_der.scatter(dict_r['Grupo'], defl_r_max)
            subfigure_der.plot(dict_r['Grupo'],defl_r_car)
            subfigure_der.grid(axis='both',linestyle='dotted')
            
            self.rad_mean_r.draw()
        
            # self.rad_mean_widget_r.draw()

    def show_deflexiones_gmean_graph(self,lado):

        if(lado == "Izquierdo"):

            self.figure_defl_mean_r, self.defl_mean_r, self.defl_mean_widget_l = self.deflexiones_gmean_graph(3,1,1,"Deflexiones Izquierda")

        if(lado == "Derecho"):

            self.figure_defl_mean_l, self.defl_mean_l, self.defl_mean_widget_l = self.deflexiones_gmean_graph(3,1,1,"Deflexiones Derecha")