from logger_base import *

class Autor_libro:
    def __init__(self, id_autor = None, isbn = None):
        self._id_autor = id_autor
        self._isbn = isbn
        
    def __str__(self):
        return f'''
                ID Autor: {self._id_autor}
                ISBN: = {self._isbn}
                '''
                
    @property
    def id_autor(self):
        return self._id_autor
    
    @id_autor.setter
    def id_autor(self, id_autor):
        self._id_autor = id_autor
        
    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        self._isbn = isbn

if __name__ == '__main__':
    autor_lib1 = Autor_libro(1,'9796078828326')
    log.debug(autor_lib1)
    
    # Simular un INSERT INTO
    autor_lib1 = Autor_libro(id_autor = 2, isbn= '9796078828327')
    log.debug(autor_lib1)
    
    # Simular un DELETE
    autor_lib1 = Autor_libro(id_autor=1)
    log.debug(autor_lib1)