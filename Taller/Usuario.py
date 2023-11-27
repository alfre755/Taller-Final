class Usuario:
    def __init__(self,cod_usuario,rol,contraseña,username,estado) -> None:
        self.CodigoUsuario = cod_usuario
        self.Rol=rol
        self.Contraseña = contraseña
        self.Username = username
        self.Estado=estado

    def getCodigoUsuario(self):
        return self.CodigoUsuario
    
    def getRol(self):
        return self.Rol

    def getContraseña(self):
        return self.Contraseña

    def getUsername(self):
        return self.Username

    def getEstado(self):
        return self.Estado
    
    def setContraseña(self,nuevaContraseña):
        self.Contraseña = nuevaContraseña

    def setRol(self,nuevoRol):
        self.Rol = nuevoRol
    
    def setUsername(self,nuevoUsername):
        self.Username = nuevoUsername
    
    def setEstado(self,nuevoEstado):
        self.Estado = nuevoEstado
    
    def setCodigoUsuario(self,nuevoCodigoUsuario):
        self.CodigoUsuario = nuevoCodigoUsuario
        


