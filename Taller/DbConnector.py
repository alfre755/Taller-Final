import mysql.connector
from typing import List
import os
from Usuario import Usuario

class DAO:
    def __init__(self) -> None:
        self.cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='Taller')
        
    def InsertarUsuario(self, Usuarios:Usuario)->None:
        cursor = self.cnx.cursor()
        query = ("INSERT INTO usuarios (cod_usuario,rol,contraseña,username,estado) VALUES (%s,%s,%s,%s,%s)")
        data = (Usuarios.getCodigoUsuario(),Usuarios.getRol(),Usuarios.getContraseña(),Usuarios.getUsername(),Usuarios.getEstado())
        cursor.execute(query, data)
        self.cnx.commit()

    def EliminarUsuario(self, cod)->None:
        cursor = self.cnx.cursor()
        query = ("DELETE FROM usuarios WHERE cod_usuario = %s")
        data = (cod,)
        cursor.execute(query, data)
        self.cnx.commit()

    def ActualizarContraseña(self, nueva_contraseña,codigo_usuario)->None:
        cursor = self.cnx.cursor()
        query = ("UPDATE usuarios SET contraseña = %s WHERE cod_usuario = %s")
        data = (nueva_contraseña,codigo_usuario)
        cursor.execute(query, data)
        self.cnx.commit()

    def VerUsuarios(self)->List[Usuario]:
        cursor = self.cnx.cursor()
        query = ("SELECT * FROM usuarios")
        cursor.execute(query)

        usuariosList:List[Usuario] = []
        for (cod_usuario, rol,contraseña,username,estado) in cursor:
            usuario = Usuario(cod_usuario,rol,contraseña,username,estado)
            usuariosList.append(usuario)
        return usuariosList
    
    def VerUsuario(self,cod)->Usuario:
        cursor = self.cnx.cursor()
        query = ("SELECT * FROM usuarios where cod_usuario = %s")
        data=(cod,)
        cursor.execute(query,data)
        for (cod_usuario, rol,contraseña,username,estado) in cursor:
            usuario = Usuario(cod_usuario,rol,contraseña,username,estado)
            return usuario
        
    def ActualizarUsuario(self,codigo_usuario,nuevo_rol,nueva_contraseña,nuevo_username,nuevo_estado)->None:
        cursor = self.cnx.cursor()
        query = ("UPDATE usuarios SET rol = %s,contraseña=%s,username=%s,estado = %s WHERE cod_usuario = %s")
        data = (nuevo_rol,nueva_contraseña,nuevo_username,nuevo_estado,codigo_usuario)
        cursor.execute(query, data)
        self.cnx.commit()
            
    def Autenticar(self,username,contraseña)->Usuario:
        cursor = self.cnx.cursor()
        query =("SELECT * from usuarios where username=%s and contraseña = %s")
        data= (username,contraseña)
        cursor.execute(query,data)
        for (cod_usuario, rol,contraseña,username,estado) in cursor:
            autenticado = Usuario(cod_usuario,rol,contraseña,username,estado)
            return autenticado
        return None
    
    def BloquearUsuario(self,cod,nuevoestado)->None:
        cursor=self.cnx.cursor()
        query=("UPDATE usuarios SET estado=%s where cod_usuario=%s")
        data=(nuevoestado,cod)
        cursor.execute(query,data)
        self.cnx.commit()
        
    def DesbloquearUsuario(self,cod,nuevoestado)->None:
        cursor=self.cnx.cursor()
        query=("UPDATE usuarios SET estado=%s where cod_usuario=%s")
        data=(nuevoestado,cod)
        cursor.execute(query,data)
        self.cnx.commit()
        
    
        