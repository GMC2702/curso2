playlist = {}
playlist['canciones'] = [] #CREE UN DICCIONARIO

def app(): #funcion principal para el ejercicio
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Cómo deseas nombrar tu playlist: \n')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False # Ya tenemos un nombre desactivamos el true
            agregar_canciones()
            mostrar_resumen()


def agregar_canciones():
    print('Agregando canciones a la playlist:', playlist['nombre'])
    while True:
        cancion = input('Ingresa el nombre de la canción (o "X" para salir): ')
        if cancion.lower() == 'x':

            break #DEJA DE AGREGAR CANCIONES

        playlist['canciones'].append(cancion)

        print('Canción agregada:', cancion)

        print('Playlist completa!')
        print(playlist)

def eliminar_canciones():
    print('Eliminando canciones de la playlist:', playlist['nombre'])
    while True:
        cancion_eliminar = input('Ingresa el nombre de la canción a eliminar (o "X" para salir.)')
        if cancion_eliminar.lower() == 'x':
            break
        if cancion_eliminar in playlist['canciones']:
            playlist['canciones'].remove(cancion_eliminar)
            print('Canción eliminada:', cancion_eliminar)
        else:
            print('La canción no se encuentra en la playlist.')

        print('Playlist actualizada!')
        print(playlist)

def mostrar_resumen():
    print(f'Playlist', playlist['nombre'])
    print('Canciones de la playlist:\r\n')
    for cancion in playlist['canciones']:
        print(cancion)

app()
