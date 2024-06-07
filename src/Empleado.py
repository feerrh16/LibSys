from logger_base import *

class Empleado:
    def __init__(self, id_empleado = None, nombre_usuario = None, nombre = None,
                 apellido_paterno = None, apellido_materno = None):
        self._id_empleado = id_empleado
        self._nombre_usuario = nombre_usuario
        self._nombre = nombre
        self._apellido_paterno = apellido_paterno
        self._apellido_materno = apellido_materno

    def __str__(self):
        return  f'''
                ID Empleado: {self._id_empleado}
                Usuario: {self._nombre_usuario}
                Nombre(s) = {self._nombre}
                Apellido Paterno: {self._apellido_paterno}
                Apellido Materno: {self._apellido_materno}
                '''
    
    @property
    def id_cliente(self):
        return self._id_empleado
    
    @id_cliente.setter
    def id_cliente(self, id_empleado):
        self._id_empleado = id_empleado

    @property
    def nombre_usuario(self):
        return self._nombre_usuario

    @nombre_usuario.setter
    def nombre_usuario(self, nombre_usuario):
        self._nombre_usuario = nombre_usuario

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido_paterno(self):
        return self._apellido_paterno
    
    @apellido_paterno.setter
    def apellido_paterno(self, apellido_paterno):
        self._apellido_paterno = apellido_paterno

    @property
    def apellido_materno(self):
        return self._apellido_paterno
    
    @apellido_materno.setter
    def apellido_materno(self, apellido_materno):
        self._apellido_materno = apellido_materno

if __name__ == '__main__':
    empleado1 = Empleado(1, 'pepe', 'José', 'Flores', 'Alvarado')
    log.debug(empleado1)

    # Simular un INSERT INTO
    empleado1 = Empleado(id_empleado= 2, nombre_usuario= 'jesgut', nombre= 'Jesús', apellido_paterno= 'Gutiérrez', 
                        apellido_materno= 'Alvarado')
    log.debug(empleado1)

    #Simular un DELETE
    empleado1 = Empleado(id_empleado=1)
    log.debug(empleado1)
    