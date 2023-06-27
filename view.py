import tkinter as tk
from tkinter.ttk import Style
import config
import plot

class View():
    def __init__(self, root):

        # variable globales
        global temp
        global grupos
        global muestras
        temp = None
        grupos = None
        muestras = None

        self.is_plotting = False

        self.start(root)
                
        self.Plot = plot.Plot(root,self.plot_callback)
        
        self.Config = config.Config(root, self.config_callback)
        self.Config.show()
        # self.Plot.show()

     # Metodo que inicializa la view:
    def start(self,root):
        root.title('Deflectómetro')

        root.tk.call("source", "azure.tcl")
        root.tk.call("set_theme", "light")

        style = Style(root)

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        root.geometry(f"{screen_width}x{screen_height}")

    # Metodo que borra el frame plot y abre el de config
    def plot_callback(self):
        self.Plot.close()
        self.Config.show()
    
    # Metodo que borra el frame config y abre el de ploteo
    def config_callback(self):
        self.Config.close()
        self.Plot.show()
        self.is_plotting = True

   

    # Metodo que obtiene los datos nuevos y debe mandar a actualizar los ploteos y las estructuras
    def new_group_data(self, dict_r, dict_l):
        self.Plot.new_group_data(dict_r, dict_l)
        # self.Plot.update_table(df)

    # Metodo que manda a actualizar el gafico de barras 
    def update_bar(self, hist_dict):
        self.Plot.update_bar(hist_dict)

    def get_config(self):
        self.Config.get_config()
    
    def on_plot(self):
        return self.is_plotting;
      
