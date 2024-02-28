import mysql.connector
from mysql.connector import Error

def testear_conexion():

    conexion=None
    try:
        # Configurar la conexión
        conexion = mysql.connector.connect(
            host='localhost',
            user='slave_anomaly_detector',
            password='W4xwckLUN2xJtnIVhV6J',
            database='anomaly_http'
        )

        if conexion.is_connected():
            print('Conexión exitosa')
            print(f'Versión del servidor: {conexion.get_server_info()}')
    except Error as e:
        print(f'Error al conectar a MySQL: {e}')
    finally:
        # Cerrar la conexión si está abierta
        if conexion and conexion.is_connected():
            conexion.close()
            print('Conexión cerrada')
