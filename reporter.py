# import db

# class Reporter():
#     def __init__(self):
#         self.last_cicle = 0
#         self.last_measurement_data = []
#         self.puesto = 0  # Registro del puesto actual, todas las mediciones deben pertenecer al mismo puesto
#         self.last_puesto = None  # Variable para almacenar el 'puesto' de la iteración anterior
#         self.database = db.Database()
#         # self.start()

#     def start(self):
#         self.get_last_measurement()

#     # Método que obtiene el número de ciclo correspondiente a la medición más nueva
#     def get_last_measurement(self):
#         result = self.database.query('SELECT nro_puesto, nro_ciclo, TIME(fecha_hora_inicio) as last_measurement FROM ciclo ORDER BY fecha_hora_inicio DESC LIMIT 1;')
#         if result:
#             self.puesto = result[0]['nro_puesto']
#             print("Puesto:",self.puesto)
            
#             self.last_puesto = self.puesto
#             self.last_cicle = result[0]['nro_ciclo']

#     # Método para manejar el cambio de 'puesto'
#     def handle_puesto_change(self):
#         # Aquí puedes ejecutar las funciones que necesitas cuando cambie el 'puesto'
#         print("El puesto ha cambiado. Puesto actual:", self.puesto)

#     # Método que obtiene las mediciones nuevas de la base
#     def get_new_measurements(self):
#         self.get_last_measurement()  # Obtenemos el último 'puesto' antes de obtener nuevas mediciones
#         cicle = self.database.query('SELECT nro_ciclo FROM ciclo WHERE nro_puesto = {} ORDER BY fecha_hora_inicio DESC LIMIT 1;'.format(self.puesto))

#         if cicle and cicle[0]['nro_ciclo'] > self.last_cicle:
#             query = 'SELECT nro_medicion, valor FROM mediciones_ciclo WHERE nro_ciclo = {} AND nro_puesto = {};'.format(self.last_cicle, self.puesto)
#             self.last_measurement_data.clear()
#             self.last_measurement_data = self.database.query(query)
#             self.last_cicle = cicle[0]['nro_ciclo']

#             # Verificamos si cambió el 'puesto' durante la obtención de nuevas mediciones
#             if self.puesto != self.last_puesto:
#                 self.handle_puesto_change()
#                 self.last_puesto = self.puesto  # Actualizamos el último 'puesto' para la próxima iteración

#             return self.last_measurement_data, self.last_cicle

#         return None, None






























import db
from time import sleep
import os, sys

class Reporter():
    def __init__(self):
        self.last_cicle = 0
        self.last_measurement_data = []
        self.puesto = 0  # Registro del puesto actual, todas las mediciones deben pertenecer al mismo puesto
        self.database = db.Database()
        self.puesto_changed = 0

    def start(self):
        self.get_last_measurement()

    def set_puesto_change(self, value):
        self.puesto_changed=value

    def get_puesto_change(self):
        return self.puesto_changed

    # Método que obtiene el número de ciclo correspondiente a la medición más nueva
    def get_last_measurement(self):
        result = self.database.query('SELECT nro_puesto, nro_ciclo, TIME(fecha_hora_inicio) as last_measurement FROM ciclo ORDER BY fecha_hora_inicio DESC LIMIT 1;')
        if result:
            self.puesto = result[0]['nro_puesto']
            self.last_cicle = result[0]['nro_ciclo']
            # print("Result:",result)
            # print("Puesto:",self.puesto)
            # print("Ciclo:",self.last_cicle)
            

    def get_last_puesto(self):
        result = self.database.query('SELECT nro_puesto, nro_ciclo, TIME(fecha_hora_inicio) as last_measurement FROM ciclo ORDER BY fecha_hora_inicio DESC LIMIT 1;')
        if result:
            last_puesto = result[0]['nro_puesto']
        return last_puesto
    

    # Método que obtiene las mediciones nuevas de la base
    def get_new_measurements(self):
        if(self.get_last_puesto()!=self.puesto):
            self.set_puesto_change(value=1)
            print("Cambio el puesto, seteo con value = 1")
            return None, None

        cicle = self.database.query('SELECT nro_ciclo FROM ciclo WHERE nro_puesto = {} ORDER BY fecha_hora_inicio DESC LIMIT 1;'.format(self.puesto))

        if cicle and cicle[0]['nro_ciclo'] > self.last_cicle:
            query = 'SELECT nro_medicion, valor FROM mediciones_ciclo WHERE nro_ciclo = {} AND nro_puesto = {};'.format(self.last_cicle, self.puesto)
            self.last_measurement_data.clear()
            self.last_measurement_data = self.database.query(query)
            self.last_cicle = cicle[0]['nro_ciclo']
            return self.last_measurement_data, self.last_cicle

        return None, None







        


                
