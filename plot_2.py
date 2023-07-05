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
        self.main_plot_frame = None
        self.second_plot_frame = None
        self.third_plot_frame = None
        self.go_to_plot_1_from_plot_2 = go_to_plot_1_from_plot_2

        
        self.Graphs = None

    # Metodo que elimina todo lo que muestra la pagina
    def close(self):
        self.third_plot_frame.destroy()

    def show(self):

        columns = ("columna1", "columna2", "columna3", "columna4","columna5","columna6")  # Especifica los nombres de las columnas
       
        width = self.root.winfo_screenwidth()

        height = self.root.winfo_screenheight()

        third_plot_frame = Frame(self.root,width=width,height=height)

        third_plot_frame.grid(rowspan=5,columnspan=5)

        self.third_plot_frame = third_plot_frame
        
        back = Button(third_plot_frame, text="Atras", command=self.go_to_plot_1_from_plot_2)

        back.grid(row=0, column=1)
        

   


