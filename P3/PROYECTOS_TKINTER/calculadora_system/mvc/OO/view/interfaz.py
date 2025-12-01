from tkinter import *
from controller import funciones
from model import operaciones

class Vista:
    def __init__(self,ventana):
        ventana.title("Calculadora Básica")
        ventana.geometry("600x400")
        ventana.resizable(False,False)
        self.interfaz_principal(ventana)

    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    # Vista de Agregar operaciones
    @staticmethod
    def interfaz_principal(ventana):
        
        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)

        n1 = IntVar(value=0)
        n2 = IntVar(value=0) 

        main_frame = Frame(ventana, bg="#E0E0E0", padx=20, pady=20)
        main_frame.pack(expand=True, fill='both') 

        # ----------------------------------
        # I. SECCIÓN DE ENTRADA (ROW 0, 1)
        # ----------------------------------
        Label(main_frame, text="Número 1:", font=("Arial", 10), bg="#E0E0E0", anchor='w').grid(row=0, column=0, padx=5, pady=5, sticky='w')

        numero1 = Entry(main_frame, textvariable=n1, width=15, justify=RIGHT, 
                        font=("Courier New", 14, "bold"), bd=3, relief=SUNKEN, bg="#FFFFFF")
        numero1.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky='ew')

        Label(main_frame, text="Número 2:", font=("Arial", 10), bg="#E0E0E0", anchor='w').grid(row=1, column=0, padx=5, pady=5, sticky='w')

        numero2 = Entry(main_frame, textvariable=n2, width=15, justify=RIGHT, 
                        font=("Courier New", 14, "bold"), bd=3, relief=SUNKEN, bg="#FFFFFF")
        numero2.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky='ew')


        # ----------------------------------
        # II. SECCIÓN DE OPERACIONES (ROW 2)
        # ----------------------------------
        oper_style = {"font": ("Arial", 12, "bold"), "width": 5, "height": 1, 
                      "bg": "#4CAF50", "fg": "white", "activebackground": "#66BB6A", "relief": "raised"}

        # Botón Suma
        btn_suma = Button(main_frame, text="+", 
                          command=lambda: funciones.Funciones.operaciones(n1.get(), n2.get(), "+"),
                          **oper_style)
        btn_suma.grid(row=2, column=0, padx=5, pady=10)

        # Botón Resta
        btn_resta = Button(main_frame, text="-", 
                           command=lambda: funciones.Funciones.operaciones(n1.get(), n2.get(), "-"),
                           **oper_style)
        btn_resta.grid(row=2, column=1, padx=5, pady=10)

        # Botón Multiplicar
        btn_multiplicar = Button(main_frame, text="x", # Usamos 'x' para más claridad visual
                                 command=lambda: funciones.Funciones.operaciones(n1.get(), n2.get(), "x"),
                                 **oper_style)
        btn_multiplicar.grid(row=2, column=2, padx=5, pady=10)
        
        # Botón División
        btn_division = Button(main_frame, text="/", 
                              command=lambda: funciones.Funciones.operaciones(n1.get(), n2.get(), "/"),
                              **oper_style)
        btn_division.grid(row=3, column=0, padx=5, pady=5) 


        # ----------------------------------
        # III. SECCIÓN DE ACCIÓN (ROW 4)
        # ----------------------------------
        btn_salir = Button(main_frame, text="Salir", command=ventana.quit,
                           font=("Arial", 10), width=10, bg="#F44336", fg="white", 
                           activebackground="#E57373", relief="raised")
        btn_salir.grid(row=4, column=1, columnspan=2, pady=15, sticky='e')

    # Vista de la App de operaciones
    @staticmethod
    def menuPrincipal(ventana):
        menuBar = Menu(ventana)
        ventana.config(menu=menuBar)

        operacionesMenu = Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Operaciones", menu=operacionesMenu)
        operacionesMenu.add_command(label="Agregar",command=lambda: Vista.interfaz_principal(ventana))
        operacionesMenu.add_command(label="Consultar",command=lambda: Vista.interfaz_consultar(ventana))
        operacionesMenu.add_command(label="Cambiar",command=lambda: Vista.interfaz_actualizar(ventana))
        operacionesMenu.add_command(label="Borrar",command=lambda: Vista.interfaz_eliminar(ventana))
        operacionesMenu.add_separator()
        operacionesMenu.add_command(label="Salir", command = ventana.quit)

    # Vista de Eliminar operaciones
    @staticmethod
    def interfaz_eliminar(ventana):
        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)

        titulo = Label(ventana, text=".:: Borrar una operación ::.")
        titulo.pack()

        lbl_accion = Label(ventana, text="ID de la operación: ")
        lbl_accion.pack()

        id = IntVar()
        txt_id = Entry(ventana, textvariable=id)
        txt_id.focus()
        txt_id.pack()

        btn_eliminar = Button(ventana, text="Eliminar", command=lambda: funciones.Funciones.eliminar_operaciones(id.get()))
        btn_eliminar.pack(pady=20)

        btn_regresar = Button(ventana, text="Volver", command=lambda: Vista.interfaz_principal(ventana)) 
        btn_regresar.pack()

    @staticmethod
    def interfaz_consultar(ventana):
        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)

        titulo = Label(ventana, text=".:: Listado de Operaciones ::.").pack()

        funciones.Funciones.consultar_operaciones(ventana)

        btn_regresar = Button(ventana, text="Volver", command=lambda: Vista.interfaz_principal(ventana)) 
        btn_regresar.pack()
    
    @staticmethod
    def interfaz_actualizar(ventana):
        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)

        titulo = Label(ventana, text=".:: Cambiar una operacion ::.").pack(pady=20)

        lbl_id = Label(ventana, text="ID de la operacion a cambiar: ")
        lbl_id.pack()

        id = IntVar()
        n1 = IntVar()
        n2 = IntVar()
        signo = StringVar()
        resultado = DoubleVar()

        txt_id = Entry(ventana, textvariable=id)
        txt_id.focus()
        txt_id.pack(pady=20)

        btn_buscar = Button(ventana, text="Buscar", command=lambda: funciones.Funciones.checar_operacion(id.get()))
        btn_buscar.pack(pady=20)
        # lbl_n1 = Label(ventana, text="Nuevo Numero 1:")
        # lbl_n1.pack()
        # txt_n1 = Entry(ventana, textvariable=n1, justify=RIGHT, width=5)
        # txt_n1.pack()
        # lbl_n2 = Label(ventana, text="Nuevo Numero 2:")
        # lbl_n2.pack()
        # txt_n2 = Entry(ventana, textvariable=n2, justify=RIGHT, width=5)
        # txt_n2.pack()
        # lbl_signo = Label(ventana, text="Nuevo signo:")
        # lbl_signo.pack()
        # txt_signo = Entry(ventana, textvariable=signo, justify=RIGHT, width=5)
        # txt_signo.pack()
        # lbl_resultado = Label(ventana, text="Nuevo resultado:")
        # lbl_resultado.pack()
        # txt_resultado = Entry(ventana, textvariable=resultado, justify=RIGHT, width=5)
        # txt_resultado.pack()

        # btn_guardar = Button(ventana, text="Guardar", command=lambda: funciones.Funciones.actualizar_operaciones(n1.get(),n2.get(),signo.get(),resultado.get(),id.get()))
        # btn_guardar.pack(pady=20)

        btn_regresar = Button(ventana, text="Volver", command=lambda: Vista.interfaz_principal(ventana)) 
        btn_regresar.pack()

    @staticmethod
    def actualizar_campos(ventana,n1,n2,signo,resultado):
        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)

        titulo = Label(ventana, text=".:: Cambiar una operacion ::.").pack(pady=20)

        txt_id = Entry(ventana, text=id, readonlybackground=True)

        lbl_n1 = Label(ventana, text="Nuevo Numero 1:")
        lbl_n1.pack()
        txt_n1 = Entry(ventana, textvariable=n1, justify=RIGHT, width=5)
        txt_n1.pack()
        lbl_n2 = Label(ventana, text="Nuevo Numero 2:")
        lbl_n2.pack()
        txt_n2 = Entry(ventana, textvariable=n2, justify=RIGHT, width=5)
        txt_n2.pack()
        lbl_signo = Label(ventana, text="Nuevo signo:")
        lbl_signo.pack()
        txt_signo = Entry(ventana, textvariable=signo, justify=RIGHT, width=5)
        txt_signo.pack()
        lbl_resultado = Label(ventana, text="Nuevo resultado:")
        lbl_resultado.pack()
        txt_resultado = Entry(ventana, textvariable=resultado, justify=RIGHT, width=5)
        txt_resultado.pack()

        btn_guardar = Button(ventana, text="Guardar", command=lambda: funciones.Funciones.actualizar_operaciones(n1.get(),n2.get(),signo.get(),resultado.get(),id.get()))
        btn_guardar.pack(pady=20)

        btn_regresar = Button(ventana, text="Volver", command=lambda: Vista.interfaz_principal(ventana)) 
        btn_regresar.pack()


