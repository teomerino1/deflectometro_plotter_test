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
        self.title_frame=None
        self.graphs_frame=None
        self.title = None
        self.subtitle=None
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

            third_plot_frame = Frame(self.root, width=width, height=height,background='#F6F4F2')
            self.third_plot_frame = third_plot_frame

            title_frame=Frame(self.third_plot_frame,background='#F6F4F2')
            self.title_frame=title_frame

            graphs_frame=Frame(self.third_plot_frame)
            self.graphs_frame=graphs_frame

            title = Label(self.title_frame, text="Deflexiones y Radios",font=("Helvetica", 25),background='#F6F4F2',foreground='#625651') 
            self.title=title
            #azul: #66A7EF
            #letras theme: #625651
            subtitle=Label(self.title_frame, text="Lado Izquierdo",font=("Helvetica", 22),background='#F6F4F2',foreground='#625651')
            self.subtitle=subtitle

            back = ttk.Button(self.third_plot_frame, text="Atrás", command=self.go_to_plot_1_from_plot_2,style="TButton")
            self.back = back

            next = ttk.Button(self.third_plot_frame, text="Next", command=self.go_to_plot_3_from_plot2,style="TButton")
            self.next = next

            self.Graphs2 = graphs_2.Graphs2(self.graphs_frame,lado="Izquierdo")
            self.Graphs3 = graphs_3.Graphs3(self.graphs_frame,lado="Izquierdo")
            

        if(a == 1):
            # self.third_plot_frame.grid(rowspan=3,columnspan=3)
            self.third_plot_frame.grid(columnspan=2)
            self.back.grid(row=0, column=0,sticky=NW)
            self.next.grid(row=0,column=1,padx=(1000,40),sticky=NE)
            self.title_frame.grid(row=1,columnspan=2,pady=(50,0))
            self.title.grid()
            self.subtitle.grid()
            # self.title.grid(row = 0, column = 0,sticky=NW)
            self.graphs_frame.grid(row=2,columnspan=2,pady=(50,0))
            
            

##F6F4F2
    def download_graphs(self):
        self.Graphs2.download_graphs2(lado="Izquierdo")
        self.Graphs3.download_graphs3(lado="Izquierdo")

    def new_group_data_plot2(self,dict_r, dict_l, defl_r_car, defl_l_car, defl_r_max, defl_l_max,grupos):
        self.Graphs2.update_gmean(dict_r, dict_l,grupos,lado = "Izquierdo")
        self.Graphs3.update_deflexiones_gmean(dict_r, dict_l, defl_r_car, defl_l_car, defl_r_max, defl_l_max,grupos, lado="Izquierdo")

    def go_to_plot_1_from_plot_2(self):
        self.view_instance.enqueue_transition('go_to_plot_1_from_plot_2')
        
    def go_to_plot_3_from_plot2(self):
        self.view_instance.enqueue_transition('go_to_plot_3_from_plot_2')
        

        

   


