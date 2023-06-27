import mysql.connector
from mysql.connector import errorcode 
import json

class Database():
    def __init__(self):
        
        config_file = open('config.json', 'r')
        self.config = json.load(config_file)
        self.conn = self.connect()
        self.cursor = self.conn.cursor(buffered=True,dictionary=True)

    def connect(self):
        try:
            return mysql.connector.connect(**self.config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Bad name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)


    def query(self,query):
        self.cursor.execute(query) # en cursor queda apuntando a una tupla
        self.conn.commit()
        result = self.cursor.fetchall()
        return result
        
    def close(self):
        self.cursor.close()
        self.conn.close()