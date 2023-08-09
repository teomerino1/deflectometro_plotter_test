import view
import tkinter as tk
import data
import reporter
from threading import Thread
import threading
from time import sleep


def show_stats(View,Data):
    # media_defl_r, media_defl_izq,media_rad_der, media_rad_izq,desv_defl_der, desv_defl_l,coef_var_der,coef_var_izq,defl_car_der,defl_car_izq,rad_car_der,rad_car_izq, d_r_der,d_r_izq ,d_x_r_der, d_x_r_izq, total_mediciones_defl, total_mediciones_rad =Data.calculate_stats()
    # View.show_stats_in_plot(
    #     media_defl_r, media_defl_izq,media_rad_der, media_rad_izq,
    #     desv_defl_der, desv_defl_l,coef_var_der,coef_var_izq,
    #     defl_car_der,defl_car_izq ,rad_car_der, rad_car_izq,
    #     d_r_der,d_r_izq,
    #     d_x_r_der, d_x_r_izq, 
    #     total_mediciones_defl, total_mediciones_rad
    # )
    # View.reset_all_data()
    View.enqueue_transition('generate_stats')

def update_all(Data,View,grupos):
    Data.update_structures()
    dict_r, dict_l = Data.get_data_dict()
    defl_l_max, defl_r_max = Data.get_max_defl()
    defl_l_car, defl_r_car = Data.get_std_defl()
    View.new_group_data_view(dict_r,dict_l,defl_l_max,defl_r_max,defl_l_car,defl_r_car,grupos)

def update_defl_one(Data,View,amount):
    defl_r, defl_l = Data.update_bar_data(amount)
    # indexes= Data.get_indexes()
    View.update_bar_view(defl_r,defl_l)
    Data.clear_bar_data()


def obtain_data(Reporter, View, Data):

    # Reporter.reset_reporter()
    # Data.reset_all()

    # print("Estoy en obtain data")
    while True:
        if(View.get_data_ready()==1):
            break
        else: 
            continue
    process_data(Reporter,View,Data)


def process_data(Reporter,View,Data):
    # print("Estoy en process data")
    Reporter.start()
    grupos=View.get_grupos()
    muestras=View.get_muestras()
    print("Muestras:",muestras)
    print("Grupos:",grupos)
    a=0
    b=0
    while True:
        data, this_cycle = Reporter.get_new_measurements()
        
        if data is None or this_cycle is None:
            if(Reporter.get_puesto_change()==1 or a==muestras):
                # View.enqueue_transition('generate_stats')
                # show_stats_thread = Thread(target=show_stats,args=(View,Data))
                # show_stats_thread.daemon=True
                # show_stats_thread.start()
                print("Vuelvo a empezar")
                View.set_data_ready(value=0)
                sleep(1)
                obtain_data(Reporter,View,Data)
            else:
                continue

        Data.data_destruct(data)
        cantidad=Data.cant_mediciones()
        a=a+1
        print(cantidad)
        
        if(Reporter.get_puesto_change()==0):

            if(a>=100):
                b=b+1
                if(b==10):
                    print("Grafico de a 10")
                    b=0
                    update_bar_thread = Thread(target=update_defl_one,args=(Data,View,10))
                    update_bar_thread.daemon=True
                    update_bar_thread.start()
            else:
                print("Grafico de a 1")
                update_bar_thread = Thread(target=update_defl_one,args=(Data,View,1))
                update_bar_thread.daemon=True
                update_bar_thread.start()

            if(cantidad%10 == 0):
                print("Graficando mediciones de grupo...")
                update_all_thread = Thread(target=update_all,args=(Data,View,grupos))
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