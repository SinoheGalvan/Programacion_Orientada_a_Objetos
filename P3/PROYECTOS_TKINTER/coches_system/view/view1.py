from tkinter import *
from tkinter import messagebox

class View:
    def __init__(self,ventana):
        self.ventana = ventana
        ventana.title("Coches")
        ventana.geometry("800x800")
        ventana.resizable(0,0)

        self.menu_principal(ventana)

    @staticmethod
    def limpiar_pantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def agarrar_tipo(tipo_auto):
        pass

    @staticmethod
    def menu_principal(ventana):
        View.limpiar_pantalla(ventana)
        lbl_titulo = Label(ventana, text=".:: Sistema de gestion de Coches ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)

        btn_registro = Button(ventana, text="Autos", command=lambda: View.menu_acciones(ventana), justify=CENTER)
        btn_registro.pack(pady=15)

        btn_login = Button(ventana, text="Camionetas", command=lambda: View.menu_acciones(ventana), justify=CENTER)
        btn_login.pack(pady=15)

        btn_login = Button(ventana, text="Camiones", command=lambda: View.menu_acciones(ventana), justify=CENTER)
        btn_login.pack(pady=15)

        btn_salir = Button(ventana, text="Salir", command=ventana.quit, justify=CENTER)
        btn_salir.pack(pady=15)

    @staticmethod
    def menu_acciones(ventana):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=".:: Menu de [tipo] ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)

        btn_registro = Button(ventana, text="Insertar", command=lambda: View.insertar_autos(ventana), justify=CENTER)
        btn_registro.pack(pady=15)

        btn_login = Button(ventana, text="Consultar", command=lambda: View.consultar_autos(ventana), justify=CENTER)
        btn_login.pack(pady=15)

        btn_login = Button(ventana, text="Actualizar", command=lambda: View.buscar_id(ventana,"actualizar"), justify=CENTER)
        btn_login.pack(pady=15)

        btn_login = Button(ventana, text="Eliminar", command=lambda: View.buscar_id(ventana,"eliminar"), justify=CENTER)
        btn_login.pack(pady=15)

        btn_salir = Button(ventana, text="Regresar", command=lambda: View.menu_principal(ventana), justify=CENTER)
        btn_salir.pack(pady=15)

    def insertar_autos(ventana):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=".:: Insertar [tipo] ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)

        lbl_marca = Label(ventana, text="Marca: ", justify=CENTER)
        lbl_marca.pack(pady=5)

        txt_marca = Entry(ventana)
        txt_marca.pack(pady=15)

        lbl_color = Label(ventana, text="Color: ", justify=CENTER)
        lbl_color.pack(pady=5)

        txt_color = Entry(ventana)
        txt_color.pack(pady=15)

        lbl_modelo = Label(ventana, text="Modelo: ", justify=CENTER)
        lbl_modelo.pack(pady=5)

        txt_modelo = Entry(ventana)
        txt_modelo.pack(pady=15)

        lbl_velocidad = Label(ventana, text="Velocidad: ", justify=CENTER)
        lbl_velocidad.pack(pady=5)

        txt_velocidad = Entry(ventana)
        txt_velocidad.pack(pady=15)

        lbl_potencia = Label(ventana, text="Potencia: ", justify=CENTER)
        lbl_potencia.pack(pady=5)

        txt_potencia = Entry(ventana)
        txt_potencia.pack(pady=15)

        lbl_num_plazas = Label(ventana, text="Numero de plazas: ", justify=CENTER)
        lbl_num_plazas.pack(pady=5)

        txt_num_plazas = Entry(ventana)
        txt_num_plazas.pack(pady=15)

        btn_insertar = Button(ventana, text="Regresar", command=lambda: View.menu_principal(ventana), justify=CENTER)
        btn_insertar.pack(pady=15)

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana), justify=CENTER)
        btn_regresar.pack(pady=15)

    def consultar_autos(ventana):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=".:: Consultar [tipo] ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)
        

        registro = ["Marca: toyota","Color: blanco","Modelo: 2010","Velocidad: 200","Potencia: 180","Numero de plazas: 4"]


        txt_registro = Text(ventana, height=10, width=30)
        txt_registro.pack()

        for item in registro:
            txt_registro.insert(END, item + "\n")

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana), justify=CENTER)
        btn_regresar.pack(pady=15)

    def buscar_id(ventana,tipo):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=f".:: {tipo} un auto ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)

        lbl_id = Label(ventana, text="Ingresa el ID a buscar: ", justify=CENTER).pack(pady=5)

        id = IntVar()
        txt_id = Entry(ventana)
        txt_id.pack(pady=15)

        if tipo == "actualizar":
            btn_buscar = Button(ventana, text="Buscar", command=lambda: View.cambiar_autos(ventana, id.get()), justify=CENTER).pack(pady=15)
        elif tipo == "eliminar":
            btn_buscar = Button(ventana, text="Buscar", command=lambda: View.borrar_autos(ventana, id.get()), justify=CENTER).pack(pady=15)

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana), justify=CENTER)
        btn_regresar.pack(pady=15)

    def cambiar_autos(ventana,id):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=f".:: Cambiar un auto ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)

        id = IntVar()
        txt_id = Entry(ventana, textvariable=id, justify=RIGHT, width=5, state="readonly")
        txt_id.pack(pady=5)
        
        lbl_marca = Label(ventana, text="Marca: ", justify=CENTER)
        lbl_marca.pack(pady=5)

        txt_marca = Entry(ventana)
        txt_marca.pack(pady=15)

        lbl_color = Label(ventana, text="Color: ", justify=CENTER)
        lbl_color.pack(pady=5)

        txt_color = Entry(ventana)
        txt_color.pack(pady=15)

        lbl_modelo = Label(ventana, text="Modelo: ", justify=CENTER)
        lbl_modelo.pack(pady=5)

        txt_modelo = Entry(ventana)
        txt_modelo.pack(pady=15)

        lbl_velocidad = Label(ventana, text="Velocidad: ", justify=CENTER)
        lbl_velocidad.pack(pady=5)

        txt_velocidad = Entry(ventana)
        txt_velocidad.pack(pady=15)

        lbl_potencia = Label(ventana, text="Potencia: ", justify=CENTER)
        lbl_potencia.pack(pady=5)

        txt_potencia = Entry(ventana)
        txt_potencia.pack(pady=15)

        lbl_num_plazas = Label(ventana, text="Numero de plazas: ", justify=CENTER)
        lbl_num_plazas.pack(pady=5)

        txt_num_plazas = Entry(ventana)
        txt_num_plazas.pack(pady=15)

        btn_cambiar = Button(ventana, text="Guardar", command="", justify=CENTER)
        btn_cambiar.pack(pady=15)

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana), justify=CENTER)
        btn_regresar.pack(pady=15)

    def borrar_autos(ventana,id_auto):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=f".:: Borrar un auto ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)

        lbl_id = Label(ventana, text="ID de la operación: ")
        lbl_id.pack(pady=5)

        id = IntVar()
        txt_id = Entry(ventana, textvariable=id, justify=RIGHT, width=5, state="readonly")
        id.set(id_auto)
        txt_id.focus()
        txt_id.pack(pady=5)

        btn_cambiar = Button(ventana, text="Borrar", command="", justify=CENTER)
        btn_cambiar.pack(pady=15)

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana), justify=CENTER)
        btn_regresar.pack(pady=15)



