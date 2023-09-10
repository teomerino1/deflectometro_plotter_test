import mysql.connector
from mysql.connector import errorcode 
import json

class Database():
    def __init__(self):
        config_file = open('config.json', 'r')
        self.config = json.load(config_file)
        self.conn = self.connect()

        if self.conn is not None:
            print("Conexión a la base de datos exitosa.")
            self.cursor = self.conn.cursor(buffered=True, dictionary=True)
        else:
            print("Error al conectar a la base de datos.")

    def connect(self):
        try:
            return mysql.connector.connect(**self.config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error: Nombre de usuario o contraseña incorrectos")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Error: La base de datos no existe")
            else:
                print(f"Error desconocido: {err}")

    def query(self, query):
        self.cursor.execute(query)
        self.conn.commit()
        result = self.cursor.fetchall()
        return result

    def close(self):
        self.cursor.close()
        self.conn.close()
