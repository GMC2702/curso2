class Carrito:

    def __init__(self, marca, modelo): #CONSTRUCTOR DE CLASE
       self.marca = marca
       self.modelo = modelo
    
def encender(self):
    self.encendido = True
    print("el carro ha encendido.")

def apagar(self):
    self.encendido = False
    print("El carro ha apagado")

def acelerar(self):
    if self.encendido:
        print("El carro está acelerando.")
    else:
        print("El carro ha apagado")

#Creamos un objeto de la clase carro
carro = Carrito("Toyota", "Corolla, Blanco")

#Acceder a los atributos del objeto
print(carro.marca) #imprime: toyota

#llamar un método del objeto
carro.encender()
carro.acelerar()

#medico q dice q opera, especialidad, si está operando o no