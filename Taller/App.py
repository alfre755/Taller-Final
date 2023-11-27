from DbConnector import DAO
from Usuario import Usuario
import os
import sys

dao = DAO()
usuarioAutenticado = None
listaUsuariosEnBase = dao.VerUsuarios()


if len(listaUsuariosEnBase) == 0:
    cod = 0
    rol = 0
    contraseña = "123456"
    username = "Luis Miguel"
    estado = "Desbloqueado"
    usuario = Usuario(cod, rol, contraseña, username, estado)
    listaUsuariosEnBase.append(usuario)
    dao.InsertarUsuario(usuario)
    input("Usuario Creado! Presiona ENTER para Continuar...")
else:
    while True:
        os.system("cls")
        if usuarioAutenticado is None:
            usernameUsuarioAutenticado = input("Ingresa el usuario: ")
            contraseñaUsuarioAutenticado = input("Ingrese contraseña: ")
            usuarioAutenticado = dao.Autenticar(
                usernameUsuarioAutenticado, contraseñaUsuarioAutenticado
            )
            
            # print(usuarioAutenticado.getEstado())
            if usuarioAutenticado.getEstado() == "Bloqueado":
                input("El usuario no puede ingresar ya que esta bloqueado")
            else:
                if (usuarioAutenticado.getRol()==1 or usuarioAutenticado.getRol()==2):
                    input("El usuario no puede ingresar debido a que no posee el rol de administrador")
                else:
                    print("{1} . Insertar Nuevo Usuario")
                    print("{2} . Eliminar Usuario")
                    print("{3} . Ver Usuarios")
                    print("{4} . Actualizar contraseña")
                    print("{5} . Actualizar Usuario")
                    print("{6} . Bloquear Usuario")
                    print("{7} . Desbloquear Usuario")

                    op = input("Selecciones una opcion")

                    if op == "1":
                        cod = input("Codigo del usuario: ")
                        rol = input("Nombre del rol: ")
                        contraseña = input("Ingrese contraseña: ")
                        username = input("Ingrese su username: ")
                        estado = input("Ingrese su estado: ")
                        if rol == "1" or rol == "2" or rol == "3":
                            usuario = Usuario(cod, rol, contraseña, username, estado)
                            dao.InsertarUsuario(usuario)
                            input("Usuario Creado! Presiona ENTER para Continuar...")
                        else:
                            input(
                                "El usuario no pudo ser creado, ya que el rol esta mal ingresado"
                            )

                    if op == "2":
                        os.system("cls")
                        for usuario in dao.VerUsuarios():
                            print(
                                f"{usuario.getCodigoUsuario()} | {usuario.getUsername()}"
                            )
                        codigoUsuario = input("Ingresa del usuario a eliminar: ")
                        if codigoUsuario == "0":
                            input(
                                "El usuario SuperAdministrador no puede ser eliminado"
                            )
                        else:
                            dao.EliminarUsuario(codigoUsuario)
                            input("Usuario Eliminado! Presiona ENTER para Continuar...")

                    if op == "3":
                        os.system("cls")
                        for usuario in dao.VerUsuarios():
                            print(
                                f"{usuario.getCodigoUsuario()} | {usuario.getRol()} | {usuario.getContraseña()} | {usuario.getUsername()} | {usuario.getEstado()}"
                            )
                        input("Usuarios Listados! Presiona ENTER para continar...")

                    if op == "4":
                        os.system("cls")
                        for usuario in dao.VerUsuarios():
                            print(
                                f"{usuario.getCodigoUsuario()} | {usuario.getUsername()}"
                            )
                        codigoUsuario = input(
                            "Ingresa el Codigo de el usuario a actualizar: "
                        )
                        nuevaContraseña = input(
                            "Ingresa la nueva contraseña de usuario: "
                        )
                        usuario = dao.VerUsuario(codigoUsuario)
                        print(usuario.getContraseña())
                        usuario.setContraseña(nuevaContraseña)
                        print(usuario.getContraseña())
                        dao.ActualizarContraseña(nuevaContraseña, codigoUsuario)
                        input(
                            "Contraseña actualizada! Presiona ENTER para Continuar..."
                        )

                    if op == "5":
                        os.system("cls")
                        for usuario in dao.VerUsuarios():
                            print(
                                f"{usuario.getCodigoUsuario()} | {usuario.getUsername()}"
                            )
                        codigoUsuario = input(
                            "Ingresa el Codigo de el usuario a actualizar: "
                        )

                        nuevoRol = input("Ingresa el rol del usuario: ")
                        nuevaContraseña = input(
                            "Ingresa la nueva contraseña de usuario: "
                        )
                        nuevoUsername = input("Ingresa el username del usuario: ")
                        nuevoEstado = input("Ingresa el estado del usuario: ")
                        usuario = dao.VerUsuario(codigoUsuario)
                        print(
                            usuario.getContraseña(),
                            usuario.getCodigoUsuario(),
                            usuario.getEstado(),
                            usuario.getRol(),
                            usuario.getUsername(),
                        )

                        usuario.setRol(nuevoRol)
                        usuario.setContraseña(nuevaContraseña)
                        usuario.setUsername(nuevoUsername)
                        usuario.setEstado(nuevoEstado)
                        print(
                            usuario.getContraseña(),
                            usuario.getCodigoUsuario(),
                            usuario.getEstado(),
                            usuario.getRol(),
                            usuario.getUsername(),
                        )
                        dao.ActualizarUsuario(
                            codigoUsuario,
                            nuevaContraseña,
                            nuevoRol,
                            nuevoUsername,
                            nuevoEstado,
                        )
                        input(
                            "Contraseña actualizada! Presiona ENTER para Continuar..."
                        )

                    if op == "6":
                        os.system("cls")
                        for usuario in dao.VerUsuarios():
                            print(
                                f"{usuario.getCodigoUsuario()} | {usuario.getUsername()}"
                            )
                        codigo1 = input("Ingrese el codigo de usuario a bloquear: ")
                        nuevoEstado = input("Escriba 1. Para bloquear, 0 para salir")
                        usuario2 = dao.VerUsuario(codigo1)
                        if codigo1 == "0":
                            input(
                                "El usuario Super Administrador no puede ser bloqueado"
                            )
                        else:
                            if nuevoEstado == "1":
                                nuevoEstado = "Bloqueado"
                                usuario2.setEstado(nuevoEstado)
                                dao.BloquearUsuario(codigo1, nuevoEstado)
                                input("El usuario ha sido bloqueado con exito!")
                            else:
                                input("Volviendo al menu")

                    if op == "7":
                        os.system("cls")
                        for usuario in dao.VerUsuarios():
                            print(
                                f"{usuario.getCodigoUsuario()} | {usuario.getUsername()}"
                            )
                        codigo1 = input("Ingrese el codigo de usuario a bloquear: ")
                        nuevoEstado = input("Escriba 1. Para Desbloquear, 0 para salir")
                        usuario2 = dao.VerUsuario(codigo1)
                        if nuevoEstado == "1":
                            nuevoEstado = "Desbloqueado"
                            usuario2.setEstado(nuevoEstado)
                            dao.DesbloquearUsuario(codigo1, nuevoEstado)
                            input("El usuario ha sido desbloqueado con exito!")
                        else:
                            input("Volviendo al menu")
