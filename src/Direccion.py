from logger_base import *


class Direccion:
    def __init__(self, id_direccion = None, id_cliente = None, direccion = None,
                 ciudad = None, municipio = None, cp = None):
        self._id_direccion = id_direccion
        self._id_cliente = id_cliente
        self._direccion = direccion
        self._ciudad = ciudad
        self._municipio = municipio
        self._cp = cp


    def __str__(self):
        return f'''
                ID Direccion: {self._id_direccion}
                ID Cliente: {self._id_cliente}
                Direccion: {self._direccion}
                Ciudad: {self._ciudad}
                Municipio: {self._municipio}
                Codigo Postal: {self._cp}
                '''

    @property
    def id_direccion(self):
        return self._id_direccion

    @id_direccion.setter
    def id_direccion(self, id_direccion):
        self._id_direccion = id_direccion

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self._id_cliente = id_cliente

    @property
    def ciudad(self):
        return self._ciudad

    @ciudad.setter
    def ciudad(self, ciudad):
        self._ciudad = ciudad

    @property
    def municipio(self):
        return self._municipio

    @municipio.setter
    def municipio(self, municipio):
        self._municipio = municipio

    @property
    def cp(self):
        return self._cp

    @cp.setter
    def cp(self, cp):
        self._cp = cp


if __name__ == '__main__':
    direccion1 = Direccion(2, 23312, 'Juan Gomez Albarran 18', 'Ciudad de Mexico', 'Gustavo A Madero', '78000')
    log.debug(direccion1)

    # Simular un INSERT INTO
    direccion1 = Direccion(id_direccion= 2, id_cliente= 23312, direccion= 'Juan Gomez Albarran 18',
                           ciudad='Ciudad de Mexico', municipio= 'Gustavo A Madero', cp= '78000')
    log.debug(direccion1)

    # Simular un DELETE
    direccion1 = Direccion(id_direccion=2)
    log.debug(direccion1)
