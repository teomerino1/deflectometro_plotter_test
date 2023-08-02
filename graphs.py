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

        ######################
        # Inicializa las listas para almacenar los datos
        self.defl_r_data = []
        self.defl_l_data = []
        self.indexes = []
        ######################

    # Grafico que corresponde a las deflexiones individuales
    def bar_graph(self, row, column, columnspan,title):
        
        figure = Figure(figsize=(7, 7), dpi=100)
        sub_figure=figure.add_subplot(211)

        # sub_figure.set_xlim(0,1000)
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
    
    
    
    def update_bar(self, defl_r,defl_l):

        self.defl_r_data.extend(defl_r)
        self.defl_l_data.extend(defl_l)
        self.indexes = list(range(len(self.defl_r_data)))

        if(len(self.defl_r_data)==len(self.indexes)):
            print("Indices iguales!")
        else:
            print("Indices NO iguales")
        
        self.figure_bar_r.clear()
        self.figure_bar_l.clear()

        subfigure_der = self.figure_bar_r.add_subplot(211)
        subfigure_izq = self.figure_bar_l.add_subplot(211)


        # subfigure_der.set_xlim(0, 1000)
        # subfigure_izq.set_xlim(0, 1000)
        
        subfigure_der.set_xlim(0, len(self.defl_r_data))
        subfigure_izq.set_xlim(0, len(self.defl_l_data))


        # Grafica todos los datos almacenados
        subfigure_der.bar(self.indexes, self.defl_r_data, width=1)
        subfigure_izq.bar(self.indexes, self.defl_l_data, width=1)


        subfigure_der.set_title("Deflexion Derecha")
        subfigure_izq.set_title("Deflexion Izquierda")

        subfigure_der.set_xlabel("Nº grupo")
        subfigure_izq.set_xlabel("Nº grupo")

        subfigure_der.set_ylabel("Deflexiones")
        subfigure_izq.set_ylabel("Deflexiones")
       
        subfigure_der.grid(axis='both',linestyle='dotted')
        subfigure_izq.grid(axis='both',linestyle='dotted')

         # Llama al método draw_idle() para actualizar la interfaz gráfica
        self.figure_bar_r.canvas.draw_idle()
        self.figure_bar_l.canvas.draw_idle()



        # self.figure_bar_r.clear()
        # self.figure_bar_l.clear()

        # subfigure_der = self.figure_bar_r.add_subplot(211)
        # subfigure_izq = self.figure_bar_l.add_subplot(211)

        # # index_der = list(range(1,len(defl_left_right_dict['right'])+1))
        # # index_izq = list(range(1,len(defl_left_right_dict['left'])+1))

        # if(len(indexes) != (len(defl_r))):
        #     print("Corrijo indices:",len(indexes))
        #     indexes.append(len(indexes)+1)
        #     print("Indexes corrijed:",len(indexes))
        # elif(len(indexes)==len(defl_r)):
        #     print("Indices iguales!")

        # subfigure_der.set_xlim(0,1000)
        # subfigure_izq.set_xlim(0,1000)

        # subfigure_der.bar(indexes, defl_r,width = 1)
        # subfigure_izq.bar(indexes, defl_l,width =1)

        # subfigure_der.set_title("Deflexion Derecha")
        # subfigure_izq.set_title("Deflexion Izquierda")

        
        # # subfigure_der.set_ylim(0,100)
        # # # # subfigure_izq.set_ylim(0,100)

        # subfigure_der.set_xlabel("Nº grupo")
        # subfigure_izq.set_xlabel("Nº grupo")

        # subfigure_der.set_ylabel("Deflexiones")
        # subfigure_izq.set_ylabel("Deflexiones")
       
        # subfigure_der.grid(axis='both',linestyle='dotted')
        # subfigure_izq.grid(axis='both',linestyle='dotted')

        # self.bar_r.draw()
        # self.bar_l.draw()
        

    def show_bar_graph(self):

        self.figure_bar_l, self.bar_l, self.bar_widget_l = self.bar_graph(10, 0, 1,"Deflexion Izquierda")
        
        self.figure_bar_r, self.bar_r, self.bar_widget_r = self.bar_graph(10, 1, 1,"Deflexion Derecha")  # Ajusta las coordenadas para la posición deseada
        

    def show(self):

        self.show_bar_graph()