
from conexion import conectar_bd
import mysql.connector

def crear_registro(conexion, nombre, edad):
    cursor = conexion.cursor()
    sql = "INSERT INTO pacientes (nombre, edad) VALUES (%s, %s)"
    valores = (nombre, edad)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Tu datos se han ingresado con exito")
    cursor.close()

def leer_registros(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM pacientes")
    resultados = cursor.fetchall() #Obtiene los datos y los imprime.
    for pacientes in resultados:
        print(pacientes)
    cursor.close()

leer_registros(conexion) #Llama a la función de ese nombre.

def actualizar_registro(coneion, paciente_id, nombre, edad):
    cursor = conexion.cursor()
    try:
        sql = "UPDATE pacientes SET nombre = %s, edad = %s WHERE paciente_id = %s"
        valores = (nombre, edad, paciente_id)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Tus datos se actualizaron con éxito.")
    except mysql.connector.Error as error:
        print(f"Error al actualizar el registro: {error}")
    finally:
        cursor.close()

def eliminar_registro(conexion, paciente_id):
    cursor = conexion.cursor()
    sql = "DELETE FROM pacientes WHERE paciente_id = %s"
    valores = (paciente_id )
    cursor.execute(sql, valores)
    conexion.commit()
    print("Tus datos se han eliminado con éxito.")
    cursor.close()

conexion = conectar_bd()

if conexion:
    #leer_registros(conexion)
    actualizar_registro(conexion, 5, "TAL TAL TAL", 84)
    leer_registros(conexion)
    #eliminar_registro(conexion, 4)
    conexion.close