import view
import tkinter as tk
import data
import reporter
from threading import Thread
import threading


def show_stats(View,Data,z,ft,fh,fc):
    media_defl_r, media_defl_izq,media_rad_der, media_rad_izq,desv_defl_der, desv_defl_l,coef_var_der,coef_var_izq,defl_car_der,defl_car_izq,rad_car_der,rad_car_izq, d_r_der,d_r_izq ,d_x_r_der, d_x_r_izq, total_mediciones_defl, total_mediciones_rad =Data.calculate_stats(z,ft,fh,fc)
    View.show_stats_in_plot(
        media_defl_r, media_defl_izq,media_rad_der, media_rad_izq,
        desv_defl_der, desv_defl_l,coef_var_der,coef_var_izq,
        defl_car_der,defl_car_izq ,rad_car_der, rad_car_izq,
        d_r_der,d_r_izq,
        d_x_r_der, d_x_r_izq, 
        total_mediciones_defl, total_mediciones_rad
    )

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


def process_data(Reporter, View, Data):
    
    
    # temp,grupos,muestras,espesor,ft,fh,fc,z = View.obtain_values()
    while True:
        temp,grupos,muestras,espesor,ft,fh,fc,z = View.obtain_values()
        if temp and espesor and grupos and ft and fh and fc and z is not None:
            break

    
    Reporter.start()

    while True:
        data, this_cycle = Reporter.get_new_measurements()
        
        if data is None or this_cycle is None:
            # print("Estoy en None")
            continue

        
        Data.data_destruct(data)
        cantidad=Data.cant_mediciones()
        print(cantidad)
        
        # View.update_bar_view(Data.get_defl())
        # Actualizar el gráfico de barras en un hilo separado
        if(cantidad%6 == 0):
            
            update_bar_thread = Thread(target=update_defl,args=(Data,View))
            update_bar_thread.daemon=True
            update_bar_thread.start()

        if(cantidad% grupos == 0):
            
            # a=a+1
            update_all_thread = Thread(target=update_all,args=(Data,View))
            update_all_thread.daemon=True 
            update_all_thread.start()

            # if(a==20):
            #     show_stats(View,Data,z,ft,fh,fc)
            #     break
        
        

        
def main():
    root = tk.Tk()
    
    
    Reporter = reporter.Reporter()
    Data = data.Data()

    View = view.View(root,Data)
    
    # Crear y ejecutar el hilo para procesar los datos
    data_thread = Thread(target=process_data, args=(Reporter, View, Data))
    data_thread.daemon = True
    data_thread.start()
    
    # Ejecutar el bucle principal de la interfaz gráfica
    root.mainloop()

if __name__ == "__main__":
    main()