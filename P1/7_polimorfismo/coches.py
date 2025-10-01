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
      self.plazas=plazas
      
    #Crear los metodos setters y getters. Estos metodos son importantes y necesarios en todas las clases pqra que el programador interactue con los valores de los atributos a traves de estos metodos .. digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la case a traves de un objeto.
    #En teoria se deberia de crear un metodo Getters y Setters por cada atributo que contega la clase
    #Los metodos get siempre regresan valor, es decir, el valor de la propiedad a traves del return
    #Por otro lado, el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

   @property
   def marca(self):
      return self._marca
    
   @marca.setter
   def marca(self,marca):
      self._marca = marca

   @property
   def color(self):
      return self._color
      
   @color.setter
   def color(self,color):
      self._color = color

   @property
   def modelo(self):
      return self._modelo
      
   @modelo.setter
   def modelo(self,modelo):
      self._modelo = modelo

   @property
   def velocidad(self):
      return self._velocidad
      
   @velocidad.setter
   def velocidad(self,velocidad):
      self._velocidad = velocidad

   @property
   def caballaje(self):
      return self._caballaje
      
   @caballaje.setter
   def caballaje(self,caballaje):
      self._caballaje = caballaje

   @property
   def plazas(self):
      return self._plazas
      
   @plazas.setter
   def plazas(self,plazas):
      self._plazas = plazas

    #Metodos o acciones o funciones que hace el objeto 

   def acelerar(self):
      return "Estas acelerando el coche"

   def frenar(self):
      return "Estas frenando el coche"

#Fin definir clase

class Camiones(Coches):
   def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
      super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
      self.__eje = eje
      self.__capacidadCarga = capacidadCarga

   def cargar(self,tipo_carga):
      self.tipo_carga = tipo_carga
      return self.tipo_carga
   
   def acelerar(self):
      return "Estas acelerando el camion"
   
   def frenar(self):
      return "Estas frenando el camion"

   @property
   def eje(self):
      return self.__eje
   
   @eje.setter
   def eje(self,eje):
      self.__eje=eje

   @property
   def capacidadCarga(self):
      return self.__capacidadCarga
   
   @capacidadCarga.setter
   def capacidadCarga(self,capacidadCarga):
      self.__capacidadCarga=capacidadCarga

class Camionetas(Coches):
   def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
      super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
      self.__traccion = traccion
      self.__cerrada = cerrada

   def transportar(self,num_pasajeros):
      self.num_pasajeros = num_pasajeros
      return self.tipo_carga
   
   def acelerar(self):
      return "Estas acelerando la camioneta"
   
   def frenar(self):
      return "Estas frenando la camioneta"

   @property
   def traccion(self):
      return self.__traccion
   
   @traccion.setter
   def eje(self,traccion):
      self.__traccion=traccion

   @property
   def cerrada(self):
      return self.__cerrada
   
   @cerrada.setter
   def cerrada(self,cerrada):
      self.__cerrada=cerrada