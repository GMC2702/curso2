#Operaciones basicas en python

a = 15
b = 40
print('La suma de a + b es igual a ' + str(a) + ' + ' + str(b) + ' = ' +  str(a+b))

#para concatenar variables numericas es necesario usar la palabra str para
#convertir el valor en una cadena de texto o puedes usar lo siguiente:

print(f'La suma de a + b es igual a {a} + {b} = {a+b}')

#python 3.6, se introdujeron las f-strings.

print(f'la multiplicación de a por b es igual a {a} X {b} = {a*b}')
print(f'la división de a entre b es igual a {a} entre {b} = {a/b}')
print(f'la resta de a entre b es igual a {a} menos {b} = {b-a}')