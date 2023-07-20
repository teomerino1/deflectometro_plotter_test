from tkinter import *
import tkinter as tk
from tkinter.ttk import Label, Frame, Button, Scrollbar, Treeview
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Clase donde se inicializan y actualizan los graficos

class Graphs():
    def __init__(self, frame):
        self.a=None
        self.frame = frame
        # self.plot_number=plot_number
        self.show()
        self.figure_rad_mean_r=None
        self.rad_mean_r=None
        
    # Grafico que corresponde a las deflexiones individuales
    def bar_graph(self, row, column, columnspan,title):
        
        figure = Figure(figsize=(7, 7), dpi=100)
        sub_figure=figure.add_subplot(211)

        sub_figure.set_xlim(0,1000)
        sub_figure.set_ylim(0,100)
        sub_figure.set_title(title)

        sub_figure.set_xlabel("Nº grupo")
        sub_figure.set_ylabel("Deflexiones")

        sub_figure.bar([], [], width = 0.3, linewidth=0.1)
        sub_figure.grid(axis='both',linestyle='dotted')

        bar = FigureCanvasTkAgg(figure,self.frame)

        bar_widget = bar.get_tk_widget()
        bar_widget.grid(row = row, column = column, columnspan = columnspan)

        return figure, bar, bar_widget
    
    
    
    def update_bar(self, defl_left_right_dict,indexes):

        self.figure_bar_r.clear()
        self.figure_bar_l.clear()

        subfigure_der = self.figure_bar_r.add_subplot(211)
        subfigure_izq = self.figure_bar_l.add_subplot(211)

        index_der = list(range(1,len(defl_left_right_dict['right'])+1))
        index_izq = list(range(1,len(defl_left_right_dict['left'])+1))

        if(len(indexes) != (len(defl_left_right_dict['right']))):
            print("Corrijo indices:",len(indexes))
            indexes.append(len(indexes)+1)
            print("Indexes corrijed:",len(indexes))
        elif(len(indexes)==len(defl_left_right_dict['right'])):
            print("Indices iguales!")

        subfigure_der.bar(indexes, defl_left_right_dict['right'],width = 1)
        subfigure_izq.bar(indexes, defl_left_right_dict['left'],width = 1)

        print("Arg 0 derecha (index der):",len(index_der))
        print("Arg 1 derecha len:",len(defl_left_right_dict['right']))
        # print("Arg 0 derecha (index izq):",len(index_der))
        print("Arg 1 derecha izq:",len(defl_left_right_dict['left']))
        # print("REAL index IZQ:",len(index_izq))
        # print("Indexes:",len(indexes))

        subfigure_der.set_title("Deflexion Derecha")
        subfigure_izq.set_title("Deflexion Izquierda")

        subfigure_der.set_xlim(0,1000)
        subfigure_izq.set_xlim(0,1000)

        # subfigure_der.set_ylim(0,100)
        # # # subfigure_izq.set_ylim(0,100)

        subfigure_der.set_xlabel("Nº grupo")
        subfigure_izq.set_xlabel("Nº grupo")

        subfigure_der.set_ylabel("Deflexiones")
        subfigure_izq.set_ylabel("Deflexiones")
       
        subfigure_der.grid(axis='both',linestyle='dotted')
        subfigure_izq.grid(axis='both',linestyle='dotted')

        self.bar_r.draw()
        self.bar_l.draw()
        

    def show_bar_graph(self):

        self.figure_bar_l, self.bar_l, self.bar_widget_l = self.bar_graph(10, 0, 1,"Deflexion Izquierda")
        
        self.figure_bar_r, self.bar_r, self.bar_widget_r = self.bar_graph(10, 1, 1,"Deflexion Derecha")  # Ajusta las coordenadas para la posición deseada
        

    def show(self):

        self.show_bar_graph()

        



    





























   

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


