from tkinter import *
from tkinter.ttk import Label, Frame, Button, Scrollbar, Treeview
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Clase donde se inicializan y actualizan los graficos

class Graphs():
    def __init__(self, frame):
        self.frame = frame

        self.show()

    # Grafico que corresponde a las deflexiones individuales
    def bar_graph(self, row, column, columnspan = 3):
        
        figure = Figure(figsize=(8,5), dpi = 100)

        figure.add_subplot(111).bar([], [], width = 0.5, linewidth=0)
        bar = FigureCanvasTkAgg(figure,self.frame)
        bar_widget = bar.get_tk_widget()
        bar_widget.grid(row = row, column = column, columnspan = columnspan)

        return figure, bar, bar_widget

    # Grafico que corresponde a las medias del radio
    def radio_gmean_graph(self,row, column, columnspan = 3):
        figure = Figure(figsize=(8,5), dpi = 100)

        figure.add_subplot(211).scatter([], [])
        graph = FigureCanvasTkAgg(figure, self.frame)
        graph_widget = graph.get_tk_widget()
        graph_widget.grid(row = row, column = column, columnspan = columnspan)

        return figure, graph, graph_widget

    # Metodo donde se inicializan los graficos
    def show(self):

        # definicion de graficos de barra
        self.figure_bar_r, self.bar_r, self.bar_widget_r = self.bar_graph(4,0,3)
        # self.figure_bar_l, self.bar_l, self.bar_widget_l = self.bar_graph(5,0,3)


        # definicion de los graficos de medias de radio
        self.figure_rad_mean_r, self.rad_mean_r, self.rad_mean_widget_r = self.radio_gmean_graph(5,0,3)
        # self.figure_rad_mean_l, self.rad_mean_l, self.rad_mean_widget_l = self.radio_gmean_graph(6,0,3)
        
        # self.bar_r.draw()
        # self.bar_l.draw()
        self.rad_mean_r.draw()
        # self.rad_mean_l.draw()

    # Actualiza el grafico de bars de mediciones individuales
    # se pasa como parametro un dict con los datos de los dos lados
    def update_bar(self, bar_dict):

        index = list(range(1,len(bar_dict['right'])+1))
        self.figure_bar_r.clear()
        self.figure_bar_r.add_subplot(211).bar(index, bar_dict['right'])
        self.bar_r.draw()

        # self.figure_bar_l.clear()
        # self.figure_bar_l.add_subplot(111).bar(index, bar_dict['left'])
        # self.bar_l.draw()

    # Toma los nuevos valores y hace el update de los graficos
    # el update se hace limpiando y volviendo a graficar. (quizas hay otra solucion, la que probe no funcionaba)
    def update_gmean(self, dict_r, dict_l):
        self.figure_rad_mean_r.clear()
        self.figure_rad_mean_r.add_subplot(211).scatter(dict_r['Grupo'], dict_r['Defl.'], color = 'r')
        self.rad_mean_r.draw()

        # self.figure_rad_mean_l.clear()
        # self.figure_rad_mean_l.add_subplot(211).scatter(dict_l['Grupo'], dict_l['Defl.'], color = 'r')
        # self.rad_mean_l.draw()