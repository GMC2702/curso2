nombre = input('Cuál es tu nombre?\r\n')  #\r\n es un salto de linea.
print(f'tu nombre es {nombre}')

#leer los datos cuando sean números podemos hacer un if
#NOTA LAS ENTRADAS DE DATOS SIEMPRE VIENEN EN STRING

edad = input('Cual es tu edad?')
#convertir edad en un entero
edad = int(edad) #float #str

if edad >=18:
    print(f'eres mayor de edad y puedes votar')
else:
    print(f'lo sentimos aún eres un bebé')

#cano que un usuario ingrese otro valor que no sea número
nombre = input('Cuál es tu nombre?')
print(f'Tu nombre es {nombre}')

edad = input('Cual es tu edad?')
try:
    edad = int(edad)
    if edad >= 18:
        print(f'eres mayor de edad y puedes votar')
    else:
        print(f'eres menor de edad y NO puedes votar')
except ValueError:
    print("Por favor, ingresa un número válido para la edad")
