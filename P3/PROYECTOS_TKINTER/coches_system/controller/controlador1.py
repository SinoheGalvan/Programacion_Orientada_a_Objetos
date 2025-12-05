from model import cochesBD
from tkinter import *
from tkinter import messagebox, ttk
from conexionBD import *

class Controller:
    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            messagebox.showinfo(title="Correcto", icon="info", message="Acción realizada con éxito")
        else:
            messagebox.showinfo(title="Atención", icon="warning", message="No se ha podido realizar la operación con éxito")

    @staticmethod
    def consultar_id_auto(id):
            try:
                cursor.execute("select * from autos where id_coche=%s",(id,))
                return cursor.fetchone()
            except:
                return []

    @staticmethod
    def consultar_id_camioneta(id):
            try:
                cursor.execute("select * from camionetas where id_camioneta=%s",(id,))
                return cursor.fetchone()
            except:
                return []

    @staticmethod
    def consultar_id_camion(id):
            try:
                cursor.execute("select * from camiones where id_camion=%s",(id,))
                return cursor.fetchone()
            except:
                return []

    @staticmethod
    def insertar_miones(marca,color,modelo,velocidad,caballaje,num_plazas):
        respuesta = cochesBD.Autos.insertar(marca,color,modelo,velocidad,caballaje,num_plazas)
        Controller.respuesta_sql(respuesta)

    @staticmethod
    def consultar_autos(ventana):
        registros = cochesBD.Autos.consultar()

        columnas = ["ID","Marca","Color","Modelo","velocidad","Caballaje","Plazas"]
        tabla = ttk.Treeview(ventana, columns=columnas, show="headings")

        for col in columnas:
            tabla.heading(col, text=col, anchor=W)
            if col == "ID":
                tabla.column(col, anchor=CENTER, width=50)
            else:
                tabla.column(col, anchor=W, width=120)

        for i, fila in enumerate(registros):
            tabla.insert(parent='', index=END, iid=fila[0], values=fila)

        tabla.pack(pady=20, padx=20,fill="both")

    @staticmethod
    def actualizar_auto(marca,color,modelo,velocidad,caballaje,plazas,id):
        respuesta = cochesBD.Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id)
        Controller.respuesta_sql(respuesta)

    @staticmethod
    def eliminar_auto(id):
        respuesta = cochesBD.Autos.eliminar(id)
        Controller.respuesta_sql(respuesta)

    @staticmethod
    def insertar_camioneta(marca,color,modelo,velocidad,caballaje,num_plazas,traccion,cerrada):
        respuesta = cochesBD.Camionetas.insertar(marca,color,modelo,velocidad,caballaje,num_plazas,traccion,cerrada)
        Controller.respuesta_sql(respuesta)

    @staticmethod
    def consultar_camionetas(ventana):
        registros = cochesBD.Camionetas.consultar()

        columnas = ["ID","Marca","Color","Modelo","velocidad","Caballaje","Plazas","Traccion","¿Cerrada?"]
        tabla = ttk.Treeview(ventana, columns=columnas, show="headings")

        for col in columnas:
            tabla.heading(col, text=col, anchor=W)
            if col == "ID":
                tabla.column(col, anchor=CENTER, width=50)
            else:
                tabla.column(col, anchor=W, width=120)

        for i, fila in enumerate(registros):
            tabla.insert(parent='', index=END, iid=fila[0], values=fila)

        tabla.pack(pady=20, padx=20,fill="both")

    @staticmethod
    def actualizar_camioneta(marca,color,modelo,velocidad,caballaje,num_plazas,traccion,cerrada,id):
        respuesta = cochesBD.Camionetas.actualizar(marca,color,modelo,velocidad,caballaje,num_plazas,traccion,cerrada,id)
        Controller.respuesta_sql(respuesta)

    @staticmethod
    def eliminar_camioneta(id):
        respuesta = cochesBD.Camionetas.eliminar(id)
        Controller.respuesta_sql(respuesta)

    @staticmethod
    def insertar_camion(modelo,color,marca,velocidad,caballaje,num_plazas,num_ejes,capacidadCarga):
        respuesta = cochesBD.Camiones.insertar(modelo,color,marca,velocidad,caballaje,num_plazas,num_ejes,capacidadCarga)
        Controller.respuesta_sql(respuesta)

    @staticmethod
    def consultar_camiones(ventana):
        registros = cochesBD.Camiones.consultar()

        columnas = ["ID","Modelo","Color","Marca","velocidad","Caballaje","Plazas", "# de ejes","Capacidad de carga"]
        tabla = ttk.Treeview(ventana, columns=columnas, show="headings")

        for col in columnas:
            tabla.heading(col, text=col, anchor=W)
            if col == "ID":
                tabla.column(col, anchor=CENTER, width=50)
            else:
                tabla.column(col, anchor=W, width=120)

        for i, fila in enumerate(registros):
            tabla.insert(parent='', index=END, iid=fila[0], values=fila)

        tabla.pack(pady=20, padx=20,fill="both")

    @staticmethod
    def actualizar_camion(modelo,color,marca,velocidad,caballaje,plazas,num_ejes,capacidadCarga,id):
        respuesta = cochesBD.Camiones.actualizar(modelo,color,marca,velocidad,caballaje,plazas,num_ejes,capacidadCarga,id)
        Controller.respuesta_sql(respuesta)

    @staticmethod
    def eliminar_camion(id):
        respuesta = cochesBD.Camiones.eliminar(id)
        Controller.respuesta_sql(respuesta)