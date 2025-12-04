from tkinter import *
from tkinter import messagebox, ttk
from controller import controlador1

class View:
    def __init__(self,ventana):
        self.ventana = ventana
        ventana.title("Coches")
        ventana.geometry("1200x960")
        ventana.resizable(0,0)

        self.menu_principal(ventana)

    @staticmethod
    def limpiar_pantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def menu_principal(ventana):
        View.limpiar_pantalla(ventana)
        lbl_titulo = Label(ventana, text=".:: Sistema de gestion de Coches ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)

        btn_registro = Button(ventana, text="Autos", command=lambda: View.menu_acciones(ventana, "autos"), justify=CENTER)
        btn_registro.pack(pady=15)

        btn_login = Button(ventana, text="Camionetas", command=lambda: View.menu_acciones(ventana, "camionetas"), justify=CENTER)
        btn_login.pack(pady=15)

        btn_login = Button(ventana, text="Camiones", command=lambda: View.menu_acciones(ventana, "camiones"), justify=CENTER)
        btn_login.pack(pady=15)

        btn_salir = Button(ventana, text="Salir", command=ventana.quit, justify=CENTER)
        btn_salir.pack(pady=15)

    @staticmethod
    def menu_acciones(ventana,tipo):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=f".:: Menu de {tipo} ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)

        if tipo == "autos":
            btn_registro = Button(ventana, text="Insertar", command=lambda: View.insertar_autos(ventana), justify=CENTER)
            btn_registro.pack(pady=15)

            btn_login = Button(ventana, text="Consultar", command=lambda: View.consultar_autos(ventana), justify=CENTER)
            btn_login.pack(pady=15)
        
            btn_login = Button(ventana, text="Actualizar", command=lambda: View.buscar_id_autos(ventana,"actualizar"), justify=CENTER)
            btn_login.pack(pady=15)

            btn_login = Button(ventana, text="Eliminar", command=lambda: View.buscar_id_autos(ventana,"eliminar"), justify=CENTER)
            btn_login.pack(pady=15)

        elif tipo == "camionetas":
            btn_registro = Button(ventana, text="Insertar", command=lambda: View.insertar_camionetas(ventana), justify=CENTER)
            btn_registro.pack(pady=15)

            btn_login = Button(ventana, text="Consultar", command=lambda: View.consultar_camionetas(ventana), justify=CENTER)
            btn_login.pack(pady=15)
        
            btn_login = Button(ventana, text="Actualizar", command=lambda: View.buscar_id_camionetas(ventana,"actualizar"), justify=CENTER)
            btn_login.pack(pady=15)

            btn_login = Button(ventana, text="Eliminar", command=lambda: View.buscar_id_camionetas(ventana,"eliminar"), justify=CENTER)
            btn_login.pack(pady=15)

        elif tipo == "camiones":
            btn_registro = Button(ventana, text="Insertar", command=lambda: View.insertar_camiones(ventana), justify=CENTER)
            btn_registro.pack(pady=15)

            btn_login = Button(ventana, text="Consultar", command=lambda: View.consultar_camiones(ventana), justify=CENTER)
            btn_login.pack(pady=15)
        
            btn_login = Button(ventana, text="Actualizar", command=lambda: View.buscar_id_camiones(ventana,"actualizar"), justify=CENTER)
            btn_login.pack(pady=15)

            btn_login = Button(ventana, text="Eliminar", command=lambda: View.buscar_id_camiones(ventana,"eliminar"), justify=CENTER)
            btn_login.pack(pady=15)

        btn_salir = Button(ventana, text="Regresar", command=lambda: View.menu_principal(ventana), justify=CENTER)
        btn_salir.pack(pady=15)

    def insertar_autos(ventana):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=".:: Insertar auto ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)

        lbl_marca = Label(ventana, text="Marca: ", justify=CENTER)
        lbl_marca.pack(pady=5)

        marca = StringVar()
        txt_marca = Entry(ventana, textvariable=marca)
        txt_marca.pack(pady=15)

        lbl_color = Label(ventana, text="Color: ", justify=CENTER)
        lbl_color.pack(pady=5)

        color = StringVar()
        txt_color = Entry(ventana, textvariable=color)
        txt_color.pack(pady=15)

        lbl_modelo = Label(ventana, text="Modelo: ", justify=CENTER)
        lbl_modelo.pack(pady=5)

        modelo = StringVar()
        txt_modelo = Entry(ventana, textvariable=modelo)
        txt_modelo.pack(pady=15)

        lbl_velocidad = Label(ventana, text="Velocidad: ", justify=CENTER)
        lbl_velocidad.pack(pady=5)

        velocidad = StringVar()
        txt_velocidad = Entry(ventana, textvariable=velocidad)
        txt_velocidad.pack(pady=15)

        lbl_caballaje = Label(ventana, text="Caballaje: ", justify=CENTER)
        lbl_caballaje.pack(pady=5)

        caballaje = StringVar()
        txt_caballaje = Entry(ventana, textvariable=caballaje)
        txt_caballaje.pack(pady=15)

        lbl_num_plazas = Label(ventana, text="Numero de plazas: ", justify=CENTER)
        lbl_num_plazas.pack(pady=5)

        num_plazas = StringVar()
        txt_num_plazas = Entry(ventana, textvariable=num_plazas)
        txt_num_plazas.pack(pady=15)

        btn_insertar = Button(ventana, text="Guardar", command=lambda: controlador1.Controller.insertar_auto(marca.get(),color.get(),modelo.get(),velocidad.get(),caballaje.get(),num_plazas.get()), justify=CENTER)
        btn_insertar.pack(pady=15)

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana, "autos"), justify=CENTER)
        btn_regresar.pack(pady=15)

    def consultar_autos(ventana):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=".:: Consultar autos ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)
        
        controlador1.Controller.consultar_auto(ventana)

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana,"autos"), justify=CENTER)
        btn_regresar.pack(pady=15)

    def buscar_id_autos(ventana,tipo):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=f".:: {tipo} un auto ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)

        lbl_id = Label(ventana, text="Ingresa el ID a buscar: ", justify=CENTER).pack(pady=5)

        id = IntVar()
        txt_id = Entry(ventana, textvariable=id)
        txt_id.pack(pady=15)

        if tipo == "actualizar":
            btn_buscar = Button(ventana, text="Buscar", command=lambda: View.cambiar_autos(ventana, id.get()), justify=CENTER).pack(pady=15)
        elif tipo == "eliminar":
            btn_buscar = Button(ventana, text="Buscar", command=lambda: View.borrar_autos(ventana, id.get()), justify=CENTER).pack(pady=15)

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana, "autos"), justify=CENTER)
        btn_regresar.pack(pady=15)

    def cambiar_autos(ventana,id_auto):
        registro = controlador1.Controller.consultar_id_auto(id_auto)

        if registro is None:
            messagebox.showinfo(icon="warning", message=f"No existe un registro con el id {id_auto}")
        else:
            View.limpiar_pantalla(ventana)

            lbl_titulo = Label(ventana, text=f".:: Cambiar un auto ::.", justify=CENTER)
            lbl_titulo.pack(pady=10)

            id = IntVar()
            txt_id = Entry(ventana, textvariable=id, justify=RIGHT, width=5, state="readonly")
            id.set(id_auto)
            txt_id.pack(pady=5)
            
            lbl_marca = Label(ventana, text="Marca: ", justify=CENTER)
            lbl_marca.pack(pady=5)

            marca = StringVar()
            txt_marca = Entry(ventana, textvariable=marca)
            marca.set(registro[1])
            txt_marca.pack(pady=15)

            lbl_color = Label(ventana, text="Color: ", justify=CENTER)
            lbl_color.pack(pady=5)

            color = StringVar()
            txt_color = Entry(ventana, textvariable=color)
            color.set(registro[2])
            txt_color.pack(pady=15)

            lbl_modelo = Label(ventana, text="Modelo: ", justify=CENTER)
            lbl_modelo.pack(pady=5)

            modelo = StringVar()
            txt_modelo = Entry(ventana, textvariable=modelo)
            modelo.set(registro[3])
            txt_modelo.pack(pady=15)

            lbl_velocidad = Label(ventana, text="Velocidad: ", justify=CENTER)
            lbl_velocidad.pack(pady=5)

            velocidad = StringVar()
            txt_velocidad = Entry(ventana, textvariable=velocidad)
            velocidad.set(registro[4])
            txt_velocidad.pack(pady=15)

            lbl_potencia = Label(ventana, text="Caballaje: ", justify=CENTER)
            lbl_potencia.pack(pady=5)

            caballaje = StringVar()
            txt_caballaje = Entry(ventana, textvariable=caballaje)
            caballaje.set(registro[5])
            txt_caballaje.pack(pady=15)

            lbl_num_plazas = Label(ventana, text="Numero de plazas: ", justify=CENTER)
            lbl_num_plazas.pack(pady=5)

            num_plazas = StringVar()
            txt_num_plazas = Entry(ventana, textvariable=num_plazas)
            num_plazas.set(registro[6])
            txt_num_plazas.pack(pady=15)

            btn_cambiar = Button(ventana, text="Guardar", command=lambda: controlador1.Controller.actualizar_auto(marca.get(),color.get(),modelo.get(),velocidad.get(),caballaje.get(),num_plazas.get(),id_auto), justify=CENTER)
            btn_cambiar.pack(pady=15)

            btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana, "autos"), justify=CENTER)
            btn_regresar.pack(pady=15)

    def borrar_autos(ventana,id_auto):
        registro = controlador1.Controller.consultar_id_auto(id_auto)

        if registro is None:
            messagebox.showinfo(icon="warning", message=f"No existe un registro con el id {id_auto}")
        else:
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

            btn_cambiar = Button(ventana, text="Borrar", command=lambda: controlador1.Controller.eliminar_auto(id_auto), justify=CENTER)
            btn_cambiar.pack(pady=15)

            btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana, "autos"), justify=CENTER)
            btn_regresar.pack(pady=15)

    def insertar_camionetas(ventana):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=".:: Insertar camioneta ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)

        lbl_marca = Label(ventana, text="Marca: ", justify=CENTER)
        lbl_marca.pack(pady=5)

        txt_marca = Entry(ventana)
        txt_marca.pack(pady=5)

        lbl_color = Label(ventana, text="Color: ", justify=CENTER)
        lbl_color.pack(pady=5)

        txt_color = Entry(ventana)
        txt_color.pack(pady=5)

        lbl_modelo = Label(ventana, text="Modelo: ", justify=CENTER)
        lbl_modelo.pack(pady=5)

        txt_modelo = Entry(ventana)
        txt_modelo.pack(pady=5)

        lbl_velocidad = Label(ventana, text="Velocidad: ", justify=CENTER)
        lbl_velocidad.pack(pady=5)

        txt_velocidad = Entry(ventana)
        txt_velocidad.pack(pady=5)

        lbl_potencia = Label(ventana, text="Caballaje: ", justify=CENTER)
        lbl_potencia.pack(pady=5)

        txt_caballaje = Entry(ventana)
        txt_caballaje.pack(pady=5)

        lbl_num_plazas = Label(ventana, text="Numero de plazas: ", justify=CENTER)
        lbl_num_plazas.pack(pady=5)

        txt_num_plazas = Entry(ventana)
        txt_num_plazas.pack(pady=5)

        lbl_traccion = Label(ventana, text="Selecciona la tracción: ", justify=CENTER)
        lbl_traccion.pack(pady=5)

        cmb_traccion = ttk.Combobox(ventana, values=["Delantera", "Trasera"])
        cmb_traccion.pack(pady=5)

        lbl_cerrada = Label(ventana, text="¿Es cerrada?", justify=CENTER)
        lbl_cerrada.pack(pady=5)

        cerrada = StringVar()
        rdn_si = Radiobutton(ventana, text="Si", variable=cerrada, value="Si")
        rdn_si.pack()
        rdn_no = Radiobutton(ventana, text="No", variable=cerrada, value="No")
        rdn_no.pack()

        btn_insertar = Button(ventana, text="Guardar", command="", justify=CENTER)
        btn_insertar.pack(pady=5)

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana, "camionetas"), justify=CENTER)
        btn_regresar.pack(pady=15)

    def consultar_camionetas(ventana):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=".:: Consultar camionetas ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)
        

        registro = ["Marca: toyota","Color: blanca","Modelo: 2006","Velocidad: 200","Caballaje: 230","Numero de plazas: 4", "Traccion: Delantera", "Cerrada: No"]


        txt_registro = Text(ventana, height=10, width=30)
        txt_registro.pack()

        for item in registro:
            txt_registro.insert(END, item + "\n")

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana, "camionetas"), justify=CENTER)
        btn_regresar.pack(pady=15)

    def buscar_id_camionetas(ventana,tipo):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=f".:: {tipo} un auto ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)

        lbl_id = Label(ventana, text="Ingresa el ID a buscar: ", justify=CENTER).pack(pady=5)

        id = IntVar()
        txt_id = Entry(ventana)
        txt_id.pack(pady=15)

        if tipo == "actualizar":
            btn_buscar = Button(ventana, text="Buscar", command=lambda: View.cambiar_camionetas(ventana, id.get()), justify=CENTER).pack(pady=15)
        elif tipo == "eliminar":
            btn_buscar = Button(ventana, text="Buscar", command=lambda: View.borrar_camionetas(ventana, id.get()), justify=CENTER).pack(pady=15)

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana, "camionetas"), justify=CENTER)
        btn_regresar.pack(pady=15)

    def cambiar_camionetas(ventana,id):
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

        lbl_potencia = Label(ventana, text="Caballaje: ", justify=CENTER)
        lbl_potencia.pack(pady=5)

        txt_caballaje = Entry(ventana)
        txt_caballaje.pack(pady=15)

        lbl_num_plazas = Label(ventana, text="Numero de plazas: ", justify=CENTER)
        lbl_num_plazas.pack(pady=5)

        txt_num_plazas = Entry(ventana)
        txt_num_plazas.pack(pady=15)

        lbl_traccion = Label(ventana, text="Selecciona la tracción: ", justify=CENTER)
        lbl_traccion.pack(pady=5)

        cmb_traccion = ttk.Combobox(ventana, values=["Delantera", "Trasera"])
        cmb_traccion.pack(pady=5)

        lbl_cerrada = Label(ventana, text="¿Es cerrada?", justify=CENTER)
        lbl_cerrada.pack(pady=5)

        cerrada = StringVar()
        rdn_si = Radiobutton(ventana, text="Si", variable=cerrada, value="Si")
        rdn_si.pack()
        rdn_no = Radiobutton(ventana, text="No", variable=cerrada, value="No")
        rdn_no.pack()

        btn_cambiar = Button(ventana, text="Guardar", command="", justify=CENTER)
        btn_cambiar.pack(pady=15)

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana, "camionetas"), justify=CENTER)
        btn_regresar.pack(pady=15)

    def borrar_camionetas(ventana,id_auto):
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

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana, "camionetas"), justify=CENTER)
        btn_regresar.pack(pady=15)

    def insertar_camiones(ventana):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=".:: Insertar camion ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)

        lbl_marca = Label(ventana, text="Marca: ", justify=CENTER)
        lbl_marca.pack(pady=5)

        txt_marca = Entry(ventana)
        txt_marca.pack(pady=5)

        lbl_color = Label(ventana, text="Color: ", justify=CENTER)
        lbl_color.pack(pady=5)

        txt_color = Entry(ventana)
        txt_color.pack(pady=5)

        lbl_modelo = Label(ventana, text="Modelo: ", justify=CENTER)
        lbl_modelo.pack(pady=5)

        txt_modelo = Entry(ventana)
        txt_modelo.pack(pady=5)

        lbl_velocidad = Label(ventana, text="Velocidad: ", justify=CENTER)
        lbl_velocidad.pack(pady=5)

        txt_velocidad = Entry(ventana)
        txt_velocidad.pack(pady=5)

        lbl_potencia = Label(ventana, text="Caballaje: ", justify=CENTER)
        lbl_potencia.pack(pady=5)

        txt_caballaje = Entry(ventana)
        txt_caballaje.pack(pady=5)

        lbl_num_plazas = Label(ventana, text="Numero de plazas: ", justify=CENTER)
        lbl_num_plazas.pack(pady=5)

        txt_num_plazas = Entry(ventana)
        txt_num_plazas.pack(pady=5)

        lbl_eje = Label(ventana, text="Numero de Ejes: ", justify=CENTER)
        lbl_eje.pack(pady=5)

        txt_eje = Entry(ventana)
        txt_eje.pack(pady=5)

        lbl_capacidad_carga = Label(ventana, text="Capacidad de carga: ", justify=CENTER)
        lbl_capacidad_carga.pack(pady=5)

        txt_num_plazas = Entry(ventana)
        txt_num_plazas.pack(pady=5)


        btn_insertar = Button(ventana, text="Guardar", command="", justify=CENTER)
        btn_insertar.pack(pady=5)

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana, "camiones"), justify=CENTER)
        btn_regresar.pack(pady=15)

    def consultar_camiones(ventana):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=".:: Consultar camiones ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)
        

        registro = ["Modelo: 2006","Color: blanca", "Marca: Volvo","Velocidad: 120","Caballaje: 350","Numero de plazas: 2", "# de Ejes: 3", "Capacidad de Carga: 4000"]


        txt_registro = Text(ventana, height=10, width=30)
        txt_registro.pack()

        for item in registro:
            txt_registro.insert(END, item + "\n")

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana, "camiones"), justify=CENTER)
        btn_regresar.pack(pady=15)

    def buscar_id_camiones(ventana,tipo):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=f".:: {tipo} un auto ::.", justify=CENTER)
        lbl_titulo.pack(pady=10)

        lbl_id = Label(ventana, text="Ingresa el ID a buscar: ", justify=CENTER).pack(pady=5)

        id = IntVar()
        txt_id = Entry(ventana)
        txt_id.pack(pady=15)

        if tipo == "actualizar":
            btn_buscar = Button(ventana, text="Buscar", command=lambda: View.cambiar_camiones(ventana, id.get()), justify=CENTER).pack(pady=15)
        elif tipo == "eliminar":
            btn_buscar = Button(ventana, text="Buscar", command=lambda: View.borrar_camiones(ventana, id.get()), justify=CENTER).pack(pady=15)

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana, "camiones"), justify=CENTER)
        btn_regresar.pack(pady=15)

    def cambiar_camiones(ventana,id):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=f".:: Cambiar un camion ::.", justify=CENTER)
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

        lbl_potencia = Label(ventana, text="Caballaje: ", justify=CENTER)
        lbl_potencia.pack(pady=5)

        txt_caballaje = Entry(ventana)
        txt_caballaje.pack(pady=15)

        lbl_num_plazas = Label(ventana, text="Numero de plazas: ", justify=CENTER)
        lbl_num_plazas.pack(pady=5)

        txt_num_plazas = Entry(ventana)
        txt_num_plazas.pack(pady=15)

        lbl_eje = Label(ventana, text="Numero de Ejes: ", justify=CENTER)
        lbl_eje.pack(pady=5)

        txt_eje = Entry(ventana)
        txt_eje.pack(pady=5)

        lbl_capacidad_carga = Label(ventana, text="Capacidad de carga: ", justify=CENTER)
        lbl_capacidad_carga.pack(pady=5)

        txt_num_plazas = Entry(ventana)
        txt_num_plazas.pack(pady=5)

        btn_cambiar = Button(ventana, text="Guardar", command="", justify=CENTER)
        btn_cambiar.pack(pady=15)

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana, "camionetas"), justify=CENTER)
        btn_regresar.pack(pady=15)

    def borrar_camiones(ventana,id_auto):
        View.limpiar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=f".:: Borrar un camion ::.", justify=CENTER)
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

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana, "camionetas"), justify=CENTER)
        btn_regresar.pack(pady=15)