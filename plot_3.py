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
from PIL import Image, ImageTk


"""
Esta clase corresponde a la interfaz que contiene los gráficos de radios por grupo y los gráficos de deflexion por grupo,
deflexion característica y deflexión máxima correspondientes al lado derecho.
Se encarga de crear e instanciar sus respectivos objetos.
Tiene métodos en los cuales indica a sus objetos lo que debe suceder durante la ejecución.
"""
class Plot3():
    def __init__(self,root,view_instance):
        self.root = root
        self.fourth_plot_frame = None
        self.botones_frame=None
        self.state_label=None
        self.hora_label=None
        self.puesto_label=None
        self.title_frame=None
        self.graphs2_frame=None
        self.graphs3_frame=None
        self.image_cba=None
        self.image_label=None
        self.imagenes_frame=None
        self.title = None
        self.subtitle=None
        self.next = None
        self.back = None 
        self.configuration=None 
        self.view_instance = view_instance
        self.Graphs2 = None 
        self.Graphs3 = None

    """
    Este método cierra la interfaz. No la elimina, queda en 'background'
    """
    def close(self):
        self.fourth_plot_frame.grid_forget()

    """
    Este método destruye la interfaz principal de la clase por lo que se elimina todo
    Se ejecuta cuando hay un reset
    """
    def reset(self):
        self.fourth_plot_frame.destroy()

    """
    Get para saber la hora en la que inició la adquisición de datos.
    """
    def get_hora_label(self):
        return self.hora_label
    
    """
    Get para saber cual es el nro de puesto de la base de datos en la ejecución.
    """
    def get_puesto_label(self):
        return self.puesto_label

    """
    Get para saber cual es el estado
    """
    def get_state_label(self):
        return self.state_label
    
    """
    Esta función se llama cuando se accede o se instancia la interfaz.

    @params a:  Si a es 0, se instancia la clase por lo que se crean todos los objetos.
                Si a es 1, se accede a la interfaz por lo que se muestran los objetos creados.         
    """
    def show(self,a):
       
        if(a == 0):

            width = self.root.winfo_screenwidth()
            height = self.root.winfo_screenheight()

            fourth_plot_frame = Frame(self.root,background='#F6F4F2')
            self.fourth_plot_frame = fourth_plot_frame

            botones_frame=Frame(self.fourth_plot_frame,background='#F6F4F2')
            self.botones_frame=botones_frame

            title_frame=Frame(self.fourth_plot_frame,background='#F6F4F2')
            self.title_frame=title_frame

            graphs2_frame=Frame(self.fourth_plot_frame)
            self.graphs2_frame=graphs2_frame

            graphs3_frame=Frame(self.fourth_plot_frame)
            self.graphs3_frame=graphs3_frame

            imagenes_frame=Frame(self.fourth_plot_frame)
            self.imagenes_frame=imagenes_frame

            state_label=Label(self.botones_frame,text='', font=(None,10), background='white', foreground='black', relief='groove')
            self.state_label=state_label

            puesto_label=Label(self.botones_frame,text='',font=(None,12),background='#F6F4F2',foreground='#66A7EF')
            self.puesto_label=puesto_label

            hora_label=Label(self.botones_frame,text='',font=(None,12),background='#F6F4F2',foreground='#66A7EF')
            self.hora_label=hora_label

            back = ttk.Button(self.botones_frame, text="← Atras", command=self.go_to_plot_2_from_plot_3,style="TButton")
            self.back = back

            next = ttk.Button(self.botones_frame, text="Siguiente →", command=self.go_to_plot_4_from_plot_3,style="TButton")
            self.next = next

            configuration=ttk.Button(self.botones_frame,text="Ver configuración",command=self.show_configuration,style="TButton")
            self.configuration=configuration 

            title = Label(self.title_frame, text="Deflexiones y Radios",font=("Helvetica", 25),background='#F6F4F2',foreground='#625651')
            self.title=title
            
            subtitle=Label(self.title_frame, text="Lado Derecho",font=("Helvetica", 22),background='#F6F4F2',foreground='#625651')
            self.subtitle=subtitle

            self.Graphs2 = graphs_2.Graphs2(self.graphs2_frame, lado="Derecho")
            self.Graphs3 = graphs_3.Graphs3(self.graphs3_frame, lado="Derecho")

            original_image=Image.open("image3.png")
            screen_width = self.root.winfo_screenwidth()

            desired_width = screen_width
            aspect_ratio = original_image.width / original_image.height
            height=60
            resized_image = original_image.resize((desired_width, height))

            self.image_cba = ImageTk.PhotoImage(resized_image)
            self.image_label = Label(self.imagenes_frame, image=self.image_cba)
            self.image_label.image = self.image_cba

        if(a == 1):
            self.fourth_plot_frame.grid(sticky="NSEW")
            self.botones_frame.grid(row=0,columnspan=2,padx=(0,0),pady=(0,0))
            self.back.grid(row=0, column=0,padx=(0,1285),pady=(0,0),sticky=NW)
            self.next.grid(row=1,column=0,padx=(0,1285),pady=(0,0),sticky=NW)
            self.configuration.grid(row=2,column=0,padx=(0,1285),pady=(0,0))
            self.state_label.grid(row=0,column=0,padx=(0,950),pady=(0,0))
            self.puesto_label.grid(row=0,column=0,padx=(1100,0),pady=(0,0))
            self.hora_label.grid(row=1,column=0,padx=(1100,0),pady=(0,0))
            self.title_frame.grid(row=1,columnspan=2,pady=(0,0))
            self.title.grid()
            self.subtitle.grid()
            self.graphs2_frame.grid(row=2,column=0,padx=(0,650),pady=(0,0))
            self.graphs3_frame.grid(row=2,column=0,padx=(650,0),pady=(0,0))
            self.imagenes_frame.grid(row=2,padx=(0,90),pady=(385,0))
            self.image_label.grid(row=0,columnspan=2,padx=(0,0))

    """
    Este método le indica a los objetos Graphs2 y Graphs3 que guarden los gráficos
    correspondientes para armar el PDF.
    """
    def download_graphs(self):
        self.Graphs2.download_graphs2(lado="Derecho")
        self.Graphs3.download_graphs3(lado="Derecho")

    """
    Este método le indica a los objetos Graphs2 y Graphs3 que deben actualizar sus gráficos porque se cumplió el grupo (50 o 100).

    @params dict_r, dict_l: Diccionarios con valores de lado derecho e izquierdo.
            defl_r_car, defl_l_car: Valores de deflexión característica de lado derecho e izquierdo.
            defl_r_max, defl_l_max: Valores de deflexión máximos de lado derecho e izquierdo.
            grupos: El valor del grupo (50 o 100) seleccionado por el usuario. 
    """
    def new_group_data_plot3(self,dict_r, dict_l, defl_r_car, defl_l_car, defl_r_max, defl_l_max,grupos):
        self.Graphs2.update_gmean(dict_r, dict_l,grupos,lado="Derecho")
        self.Graphs3.update_deflexiones_gmean(dict_r,dict_l, defl_r_car, defl_l_car, defl_r_max, defl_l_max,grupos,lado="Derecho")

    """
    Este método se ejecuta cuando el usuario presiona el botón de '← Atras'.
    """
    def go_to_plot_2_from_plot_3(self):
        self.view_instance.enqueue_transition('go_to_plot_2_from_plot_3')

    """
    Este método se ejecuta cuando el usuario presiona el botón de 'Siguiente →'.
    """
    def go_to_plot_4_from_plot_3(self):
        self.view_instance.enqueue_transition('go_to_plot_4_from_plot_3')

    """
    Este método muestra la configuración establecida por el usuario.
    """
    def show_configuration(self):
        self.view_instance.enqueue_transition('show_configuration')