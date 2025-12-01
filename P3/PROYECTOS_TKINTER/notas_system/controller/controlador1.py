from tkinter import messagebox
from model import usuario,nota
from view import view1

class Controlador:
    @staticmethod
    def registro(nombre, apellidos, email, password):
        resultado = usuario.Usuarios.registrar(nombre, apellidos, email, password)
        if resultado:
            messagebox.showinfo(icon='info',title="Usuarios" ,message=f"{nombre} {apellidos}, se registro correctamente, con el email: {email}")
        else:
            messagebox.showwarning(icon="warning", title="Usuarios", message=f"\n\t ** Por favor intentelo de nuevo, no fue posible insertar el registro ** ...")  

    @staticmethod
    def inicio_sesion(ventana,email, password):
        registro = usuario.Usuarios.iniciar_sesion(email, password)
        if registro:
            messagebox.showinfo(icon='info',title="Usuarios" ,message=f"{registro[1]} {registro[2]}, iniciaste sesión correctamente")
            view1.View.interfaz_menu_notas(ventana,registro[0],registro[1],registro[2])
        else:
            messagebox.showwarning(icon="warning", title="Usuarios", message=f"Email y/o contraseña incorrectas... vuelva a intentarlo ...")  
        
    @staticmethod
    def insertar(usuario_id,titulo,descripcion):
        respuesta = nota.Notas.crear(usuario_id,titulo,descripcion)
        Controlador.respuesta_sql(respuesta) 

    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            messagebox.showinfo(title="Correcto", icon="info", message="Acción realizada con éxito")
        else:
            messagebox.showinfo(title="Atención", icon="warning", message="No se ha podido realizar la operación con éxito")