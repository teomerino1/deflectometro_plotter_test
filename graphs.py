from tkinter import *
import tkinter as tk
from tkinter.ttk import Label, Frame, Button, Scrollbar, Treeview
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Clase donde se inicializan y actualizan los graficos

class Graphs():
    def __init__(self, frame,plot_number):
        self.frame = frame
        self.plot_number=plot_number
        self.show(plot_number)
        self.figure_rad_mean_r=None
        self.rad_mean_r=None
    # Grafico que corresponde a las deflexiones individuales
    def bar_graph(self, row, column, columnspan,title):
        
        figure = Figure(figsize=(7, 7), dpi=100)

        sub_figure=figure.add_subplot(211)

        sub_figure.set_title(title)

        sub_figure.bar([], [], width = 0.1, linewidth=0)

        bar = FigureCanvasTkAgg(figure,self.frame)

        bar_widget = bar.get_tk_widget()

        bar_widget.grid(row = row, column = column, columnspan = columnspan)

        return figure, bar, bar_widget
    
     # # Grafico que corresponde a las medias del radio
    def radio_gmean_graph(self,row, column, columnspan,title):
        
        figure = Figure(figsize=(6, 7), dpi=100)

        sub_figure = figure.add_subplot(211)
        
        sub_figure.set_title(title)

        sub_figure.scatter([], [])

        # figure.add_subplot(121).scatter([], [])

        graph = FigureCanvasTkAgg(figure, self.frame)

        graph_widget = graph.get_tk_widget()

        graph_widget.grid(row = row, column = column, columnspan = columnspan)

        return figure, graph, graph_widget
    
    
    def update_bar(self, defl_left_right_dict):

        index = list(range(1,len(defl_left_right_dict['right'])+1))
        self.figure_bar_r.clear()

        subfigure=self.figure_bar_r.add_subplot(211)

        subfigure.set_title("Deflexion Derecha")

        subfigure.bar(index, defl_left_right_dict['right'])

        self.bar_r.draw()

        self.figure_bar_l.clear()

        subfigure=self.figure_bar_l.add_subplot(211)

        subfigure.set_title("Deflexion Izquierda")

        subfigure.bar(index, defl_left_right_dict['left'])

        self.bar_l.draw()

    # def update_gmean(self, dict_r, dict_l):

    #     self.figure_rad_mean_l, self.rad_mean_l, self.rad_mean_widget_l = self.radio_gmean_graph(3,0,1,"Radio Izquierda")
    #     self.figure_rad_mean_r, self.rad_mean_r, self.rad_mean_widget_r = self.radio_gmean_graph(3,2,1,"Radio Derecha")
    #     self.figure_rad_mean_r.clear()
    #     subfigure=self.figure_rad_mean_r.add_subplot(211)
    #     subfigure.set_title("Differentei")
    #     subfigure.scatter(dict_r['Grupo'], dict_r['Defl.'], color = 'r')
    #     self.rad_mean_r.draw()
    #     # self.figure_rad_mean_r.add_subplot(211).scatter(dict_r['Grupo'], dict_r['Defl.'], color = 'r')
    #     # self.rad_mean_r.draw()
    #     # self.rad_mean_widget_r.draw()

    #     # self.figure_rad_mean_l.clear()
    #     # self.figure_rad_mean_l.add_subplot(211).scatter(dict_l['Grupo'], dict_l['Defl.'], color = 'r')
    #     # self.rad_mean_l.draw()

    def show_bar_graph(self):

        self.figure_bar_l, self.bar_l, self.bar_widget_l = self.bar_graph(10, 0, 1,"Deflexion Izquierda")
        self.figure_bar_r, self.bar_r, self.bar_widget_r = self.bar_graph(10, 1, 1,"Deflexion Derecha")  # Ajusta las coordenadas para la posición deseada

        # definicion de los graficos de medias de radio
        
        # self.bar_r.draw()
        # self.bar_l.draw()
        # self.rad_mean_r.draw()
        # self.rad_mean_l.draw()

    def show_radio_gmean_graph(self):

        self.figure_rad_mean_l, self.rad_mean_l, self.rad_mean_widget_l = self.radio_gmean_graph(3,0,1,"Radio Izquierda")
        self.figure_rad_mean_r, self.rad_mean_r, self.rad_mean_widget_r = self.radio_gmean_graph(3,2,1,"Radio Derecha")


    def show(self,plot_number):

        if(plot_number==1):
            self.show_bar_graph()

        if(plot_number==2):
            self.show_radio_gmean_graph()



    





























   

    # # Metodo donde se inicializan los graficos
    

    

   
       

    # Actualiza el grafico de bars de mediciones individuales
    # se pasa como parametro un dict con los datos de los dos lados
    
        # self.figure_bar_l.add_subplot(211).bar(index, defl_left_right_dict['left'])
        

    # Toma los nuevos valores y hace el update de los graficos
    # el update se hace limpiando y volviendo a graficar. (quizas hay otra solucion, la que probe no funcionaba)
    def update_gmean(self, dict_r, dict_l):

        self.figure_rad_mean_r.clear()

        subfigure = self.figure_rad_mean_r.add_subplot(211)

        subfigure.set_title("Radio Derecha")

        subfigure.scatter(dict_r['Grupo'], dict_r['Defl.'], color = 'r')

        subfigure.draw()

        self.figure_rad_mean_r.add_subplot(211).scatter(dict_r['Grupo'], dict_r['Defl.'], color = 'r')

        self.rad_mean_r.draw()

        self.figure_rad_mean_l.clear()
        self.figure_rad_mean_l.add_subplot(211).scatter(dict_l['Grupo'], dict_l['Defl.'], color = 'r')
        self.rad_mean_l.draw()


