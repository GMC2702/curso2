# OBJETOS 
# un objeto como ya sabemos es similar a un array, te permite agrupar contenido
# diferentes tipos de datos
# AQUI SE CONOCEN COMO DICCIONARIOS


# cancion = {
#     'artista': 'Ricardo Arjona',
#     'nombre': 'El problema'
# }
# #acceder a los elementos del diccionario
# print(cancion['artista']) #1era. forma de acceder.

# artista = cancion['artista'] #2da. forma de acceder.
# print(artista)


# #agregar un key al diccionario
# cancion['playlist_id'] = 'Romantica'
# print(cancion)


# #eliminar el valor de un diccionario
# del cancion['playlist_id']
# print(cancion)

computadora = {
    'modelo': 'Lenovo',
    'procesador': '64 bits',
    'almacenamiento': '200gb',
    'grafica': 'ryzen' 

}

print(computadora['almacenamiento'])
computadora['pantalla'] = '700px'
print(computadora)