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


# Clase correspondiente a la vista encargada de mostrar los datos y graficos

class Plot5():
    def __init__(self,root,view_instance):

        self.root = root
        # self.main_plot_frame = None
        # self.second_plot_frame = None
        self.sixth_plot_frame = None
        self.title = None
        self.back = None  
        # self.go_to_plot_4_from_plot_5 = go_to_plot_4_from_plot_5
        self.view_instance = view_instance
        self.Graphs2 = None

        self.huella_ext = None  
        self.defl_media_der = None
        self.desv_std_der = None
        self.coef_var_der = None
        self.defl_car_der = None
        self.total_med_defl_der = None
        self.radio_med_der = None
        self.radio_car_der = None
        self.total_med_rad_der = None
        self.d_r_med_der = None
        self.r_x_d_der = None
        ##############
        self.whitespace = None 
        ##############
        self.huella_int = None
        self.defl_media_izq = None
        self.desv_std_izq = None
        self.coef_var_izq = None
        self.defl_car_izq = None
        self.total_med_defl_izq = None
        self.radio_med_izq = None
        self.radio_car_izq = None
        self.total_med_rad_izq = None
        self.d_r_med_izq = None
        self.r_x_d_izq = None

    # Metodo que elimina todo lo que muestra la pagina
    def close(self):

        self.sixth_plot_frame.grid_forget()


    def show(self,a):
       
        if(a == 0):

            width = self.root.winfo_screenwidth()

            height = self.root.winfo_screenheight()

            sixth_plot_frame = Frame(self.root, width=width, height=height)

            self.sixth_plot_frame = sixth_plot_frame

            title = Label(sixth_plot_frame, text="Plantilla de resultados estadísticos",font=(None, 30)) 

            self.title = title

            back = Button(sixth_plot_frame, text="Atrás", command=self.go_to_plot_4_from_plot_5)

            self.back = back

            huella_ext = Label(sixth_plot_frame, text="HUELLA EXTERNA (DERECHA)",font=(None, 20))

            self.huella_ext = huella_ext

            defl_media_der = Label(sixth_plot_frame, text="Deflexion media:",font=(None, 15))

            self.defl_media_der = defl_media_der

            desv_std_der = Label(sixth_plot_frame, text="Desviacion Standart:",font=(None, 15))

            self.desv_std_der = desv_std_der
            
            coef_var_der = Label(sixth_plot_frame, text="Coeficiente de variacion:",font=(None, 15))

            self.coef_var_der = coef_var_der
            
            defl_car_der = Label(sixth_plot_frame, text="Deflexion caracteristica:",font=(None, 15))

            self.defl_car_der = defl_car_der
            
            total_med_defl_der = Label(sixth_plot_frame, text="Total de mediciones:",font=(None, 15))

            self.total_med_defl_der = total_med_defl_der
            
            radio_med_der = Label(sixth_plot_frame, text="Radio Medio:",font=(None, 15))

            self.radio_med_der = radio_med_der
            
            radio_car_der = Label(sixth_plot_frame, text="Radio Caracteristico:",font=(None, 15))

            self.radio_car_der = radio_car_der
            
            total_med_rad_der = Label(sixth_plot_frame, text="Total de Mediciones:",font=(None, 15))
        
            self.total_med_rad_der = total_med_rad_der
            
            d_r_med_der = Label(sixth_plot_frame, text="(D / R) Medio:",font=(None, 15))
        
            self.d_r_med_der = d_r_med_der
            
            r_x_d_der = Label(sixth_plot_frame, text="(R x D) Medio:",font=(None, 15))
        
            self.r_x_d_der = r_x_d_der

            ################################################################################################################
            whitespace = Label(sixth_plot_frame, text="          ",font=(None, 15))

            self.whitespace = whitespace
            ################################################################################################################

            huella_int = Label(sixth_plot_frame, text="HUELLA INTERNA (INTERNA)",font=(None, 20))

            self.huella_int = huella_int

            defl_media_izq = Label(sixth_plot_frame, text="Deflexion media:",font=(None, 15))

            self.defl_media_izq = defl_media_izq
            
            desv_std_izq = Label(sixth_plot_frame, text="Desviacion Standart:",font=(None, 15))

            self.desv_std_izq = desv_std_izq
            
            coef_var_izq = Label(sixth_plot_frame, text="Coeficiente de variacion:",font=(None, 15))

            self.coef_var_izq = coef_var_izq
            
            defl_car_izq = Label(sixth_plot_frame, text="Deflexion caracteristica:",font=(None, 15))

            self.defl_car_izq = defl_car_izq
            
            total_med_defl_izq = Label(sixth_plot_frame, text="Total de mediciones:",font=(None, 15))

            self.total_med_defl_izq = total_med_defl_izq
            
            radio_med_izq = Label(sixth_plot_frame, text="Radio Medio:",font=(None, 15))

            self.radio_med_izq = radio_med_izq
            
            radio_car_izq = Label(sixth_plot_frame, text="Radio Caracteristico:",font=(None, 15))

            self.radio_car_izq = radio_car_izq
            
            total_med_rad_izq = Label(sixth_plot_frame, text="Total de Mediciones:",font=(None, 15))
        
            self.total_med_rad_izq = total_med_rad_izq
            
            d_r_med_izq = Label(sixth_plot_frame, text="(D / R) Medio:",font=(None, 15))
        
            self.d_r_med_izq = d_r_med_izq
            
            r_x_d_izq = Label(sixth_plot_frame, text="(R x D) Medio:",font=(None, 15))
        
            self.r_x_d_izq = r_x_d_izq

        if(a == 1):

            self.sixth_plot_frame.grid(rowspan=3,columnspan=3)

            self.title.grid(row = 0, column = 0,sticky=NW)

            self.back.grid(row=1, column=0,sticky=NW)

            self.huella_ext.grid(row=2+1, column=0,sticky=NW)

            self.defl_media_der.grid(row=3+1, column=0,sticky=NW)

            self.desv_std_der.grid(row=4+1, column=0,sticky=NW)

            self.coef_var_der.grid(row=5+1, column=0,sticky=NW)

            self.defl_car_der.grid(row=6+1, column=0,sticky=NW)

            self.total_med_defl_der.grid(row=7+1, column=0,sticky=NW)

            self.radio_med_der.grid(row=8+1, column=0,sticky=NW)

            self.radio_car_der.grid(row=9+1, column=0,sticky=NW)

            self.total_med_rad_der.grid(row=10+1, column=0,sticky=NW)

            self.d_r_med_der.grid(row=11+1, column=0,sticky=NW)

            self.r_x_d_der.grid(row=12+1, column=0,sticky=NW)

            self.whitespace.grid(row=12+2, column=0,sticky=NW)

            self.huella_int.grid(row=13+2, column=0,sticky=NW)
            
            self.defl_media_izq.grid(row=14+2, column=0,sticky=NW)

            self.desv_std_izq.grid(row=15+2, column=0,sticky=NW)

            self.coef_var_izq.grid(row=16+2, column=0,sticky=NW)

            self.defl_car_izq.grid(row=17+2, column=0,sticky=NW)

            self.total_med_defl_izq.grid(row=18+2, column=0,sticky=NW)

            self.radio_med_izq.grid(row=19+2, column=0,sticky=NW)

            self.radio_car_izq.grid(row=20+2, column=0,sticky=NW)

            self.total_med_rad_izq.grid(row=21+2, column=0,sticky=NW)

            self.d_r_med_izq.grid(row=22+2, column=0,sticky=NW)

            self.r_x_d_izq.grid(row=23+2, column=0,sticky=NW)

    def go_to_plot_4_from_plot_5(self):
        self.view_instance.enqueue_transition('go_to_plot_4_from_plot_5')

            

