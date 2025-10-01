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
os.system("clear")

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

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
      pass

    def frenar(self):
      pass  

#Fin definir clase

#Crear un objetos o instanciar la clase

coche1=Coches()
coche1.marca="VW"
coche1.color="Blanco"
coche1.modelo="2022"
coche1.velocidad=220
coche1.caballaje=150
coche1.plazas=5

print(f"Datos del Vehiculo: \n Marca:{coche1.marca} \n color: {coche1.color} \n Modelo: {coche1.modelo} \n velocidad: {coche1.velocidad} \n caballaje: {coche1.caballaje} \n plazas: {coche1.plazas} ")

coche2=Coches()

coche2.marca="Nissan"
coche2.color="Azul"
coche2.modelo="2020"
coche2.velocidad=180
coche2.caballaje=150
coche2.plazas=6

print(f"\nDatos del Vehiculo: \n Marca:{coche2.marca} \n color: {coche2.color} \n Modelo: {coche2.modelo} \n velocidad: {coche2.velocidad} \n caballaje: {coche2.caballaje} \n plazas: {coche2.plazas} ")