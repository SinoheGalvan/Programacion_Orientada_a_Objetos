from tkinter import *
from tkinter import messagebox
from controller import controlador1

class View:
    def __init__(self,ventana):
        self.ventana = ventana
        ventana.title("Gestion de Notas")
        ventana.geometry("800x600")
        ventana.resizable(0,0)

        self.interfaz_principal(ventana)

    @staticmethod
    def limpiar_pantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def interfaz_principal(ventana):
        View.limpiar_pantalla(ventana)
        lbl_titulo = Label(ventana, text=".:: Gestion de Notas ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)

        btn_registro = Button(ventana, text="1.- Registro", command=lambda: View.interfaz_registro(ventana), justify=CENTER)
        btn_registro.pack(pady=15)

        btn_login = Button(ventana, text="2.- Login", command=lambda: View.interfaz_login(ventana), justify=CENTER)
        btn_login.pack(pady=15)

        btn_salir = Button(ventana, text="3.- Salir", command=ventana.quit, justify=CENTER)
        btn_salir.pack(pady=15)

    @staticmethod
    def interfaz_registro(ventana):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=".:: Registro en el sistema ::.")
        lbl_titulo.pack(pady=2)

        lbl_nombre = Label(ventana, text="¿Cuál es tu nombre?")
        lbl_nombre.pack(pady=10)

        nombre = StringVar()
        txt_nombre = Entry(ventana, textvariable=nombre)
        txt_nombre.focus()
        txt_nombre.pack(pady=15)
        
        lbl_apellidos = Label(ventana, text="¿Cuales son tus apellidos?")
        lbl_apellidos.pack(pady=10)

        apellidos = StringVar()
        txt_apellidos = Entry(ventana, textvariable=apellidos)
        txt_apellidos.pack(pady=15)

        lbl_email = Label(ventana, text="Ingresa tu email")
        lbl_email.pack(pady=10)

        email = StringVar()
        txt_email = Entry(ventana, textvariable=email)
        txt_email.pack(pady=15)

        lbl_password = Label(ventana, text="Ingresa tu contraseña")
        lbl_password.pack(pady=10)

        password = StringVar()
        txt_password = Entry(ventana, show="*", textvariable=password)
        txt_password.pack(pady=15)

        btn_registrar = Button(ventana, text="Registrar", command=lambda: {
            controlador1.Controlador.registro(nombre.get(),apellidos.get(),email.get(),password.get()),
                                               View.interfaz_login(ventana) }, justify=CENTER)
        btn_registrar.pack(pady=15)

        btn_volver = Button(ventana, text="Volver", justify=CENTER, command=lambda: View.interfaz_principal(ventana))
        btn_volver.pack(pady=15)

    @staticmethod
    def interfaz_login(ventana):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=".:: Inicio de Sesión ::.")
        lbl_titulo.pack(pady=2)

        lbl_email = Label(ventana, text="Ingresa tu email")
        lbl_email.pack(pady=10)

        txt_email = Entry(ventana)
        txt_email.focus()
        txt_email.pack(pady=15)

        lbl_password = Label(ventana, text="Ingresa tu contraseña")
        lbl_password.pack(pady=10)

        txt_password = Entry(ventana, show="*")
        txt_password.pack(pady=15)

        btn_login = Button(ventana, text="Iniciar Sesion", command=lambda:  controlador1.Controlador.inicio_sesion(ventana,txt_email.get(),txt_password.get()), justify=CENTER)
        btn_login.pack(pady=15)

        btn_volver = Button(ventana, text="Volver", justify=CENTER, command=lambda: View.interfaz_principal(ventana))
        btn_volver.pack(pady=15)

    @staticmethod
    def interfaz_menu_notas(ventana,usuario_id,nombre,apellidos):
        global id_user, nom_user, ape_user
        id_user = usuario_id
        nom_user = nombre
        ape_user = apellidos

        View.limpiar_pantalla(ventana)

        lbl_bienvenida = Label(ventana, text=f".:: Bienvenido {nombre} {apellidos}, has iniciado sesión ::.")
        lbl_bienvenida.pack(pady=10)

        btn_crear = Button(ventana, text="1.- Crear", command=lambda: View.interfaz_crear(ventana), justify=CENTER)
        btn_crear.pack(pady=15)

        btn_mostrar = Button(ventana, text="2.- Mostrar", command=lambda: View.interfaz_mostrar(ventana), justify=CENTER)
        btn_mostrar.pack(pady=15)

        btn_cambiar = Button(ventana, text="3.- Cambiar", command=lambda: View.interfaz_cambiar(ventana, id_user ,nom_user,ape_user), justify=CENTER)
        btn_cambiar.pack(pady=15)

        btn_eliminar = Button(ventana, text="4.- Eliminar", command=lambda: View.interfaz_eliminar(ventana), justify=CENTER)
        btn_eliminar.pack(pady=15)

        btn_regresar = Button(ventana, text="5.- Regresar", command=lambda: View.interfaz_login(ventana), justify=CENTER)
        btn_regresar.pack(pady=15)

    @staticmethod
    def interfaz_crear(ventana):
        View.limpiar_pantalla(ventana)

        lbl_bienvenida = Label(ventana, text=f".:: Crear Nota ::.")
        lbl_bienvenida.pack(pady=10)

        lbl_email = Label(ventana, text="Titulo:")
        lbl_email.pack(pady=10)

        nota_titulo = StringVar()
        txt_email = Entry(ventana)
        txt_email.focus()
        txt_email.pack(pady=15)

        lbl_password = Label(ventana, text="Descripción:")
        lbl_password.pack(pady=10)

        nota_titulo = StringVar()
        txt_nombre = Entry(ventana, show="*")
        txt_nombre.pack(pady=15)

        btn_guardar= Button(ventana, text="Guardar", command="", justify=CENTER)
        btn_guardar.pack(pady=15)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.interfaz_menu_notas(ventana,id_user,nom_user,ape_user), justify=CENTER)
        btn_volver.pack(pady=15)

    @staticmethod
    def interfaz_mostrar(ventana):
        View.limpiar_pantalla(ventana)
        
        lbl_bienvenida = Label(ventana, text=f"[Nombre y apellidos], tus notas son:")
        lbl_bienvenida.pack(pady=10)

        # ope = operaciones.Operaciones.consultar()
        # if len(ope)>0:
        #     for fila in ope:
        #         num_ope = 1
        #         calculo = Label(ventana, text=f"Operacion {num_ope} ID: {fila[0]} Fecha de Creación: {fila[1]} \n Operacion: {fila[2]} {fila[4]} {fila[3]} = {fila[5]}")
        #         num_ope+=1
        #         calculo.pack()

        filas = ""
        registros=[("1","100","Nota 1","Descripcion de la nota 1","2025-11-24")]
        num_nota = 1
        if len(registros)>0:
            for fila in registros:
                filas = filas + f"Nota: {num_nota}\n ID {fila[0]} .- Título: {fila[2]}. Fecha de creacion: {fila[4]} \n Descripción: {fila[3]} "
                num_nota+=1
        else:
            messagebox.showinfo(icon="warning", message="...¡NO existen notas para este usuario!...")

        lbl_resultado = Label(ventana, text=f"{filas}")
        lbl_resultado.pack(pady=10)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.interfaz_menu_notas(ventana), justify=CENTER)
        btn_volver.pack(pady=10)

    @staticmethod
    def interfaz_cambiar(ventana, id_user, nom_user, ape_user):
        View.limpiar_pantalla(ventana)

        lbl_bienvenida = Label(ventana, text=f".:: {nom_user} {ape_user}, vamos a modificar una Nota ::.")
        lbl_bienvenida.pack(pady=10)

        lbl_id = Label(ventana, text="ID de la Nota a cambiar:")
        lbl_id.pack(pady=10)

        id = IntVar()
        txt_id = Entry(ventana)
        txt_id.focus()
        txt_id.pack(pady=15)

        lbl_titulo = Label(ventana, text="Nuevo titulo:")
        lbl_titulo.pack(pady=10)

        titulo = StringVar()
        txt_titulo = Entry(ventana)
        txt_titulo.pack(pady=15)

        lbl_descripcion = Label(ventana, text="Nueva Descripción:")
        lbl_descripcion.pack(pady=10)

        descripcion = StringVar()
        txt_descripcion = Entry(ventana)
        txt_descripcion.pack(pady=15)

        btn_guardar= Button(ventana, text="Guardar", command=lambda: controlador1.Controlador.cambiar(ventana, id_user ,id.get(),titulo.get(),descripcion.get()), justify=CENTER)
        btn_guardar.pack(pady=15)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.interfaz_menu_notas(ventana), justify=CENTER)
        btn_volver.pack(pady=15)

    @staticmethod
    def interfaz_eliminar(ventana):
        View.limpiar_pantalla(ventana)

        lbl_bienvenida = Label(ventana, text=f".:: [nombre y apellidos], vamos a eliminar una Nota ::.")
        lbl_bienvenida.pack(pady=10)

        lbl_id = Label(ventana, text="ID de la Nota a eliminar:")
        lbl_id.pack(pady=10)

        id = IntVar()
        txt_id = Entry(ventana)
        txt_id.focus()
        txt_id.pack(pady=15)

        btn_eliminar= Button(ventana, text="Eliminar", command="", justify=CENTER)
        btn_eliminar.pack(pady=15)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.interfaz_menu_notas(ventana), justify=CENTER)
        btn_volver.pack(pady=15)