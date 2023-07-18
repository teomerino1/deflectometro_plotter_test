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
class View():
    def __init__(self, root):

        # variable globales
        global temp
        global grupos
        global muestras
        global espesor 
        global fh_ntry
        global ft_ntry 
        global fc_ntry
        global z_ntry
    
        temp = None
        grupos = None
        muestras = None
        espesor = None
        ft_ntry = None
        fh_ntry = None
        fc_ntry = None
        z_ntry = None
        
        #Se crean los objetos Plot y Config como atributos de view 
        self.Config = config.Config(root, self.go_to_plot1_from_config)

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
        
        self.start(root)

        self.first_time_plot=True
        
        self.first_time_plot2=True

         # Crear una cola bloqueante para las funciones de transición de interfaz
        self.interface_transition_queue = queue.Queue()

        # Crear un solo hilo para ejecutar las funciones de transición de interfaz
        self.interface_transition_thread = threading.Thread(target=self.interface_transition_function)
        self.interface_transition_thread.start()
       

        # self.Plot.show()

     # Metodo que inicializa la view:
    def start(self,root):

        #Se ejecuta el metodo show de Config para que aparezca la ventana principal
        self.Config.show()

        root.title('Deflectómetro')

        root.tk.call("source", "azure.tcl")

        root.tk.call("set_theme", "light")

        style = Style(root)

        screen_width = root.winfo_screenwidth()

        screen_height = root.winfo_screenheight()

        root.geometry(f"{screen_width}x{screen_height}")

        ###############################################

        self.Plot.show(0)

        self.Plot2.show(0)

        self.Plot3.show(0)

        self.Plot4.show(0)

        self.Plot5.show(0)


     # Metodo que borra el frame Config y abre el Plot1
    def go_to_plot1_from_config(self):

        self.is_plotting = True

        if(self.first_time_plot):

            self.first_time_plot=False

            self.Config.close()

            self.Plot.show(1)

            self.Plot2.show(0)

        else:

            self.Config.close()

            self.Plot.show(1)

    # Metodo que borra el Plot 1 y abre el de Config
    def go_to_config(self):

        self.Plot.close()

        self.Config.show()

    # def go_to_config(self):
    #     def thread_funcion():
    #         self.Plot.close()

    #         self.Config.show()

    #     thread= threading.Thread(target=thread_funcion)
    #     thread.start()

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

# Metodo que obtiene los datos nuevos y debe mandar a actualizar los ploteos y las estructuras
    def new_group_data_view(self, dict_r, dict_l, defl_r_max, defl_l_max, defl_r_car, defl_l_car):

        self.Plot.new_group_data_plot(dict_r, dict_l)

        self.Plot2.new_group_data_plot2(dict_r,dict_l, defl_r_max, defl_l_max, defl_r_car, defl_l_car)

        self.Plot3.new_group_data_plot3(dict_r,dict_l, defl_r_max, defl_l_max, defl_r_car, defl_l_car)

        self.Plot4.new_group_data_plot4(dict_r, dict_l)

        

    # Metodo que manda a actualizar el gafico de barras 
    def update_bar_view(self, defl_left_right_dict):

        self.Plot.update_bar_plot(defl_left_right_dict)

    def get_config(self):
        return self.Config.get_config()

    def get_params(self):
        return self.Config.get_params()
    
    def on_plot(self):
        return self.is_plotting
    


    def interface_transition_function(self):
            while True:
                # Utilizar una cola bloqueante para esperar a que se solicite una función de transición
                target_function = self.interface_transition_queue.get()

                # Ejecutar la función de transición de interfaz correspondiente
                if target_function == 'go_to_config':
                    self.go_to_config()

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

                # Indicar que la función se ha procesado y la cola puede esperar nuevamente
                self.interface_transition_queue.task_done()

    def enqueue_transition(self, function_name):
        self.interface_transition_queue.put(function_name)





















# import tkinter as tk
# from tkinter import *
# from tkinter.ttk import Scrollbar
# import threading
# from threading import Thread
# from tkinter.ttk import Style
# import config
# import plot
# import plot_2
# import plot_3
# import plot_4
# import plot_5

# class View():
#     def __init__(self, root):

#         # variable globales
#         global temp
#         global grupos
#         global muestras
#         global espesor 
#         global fh_ntry
#         global ft_ntry 
#         global fc_ntry
#         global z_ntry
    
#         temp = None
#         grupos = None
#         muestras = None
#         espesor = None
#         ft_ntry = None
#         fh_ntry = None
#         fc_ntry = None
#         z_ntry = None
        
#         #Se crean los objetos Plot y Config como atributos de view 
#         self.Config = config.Config(root, self.go_to_plot1_from_config)

#         self.Plot = plot.Plot(root, self.go_to_config, self.go_to_plot_2_from_plot_1)

#         self.Plot2 = plot_2.Plot2(root, self.go_to_plot_1_from_plot_2, self.go_to_plot_3_from_plot2)

#         self.Plot3 = plot_3.Plot3(root, self.go_to_plot_2_from_plot_3, self.go_to_plot_4_from_plot_3)

#         self.Plot4 = plot_4.Plot4(root, self.go_to_plot_3_from_plot_4, self.go_to_plot_5_from_plot_4)

