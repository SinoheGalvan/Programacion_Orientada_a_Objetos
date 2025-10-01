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
    #Metodo constructor par inicializar los valores de los atributos a la hora e crear o instanciar el objeto de la clase
   def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
      self.marca=marca
      self.color=color
      self.modelo=modelo
      self.velocidad=velocidad
      self.caballaje=caballaje
      self.plazas=plazas

   def __init__(self):
      self.marca=""
      self.color=""
      self.modelo=""
      self.velocidad=0
      self.caballaje=0
      self.plazas=0

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

coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda","","",0,0,0)
coche1.num_serie="B0124535345"
coche4=Coches("","","",0,0,0)
coche4.marca2="Volvo"
print(coche4.marca2)

print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} \n Numero de serie: {coche1.num_serie} ")

print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

print(coche3.marca2)
