from logger_base import *


class Proveedor:
    def __init__(self, id_proveedor = None, nombre = None, tel_contacto = None):
        self._id_proveedor = id_proveedor
        self._nombre = nombre
        self._tel_contacto = tel_contacto
    
    def __str__(self):
        return f'''
                ID Proveedor: {self._id_proveedor}
                Nombre: {self._nombre}
                Teléfono de contacto: {self._tel_contacto}
                '''

    @property
    def id_proveedor(self):
        return self._id_proveedor

    @id_proveedor.setter
    def id_proveedor(self, id_proveedor):
        self._id_proveedor = id_proveedor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._Nombre = nombre

    @property
    def tel_contacto(self):
        return self._tel_contacto

    @tel_contacto.setter
    def tel_contacto(self, tel_contacto):
        self._Tel_Contacto = tel_contacto

if __name__ == '__main__':
    proveedor1 = Proveedor(id_proveedor= 2, nombre= 'Sandra', tel_contacto= '1345566')
    log.debug(proveedor1)

    # Simular un INSERT INTO
    proveedor1 = Proveedor(id_proveedor= 2, nombre= 'Sandra', tel_contacto= '1345566')
    log.debug(proveedor1)

    # Simular un DELETE
    proveedor1 = Proveedor(id_proveedor=2)
    log.debug(proveedor1)
