from logger_base import *

class Usuario:
    def __init__(self, nombre_usuario = None, contrasena = None, rol = None):
        self._nombre_usuario = nombre_usuario
        self._contrasena = contrasena
        self._rol = rol

    def __str__(self):
        return  f'''
                Usuario: {self._nombre_usuario}
                Contraseña: {self._contrasena}
                Rol: {self._rol}
                '''
    
    @property
    def nombre_usuario(self):
        return self._nombre_usuario
    
    @nombre_usuario.setter
    def nombre_usuario(self, nombre_usuario):
        self._nombre_usuario = nombre_usuario

    @property
    def contrasena(self):
        return self._contrasena
    
    @contrasena.setter
    def contrasena(self, contrasena):
        self._contrasena = contrasena
    
    @property
    def rol(self):
        return self._rol
    
    @rol.setter
    def rol(self, rol):
        self._rol = rol

if __name__ == '__main__':
    usuario1 = Usuario('jperez', 'password', 'Ayudante General')
    log.debug(usuario1)

    # Simular un INSERT INTO
    usuario1 = Usuario(nombre_usuario = 'davidma', contrasena = 'password', rol = 'Recepcionista')
    log.debug(usuario1)

    #Simular un DELETE
    usuario1 = Usuario(nombre_usuario = 'jperez')
    log.debug(usuario1)
    