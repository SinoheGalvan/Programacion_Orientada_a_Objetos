from tkinter import messagebox

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
    
    messagebox.showinfo(title=tipo_ope, icon="info", message=f"{n1}{signo}{n2}={ope}")


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