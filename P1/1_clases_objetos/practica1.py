'''

Crear un programa donde se realice el calculo del área de un rectangulo:
1. Con programación estructurada
2. Con programación orientada a objetos

'''
#area de un rectangulo con Programación Estructurada
a = float(input("Ingrese el ancho del rectangulo: "))
l = float(input("Ingrese el largo del rectangulo: "))
print(f"El área del rectangulo es de: {a*l} ")

#Area de un rectangulo con POO
class Figuras:
    def __init__(self,base,largo):
        self._a=base
        self._b=largo

    def area(self):
        return self._a*self._b
    
a = float(input("Ingrese el ancho del rectangulo: "))
b = float(input("Ingrese el ancho del rectangulo: "))

rectangulo = Figuras(a,b)

print(f"Area del rectangulo: {rectangulo.area()}")