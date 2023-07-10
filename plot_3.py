from tkinter import *
from tkinter.ttk import Label, Frame, Button, Scrollbar
import view
import table
import graphs
from tkinter.ttk import Treeview
import tkinter as tk
from tkinter import ttk
import graphs_2
from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk


# Clase correspondiente a la vista encargada de mostrar los datos y graficos

class Plot3():
    def __init__(self,root, go_to_plot_2_from_plot_3):

        self.root = root
        # self.main_plot_frame = None
        # self.second_plot_frame = None
        self.fourth_plot_frame = None
        self.title = None
        self.next = None
        self.back = None  
        self.go_to_plot_1_from_plot_2 = go_to_plot_2_from_plot_3
        self.Graphs2 = None

    # Metodo que elimina todo lo que muestra la pagina
    def close(self):

        self.fourth_plot_frame.grid_forget()


    def show(self,a):
       
        if(a == 0):

            width = self.root.winfo_screenwidth()

            height = self.root.winfo_screenheight()

            fourth_plot_frame = Frame(self.root, width=width, height=height)

            self.fourth_plot_frame = fourth_plot_frame

            title = Label(fourth_plot_frame, text="Deflexiones y Radios: Lado Derecho",font=(None, 20)) 

            self.title=title

            back = Button(fourth_plot_frame, text="Atrás", command=self.go_to_plot_1_from_plot_2)

            self.back = back

            next = Button(fourth_plot_frame, text="Next", command=self.go_to_plot_1_from_plot_2)

            self.next = next

            self.Graphs2 = graphs_2.Graphs2(self.fourth_plot_frame, lado="Derecho")

        if(a == 1):

            self.fourth_plot_frame.grid(rowspan=3,columnspan=3)

            self.title.grid(row = 0, column = 0,sticky=NW)

            self.back.grid(row=1, column=0,sticky=NW)

            self.next.grid(row=2,column=0,sticky=NW)


    def new_group_data_plot3(self,dict_r, dict_l):
        
        self.Graphs2.update_gmean(dict_r, dict_l,lado="Derecho")