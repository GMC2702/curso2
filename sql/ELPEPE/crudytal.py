from ELPEPE.conexion import conectar_bd
import MySQLdb

def crear_registro(conexion, nombre, edad):
    cursor = conexion.cursor()
    sql = "INSERT INTO medicos (nombre, edad) VALUES (%s, %s)"
    valores = (nombre, edad)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Tu datos se han ingresado con exito")
    cursor.close()

def leer_registros(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM medicos")
    resultados = cursor.fetchall() #Obtiene los datos y los imprime.
    for medicos in resultados:
        print(medicos)
    cursor.close()

# leer_registros(conexion) #Llama a la función sde ese nombre.

def actualizar_registro(conexion, medico_id, nombre, edad):
    cursor = conexion.cursor()
    try:
        sql = "UPDATE medicos SET nombre = %s, edad = %s WHERE medico_id = %s"
        valores = (nombre, edad, medico_id)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Tus datos se actualizaron con éxito.")
    except MySQLdb.connect.Error as error:
        print(f"Error al actualizar el registro: {error}")
    finally:
        cursor.close()

def eliminar_registro(conexion, medico_id):
    cursor = conexion.cursor()
    sql = "DELETE FROM medicos WHERE paciente_id = %s"
    valores = (medico_id )
    cursor.execute(sql, valores)
    conexion.commit()
    print("Tus datos se han eliminado con éxito.")
    cursor.close()

conexion = conectar_bd()

if conexion:
    #leer_registros(conexion)
    actualizar_registro(conexion, 5, "ETE SECH", 84)
    leer_registros(conexion)
    #eliminar_registro(conexion, 4)
    conexion.close