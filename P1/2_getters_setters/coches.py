'''


Consideraciones importantes:
- Que no tenga método constructor (__init__)
- Que todos los atributos sean publicos 
- Que los métodos de acelerar y frenar no hagan cambios (Pass)

'''

'''

import os

os.system("cls")

class Coches:
    marca=""
    color=""
    modelo=""
    velocidad=0
    caballaje=0
    plazas=0

    def acelerar():
        pass

    def frenar():
        pass

coche1 = Coches()
coche1.marca = 'VM'
coche1.color = 'Bslanco'
coche1.modelo = '2022'
coche1.velocidad = 220
coche1.caballaje = 150
coche1.plazas = 5

coche2 = Coches()
coche2.marca = 'Nissan'
coche2.color = 'Azul'
coche2.modelo = '2020'
coche2.velocidad = 180
coche2.caballaje = 150
coche2.plazas = 6

print("Coche 1:")
print(f"Marca: {coche1.marca}, Color: {coche1.color}, Modelo: {coche1.modelo}")
print(f"Velocidad: {coche1.velocidad}, Caballaje: {coche1.caballaje}, Plazas: {coche1.plazas}")

print("\nCoche 2:")
print(f"Marca: {coche2.marca}, Color: {coche2.color}, Modelo: {coche2.modelo}")
print(f"Velocidad: {coche2.velocidad}, Caballaje: {coche2.caballaje}, Plazas: {coche2.plazas}")

'''
import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    marca=""
    color=""
    modelo=""
    velocidad=0
    caballaje=0
    plazas=0

    #Crear los metodos setters y getters. Estos metodos son importantes y necesarios en todas las clases pqra que el programador interactue con los valores de los atributos a traves de estos metodos .. digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la case a traves de un objeto.
    #En teoria se deberia de crear un metodo Getters y Setters por cada atributo que contega la clase
    #Los metodos get siempre regresan valor, es decir, el valor de la propiedad a traves del return
    #Por otro lado, el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

    #1er forma

    def getMarca(self):
       return self.marca
    
    def setMarca(self,marca):
       self.marca = marca

    #2da forma

    @property
    def marca2(self):
       return self.marca
    
    @marca2.setter
    def marca2(self,marca):
       self.marca = marca

    def getColor(self):
       return self.marca
    
    def setColor(self,color):
       self.color = color

    def getModelo(self):
       return self.modelo
    
    def setModelo(self,modelo):
       self.modelo = modelo

    def getVelocidad(self):
       return self.velocidad
    
    def setVelocidad(self,velocidad):
       self.marca = velocidad

    def getCaballaje(self):
       return self.caballaje
    
    def setCaballaje(self,caballaje):
       self.marca = caballaje

    def getPlazas(self):
       return self.plazas
    
    def setPlazas(self,plazas):
       self.marca = plazas

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
      pass

    def frenar(self):
      pass  

#Fin definir clase

#Crear un objetos o instanciar la clase

coche1=Coches()
coche1.setMarca("VW")
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)

coche2=Coches()
coche1.setMarca("Nissan")
coche1.setColor("Azul")
coche1.setModelo("2020")
coche1.setVelocidad(180)
coche1.setCaballaje(150)
coche1.setPlazas(6)

coche3=Coches()
coche3.marca2="Honda"
print(coche3.marca2)

print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} ")

print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

# coche1.marca="VW"
# coche1.color="Blanco"
# coche1.modelo="2022"
# coche1.velocidad=220
# coche1.caballaje=150
# coche1.plazas=5
# coche2.marca="Nissan"
# coche2.color="Azul"
# coche2.modelo="2020"
# coche2.velocidad=180
# coche2.caballaje=150
# coche2.plazas=6

# print(f"Datos del Vehiculo: \n Marca:{coche1.marca} \n color: {coche1.color} \n Modelo: {coche1.modelo} \n velocidad: {coche1.velocidad} \n caballaje: {coche1.caballaje} \n plazas: {coche1.plazas} ")

# print(f"\nDatos del Vehiculo: \n Marca:{coche2.marca} \n color: {coche2.color} \n Modelo: {coche2.modelo} \n velocidad: {coche2.velocidad} \n caballaje: {coche2.caballaje} \n plazas: {coche2.plazas} ")
