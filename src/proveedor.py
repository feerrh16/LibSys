from logger_base import *


class Proveedor:
    def __init__(self, id_Proveedor = None, Nombre = None, Tel_Contacto = None):
        self._id_Proveedor = id_Proveedor
        self._Nombre = Nombre
        self._Tel_Contacto = Tel_Contacto
    
    def __str__(self):
        return f'''
                ID Proveedor: {self._id_Proveedor}
                ID Nombre: {self._Nombre}
                Tel Contacto: {self._Tel_Contacto}
                '''

    @property
    def id_Proveedor(self):
        return self._id_Proveedor

    @id_Proveedor.setter
    def id_Proveedor(self, id_Proveedor):
        self._id_Proveedor = id_Proveedor

    @property
    def Nombre(self):
        return self._Nombre

    @Nombre.setter
    def Nombre(self, Nombre):
        self._Nombre = Nombre

    @property
    def Tel_Contacto(self):
        return self._Tel_Contacto

    @Tel_Contacto.setter
    def Tel_Contacto(self, Tel_Contacto):
        self._Tel_Contacto = Tel_Contacto

if __name__ == '__main__':
    Proveedor1 = Proveedor(id_Proveedor= 2, Nombre= 'Sandra', Tel_Contacto= '1345566')
    log.debug(Proveedor1)

    # Simular un INSERT INTO
    Proveedor1 = Proveedor(id_Proveedor= 2, Nombre= 'Sandra', Tel_Contacto= '1345566')
    log.debug(Proveedor1)

    # Simular un DELETE
    Proveedor1 = Proveedor(id_Proveedor=2)
    log.debug(Proveedor1)
