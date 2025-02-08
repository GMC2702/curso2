
class Carrito:
    def agregar_carro(self,marca,modelo,color,año):
        self.marca= marca
        self.modelo= modelo
        self.color= color
        self.año= año
    def mostrar_informacion(self):
        print(f"El coche es: {self.marca, self.modelo, self.color, self.año}")

carro = Carrito()
carro.agregar_carro("Toyota", "Yaris", "Mandarina", "2005")
carro.mostrar_informacion()

# class Restaurante:
#     def agregar_restaurante(self,nombre): #El self se requiere para guardar.
#         self.nombre = nombre #el atributo de la clase donde se almacenan datos.
#         print(f"agregar restaurante...{self.nombre}")
#     def mostrar_informacion(self):
#         print(f"El nombre del restaurante es: {self.nombre}")


#Instanciar la clase
# restaurante = Restaurante()
# restaurante.agregar_restaurante("El pollo loco")
# restaurante.mostrar_informacion()


#Puedo crear diferentes objetos usando una misma clase

# restaurante2 = Restaurante()
# restaurante2.agregar_restaurante("El cochino andante")
# restaurante2.mostrar_informacion()

# #imprimir los objetos
