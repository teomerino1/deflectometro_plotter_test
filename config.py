import tkinter as tk
from tkinter.ttk import Label, Button, Entry, Radiobutton
import view
from PIL import Image, ImageTk 


class Config():
    def __init__(self, root,view_instance):
        
        self.root = root
        self.config_frame = None
        self.conf_inicial=None
        self.image_label=None
        self.image_infas=None
        self.image_invel=None
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

            # Cargar y mostrar una imagen en un Label
            image_cba = tk.PhotoImage(file="/home/amoyano/Documents/deflectometro_plotter_test/img/Cordoba.png")  # Cambia la ruta a la ubicación de tu imagen
            image_label = Label(config_frame, image=image_cba)
            image_label.image = image_cba  # Importante: mantener una referencia a la imagen
            self.image_label = image_label

            # Cargar y mostrar una imagen en un Label usando Pillow (PIL)
            image_infas = Image.open("/home/amoyano/Documents/deflectometro_plotter_test/img/INFAS.png")
            image_infas = image_infas.resize((298, 110), Image.ANTIALIAS)  # Ajusta el tamaño si es necesario
            photo_infas = ImageTk.PhotoImage(image_infas)
            image_label_infas = Label(config_frame, image=photo_infas)
            image_label_infas.image = photo_infas
            self.image_infas = image_label_infas

            image_invel = Image.open("/home/amoyano/Documents/deflectometro_plotter_test/img/INVEL_va.png") 
            image_invel = image_invel.resize((201, 97), Image.ANTIALIAS) 
            photo_invel = ImageTk.PhotoImage(image_invel)
            image_label_invel = Label(config_frame, image=photo_invel)
            image_label_invel.image = photo_invel  # Importante: mantener una referencia a la imagen
            self.image_invel = image_label_invel
            
            # temp
            temp_label=Label(config_frame, text="Temperatura [ºC]:",font=(None, 15))
            self.temp_label=temp_label
            
            temp_ntry = Entry(config_frame,width=10)
            temp_ntry.insert(0, "20")
            self.temp_ntry = temp_ntry

            # grupos
            grupos_label=Label(config_frame, text="Tamaño de grupos:",font=(None, 15))
            self.grupos_label=grupos_label
            
            var = tk.IntVar()
            var.set(100)
            self.var = var
            grupos_ntry_50 = Radiobutton(config_frame,text='50', variable=var, value=50)
            self.grupos_ntry_50 = grupos_ntry_50

            grupos_ntry_100 = Radiobutton(config_frame,text='100', variable=var, value=100)
            self.grupos_ntry_100 = grupos_ntry_100

            # Muestras
            muestras_label=Label(config_frame, text="Cantidad total de muestras:",font=(None, 15))
            self.muestras_label=muestras_label
           

            muestras_ntry = Entry(config_frame,width=10)
            self.muestras_ntry = muestras_ntry
            
            # Espesor
            espesor_label=Label(config_frame, text="Espesor [mm]:",font=(None, 15))
            self.espesor_label=espesor_label
           
            espesor = Entry(config_frame,width=10)
            self.espesor = espesor

            # Ft
            ft_label=Label(config_frame, text="Ft:",font=(None, 15))
            self.ft_label=ft_label
            
            ft = Entry(config_frame,width=10)
            ft.insert(0, "1") 
            self.ft_ntry=ft
        
            # Fh
            fh_label=Label(config_frame, text="Fh:",font=(None, 15))
            self.fh_label=fh_label

            fh = Entry(config_frame,width=10)
            fh.insert(0, "1")
            self.fh_ntry=fh

            # Fc
            fc_label=Label(config_frame, text="Fc:",font=(None, 15))
            self.fc_label=fc_label
           
            fc = Entry(config_frame,width=10)
            fc.insert(0, "1")
            self.fc_ntry=fc

            # Z
            z_label=Label(config_frame, text="Z:",font=(None, 15))
            self.z_label=z_label
          
            z_ntry = Entry(config_frame,width=10)
            z_ntry.insert(0, "2")
            self.z_ntry=z_ntry

            # Nº Ruta
            ruta_label=Label(config_frame, text="Ruta Nº",font=(None, 15))
            self.rutal_label=ruta_label
        
            ruta_ntry = Entry(config_frame)
            self.ruta_ntry = ruta_ntry

            # Provincia
            prov_label=Label(config_frame, text="Provincia:",font=(None, 15))
            self.prov_label=prov_label

            prov_ntry = Entry(config_frame)
            self.prov_ntry = prov_ntry
            
            # Tramo
            tramo_label=Label(config_frame, text="Tramo:",font=(None, 15))
            self.tramo_label=tramo_label
            
            tramo_ntry = Entry(config_frame)
            self.tramo_ntry = tramo_ntry
          
            # Subtramo
            subtramo_label=Label(config_frame, text="Subtramo:",font=(None, 15))
            self.subtramo_label=subtramo_label
           
            subtramo_ntry = Entry(config_frame)
            self.subtramo_ntry = subtramo_ntry
           
            # Tipo de Pavimento
            pav_label=Label(config_frame, text="Tipo de Pavimento:",font=(None, 15))
            self.pav_label=pav_label
            
            pav_ntry = Entry(config_frame)
            self.pav_ntry = pav_ntry

            confirmar=Button(config_frame, text="Confirmar", command=self.go_to_plot_1_from_config)
            self.confirmar=confirmar

            resetear=Button(config_frame, text="Resetear", command=self.reset_all_plots)
            self.resetear=resetear
           
            resetear_label=Label(config_frame, text="Reset OK!:",font=(None, 15))
            self.resetear_label=resetear_label
            
        if(a==1):

            self.config_frame.grid()
            self.conf_inicial.grid(row=0, column=0, sticky="NW",pady=(10, 0))
            self.temp_label.grid(row=1, column=0,pady=(10, 0))
            self.temp_ntry.grid(row=1, column=1,pady=(10, 0),sticky="nw")
            self.grupos_label.grid(row=2, column=0,pady=(10, 0))
            self.grupos_ntry_50.grid(row=2, column=1,pady=(10, 0))
            self.grupos_ntry_100.grid(row=2, column=2,pady=(10, 0),sticky="NW")
            self.muestras_ntry.grid( row=3, column=1,pady=(10, 0),sticky="nw")
            self.muestras_label.grid(row=3, column=0,pady=(10, 0))
            self.espesor_label.grid(row=4, column=0,pady=(10, 0))
            self.espesor.grid(row=4,column=1,pady=(10, 0))
            self.ft_label.grid(row=5,column=0,pady=(10, 0))
            self.ft_ntry.grid(row=5,column=1,pady=(10, 0),sticky="nw")
            self.fh_ntry.grid(row=6,column=1,pady=(10, 0),sticky="nw")
            self.fh_label.grid(row=6,column=0,pady=(10, 0))
            self.fc_label.grid(row=7,column=0,pady=(10, 0))
            self.fc_ntry.grid(row=7,column=1,pady=(10, 0),sticky="NW")
            self.z_label.grid(row=8,column=0,pady=(10, 0))
            self.z_ntry.grid(row=8,column=1,pady=(10, 0),sticky="nw")
            self.rutal_label.grid(row=1,column=3,sticky="NW",pady=(10, 0))
            self.ruta_ntry.grid(row=1,column=4,sticky="NW",pady=(10, 0))
            self.prov_label.grid(row=2,column=3,sticky="NW",pady=(10, 0))
            self.prov_ntry.grid(row=2,column=4,sticky="NW",pady=(10, 0))
            self.tramo_label.grid(row=3,column=3,sticky="NW",pady=(10, 0))
            self.tramo_ntry.grid(row=3,column=4,sticky="NW",pady=(10, 0))
            self.subtramo_label.grid(row=4,column=3,sticky="NW",pady=(10, 0))
            self.subtramo_ntry.grid(row=4,column=4,sticky="NW",pady=(10, 0))
            self.pav_label.grid(row=5,column=3,sticky="NW",pady=(10, 0))
            self.pav_ntry.grid(row=5,column=4,sticky="NW",pady=(10, 0))
            self.confirmar.grid(row=9, column=0,pady=(10, 0))
            self.resetear.grid(row=11, column=0,pady=(10, 0))
            self.image_label.grid(row=12,column=0,pady=(100, 0))
            self.image_infas.grid(row=12,column=2,pady=(100, 20))
            self.image_invel.grid(row=12,column=4,pady=(100, 20),sticky="SE")
            

    def close(self):

        self.view_instance.set_temp(int(self.temp_ntry.get()))
        
        self.view_instance.set_grupos(int(self.var.get()))

        if(self.espesor.get()==''):
            print("Espesor flaiao")
        else:
            self.view_instance.set_espesor(int(self.espesor.get()))

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

        if(self.muestras_ntry.get()==''):
            self.view_instance.set_muestras(10000)
        else:
            self.view_instance.set_muestras(int(self.muestras_ntry.get()))
        
        self.view_instance.set_data_ready(value=1)

        self.config_frame.grid_forget()

    def get_config(self):
        return self.temp_ntry.get(), self.var.get(), self.muestras_ntry.get(), self.espesor.get(), self.ft_ntry.get(), self.fh_ntry.get(), self.fc_ntry.get(), self.z_ntry.get()
    
    def reset(self):
        self.config_frame.destroy()
        self.show(0)
        self.show(1)

    def reset_all_plots(self):
        self.resetear_label.grid(row=11, column=1)
        self.view_instance.enqueue_transition('reset_all_plots')

    def go_to_plot_1_from_config(self):
        self.resetear_label.grid_forget()
        self.view_instance.enqueue_transition('go_to_plot_1_from_config')