from logger_base import *

class TipoVenta:
    def __init__(self, id_tipo = None, nombre = None):
        self._id_tipo = id_tipo
        self._nombre= nombre

    def __str__(self):
        return  f'''
                ID: {self._id_tipo}
                ISBN: {self._nombre}
                '''
    
    @property
    def id_tipo(self):
        return self.id_tipo
    
    @id_tipo.setter
    def id_tipo(self, id_tipo):
        self._id_tipo = id_tipo

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
if __name__ == '__main__':
    tipoventa1 = TipoVenta(2, 'Linea')
    log.debug(tipoventa1)

    # Simular un INSERT INTO
    tipoventa1 = TipoVenta(id_tipo= 2, nombre = 'Linea')
    log.debug(tipoventa1)

    #Simular un DELETE
    tipoventa1 = TipoVenta(id_tipo=2)
    log.debug(tipoventa1)
