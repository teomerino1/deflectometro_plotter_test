import view
import tkinter as tk
import data
import reporter
from threading import Thread
import threading



def update_all(View,dict_r,dict_l,defl_l_max,defl_r_max,defl_l_car,defl_r_car,defl_left_right_dict,indexes):

    View.update_bar_view(defl_left_right_dict,indexes)
    View.new_group_data_view(dict_r,dict_l,defl_l_max,defl_r_max,defl_l_car,defl_r_car)

def process_data(Reporter, View, Data):
    Reporter.start()

    while True:
        muestras = view.muestras

        if muestras is not None:
            break

    temp = int(view.temp)
    espesor =int(view.espesor)

    z = view.z_ntry
    ft = view.ft_ntry
    fh = view.fh_ntry
    fc = view.fc_ntry

    if z == '':
        z = 2
    if ft == '':
        ft = 1
    if fh == '':
        fh = 1
    if fc == '':
        fc = 1

    print("Muestras:",muestras)
    print("Temp:",temp)
    print("Espesor:",espesor)
    print("Temp type:",type(temp))

    while True:
        data, this_cycle = Reporter.get_new_measurements()

        if data is None or this_cycle is None:
            # print("Estoy en None")
            continue

        # Data.data_destruct(data)
        Data.data_destruct(data,espesor,temp)
        cantidad=Data.cant_mediciones()
        print(cantidad)
        
        # View.update_bar_view(Data.get_defl())
        # Actualizar el gráfico de barras en un hilo separado
        if(cantidad%20 == 0):

            Data.update_structures()
            dict_r, dict_l = Data.get_data_dict()
            defl_l_max, defl_r_max = Data.get_max_defl()
            defl_l_car, defl_r_car = Data.get_std_defl()
            defl_left_right_dict=Data.get_defl()
            indexes=Data.get_indexes()

            update_all_thread = Thread(target=update_all,args=(View,dict_r,dict_l,defl_l_max,defl_r_max,defl_l_car,defl_r_car,defl_left_right_dict,indexes))
            update_all_thread.daemon=True 
            update_all_thread.start()
             
        continue
        

        
def main():
    root = tk.Tk()
    View = view.View(root)
    
    Reporter = reporter.Reporter()
    Data = data.Data()
    
    # Crear y ejecutar el hilo para procesar los datos
    data_thread = Thread(target=process_data, args=(Reporter, View, Data))
    data_thread.daemon = True
    data_thread.start()
    
    # Ejecutar el bucle principal de la interfaz gráfica
    root.mainloop()

if __name__ == "__main__":
    main()



































# import view
# import tkinter as tk
# import data
# import reporter
# from threading import Thread
# import threading
# from timeit import default_timer as timer


# def process_data(Reporter,View,Data):

#     Reporter.start()

#     a=0

#     while (True):
    
#         muestras = view.muestras
        
#         if(muestras != None ):
            
#             break
        
#         continue
    
#     temp = view.temp
        
#     espesor = view.espesor

#     z = view.z_ntry

#     ft = view.ft_ntry

#     fh = view.fh_ntry

#     fc = view.fc_ntry

#     if(z==''):

#         z = 2

#     if(ft==''):

#         ft=1

#     if(fh==''):

#         fh=1

#     if(fc==''):

#         fc=1

#     print("Z:", z)
#     print("Ft:",ft)
#     print("Fh:",fh)
#     print("Fc:",fc)
#     print("Muestras", muestras)

#     while True:

#         # print("Voy a obtener nuevas mediciones")
#         # print("Soy el thred", threading.get_ident())
       
#         data, this_cycle = Reporter.get_new_measurements()

#         # print("Estoy en el while. Data:")
#             # print(data)
#             # print("Ciclo:")
#             # print(this_cicle)

#             # primer ciclo
#         if(data == None or this_cycle == None):
#             # print("Estoy en el while de data y this cicle None")
#             # print("Soy el thred", threading.get_ident())
#             continue

        

#         # print("Salgo del None while")
#         # print("Soy el thred", threading.get_ident())
#         # print(Data.cant_mediciones())

#         # print("Estoy en el while. Data:")
        
#         # print(data)

#         # # Data.data_destruct(data,temp,espesor)
#         Data.data_destruct(data)

#         print(Data.cant_mediciones())

#         # # Por cada medicion nueva debe actualizarse el grafico de barras de deflexiones individuales.
#         # View.update_bar_view(Data.get_defl())
        
           
#         # # cuando se llega ca la cantidad de muestras
#         # # debemos plotear y actualizar las estructuras

#         # if ((Data.cant_mediciones()) % muestras == 0):

#         #     a=a+1

#         #     Data.update_structures()

#         #     dict_r, dict_l = Data.get_data_dict()

#         #     defl_l_max, defl_r_max = Data.get_max_defl()

#         #     defl_l_car, defl_r_car = Data.get_std_defl()

#         #     View.new_group_data_view(dict_r, dict_l, defl_r_max, defl_l_max, defl_l_car, defl_r_car)

#             # if(a == 20):

#             #     #TODO-> Disparar calculos estadísticos. Si llegamos acá se trabajaron 1000 datos
        
        

# def main():

#     root = tk.Tk()
#     View = view.View(root)
    
#     Reporter = reporter.Reporter()
#     # Reporter.start()
    
#     Data = data.Data()
    
#     # Crear y ejecutar el hilo para procesar los datos
#     data_thread = Thread(target=process_data,args=(Reporter,View,Data))
#     data_thread.daemon = True
#     data_thread.start()
    
#     # Ejecutar el bucle principal de la interfaz gráfica
#     root.mainloop()

# if __name__ == "__main__":
#     main()


























    

