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

class Plot5():
    def __init__(self,root, go_to_plot_4_from_plot_5):

        self.root = root
        # self.main_plot_frame = None
        # self.second_plot_frame = None
        self.sixth_plot_frame = None
        self.title = None
        self.back = None  
        self.go_to_plot_4_from_plot_5 = go_to_plot_4_from_plot_5
        # self.go_to_plot_5_from_plot_4 #TODO HACERLO!
        self.Graphs2 = None

    # Metodo que elimina todo lo que muestra la pagina
    def close(self):

        self.sixth_plot_frame.grid_forget()


    def show(self,a):
       
        if(a == 0):

            width = self.root.winfo_screenwidth()

            height = self.root.winfo_screenheight()

            sixth_plot_frame = Frame(self.root, width=width, height=height)

            self.sixth_plot_frame = sixth_plot_frame

            title = Label(sixth_plot_frame, text="Plantilla de resultados estadísticos",font=(None, 20)) 

            self.title=title

            back = Button(sixth_plot_frame, text="Atrás", command=self.go_to_plot_4_from_plot_5)

            self.back = back

        if(a == 1):

            self.sixth_plot_frame.grid(rowspan=3,columnspan=3)

            self.title.grid(row = 0, column = 0,sticky=NW)

            self.back.grid(row=1, column=0,sticky=NW)