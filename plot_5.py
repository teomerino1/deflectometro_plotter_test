from tkinter import *
from tkinter.ttk import Label, Frame, Button, Scrollbar
from tkinter.ttk import Treeview

from tkinter import ttk
from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Spacer, Image, Paragraph
from reportlab.lib import utils
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Image, Spacer
from reportlab.lib.pagesizes import letter,A4
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, PageTemplate,Image, Spacer
from reportlab.lib import utils
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk


# Clase correspondiente a la vista encargada de mostrar los datos y graficos

class Plot5():
    def __init__(self,root,view_instance):

        self.root = root
        self.sixth_plot_frame = None
        self.state_frame=None
        self.state_label=None
        self.state=None
        self.title_frame=None
        self.subtitle_frame=None
        self.labels_frame=None
        self.botones_frame=None
        self.title = None
        self.back = None
        self.stats = None 
        self.pdf = None 
        self.view_instance = view_instance
        self.Graphs2 = None

        self.huella_ext = None 

        self.defl_media_der = None
        self.defl_media_der_value = None

        self.desv_std_der = None
        self.desv_std_der_value=None

        self.coef_var_der = None
        self.coef_var_der_value=None

        self.defl_car_der = None
        self.defl_car_der_value=None

        self.total_med_defl_der = None
        self.total_med_defl_der_value=None

        self.radio_med_der = None
        self.radio_med_der_value=None

        self.radio_car_der = None
        self.radio_car_der_value=None

        self.total_med_rad_der = None
        self.total_med_rad_der_value=None
        
        self.d_r_med_der = None
        self.d_r_med_der_value=None

        self.r_x_d_der = None
        self.r_x_d_der_value=None
        ##############
        self.whitespace = None 
        ##############

        self.huella_int = None
        self.huella_int_value=None

        self.defl_media_izq = None
        self.defl_media_izq_value=None

        self.desv_std_izq = None
        self.desv_std_izq_value=None

        self.coef_var_izq = None
        self.coef_var_izq_value=None

        self.defl_car_izq = None
        self.defl_car_izq_value=None

        self.total_med_defl_izq = None
        self.total_med_defl_izq_value=None

        self.radio_med_izq = None
        self.radio_med_izq_value=None

        self.radio_car_izq = None
        self.radio_car_izq_value=None

        self.total_med_rad_izq = None
        self.total_med_rad_izq_value=None

        self.d_r_med_izq = None
        self.d_r_med_izq_value=None

        self.r_x_d_izq = None
        self.r_x_d_izq_value=None

        self.ruta=None

        self.imagen_frame=None
        self.image_cba=None
        self.image_label=None

    # Metodo que elimina todo lo que muestra la pagina
    def close(self):
        self.sixth_plot_frame.grid_forget()

    def reset(self):
        self.sixth_plot_frame.destroy()
        self.show(0)

    def show(self,a):
       
        if(a == 0):

            width = self.root.winfo_screenwidth()
            height = self.root.winfo_screenheight()

            sixth_plot_frame = Frame(self.root, width=width, height=height,background='#F6F4F2')
            self.sixth_plot_frame = sixth_plot_frame

            title_frame=Frame(self.sixth_plot_frame,background='#F6F4F2')
            self.title_frame=title_frame

            subtitle_frame=Frame(self.sixth_plot_frame,background='#F6F4F2')
            self.subtitle_frame=subtitle_frame

            labels_frame=Frame(self.sixth_plot_frame,background='#F6F4F2')
            self.labels_frame=labels_frame

            botones_frame=Frame(self.sixth_plot_frame,background='#F6F4F2')
            self.botones_frame=botones_frame

            state_label=Label(self.sixth_plot_frame,text="Test",font=(None,15),background='#F6F4F2',foreground='#66A7EF')
            self.state_label=state_label

            imagen_frame=Frame(self.sixth_plot_frame)
            self.imagen_frame=imagen_frame

            title = Label(self.title_frame, text="PLANILLA GENERAL DE RESULTADOS ESTADISTICOS",font=(None, 25),background='#F6F4F2',foreground='#625651') 
            self.title = title

            back = ttk.Button(self.sixth_plot_frame, text="Atrás", command=self.go_to_plot_4_from_plot_5,style="TButton")
            self.back = back
            
            stats = ttk.Button(self.botones_frame, text="Generar Cálculos", command=self.generate_stats,style="TButton")
            self.stats = stats

            pdf = ttk.Button(self.botones_frame, text="Descargar PDF", command=self.download_pdf,style="TButton")
            self.pdf = pdf

            huella_ext = Label(self.labels_frame, text="HUELLA EXTERNA (DERECHA)",font=(None, 18),background='#F6F4F2',foreground='#625651')
            self.huella_ext = huella_ext

            defl_media_der = Label(self.labels_frame, text="Deflexion media:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.defl_media_der = defl_media_der
           
            desv_std_der = Label(self.labels_frame, text="Desviacion Standart:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.desv_std_der = desv_std_der
            
            coef_var_der = Label(self.labels_frame, text="Coeficiente de variacion:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.coef_var_der = coef_var_der

            defl_car_der = Label(self.labels_frame, text="Deflexion caracteristica:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.defl_car_der = defl_car_der
            
            total_med_defl_der = Label(self.labels_frame, text="Total de mediciones:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.total_med_defl_der = total_med_defl_der
            
            radio_med_der = Label(self.labels_frame, text="Radio Medio:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.radio_med_der = radio_med_der
            
            radio_car_der = Label(self.labels_frame, text="Radio Caracteristico:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.radio_car_der = radio_car_der
            
            total_med_rad_der = Label(self.labels_frame, text="Total de Mediciones:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.total_med_rad_der = total_med_rad_der
            
            d_r_med_der = Label(self.labels_frame, text="(D / R) Medio:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.d_r_med_der = d_r_med_der
            
            r_x_d_der = Label(self.labels_frame, text="(R x D) Medio:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.r_x_d_der = r_x_d_der

            ################################################################################################################
            whitespace = Label(self.labels_frame, text="          ",font=(None, 15))
            self.whitespace = whitespace
            ################################################################################################################

            huella_int = Label(self.labels_frame, text="HUELLA INTERNA (IZQUIERDA)",font=(None, 18),background='#F6F4F2',foreground='#625651')
            self.huella_int = huella_int

            defl_media_izq = Label(self.labels_frame, text="Deflexion media:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.defl_media_izq = defl_media_izq
            
            desv_std_izq = Label(self.labels_frame, text="Desviacion Standart:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.desv_std_izq = desv_std_izq
            
            coef_var_izq = Label(self.labels_frame, text="Coeficiente de variacion:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.coef_var_izq = coef_var_izq
            
            defl_car_izq = Label(self.labels_frame, text="Deflexion caracteristica:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.defl_car_izq = defl_car_izq
            
            total_med_defl_izq = Label(self.labels_frame, text="Total de mediciones:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.total_med_defl_izq = total_med_defl_izq
            
            radio_med_izq = Label(self.labels_frame, text="Radio Medio:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.radio_med_izq = radio_med_izq
            
            radio_car_izq = Label(self.labels_frame, text="Radio Caracteristico:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.radio_car_izq = radio_car_izq
            
            total_med_rad_izq = Label(self.labels_frame, text="Total de Mediciones:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.total_med_rad_izq = total_med_rad_izq
            
            d_r_med_izq = Label(self.labels_frame, text="(D / R) Medio:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.d_r_med_izq = d_r_med_izq
            
            r_x_d_izq = Label(self.labels_frame, text="(R x D) Medio:",font=(None, 14),background='#F6F4F2',foreground='#625651')
            self.r_x_d_izq = r_x_d_izq

            original_image=Image.open("image.png")
            screen_width = self.root.winfo_screenwidth()

            # Redimensiona la imagen al ancho de la pantalla y ajusta la altura proporcionalmente
            desired_width = screen_width
            aspect_ratio = original_image.width / original_image.height
            height=235
            desired_height = int(desired_width / aspect_ratio)
            resized_image = original_image.resize((desired_width, height), Image.ANTIALIAS)
            # Convierte la imagen redimensionada a un objeto PhotoImage
            self.image_cba = ImageTk.PhotoImage(resized_image)
            self.image_label = Label(self.imagen_frame, image=self.image_cba)
            self.image_label.image = self.image_cba
            

        if(a == 1):

            self.sixth_plot_frame.grid(sticky="nsew")
            self.back.grid(row=0, column=0,sticky=NW)
            self.state_label.grid(row=0,column=0,padx=(0,900))
            self.title_frame.grid(row=1,columnspan=2,padx=(0,0),pady=(0,10))
            self.title.grid(row=0, column=0,padx=(0,0))

            self.labels_frame.grid(row=2,columnspan=2,pady=(0,10))
            self.huella_ext.grid(row=0,column=0,padx=(0,150))
            self.huella_int.grid(row=0,column=1,padx=(150,0))
            
            self.defl_media_der.grid(row=1, column=0,sticky=NW,pady=(0,5))
            self.desv_std_der.grid(row=2,sticky=NW,pady=(0,5))
            self.coef_var_der.grid(row=3, column=0,sticky=NW,pady=(0,5))
            self.defl_car_der.grid(row=4, column=0,sticky=NW,pady=(0,5))
            self.total_med_defl_der.grid(row=5, column=0,sticky=NW,pady=(0,5))
            self.radio_med_der.grid(row=6, column=0,sticky=NW,pady=(0,5))
            self.radio_car_der.grid(row=7, column=0,sticky=NW,pady=(0,5))
            self.total_med_rad_der.grid(row=8, column=0,sticky=NW,pady=(0,5))
            self.d_r_med_der.grid(row=9, column=0,sticky=NW,pady=(0,5))
            self.r_x_d_der.grid(row=10, column=0,sticky=NW,pady=(0,5))

            # # self.whitespace.grid(row=12+2, column=0,sticky=NW)
            
            self.defl_media_izq.grid(row=1, column=1,padx=(150,0),sticky=NW,pady=(0,5))
            self.desv_std_izq.grid(row=2, column=1,padx=(150,0),sticky=NW,pady=(0,5))
            self.coef_var_izq.grid(row=3, column=1,padx=(150,0),sticky=NW,pady=(0,5))
            self.defl_car_izq.grid(row=4, column=1,padx=(150,0),sticky=NW,pady=(0,5))
            self.total_med_defl_izq.grid(row=5, column=1,padx=(150,0),sticky=NW,pady=(0,5))
            self.radio_med_izq.grid(row=6, column=1,padx=(150,0),sticky=NW,pady=(0,5))
            self.radio_car_izq.grid(row=7, column=1,padx=(150,0),sticky=NW,pady=(0,5))
            self.total_med_rad_izq.grid(row=8, column=1,padx=(150,0),sticky=NW,pady=(0,5))
            self.d_r_med_izq.grid(row=9, column=1,padx=(150,0),sticky=NW,pady=(0,5))
            self.r_x_d_izq.grid(row=10, column=1,padx=(150,0),sticky=NW,pady=(0,5))

            self.botones_frame.grid(row=3,columnspan=2,pady=(0,0))
            self.stats.grid(row=0,pady=(0,0))
            self.pdf.grid(row=1,pady=(0,0))
            self.imagen_frame.grid(row=4,padx=(0,30),pady=(0,0))
            self.image_label.grid(row=0,columnspan=2,padx=(0,0))
    

    def grid_stats(self,media_defl_r, media_defl_izq,media_rad_der, media_rad_izq,desv_defl_der, desv_defl_l,coef_var_der,coef_var_izq,defl_car_der,defl_car_izq,rad_car_der,rad_car_izq, d_r_der,d_r_izq ,d_x_r_der, d_x_r_izq, total_mediciones_defl, total_mediciones_rad):
        
        defl_media_der_value=Label(self.labels_frame, text=media_defl_r,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.defl_media_der_value=defl_media_der_value
        self.defl_media_der_value.grid(row=1, column=0,padx=(0,0),pady=(10,0),sticky=NE)

        radio_med_der_value=Label(self.labels_frame, text=media_rad_der,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.radio_med_der_value=radio_med_der_value
        self.radio_med_der_value.grid(row=2, column=0,padx=(0,0),pady=(10,0),sticky=NE)
        
        desv_std_der_value=Label(self.labels_frame, text=desv_defl_der,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.desv_std_der_value=desv_std_der_value
        self.desv_std_der_value.grid(row=3, column=0,padx=(0,0),pady=(10,0),sticky=NE)

        coef_var_der_value=Label(self.labels_frame, text=coef_var_der,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.coef_var_der_value=coef_var_der_value
        self.coef_var_der_value.grid(row=4, column=0,padx=(0,0),pady=(10,0),sticky=NE)

        defl_car_der_value=Label(self.labels_frame, text=defl_car_der,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.defl_car_der_value=defl_car_der_value
        self.defl_car_der_value.grid(row=5, column=0,padx=(0,0),pady=(10,0),sticky=NE)

        radio_car_der_value=Label(self.labels_frame, text=rad_car_der,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.radio_car_der_value=radio_car_der_value
        self.radio_car_der_value.grid(row=6, column=0,padx=(0,0),pady=(10,0),sticky=NE)

        d_r_med_der_value=Label(self.labels_frame, text=d_r_der,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.d_r_med_der_value=d_r_med_der_value
        self.d_r_med_der_value.grid(row=7, column=0,padx=(0,0),pady=(10,0),sticky=NE)

        r_x_d_der_value=Label(self.labels_frame, text=d_x_r_der,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.r_x_d_der_value=r_x_d_der_value
        self.r_x_d_der_value.grid(row=8, column=0,padx=(0,0),pady=(10,0),sticky=NE)

        total_med_defl_der_value=Label(self.labels_frame, text=total_mediciones_defl,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.total_med_defl_der_value=total_med_defl_der_value
        self.total_med_defl_der_value.grid(row=9, column=0,padx=(0,0),pady=(10,0),sticky=NE)

        total_med_rad_der_value=Label(self.labels_frame, text=total_mediciones_rad,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.total_med_rad_der_value=total_med_rad_der_value
        self.total_med_rad_der_value.grid(row=10, column=0,padx=(0,0),pady=(10,0),sticky=NE)

        defl_media_izq_value=Label(self.labels_frame, text=media_defl_izq,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.defl_media_izq_value=defl_media_izq_value
        self.defl_media_izq_value.grid(row=1, column=1,padx=(0,0),pady=(10,0),sticky=NE)

        radio_med_izq_value=Label(self.labels_frame, text=media_rad_izq,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.radio_med_izq_value=radio_med_izq_value
        self.radio_med_izq_value.grid(row=2, column=1,padx=(0,0),pady=(10,0),sticky=NE)

        desv_std_izq_value=Label(self.labels_frame, text=desv_defl_l,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.desv_std_izq_value=desv_std_izq_value
        self.desv_std_izq_value.grid(row=3, column=1,padx=(0,0),pady=(10,0),sticky=NE)

        coef_var_izq_value=Label(self.labels_frame, text=coef_var_izq,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.coef_var_izq_value=coef_var_izq_value
        self.coef_var_izq_value.grid(row=4, column=1,padx=(0,0),pady=(10,0),sticky=NE)
        
        defl_car_izq_value=Label(self.labels_frame, text=defl_car_izq,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.defl_car_izq_value=defl_car_izq_value
        self.defl_car_izq_value.grid(row=5, column=1,padx=(0,0),pady=(10,0),sticky=NE)

        radio_car_izq_value=Label(self.labels_frame, text=rad_car_izq,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.radio_car_izq_value=radio_car_izq_value
        self.radio_car_izq_value.grid(row=6, column=1,padx=(0,0),pady=(10,0),sticky=NE)

        d_r_med_izq_value=Label(self.labels_frame, text=d_r_izq,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.d_r_med_izq_value=d_r_med_izq_value
        self.d_r_med_izq_value.grid(row=7, column=1,padx=(0,0),pady=(10,0),sticky=NE)

        r_x_d_izq_value=Label(self.labels_frame, text=d_x_r_izq,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.r_x_d_izq_value=r_x_d_izq_value
        self.r_x_d_izq_value.grid(row=8, column=1,padx=(0,0),pady=(10,0),sticky=NE)

        total_med_defl_izq_value=Label(self.labels_frame, text=total_mediciones_defl,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.total_med_defl_izq_value=total_med_defl_izq_value
        self.total_med_defl_izq_value.grid(row=9, column=1,padx=(0,0),pady=(10,0),sticky=NE)

        total_med_rad_izq_value=Label(self.labels_frame, text=total_mediciones_rad,font=(None, 10),background='#F6F4F2',foreground='#625651')
        self.total_med_rad_izq_value=total_med_rad_izq_value
        self.total_med_rad_izq_value.grid(row=10, column=1,padx=(0,0),pady=(10,0),sticky=NE)

    def go_to_plot_4_from_plot_5(self):
        self.view_instance.enqueue_transition('go_to_plot_4_from_plot_5')

    def generate_stats(self):
        self.view_instance.set_state("Generando cálculos")
        self.view_instance.enqueue_transition('generate_stats')

    def download_pdf(self):
        self.view_instance.set_state("Descargando PDF...")
        self.view_instance.enqueue_transition('download_pdf')

    def set_ruta(self,ruta):
        self.ruta=ruta

    def get_ruta(self):
        return self.ruta
    
    def get_state_label(self):
        return self.state_label

    def download_stats(self):
        # Crear el buffer para el PDF usando ReportLab
        if(self.defl_car_der_value==None):
            print("Me doy cuenta q es noneing")
            return 
    
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)

        title0 = Paragraph("DEFLECTOGRAFO LACROIX",ParagraphStyle(name='CenterStyle', alignment=1, fontSize=25))
        title1 = Paragraph("PLANTILLA GENERAL DE RESULTADOS",ParagraphStyle(name='CenterStyle', alignment=1, fontSize=20))
        title2 = Paragraph("ESTADISTICOS",ParagraphStyle(name='CenterStyle', alignment=1, fontSize=20))
        title3 = Paragraph(f"Ruta: {self.get_ruta()}", ParagraphStyle(name='CenterStyle', alignment=1, fontSize=15))

        elements = []
        elements.append(title0)
        elements.append(Spacer(1,20))
        elements.append(title1)
        elements.append(Spacer(1,10))
        elements.append(title2)
        elements.append(Spacer(1,20))
        elements.append(title3)
        elements.append(Spacer(1,20))

        labels_der = [
            self.defl_media_der, self.desv_std_der, 
            self.coef_var_der, self.defl_car_der, self.total_med_defl_der, 
            self.radio_med_der, self.radio_car_der, self.total_med_rad_der, 
            self.d_r_med_der, self.r_x_d_der 
        ]
        
        labels_izq= [
            self.defl_media_izq, self.desv_std_izq, 
            self.coef_var_izq, self.defl_car_izq, self.total_med_defl_izq,
            self.radio_med_izq, self.radio_car_izq, self.total_med_rad_izq, 
            self.d_r_med_izq, self.r_x_d_izq
        ]

        labels_der_values=[
            self.defl_media_der_value, self.desv_std_der_value, 
            self.coef_var_der_value, self.defl_car_der_value, self.total_med_defl_der_value, 
            self.radio_med_der_value, self.radio_car_der_value, self.total_med_rad_der_value, 
            self.d_r_med_der_value, self.r_x_d_der_value 
        ]

        labels_izq_values= [
            self.defl_media_izq_value, self.desv_std_izq_value, 
            self.coef_var_izq_value, self.defl_car_izq_value, self.total_med_defl_izq_value,
            self.radio_med_izq_value, self.radio_car_izq_value, self.total_med_rad_izq_value, 
            self.d_r_med_izq_value, self.r_x_d_izq_value
        ]

        # Agregar los primeros elementos individuales
        tabla_der = [[self.huella_ext.cget("text")]]
        tabla_izq = [[self.huella_int.cget("text")]]
        
        for label, value in zip(labels_der, labels_der_values):
            tabla_der.append([label.cget("text"), value.cget("text")])
        
        for label, value in zip(labels_izq, labels_izq_values):
            tabla_izq.append([label.cget("text"), value.cget("text")])

        table_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                  ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                  # ... otros estilos de tabla ...
                                  ])

        table_der = Table(tabla_der, colWidths=[200, 200], rowHeights=25)
        table_der.setStyle(table_style)
        elements.append(table_der)

        table_izq = Table(tabla_izq, colWidths=[200, 200], rowHeights=25)
        table_izq.setStyle(table_style)
        elements.append(table_izq)

        doc.build(elements)

        buffer.seek(0)

        with open("pdf5.pdf", "wb") as f:
            f.write(buffer.read())




  