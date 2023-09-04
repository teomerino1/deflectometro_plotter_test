from tkinter import *
from tkinter.ttk import Label, Frame, Button, Scrollbar
import tkinter as tk
from tkinter import ttk
import graphs_2
import graphs_3
from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
from PIL import Image, ImageTk

# Clase correspondiente a la vista encargada de mostrar los datos y graficos
#azul: #66A7EF
            #letras theme: #625651
class Plot2():
    def __init__(self,root,view_instance):
        self.root = root
        self.third_plot_frame = None
        self.title_frame=None
        self.state_label=None
        self.graphs2_frame=None
        self.graphs3_frame=None
        self.botones_frame=None
        self.imagenes_frame=None
        self.image_cba=None
        self.image_label=None
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

            third_plot_frame = Frame(self.root,background='#F6F4F2')
            self.third_plot_frame = third_plot_frame

            botones_frame=Frame(self.third_plot_frame,background='#F6F4F2')
            self.botones_frame=botones_frame

            title_frame=Frame(self.third_plot_frame,background='#F6F4F2')
            self.title_frame=title_frame

            graphs2_frame=Frame(self.third_plot_frame)
            self.graphs2_frame=graphs2_frame

            graphs3_frame=Frame(self.third_plot_frame)
            self.graphs3_frame=graphs3_frame

            state_label=Label(self.botones_frame,text="Test",font=(None,15),background='#F6F4F2',foreground='#66A7EF')
            self.state_label=state_label

            imagenes_frame=Frame(self.third_plot_frame)
            self.imagenes_frame=imagenes_frame

            title = Label(self.title_frame, text="Deflexiones y Radios",font=("Helvetica", 25),background='#F6F4F2',foreground='#625651') 
            self.title=title
            
            subtitle=Label(self.title_frame, text="Lado Izquierdo",font=("Helvetica", 22),background='#F6F4F2',foreground='#625651')
            self.subtitle=subtitle

            back = ttk.Button(self.botones_frame, text="Atrás", command=self.go_to_plot_1_from_plot_2,style="TButton")
            self.back = back

            next = ttk.Button(self.botones_frame, text="Next", command=self.go_to_plot_3_from_plot2,style="TButton")
            self.next = next

            self.Graphs2 = graphs_2.Graphs2(self.graphs2_frame,lado="Izquierdo")
            self.Graphs3 = graphs_3.Graphs3(self.graphs3_frame,lado="Izquierdo")

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
            self.image_label = Label(self.imagenes_frame, image=self.image_cba)
            self.image_label.image = self.image_cba
            
        if(a == 1):
            self.third_plot_frame.grid(sticky="NSEW")
            self.botones_frame.grid(row=0,columnspan=2,padx=(0,0))
            self.back.grid(row=0, column=0,padx=(0,1270),sticky=NW)
            self.next.grid(row=0,column=0,padx=(1230,0))
            self.state_label.grid(row=0,column=0,padx=(0,900))
            self.title_frame.grid(row=1,columnspan=2,pady=(20,0))
            self.title.grid()
            self.subtitle.grid()
            self.graphs2_frame.grid(row=2,column=0,padx=(0,700),pady=(60,0))
            self.graphs3_frame.grid(row=2,column=0,padx=(700,0),pady=(60,0))
            self.imagenes_frame.grid(row=2,padx=(0,30),pady=(450,0))
            self.image_label.grid(row=0,columnspan=2,padx=(0,0))
            
##F6F4F2

    def get_state_label(self):
        return self.state_label
    
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
        

        

   


