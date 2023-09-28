import numpy as np
import view
import math
import threading

"""
Clase Data:
    Se encuentran los metodos encargados de crear, mantener y actualizar las estructuras de datos.
    Se tienen dos grupos de mediciones, unas de derecha y otra de izquierda.
    En la inicializacion de la clase Data se crean todos los campos necesarios para interactuar con los datos
"""
class Data():

    def __init__(self):

        # acumula todo lo que llega de la db
        self.data_acumulator = None 

        # acumula los valores de las deflexiones
        self.deflexiones_acumulator = [] 

        # Contador de grupos
        self.group_counter = 1

        #Grupos seleccionados por el usuario 
        self.grupos=None        

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

        # Unicamente para el ploteo de deflexiones individuales
        self.defl_bar_l = []
        self.defl_bar_r = []

        # Acumuladores que contienen todos los datos recolectados durante la ejecucion
        self.defl_r_acum = []
        self.defl_l_acum = []
        self.radio_r_acum = []
        self.radio_l_acum = []
        self.indices = []

        # Variables para el calculo de compensacion
        self.temp = None 
        self.espesor = None
        self.ft= None
        self.fh=None
        self.fc=None
        self.z = None

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

    """
    Este método desestructura los datos que vienen de la base de datos.
    Los divide en radio y deflexión, y además realiza el cálculo de compensación.

    @params data: El objeto data que contiene los valores de radio y deflexión.
    """
    def data_destruct(self,data):

        defl_r_aux=data[0]['valor']
        radio_r_aux=data[1]['valor']
        defl_l_aux=data[2]['valor']
        radio_l_aux=data[3]['valor']

        defl_r_aux,defl_l_aux,radio_r_aux,radio_l_aux = self.compensate(defl_r_aux, defl_l_aux,radio_r_aux,radio_l_aux)

        self.defl_r.append(defl_r_aux)
        self.defl_l.append(defl_l_aux)
        self.radio_r.append(radio_r_aux)
        self.radio_l.append(radio_l_aux)
        self.defl_r_acum.append(defl_r_aux)
        self.radio_r_acum.append(radio_r_aux)
        self.defl_l_acum.append(defl_l_aux)
        self.radio_l_acum.append(radio_l_aux)
       
    """
    Este método hace un update de los datos correspondientes al gráfico de barras 
    de deflexiones individuales.

    @param amount: La cantidad de datos a actualizar
    """
    def update_bar_data(self,amount):
        self.defl_bar_r.extend(self.defl_r[-amount:])
        self.defl_bar_l.extend(self.defl_l[-amount:])
        return self.defl_bar_r,self.defl_bar_l
    
    """
    Este método hace un clear de los arreglos de datos de deflexiones individuales.
    """
    def clear_bar_data(self):
        self.defl_bar_r.clear()
        self.defl_bar_l.clear()

    """
    Este método actualiza las estructuras de datos que van a graficarse.
    Es llamada cuando se cumple el grupo de 50 o 100 datos.
        -Calcula el promedio de los radios y deflexiones, y la deflexion característica
        -Añade los datos a los diccionarios que se insertan en la tabla
        -Limpia los datos porque ya se cumplió el grupo
    """
    def update_structures(self):
        
        media_defl_r = round(np.mean(self.defl_r),2)
        media_defl_l = round(np.mean(self.defl_l),2)
        media_radio_r = round(np.mean(self.radio_r),2)
        media_radio_l = round(np.mean(self.radio_l),2)

        #Deflexion caracteristica
        self.defl_l_car.append(  (media_defl_l + ((np.std(self.defl_l)*self.z)))*self.ft*self.fh*self.fc  )
        self.defl_r_car.append(  (media_defl_r + ((np.std(self.defl_r)*self.z)))*self.ft*self.fh*self.fc  )
        
        #Máximos de las deflexiones
        self.defl_l_max.append(np.max(self.defl_l))
        self.defl_r_max.append(np.max(self.defl_r))
        
        #Se agrega a los diccionarios correspondientes
        self.data_dict_r['Grupo'].append(self.group_counter*self.get_grupos())
        self.data_dict_r['Radio'].append(media_radio_r)
        self.data_dict_r['Defl.'].append(media_defl_r)
        self.data_dict_r['R*D'].append(round(media_defl_r * media_radio_r,2))
        self.data_dict_r['D/R'].append(round(media_defl_r / media_radio_r,2))
        self.data_dict_l['Grupo'].append(self.group_counter*self.get_grupos())
        self.data_dict_l['Radio'].append(media_radio_l)
        self.data_dict_l['Defl.'].append(media_defl_l)
        self.data_dict_l['R*D'].append(round(media_defl_l * media_radio_l,2))
        self.data_dict_l['D/R'].append(round(media_defl_l / media_radio_l,2))
        
        self.group_counter += 1

        #Se limpia porque ya se cumplió el grupo
        self.defl_r.clear()
        self.defl_l.clear()
        self.radio_r.clear()
        self.radio_l.clear()

    
    """
    Esta función realiza los cálculos de compensación de los datos.

    @params: Valores auxiliares de deflexiones y radios a ser compensados
    @return Los valores compensados
    """
    def compensate(self,defl_r_aux, defl_l_aux,radio_r_aux,radio_l_aux):
        defl_r_aux=round((defl_r_aux/((0.001*self.espesor*(self.temp-20))+1)),2)
        defl_l_aux=round((defl_l_aux/((0.001*self.espesor*(self.temp-20))+1)),2) 
        radio_r_aux=round((radio_r_aux*((0.001*self.espesor*(self.temp-20))+1)),2)
        radio_l_aux=round((radio_l_aux*((0.001*self.espesor*(self.temp-20))+1)),2)
        return defl_r_aux,defl_l_aux,radio_r_aux,radio_l_aux
       

    """
    Esta función es llamada cuando se realizan los cálculos estadísticos.

    @return - Si hay valores para calcular, retorna los valores de todos los cálculos estadísticos
            - Si no hay valores para calcular, los retorna todos 0 
    """
    def calculate_stats(self):

        if(self.defl_r_acum==[] or self.defl_l_acum==[] or self.radio_r_acum==[] or self.radio_l_acum==[]):
            media_defl_der=0
            media_defl_izq=0
            media_rad_der=0
            media_rad_izq=0
            desv_defl_der=0
            desv_defl_l=0
            coef_var_der=0
            coef_var_izq=0
            defl_car_der=0
            defl_car_izq=0
            rad_car_der=0
            rad_car_izq=0
            d_r_der=0
            d_r_izq=0
            d_x_r_der=0
            d_x_r_izq=0
            total_mediciones_defl=0
            total_mediciones_rad=0
            return media_defl_der,media_defl_izq,media_rad_der,media_rad_izq,desv_defl_der,desv_defl_l,coef_var_der,coef_var_izq,defl_car_der,defl_car_izq,rad_car_der,rad_car_izq,d_r_der,d_r_izq,d_x_r_der,d_x_r_izq,total_mediciones_defl,total_mediciones_rad
       
        # Calculo de medias para mediciones totales de cada cosa
        media_defl_der = round(np.mean(self.defl_r_acum),2)
        media_defl_izq = round(np.mean(self.defl_l_acum),2)
        media_rad_der =  round(np.mean(self.radio_r_acum),2)
        media_rad_izq = round(np.mean(self.radio_l_acum),2)
        
        # # Calculo de desviaciones estandar deflexiones
        desv_defl_der = round(np.std(self.defl_r_acum),2)
        desv_defl_l = round(np.std(self.defl_l_acum),2)

        # # Calculo de coeficientes de variacion deflexiones
        coef_var_der = round((desv_defl_der/media_defl_der)*100,2)
        coef_var_izq = round((desv_defl_l/media_defl_izq)*100,2)

        # # Calculo de deflexion caracteristicas
        defl_car_der = round((media_defl_der + (desv_defl_der*self.z))*self.ft*self.fh*self.fc,2)
        defl_car_izq = round((media_defl_izq + (desv_defl_l*self.z))*self.ft*self.fh*self.fc,2)

        # Calculo de radio caracteristico
        rad_car_der = round((media_rad_der + ((np.std(self.radio_r_acum)))*self.z)*self.ft*self.fh*self.fc,2)
        rad_car_izq = round((media_rad_izq + ((np.std(self.radio_l_acum)))*self.z)*self.ft*self.fh*self.fc,2)

        # # Calculo de D/R medio
        d_r_der = round(media_defl_der/media_rad_der,2)
        d_r_izq = round(media_defl_izq/media_rad_izq,2)

        # # Calculo de D*R medio
        d_x_r_der = round(media_defl_der*media_rad_der,2)
        d_x_r_izq = round(media_defl_izq*media_rad_izq,2)

        # # Calculo de total de mediciones
        total_mediciones_defl = len(self.defl_l_acum)
        total_mediciones_rad = len(self.radio_l_acum)

        return media_defl_der,media_defl_izq,media_rad_der,media_rad_izq,desv_defl_der,desv_defl_l,coef_var_der,coef_var_izq,defl_car_der,defl_car_izq,rad_car_der,rad_car_izq,d_r_der,d_r_izq,d_x_r_der,d_x_r_izq,total_mediciones_defl,total_mediciones_rad

    """
    Esta función retorna los diccionarios de valores de derecha e izquierda
    """
    def get_data_dict(self):
        return self.data_dict_r, self.data_dict_l
    
    """
    Esta función retorna los valores máximos de deflexion derecha e izquierda
    """
    def get_max_defl(self):
        return self.defl_l_max, self.defl_r_max
    
    """
    Esta función retorna los valores de deflexión característca derecha e izquierda
    """
    def get_car_defl(self):
        return self.defl_l_car, self.defl_r_car
    
    """
    Esta función retorna el diccionario del histograma de mediciones
    """
    def get_hist_dict(self):
        return self.hist_dict

    """
    Esta función retorna la cantidad de mediciones
    """
    def cant_mediciones(self):
        return len(self.defl_r)
    
    """
    Esta función retorna los índices
    """
    def get_indexes(self):
        return self.indices

    """
    Esta función retorna los arreglos para el gráfico de deflexiones individuales
    """
    def get_defl_bar(self):
        return  self.defl_bar_r, self.defl_bar_l
               

    """
    Esta función retorna un diccionario con las deflexiones derecha e izquierda totales
    """
    def get_defl(self):
        return {
                "right": self.defl_r_acum,
                "left": self.defl_l_acum
               }
    
    """
    Esta función setea el valor del espesor obtenido en la interfaz de configuración
    """
    def set_espesor(self,espesor):
        self.espesor=espesor

    """
    Esta función setea el valor de temperatura obtenido en la interfaz de configuración
    """
    def set_temp(self,temp):
        self.temp=temp

    """
    Esta función setea el valor de ft obtenido en la interfaz de configuración
    """    
    def set_ft(self,ft):
        self.ft=ft

    """
    Esta función setea el valor de fc obtenido en la interfaz de configuración
    """
    def set_fc(self,fc):
        self.fc=fc

    """
    Esta función setea el valor de fh obtenido en la interfaz de configuración
    """  
    def set_fh(self,fh):
        self.fh=fh

    """
    Esta función setea el valor de z obtenido en la interfaz de configuración
    """
    def set_z(self,z):
        self.z=z

    """
    Esta función setea el valor de los grupos obtenido en la interfaz de configuración
    """
    def set_grupos(self,grupos):
        self.grupos=grupos

    """
    Esta función retorna el valor de los grupos obtenido en la interfaz de configuración
    """
    def get_grupos(self):
        return self.grupos
    
    """
    Esta función resetea todos los datos que maneja la clase Data.
    Se ejecuta cuando ocurre un reset
    """    
    def reset_all(self):
        self.defl_r.clear()
        self.defl_l.clear()
        self.radio_r.clear()
        self.radio_l.clear()
        self.defl_l_max.clear()
        self.defl_r_max.clear()
        self.defl_r_car.clear()
        self.defl_l_car.clear()
        self.defl_l_acum.clear()
        self.defl_r_acum.clear()
        self.radio_l_acum.clear()
        self.radio_r_acum.clear()
        self.indices.clear()
        self.defl_bar_l.clear()
        self.defl_bar_r.clear()
        self.hist_dict.clear()
        self.group_counter = 1
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
         
        print("Datos reseteados!\n")
        
