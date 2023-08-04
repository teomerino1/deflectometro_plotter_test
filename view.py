import tkinter as tk
from tkinter import *
from tkinter.ttk import Scrollbar
import threading
from threading import Thread
from tkinter.ttk import Style
import config
import plot
import plot_2
import plot_3
import plot_4
import plot_5
import queue
import time
class View():
    def __init__(self, root,data_instance,reporter_instance):

        self.temp = None
        self.grupos = None
        self.muestras = None
        self.espesor = None
        self.ft_ntry = None
        self.fh_ntry = None
        self.fc_ntry = None
        self.z_ntry = None
        self.data_instance = data_instance
        self.reporter_instance = reporter_instance
        self.data_ready=0
        
        #Se crean los objetos Plot y Config como atributos de view 
        self.Config = config.Config(root,self)
        # self.Plot = plot.Plot(root, self.go_to_config, self.go_to_plot_2_from_plot_1)
        self.Plot = plot.Plot(root, self)
        # self.Plot2 = plot_2.Plot2(root, self.go_to_plot_1_from_plot_2, self.go_to_plot_3_from_plot2)
        self.Plot2 = plot_2.Plot2(root,self)
        # self.Plot3 = plot_3.Plot3(root, self.go_to_plot_2_from_plot_3, self.go_to_plot_4_from_plot_3)
        self.Plot3 = plot_3.Plot3(root,self)
        # self.Plot4 = plot_4.Plot4(root, self.go_to_plot_3_from_plot_4, self.go_to_plot_5_from_plot_4)
        self.Plot4 =plot_4.Plot4(root,self)
        # self.Plot5 = plot_5.Plot5(root,self.go_to_plot_4_from_plot_5)
        self.Plot5= plot_5.Plot5(root,self)
        self.is_plotting = False
        self.first_time_plot=True
        self.first_time_plot2=True
         # Crear una cola bloqueante para las funciones de transición de interfaz
        self.interface_transition_queue = queue.Queue()
        # Crear un solo hilo para ejecutar las funciones de transición de interfaz
        self.interface_transition_thread = threading.Thread(target=self.interface_transition_function)
        self.interface_transition_thread.start()
        self.start(root)

        # self.Plot.show()

     # Metodo que inicializa la view:
    def start(self,root):

        #Se ejecuta el metodo show de Config para que aparezca la ventana principal
        # self.Config.show(a)
        root.title('Deflectómetro')
        root.tk.call("source", "azure.tcl")
        root.tk.call("set_theme", "light")
        style = Style(root)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}")

        ###############################################

        self.Config.show(0)
        self.Config.show(1)
        self.Plot.show(0)
        self.Plot2.show(0)
        self.Plot3.show(0)
        self.Plot4.show(0)
        self.Plot5.show(0)


     # Metodo que borra el frame Config y abre el Plot1
    def go_to_plot1_from_config(self):
        
        self.Config.close()
        self.Plot.show(1)
       
    # Metodo que borra el Plot 1 y abre el de Config
    def go_to_config(self):

        self.Plot.close()
        self.Config.show(1)

    # # Metodo que borra el Plot 1 y abre el Plot 2
    def go_to_plot_2_from_plot_1(self):

        if(self.first_time_plot2):
            self.first_time_plot2=False
            self.Plot.close()
            self.Plot2.show(1)

        else:
            self.Plot.close()
            self.Plot2.show(1)

    # Metodo que borra el Plot 2 y abre el Plot 1
    def go_to_plot_1_from_plot_2(self):

        self.Plot2.close()
        self.Plot.show(1) 

    def go_to_plot_3_from_plot2(self):

        self.Plot2.close()
        self.Plot3.show(1)

    def go_to_plot_2_from_plot_3(self):
        
        self.Plot3.close()
        self.Plot2.show(1)

    def go_to_plot_4_from_plot_3(self):
        
        self.Plot3.close()
        self.Plot4.show(1)

    def go_to_plot_3_from_plot_4(self):

        self.Plot4.close()
        self.Plot3.show(1)

    def go_to_plot_5_from_plot_4(self):

        self.Plot4.close()
        self.Plot5.show(1)

    def go_to_plot_4_from_plot_5(self):

        self.Plot5.close()
        self.Plot4.show(1)

    def reset_all_plots(self):
        self.Plot.reset_table()
        self.Plot.reset()
        self.Plot2.reset()
        self.Plot3.reset()
        self.Plot4.reset()
        self.Plot5.reset()
        # self.Plot.show(0)
        # self.Plot2.show(0)
        # self.Plot3.show(0)
        # self.Plot4.show(0)
        # self.Plot5.show(0)
        
    def reset_all_data(self):
        self.data_instance.reset_all()
        self.reporter_instance.reset_reporter()
        self.temp=None
        self.grupos=None
        self.muestras=None
        self.espesor=None
        self.ft=None
        self.fh=None
        self.fc=None
        self.z=None
        self.set_data_ready(value=0)

    def download_pdf(self):
        self.Plot.generar_pdf()
        
        # self.Plot2.pdf2()
        # self.Plot3.pdf3()
        # self.Plot4.pdf4()


