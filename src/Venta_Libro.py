from logger_base import *

class Venta_Libro:
    def __init__(self, id_venta = None, ISBN = None, cantidad = None):
        self._id_venta = id_venta
        self._ISBN = ISBN
        self._cantidad = cantidad

    def __str__(self):
        return  f'''
                ID: {self._id_venta}
                ISBN: {self._ISBN}
                Cantidad = {self._cantidad}
                '''
    
    @property
    def id_venta(self):
        return self.id_venta
    
    @id_venta.setter
    def id_venta(self, id_venta):
        self._id_venta = id_venta

    @property
    def ISBN(self):
        return self._ISBN
    
    @ISBN.setter
    def ISBN(self, ISBN):
        self._ISBN = ISBN
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad
    
if __name__ == '__main__':
    venta_libro1 = Venta_Libro(2, 3, 4)
    log.debug(venta_libro1)

    # Simular un INSERT INTO
    venta_libro1 = Venta_Libro(id_venta= 2, ISBN = 3, cantidad = 4)
    log.debug(venta_libro1)

    #Simular un DELETE
    venta_libro1 = Venta_Libro(id_venta=2)
    log.debug(venta_libro1)
