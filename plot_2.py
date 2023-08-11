from tkinter import *
from tkinter.ttk import Label, Frame, Button, Scrollbar
import view
import table
import graphs
from tkinter.ttk import Treeview
import tkinter as tk
from tkinter import ttk
import graphs_2
import graphs_3
from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk


# Clase correspondiente a la vista encargada de mostrar los datos y graficos

class Plot2():
    def __init__(self,root,view_instance):
        self.root = root
        self.third_plot_frame = None
        self.title = None
        self.next = None
        self.back = None
        self.view_instance = view_instance  
        self.Graphs2 = None
        self.Graphs3 = None

    # Metodo que elimina todo lo que muestra la pagina
    def close(self):
        self.third_plot_frame.grid_forget()

    def reset(self):
        self.third_plot_frame.destroy()
        self.show(0)

    def show(self,a):
       
        if(a == 0):

            width = self.root.winfo_screenwidth()
            height = self.root.winfo_screenheight()

            third_plot_frame = Frame(self.root, width=width, height=height)
            self.third_plot_frame = third_plot_frame

            title = Label(third_plot_frame, text="Deflexiones y Radios: Lado Izquierdo",font=(None, 20)) 
            self.title=title

            back = Button(third_plot_frame, text="Atrás", command=self.go_to_plot_1_from_plot_2)
            # style = ttk.Style()
            # style.configure("Custom.TButton", background="blue", foreground="white")
            # back = ttk.Button(third_plot_frame, text="Atras", command=self.go_to_plot_1_from_plot_2, style="Custom.TButton")
            self.back = back

            next = Button(third_plot_frame, text="Next", command=self.go_to_plot_3_from_plot2)
            # style = ttk.Style()
            # style.configure("Custom.TButton", background="blue", foreground="white")
            # next = ttk.Button(third_plot_frame, text="Next", command=self.go_to_plot_3_from_plot2, style="Custom.TButton")
            self.next = next

            self.Graphs2 = graphs_2.Graphs2(self.third_plot_frame,lado="Izquierdo")
            self.Graphs3 = graphs_3.Graphs3(self.third_plot_frame,lado="Izquierdo")
            

        if(a == 1):
            # self.third_plot_frame.grid(rowspan=3,columnspan=3)
            self.third_plot_frame.grid(rowspan=10,columnspan=10)
            self.title.grid(row = 0, column = 0,sticky=NW)
            self.back.grid(row=1, column=0,sticky=NW)
            self.next.grid(row=2,column=0,sticky=NW)


    def download_graphs(self):
        self.Graphs2.download_graphs2(lado="Izquierdo")
        self.Graphs3.download_graphs3(lado="Izquierdo")

    def new_group_data_plot2(self,dict_r, dict_l, defl_r_car, defl_l_car, defl_r_max, defl_l_max,grupos):
        self.Graphs2.update_gmean(dict_r, dict_l,grupos,lado = "Izquierdo")
        self.Graphs3.update_deflexiones_gmean(dict_r, dict_l, defl_r_car, defl_l_car, defl_r_max, defl_l_max,grupos, lado="Izquierdo")

    def go_to_plot_1_from_plot_2(self):
        # Encolar la función en la cola del hilo de la clase View
        # print("go to plot 1 from plot 2")
        self.view_instance.enqueue_transition('go_to_plot_1_from_plot_2')
        
    def go_to_plot_3_from_plot2(self):
        # Encolar la función en la cola del hilo de la clase View
        # print("go to plot 3 from plot 2")
        self.view_instance.enqueue_transition('go_to_plot_3_from_plot_2')
        

        

   


