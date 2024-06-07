from logger_base import *

class Cliente:
    def __init__(self, id_cliente = None, nombre_usuario = None, nombre = None,
                 apellido_paterno = None, apellido_materno = None, id_direccion = None,
                 correo = None, telefono = None, num_tarjeta = None):
        self._id_cliente = id_cliente
        self._nombre_usuario = nombre_usuario
        self._nombre = nombre
        self._apellido_paterno = apellido_paterno
        self._apellido_materno = apellido_materno
        self._id_direccion = id_direccion
        self._correo = correo
        self._telefono = telefono
        self._num_tarjeta = num_tarjeta

    def __str__(self):
        return  f'''
                ID Cliente: {self._id_cliente}
                Usuario: {self._nombre_usuario}
                Nombre(s) = {self._nombre}
                Apellido Paterno: {self._apellido_paterno}
                Apellido Materno: {self._apellido_materno}
                Dirección asociada: {self._id_direccion}
                Correo: {self._correo}
                Teléfono: {self._telefono}
                Tarjeta: {self._num_tarjeta}
                '''
    
    @property
    def id_cliente(self):
        return self._id_cliente
    
    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self._id_cliente = id_cliente

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

    @property
    def id_direccion(self):
        return self._id_direccion
    
    @id_direccion.setter
    def id_direccion(self, id_direccion):
        self._id_direccion = id_direccion

    @property
    def correo(self):
        return self._correo
    
    @correo.setter
    def correo(self, correo):
        self._correo = correo

    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def num_tarjeta(self):
        return self._num_tarjeta
    
    @num_tarjeta.setter
    def num_tarjeta(self, num_tarjeta):
        self._num_tarjeta = num_tarjeta

if __name__ == '__main__':
    cliente1 = Cliente(1, 'jperez', 'Juan', 'Pérez', 'Juárez', 1, 'jperez@mail.com', '555 555 555', '1111 1111 1111 1111')
    log.debug(cliente1)

    # Simular un INSERT INTO
    cliente1 = Cliente(id_cliente= 2, nombre_usuario= 'jesgut', nombre= 'Jesús', apellido_paterno= 'Gutiérrez', 
                       apellido_materno= 'Alvarado', id_direccion= 2, correo= 'jesgut@mail.com', telefono= '555 555 444',
                       num_tarjeta= '2222 2222 2222 2222')
    log.debug(cliente1)

    #Simular un DELETE
    cliente1 = Cliente(id_cliente=1)
    log.debug(cliente1)
    