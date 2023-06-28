# from time import sleep
import os, sys
import db
# https://stackoverflow.com/questions/23382499/run-python-script-on-database-event
class Reporter():
    def __init__(self):
        # self.last_measurement = ''
        self.last_cicle = 0
        self.last_measurement_data = []
        self.puesto = 0 # registro del puesto actual, todas las mediciones deben pertenecer al mismo puesto
        
        self.database = db.Database()

    def start(self):
        self.get_last_measurement()

    # Metodo que obtiene el numero de ciclo correspondiente a la medicion mas nueva
    def get_last_measurement(self):
        result = self.database.query('SELECT nro_puesto, nro_ciclo, TIME(fecha_hora_inicio) as last_measurement FROM ciclo ORDER BY fecha_hora_inicio DESC LIMIT 1;')
        self.puesto = result[0]['nro_puesto']
        self.last_cicle = result[0]['nro_ciclo']

    # Metodo que obtiene las mediciones nuevas de la base
    def get_new_measurements(self):

        cicle = self.database.query('SELECT nro_ciclo FROM ciclo WHERE nro_puesto = {} ORDER BY fecha_hora_inicio DESC LIMIT 1;'.format(self.puesto))
        
        if cicle[0]['nro_ciclo'] > self.last_cicle:
            query = 'SELECT nro_medicion, valor FROM mediciones_ciclo WHERE nro_ciclo = {} AND nro_puesto = {};'.format(self.last_cicle, self.puesto)
            self.last_measurement_data.clear()
            self.last_measurement_data = self.database.query(query)

            self.get_last_measurement() 
            return self.last_measurement_data, self.last_cicle
        
        self.get_last_measurement() 
        return None, None

        


                
