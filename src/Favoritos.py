from logger_base import *

class Favoritos:
    def __init__(self, id_cliente = None, isbn = None):
        self._id_cliente = id_cliente
        self._isbn = isbn

    def __str__(self):
        return  f'''
                ID Cliente: {self._id_cliente}
                ISBN: {self._isbn}
                '''
    
    @property
    def id_cliente(self):
        return self._id_cliente
    
    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self._id_cliente = id_cliente

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        self._isbn = isbn


if __name__ == '__main__':
    favorito = Favoritos(1, 'jperez')
    log.debug(favorito)

    # Simular un INSERT INTO
    favorito = Favoritos(id_cliente= 2, isbn= 'jesgut')
    log.debug(favorito)

    #Simular un DELETE
    favorito1 = Favoritos(id_cliente=1)
    log.debug(favorito1)
    