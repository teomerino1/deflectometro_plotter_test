import tkinter as tk
from tkinter.ttk import Label, Button, Entry, Radiobutton
import view


class Config():
    def __init__(self, root, go_to_plot1_from_config,view_instance):
        
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
        self.z_ntry = None
        self.ruta_ntry = None
        self.prov_ntry = None
        self.tramo_ntry = None
        self.subtramo_ntry = None
        self.pav_ntry = None
        self.view_instance = view_instance
        self.go_to_plot1_from_config = go_to_plot1_from_config


    def show(self):
        
        config_frame = tk.Frame()

        config_frame.grid_rowconfigure(0, weight=1)
        config_frame.grid_rowconfigure(1, weight=1)
        config_frame.grid_rowconfigure(2, weight=1)
        config_frame.grid_rowconfigure(3, weight=1)
        config_frame.grid_rowconfigure(4, weight=1)

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

        # Muestras
        Label(config_frame, text="Cantidad total de muestras:").grid(row=3, column=0)
        muestras_ntry = Entry(config_frame)
        muestras_ntry.grid( row=3, column=1)
        self.muestras_ntry = muestras_ntry

        # Espesor
        Label(config_frame, text="Espesor:").grid(row=4, column=0)
        espesor = Entry(config_frame)
        espesor.grid(row=4,column=1)
        self.espesor = espesor
        
        # Ft
        Label(config_frame, text="Ft:").grid(row=5,column=0)
        ft = Entry(config_frame)
        ft.grid(row=5,column=1)
        self.ft_ntry=ft

        # Fh
        Label(config_frame, text="Fh:").grid(row=6,column=0)
        fh = Entry(config_frame)
        fh.grid(row=6,column=1)
        self.fh_ntry=fh

        # Fc
        Label(config_frame, text="Fc:").grid(row=7,column=0)
        fc = Entry(config_frame)
        fc.grid(row=7,column=1)
        self.fc_ntry=fc

        # Z
        Label(config_frame, text="Z:").grid(row=8,column=0)
        z_ntry = Entry(config_frame)
        z_ntry.grid(row=8,column=1)
        self.z_ntry=z_ntry

        # Nº Ruta
        Label(config_frame, text="Ruta Nº").grid(row=1+1,column=3,sticky="NE")
        ruta_ntry = Entry(config_frame)
        ruta_ntry.grid(row=1+1,column=4,sticky="NE")
        self.ruta_ntry = ruta_ntry

        # Provincia
        Label(config_frame, text="Provincia:").grid(row=2+1,column=3,sticky="NE")
        prov_ntry = Entry(config_frame)
        prov_ntry.grid(row=2+1,column=4,sticky="NE")
        self.prov_ntry = prov_ntry

        # Tramo
        Label(config_frame, text="Tramo:").grid(row=3+1,column=3,sticky="NE")
        tramo_ntry = Entry(config_frame)
        tramo_ntry.grid(row=3+1,column=4,sticky="NE")
        self.tramo_ntry = tramo_ntry

        # Subtramo
        Label(config_frame, text="Subtramo:").grid(row=4+1,column=3,sticky="NE")
        subtramo_ntry = Entry(config_frame)
        subtramo_ntry.grid(row=4+1,column=4,sticky="NE")
        self.subtramo_ntry = subtramo_ntry

        # Tipo de Pavimento
        Label(config_frame, text="Tipo de Pavimento:").grid(row=5+1,column=3,sticky="NE")
        pav_ntry = Entry(config_frame)
        pav_ntry.grid(row=5+1,column=4,sticky="NE")
        self.pav_ntry = pav_ntry

        Button(config_frame, text="Confirmar", command=self.go_to_plot1_from_config).grid(row=9, column=0)

        Button(config_frame, text="Resetear", command=self.reset_all_plots).grid(row=11, column=0)

    def close(self):
        view.temp, view.muestras, view.grupos, view.espesor ,view.ft_ntry, view.fh_ntry, view.fc_ntry, view.z_ntry= self.get_config()
        self.config_frame.grid_forget()
        

    def get_config(self):
        return self.temp_ntry.get(), self.var.get(), self.muestras_ntry.get(), self.espesor.get(), self.ft_ntry.get(), self.fh_ntry.get(), self.fc_ntry.get(), self.z_ntry.get()
    
    def reset(self):
        self.config_frame.destroy()

    def reset_all_plots(self):
        self.view_instance.enqueue_transition('reset_all_plots')