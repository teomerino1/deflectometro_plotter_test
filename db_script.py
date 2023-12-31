import mysql.connector
from mysql.connector import errorcode 
import json
import random
from time import sleep


# script que inserta mediciones en la base de datos cada x tiempo (para cambiar el intervalo modificar el numero de sleep())

if __name__ == "__main__":

    config_file = open('config.json', 'r')
    config = json.load(config_file)

    try:
        conn = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Bad name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    cursor = conn.cursor(buffered=True,dictionary=True)
    cursor.execute('SELECT nro_ciclo FROM ciclo ORDER BY nro_ciclo DESC LIMIT 1')
    conn.commit()
    result = cursor.fetchone()
    nro_ciclo = result['nro_ciclo'] + 1
    # nro_ciclo = 1
    for i in range (0,200):
        cursor.execute('INSERT INTO ciclo VALUES(1,%(nro_ciclo)s,800,NOW(),NOW(),200,200,"1","TARDE",1,"1","1")',{'nro_ciclo' : nro_ciclo})
        counter = 1

        for n in range(1,5):
            ran = round(random.uniform(40,55),4)
            cursor.execute('INSERT INTO mediciones_ciclo VALUES(1,%s,%s,%s)',(nro_ciclo,counter,ran))
            counter += 1
        nro_ciclo += 1
        sleep(1)
        conn.commit()

    cursor.close()
    conn.close()