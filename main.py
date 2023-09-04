import view
import tkinter as tk
from tkinter import ttk
import data
import reporter
from threading import Thread
import threading
from ttkthemes import ThemedTk
from tkinter import *
from time import sleep


def show_stats(View,Data):
    View.enqueue_transition('generate_stats')

def update_all(Data,View,grupos):
    Data.update_structures()
    dict_r, dict_l = Data.get_data_dict()
    defl_l_max, defl_r_max = Data.get_max_defl()
    defl_l_car, defl_r_car = Data.get_car_defl()
    View.new_group_data_view(dict_r,dict_l,defl_r_car,defl_l_car,defl_r_max,defl_l_max,grupos)

def update_defl_one(Data,View,amount):
    defl_r, defl_l = Data.update_bar_data(amount)
    View.update_bar_view(defl_r,defl_l)
    Data.clear_bar_data()

def obtain_data(Reporter, View, Data):
    View.set_state("Listo para obtener datos")
    while True:
        if(View.get_data_ready()==1):
            break
        else: 
            continue
    process_data(Reporter,View,Data)

def process_data(Reporter,View,Data):
    Reporter.start()
    grupos=View.get_grupos()
    muestras=View.get_muestras()
    print("Muestras:",muestras)
    print("Grupos:",grupos)
    a=0
    b=0
    View.set_state("Listo para obtener datos")
    c=0
    while True:
             
        data, this_cycle = Reporter.get_new_measurements()
        
        if data is None or this_cycle is None:
            if(Reporter.get_puesto_change()==1 or a==muestras or View.get_reset()==1):

                if(a==muestras):
                    View.set_state("Detenido, cantidad de muestras alcanzada.")
               
                print("Vuelvo a empezar")
                View.set_reset(0)
                View.set_data_ready(value=0)
                sleep(1)
                obtain_data(Reporter,View,Data)
            else:
                continue
        if(c==0):
            c=1
            View.set_state("Obteniendo datos...")
            View.set_hora_inicio()
            View.set_nro_puesto(Reporter.get_last_puesto())

        Data.data_destruct(data)
        cantidad=Data.cant_mediciones()
        a=a+1
        print(cantidad)
        
        if(Reporter.get_puesto_change()==0):
            if(a>=100):
                b=b+1
                if(b==10):
                    b=0
                    update_bar_thread = Thread(target=update_defl_one,args=(Data,View,10))
                    update_bar_thread.daemon=True
                    update_bar_thread.start()
            else:
                # View.set_state("Graficando bars...")
                update_bar_thread = Thread(target=update_defl_one,args=(Data,View,1))
                update_bar_thread.daemon=True
                update_bar_thread.start()

            if(cantidad%5 == 0):
                View.set_state("Graficando el grupo...")
                update_all_thread = Thread(target=update_all,args=(Data,View,grupos))
                update_all_thread.daemon=True 
                update_all_thread.start()
                View.set_state("Obteniendo datos...")
            
def obtain_and_process_data(Reporter, View, Data):
    while True:
        if View.get_data_ready() == 1:
            process_data(Reporter, View, Data)

def main():

 
    root=ThemedTk(theme='radiance')
    root.set_theme_advanced('radiance',hue=0.1)
    Reporter = reporter.Reporter()
    Data = data.Data()
    View = view.View(root,Data,Reporter)
    
    # Crear y ejecutar el hilo para procesar los datos
    View.set_state("En configuración")
    data_thread = Thread(target=obtain_data, args=(Reporter, View, Data))
    data_thread.daemon = True
    data_thread.start()
    print("Soy el hilo:",threading.get_ident(), "En el main")

    
    root.mainloop()

if __name__ == "__main__":
    main()