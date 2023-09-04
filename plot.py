from tkinter import *
from tkinter.ttk import Label, Frame, Button, Scrollbar
from PIL import Image, ImageTk 
import view
import table
import graphs
from tkinter.ttk import Treeview
import tkinter as tk
from tkinter import ttk
import datetime
from tkinter.ttk import Treeview
from tkinter import ttk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from tkinter import messagebox



# Clase correspondiente a la vista encargada de mostrar los datos y graficos

class Plot():
    def __init__(self,root,view_instance):

        self.root = root
        self.second_plot_frame = None
        self.botones_frame=None
        self.table_frame=None
        self.state_label=None
        self.state=None
        self.graphs_frame=None
        self.labels_frame=None
        self.imagen_frame=None
        self.image_cba=None
        self.image_label=None
        self.view_instance = view_instance
        self.title = None 
        self.temperatura = None 
        self.muestras = None 
        self.grupos = None 
        self.atras = None 
        self.next = None 
        self.Table = None
        self.Graphs = None
        self.label_der=None
        self.label_izq=None

    # Metodo que elimina todo lo que muestra la pagina
    def close(self):
        self.second_plot_frame.grid_forget()
    
    def reset(self):
        self.second_plot_frame.destroy()
        self.show(0)

    def get_state_label(self):
        return self.state_label
    
    def show(self,a):

        if(a == 0):
            second_plot_frame = Frame(self.root)
            self.second_plot_frame = second_plot_frame
            
            botones_frame=Frame(self.second_plot_frame)
            self.botones_frame=botones_frame

            labels_frame=Frame(self.second_plot_frame)
            self.labels_frame=labels_frame

            table_frame=Frame(self.second_plot_frame)
            self.table_frame=table_frame

            graphs_frame=Frame(self.second_plot_frame)
            self.graphs_frame=graphs_frame

            imagen_frame=Frame(self.second_plot_frame)
            self.imagen_frame=imagen_frame

            state_label=Label(self.botones_frame,text='',font=(None,15),foreground='#66A7EF')
            self.state_label=state_label

            columns = ("columna1", "columna2", "columna3", "columna4","columna5","columna6")  # Especifica los nombres de las columnas

            self.table = Treeview(self.table_frame, columns=columns, show='headings')
            
            atras = ttk.Button(self.botones_frame, text="Atras", command=self.go_to_config,style="TButton")
            self.atras=atras

            next = ttk.Button(self.botones_frame,text="Next",command=self.go_to_plot_2_from_plot_1,style="TButton")
            self.next = next

            self.Table = table.Table(self.table_frame) 
            self.Graphs = graphs.Graphs(self.graphs_frame) 

            label_der = Label(self.labels_frame, text="Huella Externa (DERECHA)", font=("Helvetica", 22))
            self.label_der=label_der

            label_izq = Label(self.labels_frame, text="Huella Interna (IZQUIERDA)", font=("Helvetica", 22))
            self.label_izq=label_izq

            original_image=Image.open("image3.png")
            screen_width = self.root.winfo_screenwidth()

            # Redimensiona la imagen al ancho de la pantalla y ajusta la altura proporcionalmente
            desired_width = screen_width
            aspect_ratio = original_image.width / original_image.height
            height=65
            desired_height = int(desired_width / aspect_ratio)
            print("desired height",desired_height)
            resized_image = original_image.resize((desired_width, height), Image.ANTIALIAS)

            # Convierte la imagen redimensionada a un objeto PhotoImage
            self.image_cba = ImageTk.PhotoImage(resized_image)
            self.image_label = Label(self.imagen_frame, image=self.image_cba)
            self.image_label.image = self.image_cba

        if(a == 1):
            self.second_plot_frame.grid(sticky=NSEW)
            self.botones_frame.grid(row=0,columnspan=2,padx=(0,50))  
            self.atras.grid(row=0, column=0,padx=(0,1250),pady=(0,0),sticky=NW)
            self.next.grid(row=0, column=0,padx=(1250,0),pady=(0,0))
            self.state_label.grid(row=0,column=0,padx=(0,900))

            self.labels_frame.grid(row=1,columnspan=2,padx=(0,0),pady=(0,0))
            self.label_izq.grid(row=1, column=0,padx=(0,350))
            self.label_der.grid(row=1, column=0,padx=(550,0))

            self.table_frame.grid(row=2,padx=(0,45))
            self.graphs_frame.grid(row=3,columnspan=2,padx=(0,0),pady=(0,0))

            self.imagen_frame.grid(row=3,padx=(0,30),pady=(160,0))
            self.image_label.grid(row=0,columnspan=2,padx=(0,0))
            
            
    def generar_pdf(self):
        self.Table.donwload_table()
        self.Graphs.donwload_graphs()
        
    def get_prog_max(self):
        return self.Graphs.get_max()
 
    def set_ruta(self,ruta):
        self.Table.set_ruta(ruta)
        self.Table.set_fecha(datetime.datetime.now().date())

    def grid_plot1(self):
        self.second_plot_frame.grid(ipadx=10, ipady=5)

    def update_bar_plot(self, defl_r,defl_l):
        self.Graphs.update_bar(defl_r,defl_l)

    # Metodo que recibe los datos nuevos y manda a actualizar estructuras y plots
    def new_group_data_plot(self,dict_r, dict_l):
        self.Table.insert(dict_r, dict_l)

    def go_to_plot_2_from_plot_1(self):
        self.view_instance.enqueue_transition('go_to_plot_2_from_plot_1')
        
    def go_to_config(self):
        if(self.view_instance.get_state()=="Obteniendo datos..."):
            messagebox.askokcancel("Aviso","Se están obteniendo datos. ¿Desea volver a a configuración?")
        self.view_instance.enqueue_transition('go_to_config')

    def reset_table(self):
        self.Table.reset()

    
   


