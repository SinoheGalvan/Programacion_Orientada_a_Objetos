from conexionBD import *
from tkinter import messagebox

class Operaciones():
  @staticmethod
  def insertar(numero1,numero2,signo,resultado):
          try:
            cursor.execute(
              "insert into operaciones (id,Fecha,Numero1,Numero2,Signo,Resultado) values(null,NOW(),%s,%s,%s,%s)",
              (numero1,numero2,signo,resultado)
            )
            conexion.commit()
            return True
          except:
            return False

  @staticmethod
  def consultar():
          try:
            cursor.execute("select * from operaciones")
            return cursor.fetchall()
          except:    
            return []
          
  @staticmethod
  def consultar_por_id(id):
          try:
            cursor.execute("select * from operaciones where id=%s",(id))
            return True
          except:
            return False
          
  @staticmethod
  def traer_por_id(id):
          try:
            cursor.execute("select * from operaciones where id=%s",(id))
            return cursor.fetchone()
          except:
            return []

  @staticmethod
  def actualizar(numero1,numero2,signo,resultado,id):
        #messagebox.showinfo(message=f"Operación cambiada con éxito", icon="info")
        try:
          cursor.execute(
              "update operaciones set Fecha=NOW(),Numero1=%s,Numero2=%s,Signo=%s,Resultado=%s where id=%s",
              (numero1,numero2,signo,resultado,id)
          )
          conexion.commit()
          return True
        except: 
          return False

  @staticmethod   
  def eliminar(id):
          #confirm=messagebox.askquestion(message=f"¿Deseas eliminar la operacion con id {id}?",icon="question")
          #if confirm=="yes":    
          try:
              cursor.execute(
                "delete from operaciones where id=%s",
                (id,)
              ) 
              conexion.commit() 
              return True  
          except:    
              return False
          #else:
              #pass
        
