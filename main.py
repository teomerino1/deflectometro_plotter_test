import view
import tkinter as tk
import data
import reporter
from threading import Thread
import threading
from time import sleep


def show_stats(Data,View):
    media_defl_r, media_defl_izq,media_rad_der, media_rad_izq,desv_defl_der, desv_defl_l,coef_var_der,coef_var_izq,defl_car_der,defl_car_izq,rad_car_der,rad_car_izq, d_r_der,d_r_izq ,d_x_r_der, d_x_r_izq, total_mediciones_defl, total_mediciones_rad =Data.calculate_stats()
    View.show_stats_in_plot(
        media_defl_r, media_defl_izq,media_rad_der, media_rad_izq,
        desv_defl_der, desv_defl_l,coef_var_der,coef_var_izq,
        defl_car_der,defl_car_izq ,rad_car_der, rad_car_izq,
        d_r_der,d_r_izq,
        d_x_r_der, d_x_r_izq, 
        total_mediciones_defl, total_mediciones_rad
    )
    View.reset_all_data()

def update_all(Data,View):
    Data.update_structures()
    dict_r, dict_l = Data.get_data_dict()
    defl_l_max, defl_r_max = Data.get_max_defl()
    defl_l_car, defl_r_car = Data.get_std_defl()
    View.new_group_data_view(dict_r,dict_l,defl_l_max,defl_r_max,defl_l_car,defl_r_car)

def update_defl(Data,View):
    defl_r, defl_l = Data.update_bar_data()
    # indexes= Data.get_indexes()
    View.update_bar_view(defl_r,defl_l)
    Data.clear_bar_data()


def obtain_data(Reporter, View, Data):

    Reporter.reset_reporter()
    Data.reset_all()

    print("Estoy en obtain data")
    while True:
        if(View.get_data_ready()==1):
            break
        else: 
            continue
    process_data(Reporter,View,Data)


def process_data(Reporter,View,Data):
    print("Estoy en process data")
    Reporter.start()
    while True:
        data, this_cycle = Reporter.get_new_measurements()
        
        if data is None or this_cycle is None:
            if(Reporter.get_puesto_change()==1):
                # View.enqueue_transition('generate_stats')
                show_stats_thread = Thread(target=show_stats,args=(Data,View))
                show_stats_thread.daemon=True
                show_stats_thread.start()
                sleep(2)
                obtain_data(Reporter,View,Data)
            else:
                continue

        Data.data_destruct(data)
        cantidad=Data.cant_mediciones()
        print(cantidad)
        
        if(Reporter.get_puesto_change()==0):

            print("Get puesto change:",Reporter.get_puesto_change())

            if(cantidad%6 == 0):
                
                update_bar_thread = Thread(target=update_defl,args=(Data,View))
                update_bar_thread.daemon=True
                update_bar_thread.start()

            if(cantidad% 10 == 0):
                
                update_all_thread = Thread(target=update_all,args=(Data,View))
                update_all_thread.daemon=True 
                update_all_thread.start()
            
        
        

        
def main():
    root = tk.Tk()

    Reporter = reporter.Reporter()
    Data = data.Data()

    View = view.View(root,Data,Reporter)
    
    # Crear y ejecutar el hilo para procesar los datos
    data_thread = Thread(target=obtain_data, args=(Reporter, View, Data))
    data_thread.daemon = True
    data_thread.start()
    
    # Ejecutar el bucle principal de la interfaz gráfica
    root.mainloop()

if __name__ == "__main__":
    main()