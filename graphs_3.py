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

        sub_figure.bar([], [], width = 0.1, linewidth=0)

        sub_figure.grid(axis='both',linestyle='dotted')

        bar = FigureCanvasTkAgg(figure,self.frame)

        bar_widget = bar.get_tk_widget()

        bar_widget.grid(row = row, column = column, columnspan = columnspan)

        return figure, bar, bar_widget
    
        # figure = Figure(figsize=(6, 7), dpi=100)

        # sub_figure = figure.add_subplot(211)
        
        # sub_figure.set_title(title)

        # sub_figure.bar([], [])

        # sub_figure.grid(axis='both',linestyle='dotted')

        # # figure.add_subplot(121).scatter([], [])

        # graph = FigureCanvasTkAgg(figure, self.frame)

        # graph_widget = graph.get_tk_widget()

        # graph_widget.grid(row = row, column = column, columnspan = columnspan)

        # return figure, graph, graph_widget
    
    
  

    def update_deflexiones_gmean(self, dict_r, dict_l,lado):

        if(lado == "Izquierdo"):

            self.figure_rad_mean_l, self.rad_mean_l, self.rad_mean_widget_l = self.deflexiones_gmean_graph(3,1,1,"Deflexiones Izquierda")
           
            self.figure_rad_mean_l.clear()

            subfigure2=self.figure_rad_mean_l.add_subplot(211)

            subfigure2.set_title("Deflexiones Izquierda")

            # subfigure2.scatter(dict_l['Grupo'], dict_l['Defl.'], color = 'r')

            # subfigure2.plot(dict_l['Grupo'], dict_l['Defl.'],'o-')

            subfigure2.bar(dict_l['Grupo'], dict_l['Defl.'], color='black')

            subfigure2.grid(axis='both',linestyle='dotted')
        
            self.rad_mean_l.draw()

        if(lado == "Derecho"):

            self.figure_rad_mean_r, self.rad_mean_r, self.rad_mean_widget_r = self.deflexiones_gmean_graph(3,1,1,"Deflexiones Derecha")

            self.figure_rad_mean_r.clear()

            subfigure=self.figure_rad_mean_r.add_subplot(211)

            subfigure.set_title("Deflexiones Derecha")

            # subfigure.scatter(dict_r['Grupo'], dict_r['Defl.'], color = 'r')

            # subfigure.plot(dict_r['Grupo'], dict_r['Defl.'],'o-')

            subfigure.bar(dict_l['Grupo'], dict_l['Defl.'], color='black')

            subfigure.grid(axis='both',linestyle='dotted')
            
            self.rad_mean_r.draw()
        
            # self.rad_mean_widget_r.draw()

    def show_deflexiones_gmean_graph(self,lado):

        if(lado == "Izquierdo"):

            self.figure_defl_mean_r, self.defl_mean_r, self.defl_mean_widget_l = self.deflexiones_gmean_graph(3,1,1,"Deflexiones Izquierda")

        if(lado == "Derecho"):

            self.figure_defl_mean_l, self.defl_mean_l, self.defl_mean_widget_l = self.deflexiones_gmean_graph(3,1,1,"Deflexiones Derecha")