import tkinter as tk
from tkinter import *
from tkinter.ttk import Scrollbar

from tkinter.ttk import Style
import config
import plot
import plot_2

class View():
    def __init__(self, root):

        # variable globales
        global temp
        global grupos
        global muestras
        global z_ntry 
        global fh_ntry
        global ft_ntry 
        global fc_ntry
        global first_time_plot1
        temp = None
        grupos = None
        muestras = None
        z_ntry = None
        ft_ntry = None
        fh_ntry = None
        fc_ntry = None
        

        #Se crean los objetos Plot y Config como atributos de view 
        self.Config = config.Config(root, self.go_to_plot1_from_config)
        self.Plot = plot.Plot(root,self.go_to_config, self.go_to_plot_2_from_plot_1)
        self.Plot2 = plot_2.Plot2(root,self.go_to_plot_1_from_plot_2)
        self.is_plotting = False
        self.start(root)
       
       
      
       




        # self.Plot.show()

     # Metodo que inicializa la view:
    def start(self,root):

        #Se ejecuta el metodo show de Config para que aparezca la ventana principal
        self.Config.show()

        root.title('Deflectómetro')

        root.tk.call("source", "azure.tcl")
        root.tk.call("set_theme", "light")

        style = Style(root)

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        root.geometry(f"{screen_width}x{screen_height}")

    # Metodo que borra el frame Config y abre el Plot1
    def go_to_plot1_from_config(self):
        self.Config.close()
        self.Plot.show(0)
        # self.Plot.grid_plot1()
        self.is_plotting = True

    # Metodo que borra el Plot 1 y abre el de Config
    def go_to_config(self):
        self.Plot.close()
        self.Config.show()


    # Metodo que borra el Plot 1 y abre el Plot 2
    def go_to_plot_2_from_plot_1(self):
        self.Plot.close()
        self.Plot2.show(0)

    # Metodo que borra el Plot 2 y abre el Plot 1
    def go_to_plot_1_from_plot_2(self):
        self.Plot2.close()
        self.Plot.show(1)

     
    # Metodo que obtiene los datos nuevos y debe mandar a actualizar los ploteos y las estructuras
    def new_group_data_view(self, dict_r, dict_l):
        self.Plot.new_group_data_plot(dict_r, dict_l)
        self.Plot2.new_group_data_plot2(dict_r,dict_l)
        # self.Plot.update_table(df)

    # Metodo que manda a actualizar el gafico de barras 
    def update_bar_view(self, defl_left_right_dict):
        self.Plot.update_bar_plot(defl_left_right_dict)

    def get_config(self):
        self.Config.get_config()
    
    def on_plot(self):
        return self.is_plotting;
      
