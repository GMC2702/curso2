# Operadores de comparacion
# == Igual a
# !=  Diferente de 
# <  Menor que
# >  Mayor que
# <=  Menor o igual que
# >=  Mayor o igual que

a = 5
b = 3
igual = a == b #igual es False
diferente = a != b #diferente es True
mayor = a >= b #mayor es True

#condicional

ahorro = 100
if ahorro >=0:
    print("Nos vamos de viaje")
else:
    print("no tenemos ahorros")


#REVISAMOS SI UN VALOR ES DIFERENTE EN PYTHON STRING
lenguaje = 'python'
if not lenguaje == 'python':
    print(f'super eres un crack de {lenguaje}')
else:
    print(f'no eres un crack de {lenguaje}')

#EVALUACIÓN BOOLEAN
usuario_autenticado = False
if usuario_autenticado:
    print('el usuario se autenticó con exito')
else:
    print('el usuario no se autenticó velva a intentarlo')

#CONDICIONALES CON LIST

superheroes= ['superman', 'spiderman', 'mujer maravilla', 'hercules']
if 'superman' in superheroes:
    print('amas a Batman')
else:
    print('tu superheroe no es batman')

videojuego= ['buscaminas', 'tekken', 'megaman', 'digimon', 'fifa']
if 'buscaminas' in videojuego:
    print(f'Soy un pro en {videojuego}')
else:
    print('soy malo en todo')