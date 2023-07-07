import view
import tkinter as tk
import data
import reporter
import plot
import config
from time import sleep
from threading import Thread
   

if __name__ == "__main__":

    # inicializamos la view
    # Llamamos al objeto Tk de la libreria tkinker, este crea una ventana principal para la interfaz grafica
    root = tk.Tk()
    
    #Creamos un objeto View y llamamos a la funcion principal de la clase view, le pasamos como parámetro el objeto creado
    #anteriorimente.Lo que hace la clase view es personalizar la interfaz gráfica 
    View = view.View(root)

    
    
    # Creamos un objeto reporter y lo inicializamos. Este objeto es en engarcado de proveer las mediciones de los datos,
    # los obtiene de la base de datos haciendole distintas querys
    Reporter = reporter.Reporter()
    Reporter.start()

    #Creamos un objeto Data
    Data = data.Data()

    def separate():

        while View.on_plot() == False:
            None
        
        muestras = int(view.muestras)
        print("Muestras",muestras)

        # temp=int(view.temp)
        # print("Temperatura:",temp)

        espesor=int(view.espesor)
        print("Espesor:",espesor)

        # ft=int(view.ft_ntry)
        # print("ft:",ft)

        # fh=int(view.fh_ntry)
        # print("fh:",fh)

        # fc=int(view.fc_ntry)
        # print("fc:",fc)

        while True:

            # sleep(0.001)
            
            data, this_cicle = Reporter.get_new_measurements()

            # print("Estoy en el while. Data:")
            # print(data)
            # print("Ciclo:")
            # print(this_cicle)


            # primer ciclo
            if data == None and this_cicle == None:

                continue
            
            print("Estoy en el while. Data:")
            print(data)


            # Data.data_destruct(data,temp,espesor)
            Data.data_destruct(data)

            print(Data.cant_mediciones())

            # Por cada medicion nueva debe actualizarse el grafico de barras de deflexiones individuales.
            View.update_bar_view(Data.get_defl())
            

            # cuando se llega a la cantidad de muestras
            # debemos plotear y actualizar las estructuras

            if ((Data.cant_mediciones()) % muestras == 0):

                Data.update_structures()

                dict_r, dict_l = Data.get_data_dict()

                View.new_group_data_view(dict_r, dict_l)

                

    rep_thread = Thread(target=separate) # ejecutamos la logica en un thread distinto mientras el main queda en un loop con la view

    rep_thread.daemon = True

    rep_thread.start()

    root.mainloop()


    


