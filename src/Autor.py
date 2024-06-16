from logger_base import *

class Autor:
    def __init__(self, id_autor = None, nombre = None):
        self._id_autor = id_autor
        self._nombre = nombre
        
    def __str__(self):
        return f'''
                ID Autor: {self._id_autor}
                Nombre: = {self._nombre}
                '''
    
    @property
    def id_autor(self):
        return self._id_autor
    
    @id_autor.setter
    def id_autor(self, id_autor):
        self._id_autor = id_autor
    
    @property
    def nombre(self):
        return self._nombre
        
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

        
if __name__ == '__main__':
    autor1 = Autor(1,'Fabian Gasca')
    log.debug(autor1)
    
    # Simular un INSERT INTO
    autor1 = Autor(id_autor = 2, nombre= 'Alice Oseman')
    log.debug(autor1)
    
    # Simular un DELETE
    autor1 = Autor(id_autor=1)
    log.debug(autor1)