# Metodo que obtiene los datos nuevos y debe mandar a actualizar los ploteos y las estructuras
    def new_group_data_view(self, dict_r, dict_l, defl_r_max, defl_l_max, defl_r_car, defl_l_car):
        self.Plot.new_group_data_plot(dict_r, dict_l)
        self.Plot2.new_group_data_plot2(dict_r,dict_l, defl_r_max, defl_l_max, defl_r_car, defl_l_car)
        self.Plot3.new_group_data_plot3(dict_r,dict_l, defl_r_max, defl_l_max, defl_r_car, defl_l_car)
        self.Plot4.new_group_data_plot4(dict_r, dict_l)

    # Metodo que manda a actualizar el gafico de barras 
    def update_bar_view(self, defl_r,defl_l):
        self.Plot.update_bar_plot(defl_r,defl_l)

    def show_stats_in_plot(self,media_defl_r, media_defl_izq,media_rad_der, media_rad_izq,desv_defl_der, desv_defl_l,coef_var_der,coef_var_izq,defl_car_der,defl_car_izq,rad_car_der,rad_car_izq, d_r_der,d_r_izq ,d_x_r_der, d_x_r_izq, total_mediciones_defl, total_mediciones_rad):
        self.Plot5.grid_stats(media_defl_r, media_defl_izq,media_rad_der, media_rad_izq,desv_defl_der, desv_defl_l,coef_var_der,coef_var_izq,defl_car_der,defl_car_izq,rad_car_der,rad_car_izq, d_r_der,d_r_izq ,d_x_r_der, d_x_r_izq, total_mediciones_defl, total_mediciones_rad)

    def get_config(self):
        return self.Config.get_config()

    def get_params(self):
        return self.Config.get_params()
    
    def on_plot(self):
        return self.is_plotting
    
    def obtain_values(self):
       return self.temp, self.grupos, self.muestras, self.espesor, self.ft_ntry, self.fh_ntry, self.fc_ntry, self.z_ntry

    def set_temp(self,temp):
        self.data_instance.set_temp(temp)
        self.temp=temp

    def get_temp(self):
        return self.temp

    def set_grupos(self,grupos):
        self.grupos=grupos

    def get_grupos(self):
        return self.grupos

    def set_muestras(self,muestras):
        self.muestras=muestras

    def get_muestras(self):
        return self.muestras

    def set_espesor(self,espesor):
        self.data_instance.set_espesor(espesor)
        self.espesor=espesor

    def get_espesor(self):
        return self.espesor

    def set_ft(self,ft):
        self.data_instance.set_ft(ft)
        self.ft_ntry=ft

    def get_ft(self):
        return self.ft_ntry

    def set_fh(self,fh):
        self.data_instance.set_fh(fh)
        self.fh_ntry=fh

    def get_fh(self):
        return self.fh_ntry

    def set_fc(self,fc):
        self.data_instance.set_fc(fc)
        self.fc_ntry=fc

    def get_fc(self):
        return self.fc_ntry
    
    def set_z(self,z):
        self.data_instance.set_z(z)
        self.z_ntry=z 

    def get_z(self):
        return self.z_ntry
    
    def set_data_ready(self,value):
        self.data_ready=value

    def get_data_ready(self):
        return self.data_ready
    
    def interface_transition_function(self):
            while True:
                # Utilizar una cola bloqueante para esperar a que se solicite una función de transición
                target_function = self.interface_transition_queue.get()

                # Ejecutar la función de transición de interfaz correspondiente
                if target_function == 'go_to_config':
                    self.go_to_config()

                if target_function == 'go_to_plot_1_from_config':
                    self.go_to_plot1_from_config()

                elif target_function == 'go_to_plot_2_from_plot_1':
                    self.go_to_plot_2_from_plot_1()
                
                elif target_function == 'go_to_plot_1_from_plot_2':
                    self.go_to_plot_1_from_plot_2()

                elif target_function == 'go_to_plot_3_from_plot_2':
                    self.go_to_plot_3_from_plot2()

                # Agregar más casos para otras funciones de transición...
                elif target_function == 'go_to_plot_2_from_plot_3':
                    self.go_to_plot_2_from_plot_3()

                elif target_function == 'go_to_plot_4_from_plot_3':
                    self.go_to_plot_4_from_plot_3()

                elif target_function == 'go_to_plot_3_from_plot_4':
                    self.go_to_plot_3_from_plot_4()

                elif target_function == 'go_to_plot_5_from_plot_4':
                    self.go_to_plot_5_from_plot_4()

                elif target_function == 'go_to_plot_4_from_plot_5':
                    self.go_to_plot_4_from_plot_5()

                elif target_function == 'reset_all_plots':
                    self.reset_all_plots()
                    self.reset_all_data()

                elif target_function == 'generate_stats':
                    media_defl_r, media_defl_izq,media_rad_der, media_rad_izq,desv_defl_der, desv_defl_l,coef_var_der,coef_var_izq,defl_car_der,defl_car_izq,rad_car_der,rad_car_izq, d_r_der,d_r_izq ,d_x_r_der, d_x_r_izq, total_mediciones_defl, total_mediciones_rad =self.data_instance.calculate_stats()
                    self.show_stats_in_plot(
                        media_defl_r, media_defl_izq,media_rad_der, media_rad_izq,
                        desv_defl_der, desv_defl_l,coef_var_der,coef_var_izq,
                        defl_car_der,defl_car_izq ,rad_car_der, rad_car_izq,
                        d_r_der,d_r_izq,
                        d_x_r_der, d_x_r_izq, 
                        total_mediciones_defl, total_mediciones_rad
                    )
                    # self.set_data_ready(value=0)
                    # self.reset_all_data()
                elif target_function=='download_pdf':
                    self.download_pdf()

                # Indicar que la función se ha procesado y la cola puede esperar nuevamente
                self.interface_transition_queue.task_done()

                # Pequeño descanso entre actualizaciones de la interfaz para no sobrecargar la CPU
                time.sleep(0.2)  # Ajusta el tiempo de sleep según tus necesidades


    def enqueue_transition(self, function_name):
        self.interface_transition_queue.put(function_name)














     
    