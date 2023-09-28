import mysql.connector
from mysql.connector import errorcode 
import json

"""
Esta clase se encarga de conectarse a la base de Datos y realizar las consultas para obtener los datos
"""
class Database:
    def __init__(self):
        config_file = open('config.json', 'r')
        self.config = json.load(config_file)
        self.conn = self.connect()
        if self.conn is not None:
            print("Conexión a la base de datos establecida correctamente.")
        else:
            print("No se pudo establecer la conexión a la base de datos.")
        self.cursor = self.conn.cursor(buffered=True, dictionary=True)

    """
    Este método intenta conectarse a la base de datos.
    Informa en caso de error.
    """
    def connect(self):
        try:
            return mysql.connector.connect(**self.config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error: Nombre de usuario o contraseña incorrectos.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Error: La base de datos no existe.")
            else:
                print("Error inesperado al conectar a la base de datos:", err)
            return None

    """
    Este método ejecuta una query en la base de datos.

    @return - El resultado de la query en caso exitoso
            - None en caso de error
    """
    def query(self, query):
        if self.conn is not None:
            try:
                self.cursor.execute(query)
                self.conn.commit()
                result = self.cursor.fetchall()
                return result
            except mysql.connector.Error as err:
                print("Error al ejecutar la consulta:", err)
                return None
        else:
            print("No se puede ejecutar la consulta porque no se ha establecido una conexión.")
            return None

    def close(self):
        if self.conn is not None:
            self.cursor.close()
            self.conn.close()
            print("Conexión a la base de datos cerrada.")
        else:
            print("No se puede cerrar la conexión porque no se ha establecido una conexión.")
