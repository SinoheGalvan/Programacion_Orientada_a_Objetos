from tkinter import messagebox
from tkinter import *
from model import operaciones
from view import interfaz

class Funciones:
    @staticmethod
    def operaciones(n1,n2,signo):
        if signo == "+":
            ope = n1 + n2
            tipo_ope = "Suma"
        elif signo == "-":
            ope = n1 - n2 
            tipo_ope = "Resta"
        elif signo == "x":
            ope = n1 * n2 
            tipo_ope = "Multiplicacion"
        elif signo == "/":
            ope = n1 / n2 
            tipo_ope = "Division"

        #messagebox.showinfo(title=tipo_ope, icon="info", message=f"{n1}{signo}{n2}={ope}")
        resultado=messagebox.askquestion(message=f"{n1}{signo}{n2}={ope}\n\n¿Deseas guardar la operacion en la base de datos?",icon="question")
        if resultado=="yes":
             respuesta = operaciones.Operaciones.insertar(n1,n2,signo,ope)
             Funciones.respuesta_sql(respuesta)
     
    @staticmethod
    def consultar_operaciones(ventana):
        ope = operaciones.Operaciones.consultar()
        if len(ope)>0:
            for fila in ope:
                num_ope = 1
                calculo = Label(ventana, text=f"Operacion {num_ope} ID: {fila[0]} Fecha de Creación: {fila[1]} \n Operacion: {fila[2]} {fila[4]} {fila[3]} = {fila[5]}")
                num_ope+=1
                calculo.pack()

    @staticmethod
    def checar_operacion(id):
        operacion = operaciones.Operaciones.consultar_por_id(id)
        if operacion:
            operaciones.Operaciones.traer_por_id(id)
            interfaz.Vista.actualizar_campos()
        else:
            messagebox.showwarning(title="Atencion", icon="warning",message="No existe la operacion en la base de datos")


    @staticmethod
    def actualizar_operaciones(n1,n2,signo,resultado,id):
        respuesta = operaciones.Operaciones.actualizar(n1,n2,signo,resultado,id)
        Funciones.respuesta_sql(respuesta)

    @staticmethod
    def eliminar_operaciones(id):
        respuesta = operaciones.Operaciones.eliminar(id)
        Funciones.respuesta_sql(respuesta)

    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            messagebox.showinfo(title="Correcto", icon="info", message="Acción realizada con éxito")
        else:
            messagebox.showinfo(title="Atención", icon="warning", message="No se ha podido realizar la operación con éxito")

# def resultado(tipo,operacion):
#     messagebox.showinfo(title=f"{tipo}", message=f"El resultado de la {tipo} es: {operacion}")

# def suma(n1,n2):
#     tipo = "suma"
#     operacion = n1 + n2
#     resultado(tipo,operacion)

# def resta(n1,n2):    
#     tipo = "resta"
#     operacion = n1 - n2
#     resultado(tipo,operacion)

# def multiplicacion(n1,n2):    
#     tipo = "multiplicacion"
#     operacion = n1 * n2
#     resultado(tipo,operacion)
    
# def division(n1,n2):    
#     if n2 == 0:
#         messagebox.showwarning(message="No se puede dividir entre cero")
#     else:
#         tipo = "division"
#         operacion = n1 / n2
        
#     resultado(tipo,operacion)