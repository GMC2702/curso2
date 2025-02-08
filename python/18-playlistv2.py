playlist = {}

def crear_playlist():
        nombre_playlist = input('Cómo deseas nombrar tu playlist: \n')
        playlist[nombre_playlist] = []
        return nombre_playlist



def agregar_canciones(playlist_nombre):
    print('Agregando canciones a la playlist:', playlist['nombre'])
    while True:
        cancion = input('Ingresa el nombre de la canción (o "X" para salir): ')
        if cancion.lower() == 'x':
            break #DEJA DE AGREGAR CANCIONES
        playlist[playlist_nombre].append(cancion)
        print('Canción agregada:', cancion)

def eliminar_canciones(playlist_nombre):
    print('Eliminando canciones de la playlist:', playlist[playlist_nombre])
    while True:
        cancion_eliminar = input('Ingresa el nombre de la canción a eliminar (o "X" para salir.)')
        if cancion_eliminar.lower() == 'x':
            break
        if cancion_eliminar in playlist[playlist_nombre]:
            playlist[playlist_nombre].remove(cancion_eliminar)
            print('Canción eliminada:', cancion_eliminar)
        else:
            print('La canción no se encuentra en la playlist.')

        print('Playlist actualizada!')
        print(playlist)

def mostrar_playlist():
    if not playlist:
        print("No hay playlists creadas.")
    else:
        for nombre_playlist, canciones in playlist.items():
            print(f"Playlist: {nombre_playlist}")
            for cancion in canciones:
                print(f"- {cancion}")

def app():
    while True:
        print("\nMenú:")
        print("1. Crear una una playlist.")
        print("2. Agregar canciones a una playlist.")
        print("3. Eliminar canciones de una playlist.")
        print("4. Mostrar todas las playlist.")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre_playlist = crear_playlist()
            agregar_canciones(nombre_playlist)
        elif opcion == '2':
            nombre_playlist = input("¿A que playlist deseas agregar canciones?")
            if nombre_playlist in playlist:
                agregar_canciones(nombre_playlist)
            else:
                print("La playlist no existe.")
        elif opcion == '3':
            nombre_playlist = input("¿De que playlists deseas eliminar canciones?")
            if nombre_playlist in playlist:
                eliminar_canciones(nombre_playlist)
            else:
                print("La playlist no existe.")
        elif opcion == '4':
            mostrar_playlist()
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")

app()