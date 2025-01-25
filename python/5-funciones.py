def informacion(nombre, cargo='un tilín'):
    print(f'soy {nombre}, y soy {cargo}')

informacion('Gerardo', 'chambeador')
informacion('Tilín') #Debe dar error si paso un solo parametro; pero como cargo tiene asignado algo en su declaración
#todo bien.


# ///////////////////////////////////////////////////////////////
def comida(nombre, comida='no tengo hambre'):
    print(f'soy {nombre}, y me gusta {comida}')

comida('Gerardo', 'los shawarmas ')