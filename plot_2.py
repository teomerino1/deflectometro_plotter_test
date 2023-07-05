from tkinter import *
from tkinter.ttk import Label, Frame, Button, Scrollbar
import view
import table
import graphs
from tkinter.ttk import Treeview
import tkinter as tk
from tkinter import ttk

from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk


# Clase correspondiente a la vista encargada de mostrar los datos y graficos

class Plot2():
    def __init__(self,root, go_to_plot_1_from_plot_2):

        self.root = root
        # self.main_plot_frame = None
        # self.second_plot_frame = None
        self.third_plot_frame = None
        self.go_to_plot_1_from_plot_2 = go_to_plot_1_from_plot_2
        self.Graphs = None

    # Metodo que elimina todo lo que muestra la pagina
    def close(self):
        self.third_plot_frame.destroy()

    def show(self):
       
        width = self.root.winfo_screenwidth()

        height = self.root.winfo_screenheight()

        third_plot_frame = Frame(self.root,width=width,height=height)

        self.third_plot_frame = third_plot_frame

        third_plot_frame.grid(rowspan=3,columnspan=3)

        title = Label(third_plot_frame, text="Grafico de medias",font=(None, 20)) 

        title.grid(row = 0, column = 0,sticky=NW)

        back = Button(third_plot_frame, text="Atrás", command=self.go_to_plot_1_from_plot_2)

        back.grid(row=1, column=0,sticky=NW)

        next = Button(third_plot_frame, text="Next", command=self.go_to_plot_1_from_plot_2)

        next.grid(row=2,column=0,sticky=NW)

        self.Graphs = graphs.Graphs(self.third_plot_frame).show_radio_gmean_graph()

        


        

   


