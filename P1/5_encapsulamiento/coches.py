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
      self._marca=marca
      self._color=color
      self._modelo=modelo
      self._velocidad=velocidad
      self._caballaje=caballaje
      self._plazas=plazas
      
    #Crear los metodos setters y getters. Estos metodos son importantes y necesarios en todas las clases pqra que el programador interactue con los valores de los atributos a traves de estos metodos .. digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la case a traves de un objeto.
    #En teoria se deberia de crear un metodo Getters y Setters por cada atributo que contega la clase
    #Los metodos get siempre regresan valor, es decir, el valor de la propiedad a traves del return
    #Por otro lado, el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

   def getMarca(self):
      return self._marca
    
   def setMarca(self,marca):
      self._marca = marca

    #2da forma

   @property
   def marca2(self):
      return self._marca
    
   @marca2.setter
   def marca2(self,marca):
      self._marca = marca

   def getColor(self):
      return self._marca
      
   def setColor(self,color):
      self._color = color

   def getModelo(self):
      return self._modelo
      
   def setModelo(self,modelo):
      self._modelo = modelo

   def getVelocidad(self):
      return self._velocidad
      
   def setVelocidad(self,velocidad):
      self._velocidad = velocidad

   def getCaballaje(self):
      return self._caballaje
      
   def setCaballaje(self,caballaje):
      self._caballaje = caballaje

   def getPlazas(self):
      return self._plazas
      
   def setPlazas(self,plazas):
      self._plazas = plazas

    #Metodos o acciones o funciones que hace el objeto 

   def acelerar(self):
      pass

   def frenar(self):
      pass

#Fin definir clase
