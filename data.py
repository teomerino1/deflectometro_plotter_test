import numpy as np
import view

# Clase donde se encuentran los metodos encargados de crear, mantener y actualizar las estructuras de datos
# se tienen dos grupos de mediciones, unas de derecha y otra de izquierda.
# En la inicializacion de la clase Data se crean todos los campos necesarios para interactuar con los datos
class Data():

    def __init__(self):

        self.data_acumulator = None # acumula todo lo que llega de la db
        self.deflexiones_acumulator = [] # acumula los valores de las deflexiones
        self.group_counter = 1 # Contador de grupos
        
        # contienen los datos del grupo actual
        self.defl_r = []
        self.defl_l = []
        self.radio_r = []
        self.radio_l = []

        # acumuladores que contienen todos los datos recolectados durante la ejecucion
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
        # if self.data_acumulator != None:
        #     self.data_acumulator += data
        # else:
        #     self.data_acumulator = data

        # for dato in self.data_acumulator:
        #     self.deflexiones_acumulator.append(dato['valor'])
        #     nros_medicion.append(dato['nro_medicion'])

         #<- TODO Datos compensados con operación básica, hay que modificarlo cuando pasen el algoritmo

        defl_r_aux=data[0]['valor']
        defl_l_aux=data[1]['valor']
        radio_r_aux=data[2]['valor']
        radio_l_aux=data[3]['valor']

        # print("Defl r sin compensar:",defl_r_aux)
        # print("Defl l sin compensar:",defl_l_aux)
        # print("Radio r sin compensar:",radio_r_aux)
        # print("Radio l sin compensar:",radio_l_aux)

       
        # fc=10
        # # defl_r_aux=defl_r_aux*temp*z*ft*fh*fc
        # defl_r_aux,defl_l_aux,radio_r_aux,radio_l_aux= self.compensate(defl_r_aux, defl_l_aux, radio_r_aux, radio_l_aux, fc)

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
        
        self.indices = list(range(1,len(self.defl_r)+1))
        # return deflexiones, indices

    def get_data_dict(self):
        return self.data_dict_r, self.data_dict_l
    
    def get_hist_dict(self):
        return self.hist_dict

    def cant_mediciones(self):
        return len(self.defl_r)
    
    def get_indexes(self):
        return self.hist_dict['index']
    
    # Estas dos funciones se pueden usar para pasar los valores para el grafico de barras
    def get_defl(self):
        return {
                "right": self.radio_r_acum,
                "left": self.radio_l_acum
               }



    # Metodo que se encarga de una vez cumplido el grupo, actualizar las estructuras de datos
    def update_structures(self):

        media_defl_r = round(np.mean(self.defl_r),2)
        media_defl_l = round(np.mean(self.defl_l),2)
        media_radio_r = round(np.mean(self.radio_r),2)
        media_radio_l = round(np.mean(self.radio_l),2)

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
    def compensate(self,defl_r_aux, defl_l_aux, radio_r_aux, radio_l_aux, fc):

        defl_r_aux=defl_r_aux*fc

        defl_l_aux=defl_l_aux*fc 

        radio_r_aux=radio_r_aux*fc

        radio_l_aux=radio_l_aux*fc

        return defl_r_aux,defl_l_aux,radio_r_aux,radio_l_aux
       

    # Metodo donde se realizan los calculos de radio
    def calculations_data():
        None # TODO


