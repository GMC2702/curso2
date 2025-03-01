#pip install mysql-connector-python

# scikit-learn:
# Proporciona herramientas para el aprendizaje automatico
# Incluye algoritmos para clasificación, regresión, clustering y reducción de dimensionalidad.
# TensorFlow y Pytorch:
# Son bibliteocas para el aprendizaje profundo.
# Permiten construir y entrenar redes neuronales.
# FLASK Y DJANGO
# OS

import mysql.connector

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="", #Reemplaza con tu contraseña
            database="clinica" # Reemplaza con el nombre de tu base de datos.
        )
        print("Conexión a la base de datos establecida con exito.") #Mensaje de exito.
        return conexion
    except mysql.connector.Error as error: #Si hay error de MySQL.
        print(f"Error al conectar MySql: {error}")
        return None
    except Exception as error: #si hay un error inesperado.
        print(f"Error inesperado: {error}")
        return None
    finally:
        #Bloque finally, para futuras implementaciones. Como cerrar la conexión.
        if conexion.is_connected():
            conexion.close()
        print("Conexion cerrada")

conexion = conectar_bd() #llamado.
conexion.close() #Cerrar la conexión.

#pass es una declaración nula. Esto significa
#que no hace nada cuando se ejecuta. Se utiliza como un marcador de posición
#cuando se requiere sintácticamente una declaración, pero no se desea ejecutar ningún codigo.