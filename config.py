import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Label, Button, Entry, Radiobutton,Frame
import view
from PIL import Image, ImageTk 
from tkinter import font
from reportlab.pdfgen import canvas
from tkinter import messagebox

"""
Clase Config:
    Esta clase muestra la interfaz de la configuración inicial.
    Contiene todos los objetos que se muestran en dicha interfaz
    como los textos, inputs del usuario e imágenes. 
"""
class Config():
    def __init__(self, root,view_instance):
        
        self.root = root
        self.config_frame = None
        self.title_frame=None
        self.parameters_frame=None
        self.reportes_frame=None
        self.botones_frame=None
        self.info_infas_frame=None
        self.imagenes_frame=None
        self.conf_inicial=None
        self.parametros_medicion=None
        self.info_reporte=None
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
        self.operador_ntry=None
        self.operador_label=None
        self.chofer_ntry=None
        self.chofer_label=None
        self.apoyo_ntry=None
        self.apoyo_label=None
        self.confirmar=None
        self.resetear=None
        self.resetear_label=None
        self.whatsapp_label=None
        self.email_label=None
        self.web_label=None
        self.view_instance = view_instance


    """
    Esta función se llama cuando se accede o se instancia la interfaz.

    @params a: Si a es 0, se instancia la clase por lo que se crean todos los objetos.
                Si a es 1, se accede a la interfaz por lo que se muestran los objetos creados.         
    """
    def show(self,a):
        
        if(a==0):
          
            width = self.root.winfo_screenwidth()
            height = self.root.winfo_screenheight()
            
            config_frame = Frame(self.root,width=width,height=height)
            self.config_frame = config_frame
            
            custom_font = font.Font(family="Krona_One", size=16, weight="bold")
            
            parameters_frame=Frame(config_frame,relief="groove")
            self.parameters_frame=parameters_frame
    
            reportes_frame=Frame(config_frame,relief="groove")
            self.reportes_frame=reportes_frame

            botones_frame=Frame(config_frame)
            self.botones_frame=botones_frame

            info_infas_frame=Frame(config_frame,relief="groove")
            self.info_infas_frame=info_infas_frame

            imagenes_frame=Frame(config_frame,relief='groove')
            self.imagenes_frame=imagenes_frame

            #Configuracion
            conf_inicial = ttk.Label(self.config_frame, text="Configuración", font=(custom_font,25))
            self.conf_inicial = conf_inicial

            parametros_medicion=Label(self.parameters_frame, text="Parámetros de medición",font=("Krona One", 20))
            self.parametros_medicion=parametros_medicion

            info_reporte=Label(self.reportes_frame, text="Información de Reporte",font=(None, 20))
            self.info_reporte=info_reporte

            #Temperatura
            temp_label=Label(self.parameters_frame, text="Temperatura [ºC]:",font=(None, 15))
            self.temp_label=temp_label
            
            temp_ntry = Entry(self.parameters_frame,width=10)
            temp_ntry.insert(0, "20")
            self.temp_ntry = temp_ntry

            #Grupos (por defecto en 100)
            grupos_label=Label(self.parameters_frame, text="Tamaño de grupos:",font=(None, 15))
            self.grupos_label=grupos_label
            
            var = tk.IntVar()
            var.set(100)
            self.var = var
            grupos_ntry_50 = Radiobutton(self.parameters_frame,text='50', variable=var, value=50)
            self.grupos_ntry_50 = grupos_ntry_50

            grupos_ntry_100 = Radiobutton(self.parameters_frame,text='100', variable=var, value=100)
            self.grupos_ntry_100 = grupos_ntry_100

            #Muestras
            muestras_label=Label(self.parameters_frame, text="Cantidad de muestras (opcional):",font=(None, 15))
            self.muestras_label=muestras_label
           
            muestras_ntry = Entry(self.parameters_frame,width=10)
            self.muestras_ntry = muestras_ntry
            
            # Espesor
            espesor_label=Label(self.parameters_frame, text="Espesor [cm]:",font=(None, 15))
            self.espesor_label=espesor_label
           
            espesor = Entry(self.parameters_frame,width=10)
            self.espesor = espesor

            # Ft (por defecto en 1)
            ft_label=Label(self.parameters_frame, text="Ft:",font=(None, 15))
            self.ft_label=ft_label
            
            ft = Entry(self.parameters_frame,width=10)
            ft.insert(0, "1") 
            self.ft_ntry=ft
        
            # Fh (por defecto en 1)
            fh_label=Label(self.parameters_frame, text="Fh:",font=(None, 15))
            self.fh_label=fh_label

            fh = Entry(self.parameters_frame,width=10)
            fh.insert(0, "1")
            self.fh_ntry=fh

            # Fc (por defecto en 1)
            fc_label=Label(self.parameters_frame, text="Fc:",font=(None, 15))
            self.fc_label=fc_label
           
            fc = Entry(self.parameters_frame,width=10)
            fc.insert(0, "1")
            self.fc_ntry=fc

            # Z (por defecto en 1)
            z_label=Label(self.parameters_frame, text="Z:",font=(None, 15))
            self.z_label=z_label
          
            z_ntry = Entry(self.parameters_frame,width=10)
            z_ntry.insert(0, "2")
            self.z_ntry=z_ntry

            # Nº Ruta
            ruta_label=Label(self.reportes_frame, text="Ruta Nº",font=(None, 15))
            self.rutal_label=ruta_label
        
            ruta_ntry = Entry(self.reportes_frame)
            self.ruta_ntry = ruta_ntry

            # Provincia
            prov_label=Label(self.reportes_frame, text="Provincia:",font=(None, 15))
            self.prov_label=prov_label

            prov_ntry = Entry(self.reportes_frame)
            self.prov_ntry = prov_ntry
            
            # Tramo
            tramo_label=Label(self.reportes_frame, text="Tramo:",font=(None, 15))
            self.tramo_label=tramo_label
            
            tramo_ntry = Entry(self.reportes_frame)
            self.tramo_ntry = tramo_ntry
          
            # Subtramo
            subtramo_label=Label(self.reportes_frame, text="Subtramo:",font=(None, 15))
            self.subtramo_label=subtramo_label
           
            subtramo_ntry = Entry(self.reportes_frame)
            self.subtramo_ntry = subtramo_ntry
           
            # Tipo de Pavimento
            pav_label=Label(self.reportes_frame, text="Tipo de Pavimento:",font=(None, 15))
            self.pav_label=pav_label
            
            pav_ntry = Entry(self.reportes_frame)
            self.pav_ntry = pav_ntry

            #Operador
            operador_label=Label(self.reportes_frame, text="Operador:",font=(None, 15))
            self.operador_label=operador_label

            operador_ntry=Entry(self.reportes_frame)
            self.operador_ntry=operador_ntry

            #Chofer
            chofer_label=Label(self.reportes_frame, text="Chofer:",font=(None, 15))
            self.chofer_label=chofer_label

            chofer_ntry=Entry(self.reportes_frame)
            self.chofer_ntry=chofer_ntry

            #Apoyo
            apoyo_label=Label(self.reportes_frame, text="Apoyo:",font=(None, 15))
            self.apoyo_label=apoyo_label
            
            apoyo_ntry=Entry(self.reportes_frame)
            self.apoyo_ntry=apoyo_ntry
          
            #Confirmar
            confirmar = ttk.Button(self.botones_frame, text="Confirmar", command=self.go_to_plot_1_from_config,
            style="TButton")
            self.confirmar=confirmar
              
            #Resetear
            resetear=Button(self.botones_frame, text="Resetear", command=self.reset_all_plots)
            self.resetear=resetear
           
            original_image=Image.open("image.png")
            screen_width = self.root.winfo_screenwidth()

            #Imagen
            desired_width = screen_width
            aspect_ratio = original_image.width / original_image.height
            height=245
            resized_image = original_image.resize((desired_width, height))
            self.image_cba = ImageTk.PhotoImage(resized_image)
            self.image_label = Label(self.imagenes_frame, image=self.image_cba)
            self.image_label.image = self.image_cba
    
        if(a==1):

            self.config_frame.grid(columnspan=2)
            self.conf_inicial.grid(row=0, columnspan=2,padx=(0,0),pady=(0,5))
            self.parameters_frame.grid(row=1,column=0,padx=(0,600),pady=(0,0))
            self.reportes_frame.grid(row=1,column=0,padx=(600,0),pady=(0,0))
            self.botones_frame.grid(row=2,columnspan=2,padx=(0,0),pady=(0,0))
            self.imagenes_frame.grid(row=3,pady=(0,0),padx=(0,0))
            self.imagenes_frame.grid_rowconfigure(0, weight=1)
            self.imagenes_frame.grid_columnconfigure(0, weight=1)
  
            self.parametros_medicion.grid(row=1,column=0,padx=(50,0),pady=(10, 0))

            self.temp_label.grid(row=2, column=0,padx=(50,0),pady=(10, 0),sticky="NW")
            self.temp_ntry.grid(row=2, column=0,padx=(350,0),pady=(10, 0))

            self.grupos_label.grid(row=3, column=0,padx=(50,0),pady=(10, 0),sticky="NW")
            self.grupos_ntry_50.grid(row=3, column=0,padx=(350,0),pady=(10, 0),sticky="nw")
            self.grupos_ntry_100.grid(row=3, column=0,padx=(400,20),pady=(10,0),sticky="NW")

            self.muestras_label.grid(row=4, column=0,padx=(50,0),pady=(10, 0),sticky="NW")
            self.muestras_ntry.grid( row=4, column=0,padx=(350,0),pady=(10, 0))

            self.espesor_label.grid(row=5, column=0,padx=(50,0),pady=(10, 0),sticky="NW")
            self.espesor.grid(row=5,column=0,padx=(350,0),pady=(10, 0))

            self.ft_label.grid(row=6,column=0,padx=(50,0),pady=(10, 0),sticky="NW")
            self.ft_ntry.grid(row=6,column=0,padx=(350,0),pady=(10, 0))

            self.fh_label.grid(row=7,column=0,padx=(50,0),pady=(10, 0),sticky="NW")
            self.fh_ntry.grid(row=7,column=0,padx=(350,0),pady=(10, 0))
            
            self.fc_label.grid(row=8,column=0,padx=(50,0),pady=(10, 0),sticky="NW")
            self.fc_ntry.grid(row=8,column=0,padx=(350,0),pady=(10, 0))

            self.z_label.grid(row=9,column=0,padx=(50,0),pady=(10, 0),sticky="NW")
            self.z_ntry.grid(row=9,column=0,padx=(350,0),pady=(10, 10))

            self.info_reporte.grid(row=0,column=0,padx=(30,0),pady=(5, 0))

            self.rutal_label.grid(row=1,column=0,padx=(50,0),pady=(10, 0),sticky="NW")
            self.ruta_ntry.grid(row=1,column=0,padx=(350,10),pady=(10, 0))

            self.prov_label.grid(row=2,column=0,padx=(50,0),pady=(10, 0),sticky="NW")
            self.prov_ntry.grid(row=2,column=0,padx=(350,10),pady=(10, 0))

            self.tramo_label.grid(row=3,column=0,padx=(50,0),pady=(10, 0),sticky="NW")
            self.tramo_ntry.grid(row=3,column=0,padx=(350,10),pady=(10, 0))
            
            self.subtramo_label.grid(row=4,column=0,padx=(50,0),pady=(10, 0),sticky="NW")
            self.subtramo_ntry.grid(row=4,column=0,padx=(350,10),pady=(10, 0))

            self.pav_label.grid(row=5,column=0,padx=(50,0),pady=(10, 0),sticky="NW")
            self.pav_ntry.grid(row=5,column=0,padx=(350,10),pady=(10, 0))

            self.operador_label.grid(row=6,column=0,padx=(50,0),pady=(10, 0),sticky="NW")
            self.operador_ntry.grid(row=6,column=0,padx=(350,10),pady=(10, 0))

            self.chofer_label.grid(row=7,column=0,padx=(50,0),pady=(10, 0),sticky="NW")
            self.chofer_ntry.grid(row=7,column=0,padx=(350,10),pady=(10, 0))

            self.apoyo_label.grid(row=8,column=0,padx=(50,0),pady=(10, 0),sticky="NW")
            self.apoyo_ntry.grid(row=8,column=0,padx=(350,10),pady=(10, 10))

            self.confirmar.grid(row=0, column=0,pady=(10,0),padx=(0,30))
            self.resetear.grid(row=1, column=0,pady=(0,0),padx=(0,30))

            self.image_label.grid(row=0,column=0,columnspan=2,padx=(0,0),pady=(0,0))
           
    """
    Est método se llama cuando se cierra esta interfaz.
    Corrobora que todos los parámetros hayan sido completados correctamente.
    @return: 
        0 Si todos los parámetros están correctos
        1 Si hay algún error 
    """
    def close(self):

        text_fields = [
        self.temp_ntry,
        self.apoyo_ntry,
        self.chofer_ntry,
        self.ruta_ntry,
        self.subtramo_ntry,
        self.tramo_ntry,
        self.operador_ntry,
        self.espesor,
        self.fc_ntry,
        self.fh_ntry,
        self.ft_ntry,
        self.z_ntry
        ]

        values = [
            self.temp_ntry,
            self.espesor,
            self.fc_ntry,
            self.fh_ntry,
            self.ft_ntry,
            self.z_ntry,
        ]

        for text_field in text_fields:
            if text_field.get() == '':
                messagebox.showwarning("Aviso", "Deben llenarse todos los campos de texto antes de continuar")
                return 1

        for value in values:
            try:
                float_value = float(value.get())
            except ValueError:
                messagebox.showwarning("Aviso", "Los parámetros deben ser enteros o flotantes")
                return 1

        if(self.muestras_ntry.get()==''):
            self.view_instance.set_muestras(1000000)
        else:
            self.view_instance.set_muestras(int(self.muestras_ntry.get()))

        self.view_instance.set_temp(int(self.temp_ntry.get()))
        self.view_instance.set_grupos(int(self.var.get()))
        self.view_instance.set_espesor(float(self.espesor.get()))
        self.view_instance.set_ft(float(self.ft_ntry.get()))
        self.view_instance.set_fh(float(self.fh_ntry.get()))
        self.view_instance.set_fc(float(self.fc_ntry.get()))
        self.view_instance.set_z(float(self.z_ntry.get()))
        self.view_instance.set_ruta(self.ruta_ntry.get())
        self.view_instance.set_provincia(self.prov_ntry.get())
        self.view_instance.set_tramo(self.tramo_ntry.get())
        self.view_instance.set_subtramo(self.subtramo_ntry.get())
        self.view_instance.set_pavimento(self.pav_ntry.get())
        self.view_instance.set_chofer(self.chofer_ntry.get())
        self.view_instance.set_operador(self.operador_ntry.get())
        self.view_instance.set_apoyo(self.apoyo_ntry.get())
        self.view_instance.set_data_ready(value=1)
        self.config_frame.grid_forget()
        
        return 0

    #TODO-> CORROBORAR SI ESTE MÉTODO NO SE USA. EN ESE CASO, BORRARLO.
    def get_config(self):
        return self.temp_ntry.get(), self.var.get(), self.muestras_ntry.get(), self.espesor.get(), self.ft_ntry.get(), self.fh_ntry.get(), self.fc_ntry.get(), self.z_ntry.get()
    
    """
    Este método se llama cuando hay un reset.
    Destruye el frame principal de la interfaz y todo lo que contiene
    """
    def reset(self):
        self.config_frame.destroy()


    
    #TODO-> VERIFICAR SI ESTE MÉTODO SE USA. SI NO SE USA, BORRARLO.
    def reset_all_plots(self):
        data=[
            self.apoyo_ntry,
            self.chofer_ntry,
            self.espesor,
            self.fc_ntry,
            self.fh_ntry,
            self.ft_ntry,
            self.pav_ntry,
            self.prov_ntry,
            self.ruta_ntry,
            self.subtramo_ntry,
            self.tramo_ntry,
            self.z_ntry,
            self.operador_ntry
            ]
        for data in data:
            if(data.get()==''):
                messagebox.showwarning("Aviso","No están todos los campos completos.")
                return
            else:
                self.view_instance.enqueue_transition('reset_all_plots')

    """
    Este método se llama cuando se quiere avanzar hacia
    la interfaz del plot1. Encola la función correspondiente.
    """
    def go_to_plot_1_from_config(self):
        self.view_instance.enqueue_transition('go_to_plot_1_from_config')