import numpy as np
import view
import math
import threading

# Clase donde se encuentran los metodos encargados de crear, mantener y actualizar las estructuras de datos
# se tienen dos grupos de mediciones, unas de derecha y otra de izquierda.
# En la inicializacion de la clase Data se crean todos los campos necesarios para interactuar con los datos
class Data():

    def __init__(self):

        self.data_acumulator = None # acumula todo lo que llega de la db
        self.deflexiones_acumulator = [] # acumula los valores de las deflexiones
        self.group_counter = 1 # Contador de grupos

        # Contienen los datos del grupo actual
        self.defl_r = []
        self.defl_l = []
        self.radio_r = []
        self.radio_l = []

        # Contienen las deflexiones maximas
        self.defl_l_max = [] 
        self.defl_r_max = []

        # Contienen las desviaciones estandar
        self.defl_l_car = []
        self.defl_r_car = []

        # Acumuladores que contienen todos los datos recolectados durante la ejecucion
        self.defl_r_acum = []
        self.defl_l_acum = []
        self.radio_r_acum = []
        self.radio_l_acum = []
        self.indices = []

        # dict individual para el histograma de mediciones
        self.hist_dict = {
            "index":[],
            "defl": []
        }

        # dict que va a contener los datos que se van a mostrar por tabla
        # tambien se usan en los ploteos
        self.data_dict_r = {
            "Grupo":[],
            "Radio":[],
            "Defl.":[],
            "R*D":[],
            "D/R":[],
        } 

        self.data_dict_l = {
            "Grupo":[],
            "Radio":[],
            "Defl.":[],
            "R*D":[],
            "D/R":[],
        } 
   


    # Metodo toma lo que devuelve la base de datos y coloca las deflexiones y sus indices en un diccionario.
    def data_destruct(self,data):

        defl_r_aux=data[0]['valor']
        defl_l_aux=data[1]['valor']
        radio_r_aux=data[2]['valor']
        radio_l_aux=data[3]['valor']

        # print("Defl r sin compensar:",defl_r_aux)
        # print("Defl l sin compensar:",defl_l_aux)
        # print("Radio r sin compensar:",radio_r_aux)
        # print("Radio l sin compensar:",radio_l_aux)

        # defl_r_aux,defl_l_aux,radio_r_aux,radio_l_aux= self.compensate(defl_r_aux, defl_l_aux, radio_r_aux, radio_l_aux, espesor,temp)

        self.defl_r.append(defl_r_aux)
        self.defl_l.append(defl_l_aux)
        self.radio_r.append(radio_r_aux)
        self.radio_l.append(radio_l_aux)
        
        # print("Defl r compensada:",defl_r_aux)
        # print("Defl l compensada:",defl_l_aux)
        # print("Radio r compensada:",radio_r_aux)
        # print("Radio l compensada:",radio_l_aux)

        # # los indices pueden cambiar, definirlo con el cliente
        # self.defl_r.append(data[0]['valor'])
        # self.defl_l.append(data[1]['valor'])
        # self.radio_r.append(data[2]['valor'])
        # self.radio_l.append(data[3]['valor'])

        self.defl_r_acum.append(data[0]['valor'])
        self.defl_l_acum.append(data[1]['valor'])
        self.radio_r_acum.append(data[2]['valor'])
        self.radio_l_acum.append(data[3]['valor'])
    
        self.indices = list(range(1,len(self.defl_r_acum)+1))
        print("Indexes:",len(self.indices))
        # return deflexiones, indices

   
    # Metodo que se encarga de una vez cumplido el grupo, actualizar las estructuras de datos
    def update_structures(self):

        print("Soy el thread",threading.get_ident(),"En update structures")

        # self.defl_r_acum.append(self.defl_r)
        # self.defl_l_acum.append(self.defl_l)
        # self.radio_r_acum.append(self.radio_r)
        # self.radio_l_acum.append(self.radio_l)

        # self.indices = list(range(1,len(self.defl_r_acum)+1))
        # print("Indexes:",len(self.indices))

        # Obtengo los promedios de cada cosa
        media_defl_r = round(np.mean(self.defl_r),2)
        media_defl_l = round(np.mean(self.defl_l),2)
        media_radio_r = round(np.mean(self.radio_r),2)
        media_radio_l = round(np.mean(self.radio_l),2)

       

        # Obtengo la deflexion caracteristica. Por el momento Z es igual a 2 y el resto (ft, fc, fh) es 1
        self.defl_l_car.append(  media_defl_l + (2*(np.std(self.defl_l)*2))  )
        self.defl_r_car.append(  media_defl_r + (2*(np.std(self.defl_r)*2))  )

        # Obtengo los máximos de las deflexiones
        self.defl_l_max.append(np.max(self.defl_l))
        self.defl_r_max.append(np.max(self.defl_r))

        # Los agrego a los diccionarios correspondientes
        self.data_dict_r['Grupo'].append(self.group_counter)
        self.data_dict_r['Radio'].append(media_radio_r)
        self.data_dict_r['Defl.'].append(media_defl_r)
        self.data_dict_r['R*D'].append(round(media_defl_r * media_radio_r,2))
        self.data_dict_r['D/R'].append(round(media_defl_r / media_radio_r,2))
        
        self.data_dict_l['Grupo'].append(self.group_counter)
        self.data_dict_l['Radio'].append(media_radio_l)
        self.data_dict_l['Defl.'].append(media_defl_l)
        self.data_dict_l['R*D'].append(round(media_defl_l * media_radio_l,2))
        self.data_dict_l['D/R'].append(round(media_defl_l / media_radio_l,2))
        
        self.group_counter += 1

         # limpiamos porque ya se cumplio el grupo
        self.defl_r.clear()
        self.defl_l.clear()
        self.radio_r.clear()
        self.radio_l.clear()

    
    # # Metodo que devuelve los datos compensados con respecto a la temperatura ingresada
    def compensate(self,defl_r_aux, defl_l_aux, radio_r_aux, radio_l_aux,espesor,temp):

        defl_r_aux=defl_r_aux/((0.001*espesor*(temp-20))+1)
        defl_l_aux=defl_l_aux/((0.001*espesor*(temp-20))+1) 
        # radio_r_aux=radio_r_aux*fc
        # radio_l_aux=radio_l_aux*fc
        return defl_r_aux,defl_l_aux,radio_r_aux,radio_l_aux
       

    # Metodo donde se realizan los calculos de radio
    def calculations_data():
        None # TODO

    def calculate_stats(self,z,ft,fh,fc): # TODO-> Consultar por el calculo de Radio Caracteristico. Falta ese cálculo

        # Calculo de medias para mediciones totales de cada cosa
        media_defl_der = round(np.mean(self.defl_r_acum),2)
        media_defl_izq = round(np.mean(self.defl_l_acum),2)
        media_rad_der =  round(np.mean(self.radio_r_acum),2)
        media_rad_izq = round(np.mean(self.defl_l_acum),2)
        
        # Calculo de desviaciones estandar deflexiones
        desv_defl_der = round(np.std(self.defl_r_acum))
        desv_defl_l = round(np.std(self.defl_l_acum))

        # Calculo de coeficientes de variacion deflexiones
        coef_var_der = round(desv_defl_der/media_defl_der)*100
        coef_var_izq = round(desv_defl_l/media_defl_izq)*100

        # Calculo de deflexion caracteristicas
        defl_car_der = round(media_defl_der + (2*(np.std(self.defl_r_acum)*2)))*z*ft*fh*fc
        defl_car_izq = round(media_defl_izq + (2*(np.std(self.defl_l_acum)*2)))*z*ft*fh*fc

        # Calculo de D/R medio
        d_r_der = media_defl_der/media_rad_der
        d_r_izq = media_defl_izq/media_rad_izq

        # Calculo de D*R medio
        d_x_r_der = media_defl_der*media_rad_der
        d_x_r_izq = media_defl_izq*media_rad_izq

        # Calculo de total de mediciones
        total_mediciones_defl = len(self.defl_l_acum)
        total_mediciones_rad = len(self.radio_l_acum)


    def get_data_dict(self):
        return self.data_dict_r, self.data_dict_l
    
    def get_max_defl(self):
        return self.defl_l_max, self.defl_r_max
    
    def get_std_defl(self):
        return self.defl_l_car, self.defl_r_car
    
    def get_hist_dict(self):
        return self.hist_dict

    def cant_mediciones(self):
        return len(self.defl_r)
    
    def get_indexes(self):
        return self.indices
        # return self.hist_dict['index']
    
    # Estas dos funciones se pueden usar para pasar los valores para el grafico de barras
    def get_defl(self):
        return {
                "right": self.defl_r_acum,
                "left": self.defl_l_acum
               }
