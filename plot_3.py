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

class Plot3():
    def __init__(self,root,view_instance):
        self.root = root
        self.fourth_plot_frame = None
        self.title = None
        self.next = None
        self.back = None 
        self.view_instance = view_instance
        self.Graphs2 = None 
        self.Graphs3 = None

    # Metodo que elimina todo lo que muestra la pagina
    def close(self):
        self.fourth_plot_frame.grid_forget()

    def reset(self):
        self.fourth_plot_frame.destroy()
        self.show(0)

    def show(self,a):
       
        if(a == 0):

            width = self.root.winfo_screenwidth()
            height = self.root.winfo_screenheight()

            fourth_plot_frame = Frame(self.root, width=width, height=height)
            self.fourth_plot_frame = fourth_plot_frame

            title = Label(fourth_plot_frame, text="Deflexiones y Radios: Lado Derecho",font=(None, 20)) 
            self.title=title

            back = ttk.Button(fourth_plot_frame, text="Atrás", command=self.go_to_plot_2_from_plot_3,style="TButton")
            # style = ttk.Style()
            # style.configure("Custom.TButton", background="blue", foreground="white")
            # back = ttk.Button(fourth_plot_frame, text="Atras", command=self.go_to_plot_2_from_plot_3, style="Custom.TButton")
            self.back = back

            next = ttk.Button(fourth_plot_frame, text="Next", command=self.go_to_plot_4_from_plot_3,style="TButton")
            # style = ttk.Style()
            # style.configure("Custom.TButton", background="blue", foreground="white")
            # next = ttk.Button(fourth_plot_frame, text="Next", command=self.go_to_plot_4_from_plot_3, style="Custom.TButton")
            self.next = next
            

            self.Graphs2 = graphs_2.Graphs2(self.fourth_plot_frame, lado="Derecho")
            self.Graphs3 = graphs_3.Graphs3(self.fourth_plot_frame, lado="Derecho")

        if(a == 1):

            self.fourth_plot_frame.grid(rowspan=10,columnspan=10)
            self.title.grid(row = 0, column = 0,sticky=NW)
            self.back.grid(row=1, column=0,sticky=NW)
            self.next.grid(row=2,column=0,sticky=NW)

    def download_graphs(self):
        self.Graphs2.download_graphs2(lado="Derecho")
        self.Graphs3.download_graphs3(lado="Derecho")


    def new_group_data_plot3(self,dict_r, dict_l, defl_r_car, defl_l_car, defl_r_max, defl_l_max,grupos):
        self.Graphs2.update_gmean(dict_r, dict_l,grupos,lado="Derecho")
        self.Graphs3.update_deflexiones_gmean(dict_r,dict_l, defl_r_car, defl_l_car, defl_r_max, defl_l_max,grupos,lado="Derecho")

    def go_to_plot_2_from_plot_3(self):
        self.view_instance.enqueue_transition('go_to_plot_2_from_plot_3')

    def go_to_plot_4_from_plot_3(self):
        self.view_instance.enqueue_transition('go_to_plot_4_from_plot_3')