'''

Ejercicio Practico #3 Modelar y Diagramar un sistema de escuela

'''

import os

os.system("cls")

class Alumnos:
    def __init__(self,_matricula,_nombre,_edad):
        self._matricula=_matricula
        self._nombre=_nombre
        self._edad=_edad

    def inscribirse():
        pass

    def estudiar():
        pass

    def getMatricula(self):
        return self._matricula
    
    def setMatricula(self,_matricula):
        self._matricula = _matricula
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self,_nombre):
        self._nombre = _nombre

    def getEdad(self):
        return self._edad
    
    def setEdad(self,_edad):
        self._edad = _edad

class Cursos:
    def __init__(self,_codigo,_nombre,_creditos):
        self._codigo=_codigo
        self._nombre=_nombre
        self._creditos=_creditos
    
    def asignar():
        pass

    def getCodigo(self):
        return self._codigo
    
    def setCodigo(self,_codigo):
        self._codigo = _codigo
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self,_nombre):
        self._nombre = _nombre

    def getCreditos(self):
        return self._creditos
    
    def setCreditos(self,_creditos):
        self._creditos = _creditos

class Profesores:
    def __init__(self,_num_profesor,_nombre,_experiencia):
        self._num_profesor=_num_profesor
        self._nombre=_nombre
        self._experiencia=_experiencia

    def impartir():
        pass

    def evaluar():
        pass

    def getNumProfesor(self):
        return self._num_profesor
    
    def setNumProfesor(self,_num_profesor):
        self._num_profesor = _num_profesor
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self,_nombre):
        self._nombre = _nombre

    def getExperiencia(self):
        return self._experiencia
    
    def setExperiencia(self,_experiencia):
        self._experiencia = _experiencia

alumno1 = Alumnos("84789372","Rodrigo",18)
alumno2 = Alumnos("70217387","Karla",20)
alumno3 = Alumnos("93748173","Diego",21)

curso1 = Cursos("28394753","Quimica",50)
curso2 = Cursos("0393842","Calculo Diferencial",60)
curso3 = Cursos("0373918","Etica",30)

profesor1 = Profesores("6418","Juan",4)
profesor2 = Profesores("0192","Pablo",8)
profesor3 = Profesores("8394","Enrique",1)

