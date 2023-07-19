from tkinter import *
import tkinter as tk
from tkinter.ttk import Label, Frame, Button, Scrollbar, Treeview
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Clase donde se inicializan y actualizan los graficos

class Graphs2():
    def __init__(self, frame,lado):
        self.frame = frame
        self.figure_rad_mean_r = None
        self.rad_mean_r = None
        self.rad_mean_widget_l = None
        self.figure_rad_mean_l = None 
        self.rad_mean_l = None 
        self.rad_mean_widget_l = None 
        self.show(lado)



    def show(self,lado):

        self.show_radio_gmean_graph(lado)

    
    def radio_gmean_graph(self,row, column, columnspan,title):
        
        figure = Figure(figsize=(6, 7), dpi=100)

        # figure = Figure(figsize=(4, 5), dpi=90)

        sub_figure = figure.add_subplot(211)
        sub_figure.set_xlim(0,100)
        sub_figure.set_ylim(0,100)
        sub_figure.set_title(title)
        sub_figure.set_xlabel("Nº Grupo")
        sub_figure.set_ylabel("Radio de Curvatura")
        sub_figure.scatter([], [])
        sub_figure.grid(axis='both',linestyle='dotted')

        graph = FigureCanvasTkAgg(figure, self.frame)

        graph_widget = graph.get_tk_widget()
        graph_widget.grid(row = row, column = column, columnspan = columnspan)
        return figure, graph, graph_widget
    

    def update_gmean(self, dict_r, dict_l,lado):

        if(lado == "Izquierdo"):

            self.figure_rad_mean_l, self.rad_mean_l, self.rad_mean_widget_l = self.radio_gmean_graph(3,0,1,"Radio Izquierda")
            self.figure_rad_mean_l.clear()

            subfigure_izq=self.figure_rad_mean_l.add_subplot(211)

            # subfigure2.set_xlim(0,100)
            subfigure_izq.set_ylim(0,100)

            subfigure_izq.set_title("Radio Izquierda")
            subfigure_izq.set_xlabel("Nº Grupo")
            subfigure_izq.set_ylabel("Radio de curvatura")

            subfigure_izq.plot(dict_l['Grupo'], dict_l['Radio'],'o-')

            subfigure_izq.grid(axis='both',linestyle='dotted')
        
            self.rad_mean_l.draw()

        if(lado == "Derecho"):

            self.figure_rad_mean_r, self.rad_mean_r, self.rad_mean_widget_r = self.radio_gmean_graph(3,0,1,"Radio Derecha")

            self.figure_rad_mean_r.clear()

            subfigure_der=self.figure_rad_mean_r.add_subplot(211)

            # subfigure.set_xlim(0,100)

            subfigure_der.set_ylim(0,100)
            subfigure_der.set_title("Radio Derecha")
            subfigure_der.set_xlabel("Nº Grupo")
            subfigure_der.set_ylabel("Radio de curvatura")

            subfigure_der.plot(dict_r['Grupo'], dict_r['Radio'],'o-')
            subfigure_der.grid(axis='both',linestyle='dotted')
            
            self.rad_mean_r.draw()
        
            # self.rad_mean_widget_r.draw()

    def show_radio_gmean_graph(self,lado):

        if(lado == "Izquierdo"):

            self.figure_rad_mean_l, self.rad_mean_l, self.rad_mean_widget_l = self.radio_gmean_graph(3,0,1,"Radio Izquierda")
            

        if(lado == "Derecho"):

            self.figure_rad_mean_r, self.rad_mean_r, self.rad_mean_widget_r = self.radio_gmean_graph(3,0,1,"Radio Derecha")
           
       


   



    





























   

    # # Metodo donde se inicializan los graficos
    

    

   
       

    # Actualiza el grafico de bars de mediciones individuales
    # se pasa como parametro un dict con los datos de los dos lados
    
        # self.figure_bar_l.add_subplot(211).bar(index, defl_left_right_dict['left'])
        

    # Toma los nuevos valores y hace el update de los graficos
    # el update se hace limpiando y volviendo a graficar. (quizas hay otra solucion, la que probe no funcionaba)
    # def update_gmean(self, dict_r, dict_l):

    #     self.figure_rad_mean_r.clear()

    #     subfigure = self.figure_rad_mean_r.add_subplot(211)

    #     subfigure.set_title("Radio Derecha")

    #     subfigure.scatter(dict_r['Grupo'], dict_r['Defl.'], color = 'r')

    #     subfigure.draw()

        # self.figure_rad_mean_r.add_subplot(211).scatter(dict_r['Grupo'], dict_r['Defl.'], color = 'r')

        # self.rad_mean_r.draw()

        # self.figure_rad_mean_l.clear()
        # self.figure_rad_mean_l.add_subplot(211).scatter(dict_l['Grupo'], dict_l['Defl.'], color = 'r')
        # self.rad_mean_l.draw()


