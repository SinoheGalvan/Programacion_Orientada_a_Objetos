from coches import *

# Solicitar los datos que posteriormente seran los atributos del objeto

# num_coches=int(input("¿Cuantos coches tienes? "))

# for i in range(0,num_coches):
#     print(f"\n\t ... Datos del Automovil #{i+1} ...")
#     marca = input("Ingresar marca del auto: ").upper()
#     color = input("Ingresar el color: ").upper()
#     modelo = input("Ingresar el modelo: ").upper()
#     velocidad = int(input("Ingresar la velocidad: ").upper())
#     potencia = int(input("Ingresar la potencia: ").upper())
#     plazas = int(input("Ingresar el # de plazas: ").upper())

#     coche1 = Coches(marca,color,modelo,velocidad,potencia,plazas)

#     print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}")

coche=Coches("VW","Blanco","2020",220,180,4)
print(coche.color,coche.acelerar())

camion=Camiones("Volvo","Blanco aperlado","2020",220,180,4,2,2500)
print(camion.color,camion.acelerar())

camioneta=Camionetas("VW","Azul","2020",220,180,4,"delantera",True)
print(camioneta.color,camioneta.acelerar())

# coche1=Coches("VW","Blanco","2022",220,150,5)
# coche2=Coches("Nissan","Azul","2020",180,150,6)
# coche3=Coches("Honda","","",0,0,0)
# coche1.num_serie="B0124535345"
# coche4=Coches("","","",0,0,0)
# coche4.marca2="Volvo"
# print(coche4.marca2)

# 

# print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

# print(coche3.marca2)