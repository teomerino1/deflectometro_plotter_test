import tkinter as tk
from tkinter.ttk import Label, Button, Entry, Radiobutton
import view


class Config():
    def __init__(self, root, go_to_plot1_from_config):
        self.root = root
        self.config_frame = None
        self.temp_ntry = None
        self.grupos_ntry_50 = None
        self.grupos_ntry_100 = None
        self.var = None
        self.muestras_ntry = None
        self.espesor = None 
        self.ft_ntry = None
        self.fh_ntry = None 
        self.fc_ntry = None
        
        self.go_to_plot1_from_config = go_to_plot1_from_config


    def show(self):
        config_frame = tk.Frame()
        config_frame.grid_rowconfigure(0, weight=1)
        config_frame.grid_rowconfigure(1, weight=1)
        config_frame.grid_rowconfigure(2, weight=1)
        config_frame.grid_rowconfigure(3, weight=1)
        config_frame.grid_rowconfigure(4, weight=1)
        config_frame.grid_rowconfigure(5, weight=1)
        config_frame.grid_rowconfigure(6, weight=1)
        config_frame.grid_rowconfigure(7, weight=1)
        config_frame.grid_rowconfigure(8, weight=1)

        # config_frame.grid_rowconfigure(4, weight=1)
        config_frame.grid_columnconfigure(0, weight=1)
        config_frame.grid_columnconfigure(1, weight=1)
        config_frame.grid_columnconfigure(2, weight=1)
        config_frame.grid_columnconfigure(3, weight=1)
        config_frame.grid_columnconfigure(4, weight=1)

        config_frame.grid(ipadx=3, ipady=2)
        self.config_frame = config_frame

        Label(config_frame, text="Configuración inicial",font=(None, 30)).grid(row=0, column=3, sticky="N")

        # temp
        Label(config_frame, text="Temperatura:").grid(row=1, column=0)
        temp_ntry = Entry(config_frame)
        temp_ntry.grid(row=1, column=1)
        self.temp_ntry = temp_ntry
        
        # grupos
        Label(config_frame, text="Tamanio de grupos:").grid(row=2, column=0)
        var = tk.IntVar()
        self.var = var
        grupos_ntry_50 = Radiobutton(config_frame,text='50', variable=var, value=50)
        grupos_ntry_50.grid(row=2, column=1)
        self.grupos_ntry_50 = grupos_ntry_50

        grupos_ntry_100 = Radiobutton(config_frame,text='100', variable=var, value=100)
        grupos_ntry_100.grid(row=2, column=2)
        self.grupos_ntry_100 = grupos_ntry_100

       

        # muestras
        Label(config_frame, text="Cantidad total de muestras:").grid(row=3, column=0)
        muestras_ntry = Entry(config_frame)
        muestras_ntry.grid( row=3, column=1)
        self.muestras_ntry = muestras_ntry

        Label(config_frame, text="Espesor:").grid(row=4, column=0)
        espesor = Entry(config_frame)
        espesor.grid(row=4,column=1)
        self.espesor = espesor

      

        Button(config_frame, text="Confirmar", command=self.go_to_plot1_from_config).grid(row=5, column=0)

    def close(self):
        # view.temp, view.grupos, view.muestras = self.temp_ntry.get(), self.var.get(), self.muestras_ntry.get()
        view.temp, view.muestras, view.grupos, view.espesor = self.get_config()
        self.config_frame.grid_forget()
        # self.config_frame.destroy()

    def get_config(self):
        return self.temp_ntry.get(), self.var.get(), self.muestras_ntry.get(), self.espesor.get()
    
    #  def get_config(self):
    #     return self.temp_ntry.get(), self.var.get(), self.muestras_ntry.get()