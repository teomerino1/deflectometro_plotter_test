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
from PIL import Image, ImageTk

# Clase correspondiente a la vista encargada de mostrar los datos y graficos

class Plot4():
    def __init__(self,root, view_instance):

        self.root = root
        self.fifht_plot_frame = None
        self.graphs_frame=None
        self.botones_frame=None
        self.state_label=None
        self.imagen_frame=None
        self.image_cba=None
        self.image_label=None
        self.title_frame=None
        self.title = None
        self.subtitle=None
        self.next = None
        self.back = None  
        self.view_instance = view_instance
        self.Graphs4 = None

    # Metodo que elimina todo lo que muestra la pagina
    def close(self):
        self.fifht_plot_frame.grid_forget()

    def reset(self):
        self.fifht_plot_frame.destroy()
        self.show(0)

    def show(self,a):
       
        if(a == 0):

            width = self.root.winfo_screenwidth()
            height = self.root.winfo_screenheight()

            fifht_plot_frame = Frame(self.root,background='#F6F4F2')
            self.fifht_plot_frame = fifht_plot_frame

            botones_frame=Frame(self.fifht_plot_frame,background='#F6F4F2')
            self.botones_frame=botones_frame

            title_frame=Frame(self.fifht_plot_frame,background='#F6F4F2')
            self.title_frame=title_frame
            
            graphs_frame=Frame(self.fifht_plot_frame)
            self.graphs_frame=graphs_frame

            imagen_frame=Frame(self.fifht_plot_frame)
            self.imagen_frame=imagen_frame

            state_label=Label(self.botones_frame,text="Test",font=(None,15),background='#F6F4F2',foreground='#66A7EF')
            self.state_label=state_label

            title = Label(self.title_frame, text="Informe Estadístico",font=("Helvetica", 25),background='#F6F4F2',foreground='#625651') 
            self.title=title

            back = ttk.Button(botones_frame, text="Atrás", command=self.go_to_plot_3_from_plot_4,style="TButton")
            self.back = back

            next = ttk.Button(botones_frame, text="Next", command=self.go_to_plot_5_from_plot_4,style="TButton") 
            self.next = next

            self.Graphs4 = graphs_4.Graphs4(self.graphs_frame)

            original_image=Image.open("image3.png")
            screen_width = self.root.winfo_screenwidth()

            # Redimensiona la imagen al ancho de la pantalla y ajusta la altura proporcionalmente
            desired_width = screen_width
            aspect_ratio = original_image.width / original_image.height
            height=65
            # desired_height = int(desired_width / aspect_ratio)
            resized_image = original_image.resize((desired_width, height), Image.ANTIALIAS)
            # Convierte la imagen redimensionada a un objeto PhotoImage
            self.image_cba = ImageTk.PhotoImage(resized_image)
            self.image_label = Label(self.imagen_frame, image=self.image_cba)
            self.image_label.image = self.image_cba

        if(a == 1):

            self.fifht_plot_frame.grid(sticky="NSEW")
            self.botones_frame.grid(row=0,columnspan=2,padx=(0,0))
            self.back.grid(row=0, column=0,padx=(0,1270),sticky=NW)
            self.next.grid(row=0,column=0,padx=(1230,0))
            self.state_label.grid(row=0,column=0,padx=(0,1000))
            
            self.title_frame.grid(row=1,columnspan=2,pady=(50,0))
            self.title.grid()
            self.graphs_frame.grid(row=2,columnspan=2,padx=(0,0),pady=(0,0))
            self.imagen_frame.grid(row=2,padx=(0,30),pady=(400,0))
            self.image_label.grid(row=0,columnspan=2,padx=(0,0))

    def download_graphs(self):
        self.Graphs4.download_graphs4()

    def new_group_data_plot4(self,dict_r,dict_l,grupos):
        self.Graphs4.update_deflexiones_radios_graph(dict_r,dict_l,grupos)

    def go_to_plot_3_from_plot_4(self):
        self.view_instance.enqueue_transition('go_to_plot_3_from_plot_4')

    def go_to_plot_5_from_plot_4(self):
        self.view_instance.enqueue_transition('go_to_plot_5_from_plot_4')