#         self.Plot5 = plot_5.Plot5(root,self.go_to_plot_4_from_plot_5)

#         self.is_plotting = False
        
#         self.start(root)

#         self.first_time_plot=True
        
#         self.first_time_plot2=True
       

#         # self.Plot.show()

#      # Metodo que inicializa la view:
#     def start(self,root):

#         #Se ejecuta el metodo show de Config para que aparezca la ventana principal
#         self.Config.show()

#         root.title('Deflectómetro')

#         root.tk.call("source", "azure.tcl")

#         root.tk.call("set_theme", "light")

#         style = Style(root)

#         screen_width = root.winfo_screenwidth()

#         screen_height = root.winfo_screenheight()

#         root.geometry(f"{screen_width}x{screen_height}")

#         ###############################################

#         self.Plot.show(0)

#         self.Plot2.show(0)

#         self.Plot3.show(0)

#         self.Plot4.show(0)

#         self.Plot5.show(0)


#      # Metodo que borra el frame Config y abre el Plot1
#     def go_to_plot1_from_config(self):

#         self.is_plotting = True

#         if(self.first_time_plot):

#             self.first_time_plot=False

#             self.Config.close()

#             self.Plot.show(1)

#             self.Plot2.show(0)

#         else:

#             self.Config.close()

#             self.Plot.show(1)


    
       

#     # Metodo que borra el Plot 1 y abre el de Config
#     def go_to_config(self):

#         self.Plot.close()

#         self.Config.show()

#     # def go_to_config(self):
#     #     def thread_funcion():
#     #         self.Plot.close()

#     #         self.Config.show()

#     #     thread= threading.Thread(target=thread_funcion)
#     #     thread.start()

#     # # Metodo que borra el Plot 1 y abre el Plot 2
#     def go_to_plot_2_from_plot_1(self):

#         if(self.first_time_plot2):

#             self.first_time_plot2=False

#             self.Plot.close()

#             self.Plot2.show(1)

#         else:

#             self.Plot.close()

#             self.Plot2.show(1)


#     # # Metodo que borra el Plot 1 y abre el Plot 2
#     # def go_to_plot_2_from_plot_1(self):
#     #     def thread_funcion():

#     #         if(self.first_time_plot2):

#     #             self.first_time_plot2=False

#     #             self.Plot.close()

#     #             self.Plot2.show(1)

#     #         else:

#     #             self.Plot.close()

#     #             self.Plot2.show(1)
#     #     thread= threading.Thread(target=thread_funcion)
#     #     thread.start()

    

#     # Metodo que borra el Plot 2 y abre el Plot 1
#     def go_to_plot_1_from_plot_2(self):

#         self.Plot2.close()

#         self.Plot.show(1)

#     #  # Metodo que borra el Plot 2 y abre el Plot 1
#     # def go_to_plot_1_from_plot_2(self):
#     #     def thread_funcion():
#     #         self.Plot2.close()

#     #         self.Plot.show(1)
#     #     thread=threading.Thread(target=thread_funcion)
#     #     thread.start()
        

#     def go_to_plot_3_from_plot2(self):

#         self.Plot2.close()

#         self.Plot3.show(1)

#     # def go_to_plot_3_from_plot2(self):
#     #     def thread_function():

#     #         self.Plot2.close()

#     #         self.Plot3.show(1)
#     #     thread=threading.Thread(target=thread_function)
#     #     thread.start()


#     def go_to_plot_2_from_plot_3(self):
        
#         self.Plot3.close()
       
#         self.Plot2.show(1)

#     # def go_to_plot_2_from_plot_3(self):
#     #     def thread_function():
#     #         self.Plot3.close()
        
#     #         self.Plot2.show(1)
#     #     thread=threading.Thread(target=thread_function)
#     #     thread.start()



#     def go_to_plot_4_from_plot_3(self):
        
#         self.Plot3.close()

#         self.Plot4.show(1)

#     # def go_to_plot_4_from_plot_3(self):
#     #     def thread_function():
#     #         self.Plot3.close()

#     #         self.Plot4.show(1)
#     #     thread=threading.Thread(target=thread_function)
#     #     thread.start()
        
#     def go_to_plot_3_from_plot_4(self):

#         self.Plot4.close()

#         self.Plot3.show(1)

#     # def go_to_plot_3_from_plot_4(self):
#     #     def thread_function():
#     #         self.Plot4.close()

#     #         self.Plot3.show(1)
#     #     thread=threading.Thread(target=thread_function)
#     #     thread.start()


#     def go_to_plot_5_from_plot_4(self):

#         self.Plot4.close()

#         self.Plot5.show(1)

        
#     # def go_to_plot_5_from_plot_4(self):
#     #     def thread_function():
#     #         self.Plot4.close()

#     #         self.Plot5.show(1)
#     #     thread=threading.Thread(target=thread_function)
#     #     thread.start()

#     def go_to_plot_4_from_plot_5(self):

#         self.Plot5.close()

#         self.Plot4.show(1)

    # def go_to_plot_4_from_plot_5(self):
    #     def thread_function():
    #         self.Plot5.close()

    #         self.Plot4.show(1)
    #     thread=threading.Thread(target=thread_function)
    #     thread.start()
     
    