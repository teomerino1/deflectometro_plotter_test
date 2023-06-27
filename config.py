import tkinter as tk
from tkinter.ttk import Label, Button, Entry, Radiobutton
import view


class Config():
    def __init__(self, root, config_calback):
        self.root = root
        self.config_frame = None
        self.temp_ntry = None
        self.grupos_ntry_50 = None
        self.grupos_ntry_100 = None
        self.var = None
        self.muestras_ntry = None
        
        self.config_calback = config_calback


    def show(self):
        config_frame = tk.Frame()
        config_frame.grid(ipadx=3, ipady=2)
        self.config_frame = config_frame

        Label(config_frame, text="Configuración inicial",font=(None, 30)).grid(column=15, row=0)

        # temp
        Label(config_frame, text="Temperatura:").grid(column=0, row=1)
        temp_ntry = Entry(config_frame)
        temp_ntry.grid(column=1, row=1)
        self.temp_ntry = temp_ntry
        
        # grupos
        Label(config_frame, text="Tamanio de grupos:").grid(column=0, row=2)
        var = tk.IntVar()
        grupos_ntry_50 = Radiobutton(config_frame,text='50', variable=var, value=50)
        grupos_ntry_50.grid(column=1, row=2)
        self.grupos_ntry_50 = grupos_ntry_50

        grupos_ntry_100 = Radiobutton(config_frame,text='100', variable=var, value=100)
        grupos_ntry_100.grid(column=2, row=2)
        self.grupos_ntry_100 = grupos_ntry_100

        self.var = var

        # muestras
        Label(config_frame, text="Cantidad total de muestras:").grid(column=0, row=3)
        muestras_ntry = Entry(config_frame)
        muestras_ntry.grid(column=1, row=3)
        self.muestras_ntry = muestras_ntry

        Button(config_frame, text="Confirmar", command=self.config_calback).grid(column=0, row=4)

    def close(self):
        # view.temp, view.grupos, view.muestras = self.temp_ntry.get(), self.var.get(), self.muestras_ntry.get()
        view.temp, view.muestras, view.grupos = self.get_config()
        self.config_frame.destroy()

    def get_config(self):
        return self.temp_ntry.get(), self.var.get(), self.muestras_ntry.get()