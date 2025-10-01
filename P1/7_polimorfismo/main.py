from coches import *

import os

os.system("cls")

# Solicitar los datos que posteriormente seran los atributos del objeto

def autos():
    print(f"\n\t ... Datos del vehiculo ...")
    marca = input("Ingresar marca del auto: ").upper()
    color = input("Ingresar el color: ").upper()
    modelo = input("Ingresar el modelo: ").upper()
    velocidad = int(input("Ingresar la velocidad: ").upper())
    potencia = int(input("Ingresar la potencia: ").upper())
    plazas = int(input("Ingresar el # de plazas: ").upper())

    coche = Coches(marca,color,modelo,velocidad,potencia,plazas)

    print(f"Datos del Vehiculo: \n Marca:{coche.marca} \n color: {coche.color} \n Modelo: {coche.modelo} \n velocidad: {coche.velocidad} \n caballaje: {coche.caballaje} \n plazas: {coche.plazas}")

def camionetas():
    print(f"\n\t ... Datos del vehiculo ...")
    marca = input("Ingresar marca del auto: ").upper()
    color = input("Ingresar el color: ").upper()
    modelo = input("Ingresar el modelo: ").upper()
    velocidad = int(input("Ingresar la velocidad: ").upper())
    potencia = int(input("Ingresar la potencia: ").upper())
    plazas = int(input("Ingresar el # de plazas: ").upper())
    traccion = input("Ingresar el tipo de traccion: ").upper()
    cerrada = input("Ingresar SI/NO si es cerrada o no: ").upper().strip()
    if cerrada == "SI":
        cerrada=True
    else:
        cerrada=False

    coche = Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)

    print(f"Datos del Vehiculo: \n Marca:{coche.marca} \n color: {coche.color} \n Modelo: {coche.modelo} \n velocidad: {coche.velocidad} \n caballaje: {coche.caballaje} \n plazas: {coche.plazas} \n traccion: {coche.traccion} \n cerrada: {coche.cerrada}")

def camiones():
    print(f"\n\t ... Datos del vehiculo # ...")
    marca = input("Ingresar marca del auto: ").upper()
    color = input("Ingresar el color: ").upper()
    modelo = input("Ingresar el modelo: ").upper()
    velocidad = int(input("Ingresar la velocidad: ").upper())
    potencia = int(input("Ingresar la potencia: ").upper())
    plazas = int(input("Ingresar el # de plazas: ").upper())
    eje = int(input("Ingresar el # de ejes: "))
    capacidadCarga = int(input("Ingresar la capacidad de carga: "))

    coche = Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)

    print(f"Datos del Vehiculo: \n Marca:{coche.marca} \n color: {coche.color} \n Modelo: {coche.modelo} \n velocidad: {coche.velocidad} \n caballaje: {coche.caballaje} \n plazas: {coche.plazas} \n # de Ejes: {coche.eje} \n cerrada: {coche.capacidadCarga}")

opcion=1
while opcion!="4":
    os.system("cls")
    opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.- Autos\n\t2.- Camionetas\n\t3.- Camiones\n\t4.- Salir\n\t Elige una opción: ").lower().strip()
    match opcion:
        case "1":
            autos()
            input("Oprima tecla para continuar")
        case "2":
            print("Camionetas")
            input("Oprima tecla para continuar")
        case "3":
            print("Camiones")
            input("Oprima tecla para continuar")
        case "4":
            print("Salir del sistema")
        case _:
            input("Opcion invalida .... intente de nuevo")

# coche=Coches("VW","Blanco","2020",220,180,4)
# print(coche.color,coche.acelerar())

# camion=Camiones("Volvo","Blanco aperlado","2020",220,180,4,2,2500)
# print(camion.color,camion.acelerar())

# camioneta=Camionetas("VW","Azul","2020",220,180,4,"delantera",True)
# print(camioneta.color,camioneta.acelerar())

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