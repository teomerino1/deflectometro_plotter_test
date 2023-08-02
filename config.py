import tkinter as tk
from tkinter.ttk import Label, Button, Entry, Radiobutton
import view


class Config():
    def __init__(self, root,view_instance):
        
        self.root = root
        self.config_frame = None
        self.conf_inicial=None
        self.temp_label=None
        self.temp_ntry = None
        self.grupos_label=None
        self.grupos_ntry_50 = None
        self.grupos_ntry_100 = None
        self.var = None
        self.muestras_label=None
        self.muestras_ntry = None
        self.espesor = None
        self.ft_label=None 
        self.ft_ntry = None
        self.fh_label=None
        self.fh_ntry = None
        self.fc_label=None 
        self.fc_ntry = None
        self.z_label=None
        self.z_ntry = None
        self.rutal_label=None
        self.ruta_ntry = None
        self.prov_label=None
        self.prov_ntry = None
        self.tramo_label=None
        self.tramo_ntry = None
        self.subtramo_label=None
        self.subtramo_ntry = None
        self.pav_label=None
        self.pav_ntry = None
        self.confirmar=None
        self.resetear=None
        self.resetear_label=None
        self.view_instance = view_instance
        # self.go_to_plot1_from_config = go_to_plot1_from_config


    def show(self,a):
        
        if(a==0):
            config_frame = tk.Frame()
            self.config_frame = config_frame
            
            conf_inicial=Label(config_frame, text="Configuración inicial",font=(None, 30))
            self.conf_inicial=conf_inicial
            
            # temp
            temp_label=Label(config_frame, text="Temperatura:")
            self.temp_label=temp_label
            
            temp_ntry = Entry(config_frame)
            self.temp_ntry = temp_ntry

            # grupos
            grupos_label=Label(config_frame, text="Tamaño de grupos:")
            self.grupos_label=grupos_label
            
            var = tk.IntVar()
            self.var = var
            grupos_ntry_50 = Radiobutton(config_frame,text='50', variable=var, value=50)
            self.grupos_ntry_50 = grupos_ntry_50

            grupos_ntry_100 = Radiobutton(config_frame,text='100', variable=var, value=100)
            self.grupos_ntry_100 = grupos_ntry_100

            # Muestras
            muestras_label=Label(config_frame, text="Cantidad total de muestras:")
            self.muestras_label=muestras_label
           

            muestras_ntry = Entry(config_frame)
            self.muestras_ntry = muestras_ntry
            
            # Espesor
            espesor_label=Label(config_frame, text="Espesor:")
            self.espesor_label=espesor_label
           
            espesor = Entry(config_frame)
            self.espesor = espesor

            # Ft
            ft_label=Label(config_frame, text="Ft:")
            self.ft_label=ft_label
            
            ft = Entry(config_frame)
            self.ft_ntry=ft
        
            # Fh
            fh_label=Label(config_frame, text="Fh:")
            self.fh_label=fh_label

            fh = Entry(config_frame)
            self.fh_ntry=fh

            # Fc
            fc_label=Label(config_frame, text="Fc:")
            self.fc_label=fc_label
           
            fc = Entry(config_frame)
            self.fc_ntry=fc

            # Z
            z_label=Label(config_frame, text="Z:")
            self.z_label=z_label
          
            z_ntry = Entry(config_frame)
            self.z_ntry=z_ntry

            # Nº Ruta
            ruta_label=Label(config_frame, text="Ruta Nº")
            self.rutal_label=ruta_label
        
            ruta_ntry = Entry(config_frame)
            self.ruta_ntry = ruta_ntry

            # Provincia
            prov_label=Label(config_frame, text="Provincia:")
            self.prov_label=prov_label

            prov_ntry = Entry(config_frame)
            self.prov_ntry = prov_ntry
            
            # Tramo
            tramo_label=Label(config_frame, text="Tramo:")
            self.tramo_label=tramo_label
            
            tramo_ntry = Entry(config_frame)
            self.tramo_ntry = tramo_ntry
          
            # Subtramo
            subtramo_label=Label(config_frame, text="Subtramo:")
            self.subtramo_label=subtramo_label
           
            subtramo_ntry = Entry(config_frame)
            self.subtramo_ntry = subtramo_ntry
           
            # Tipo de Pavimento
            pav_label=Label(config_frame, text="Tipo de Pavimento:")
            self.pav_label=pav_label
            
            pav_ntry = Entry(config_frame)
            self.pav_ntry = pav_ntry

            confirmar=Button(config_frame, text="Confirmar", command=self.go_to_plot_1_from_config)
            self.confirmar=confirmar

            resetear=Button(config_frame, text="Resetear", command=self.reset_all_plots)
            self.resetear=resetear
           
            resetear_label=Label(config_frame, text="Reset OK!:")
            self.resetear_label=resetear_label
            
        if(a==1):

            self.config_frame.grid_rowconfigure(0, weight=1)
            self.config_frame.grid_rowconfigure(1, weight=1)
            self.config_frame.grid_rowconfigure(2, weight=1)
            self.config_frame.grid_rowconfigure(3, weight=1)
            self.config_frame.grid_rowconfigure(4, weight=1)

            # config_frame.grid_rowconfigure(4, weight=1)
            self.config_frame.grid_columnconfigure(0, weight=1)
            self.config_frame.grid_columnconfigure(1, weight=1)
            self.config_frame.grid_columnconfigure(2, weight=1)
            self.config_frame.grid_columnconfigure(3, weight=1)
            self.config_frame.grid_columnconfigure(4, weight=1)

            self.config_frame.grid(ipadx=3, ipady=2)

            self.conf_inicial.grid(row=0, column=3, sticky="N")
            self.temp_label.grid(row=1, column=0)
            self.temp_ntry.grid(row=1, column=1)
            self.grupos_label.grid(row=2, column=0)
            self.grupos_ntry_50.grid(row=2, column=1)
            self.grupos_ntry_100.grid(row=2, column=2)
            self.muestras_ntry.grid( row=3, column=1)
            self.muestras_label.grid(row=3, column=0)
            self.espesor_label.grid(row=4, column=0)
            self.espesor.grid(row=4,column=1)
            self.ft_label.grid(row=5,column=0)
            self.ft_ntry.grid(row=5,column=1)
            self.fh_ntry.grid(row=6,column=1)
            self.fh_label.grid(row=6,column=0)
            self.fc_label.grid(row=7,column=0)
            self.fc_ntry.grid(row=7,column=1)
            self.z_label.grid(row=8,column=0)
            self.z_ntry.grid(row=8,column=1)
            self.rutal_label.grid(row=1+1,column=3,sticky="NE")
            self.ruta_ntry.grid(row=1+1,column=4,sticky="NE")
            self.prov_label.grid(row=2+1,column=3,sticky="NE")
            self.prov_ntry.grid(row=2+1,column=4,sticky="NE")
            self.tramo_label.grid(row=3+1,column=3,sticky="NE")
            self.tramo_ntry.grid(row=3+1,column=4,sticky="NE")
            self.subtramo_label.grid(row=4+1,column=3,sticky="NE")
            self.subtramo_ntry.grid(row=4+1,column=4,sticky="NE")
            self.pav_label.grid(row=5+1,column=3,sticky="NE")
            self.pav_ntry.grid(row=5+1,column=4,sticky="NE")
            self.confirmar.grid(row=9, column=0)
            self.resetear.grid(row=11, column=0)

    def close(self):

        self.view_instance.set_temp(int(self.temp_ntry.get()))
        self.view_instance.set_espesor(int(self.espesor.get()))
        self.view_instance.set_grupos(int(self.var.get()))

        if(self.ft_ntry.get()==''):
            self.view_instance.set_ft(1)
        else:
            self.view_instance.set_ft(int(self.ft_ntry.get()))

        if(self.fh_ntry.get()==''):
            self.view_instance.set_fh(1)
        else:
            self.view_instance.set_fh(int(self.fh_ntry.get()))

        if(self.fc_ntry.get()==''):
            self.view_instance.set_fc(1)
        else:
            self.view_instance.set_fc(int(self.fc_ntry.get()))

        if(self.z_ntry.get()==''):
            self.view_instance.set_z(2)
        else:
            self.view_instance.set_z(int(self.z_ntry.get()))

        
        
        # self.view_instance.set_muestras(int(self.muestras_ntry.get()))
        
        self.view_instance.set_data_ready(value=1)

        self.temp_ntry.delete(0,tk.END)
        self.espesor.delete(0,tk.END)
        self.ft_ntry.delete(0,tk.END)
        self.fh_ntry.delete(0,tk.END)
        self.fc_ntry.delete(0,tk.END)
        self.z_ntry.delete(0,tk.END)
        
        self.config_frame.grid_forget()

    def get_config(self):
        return self.temp_ntry.get(), self.var.get(), self.muestras_ntry.get(), self.espesor.get(), self.ft_ntry.get(), self.fh_ntry.get(), self.fc_ntry.get(), self.z_ntry.get()
    
    def reset(self):
        self.config_frame.destroy()

    def reset_all_plots(self):
        self.resetear_label.grid(row=11, column=1)
        self.view_instance.enqueue_transition('reset_all_plots')

    def go_to_plot_1_from_config(self):
        self.resetear_label.grid_forget()
        self.view_instance.enqueue_transition('go_to_plot_1_from_config')