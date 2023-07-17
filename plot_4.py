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
import graphs_4
from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk


# Clase correspondiente a la vista encargada de mostrar los datos y graficos

class Plot4():
    def __init__(self,root, view_instance):

        self.root = root
        # self.main_plot_frame = None
        # self.second_plot_frame = None
        self.fifht_plot_frame = None
        self.title = None
        self.next = None
        self.back = None  
        self.view_instance = view_instance
        # self.go_to_plot_3_from_plot_4 = go_to_plot_3_from_plot_4
        # self.go_to_plot_5_from_plot_4 = go_to_plot_5_from_plot_4#TODO HACERLO
        self.Graphs4 = None

    # Metodo que elimina todo lo que muestra la pagina
    def close(self):

        self.fifht_plot_frame.grid_forget()


    def show(self,a):
       
        if(a == 0):

            width = self.root.winfo_screenwidth()

            height = self.root.winfo_screenheight()

            fifht_plot_frame = Frame(self.root, width=width, height=height)

            self.fifht_plot_frame = fifht_plot_frame

            title = Label(fifht_plot_frame, text="Graficos de deflexiones vs radios",font=(None, 20)) 

            self.title=title

            back = Button(fifht_plot_frame, text="Atrás", command=self.go_to_plot_3_from_plot_4)

            self.back = back

            next = Button(fifht_plot_frame, text="Next", command=self.go_to_plot_5_from_plot_4) #TODO Hacer el next al plot 5

            self.next = next

            self.Graphs4 = graphs_4.Graphs4(self.fifht_plot_frame)


        if(a == 1):

            self.fifht_plot_frame.grid(rowspan=3,columnspan=3)

            self.title.grid(row = 0, column = 0,sticky=NW)

            self.back.grid(row=1, column=0,sticky=NW)

            self.next.grid(row=2,column=0,sticky=NW)


    def new_group_data_plot4(self,dict_r,dict_l):

        self.Graphs4.update_deflexiones_radios_graph(dict_r,dict_l)

    def go_to_plot_3_from_plot_4(self):
        self.view_instance.enqueue_transition('go_to_plot_3_from_plot_4')

    def go_to_plot_5_from_plot_4(self):
        self.view_instance.enqueue_transition('go_to_plot_5_from_plot_4')
