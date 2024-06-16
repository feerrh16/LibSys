from logger_base import *

class Autor_Libro:
    def __init__(self, id_autor = None, ISBN = None):
        self._id_autor = id_autor
        self._ISBN = ISBN
        
    def __str__(self):
        return f'''
                ID Autor: {self._id_autor}
                ISBN: {self._ISBN}
                '''
                
    @property
    def id_autor(self):
        return self._id_autor
    
    @id_autor.setter
    def id_autor(self, id_autor):
        self._id_autor = id_autor
        
    @property
    def ISBN(self):
        return self._ISBN

    @ISBN.setter
    def ISBN(self, ISBN):
        self._ISBN = ISBN

if __name__ == '__main__':
    autor_libro1 = Autor_Libro(1,'9796078828326')
    log.debug(autor_libro1)
    
    # Simular un INSERT INTO
    autor_libro1 = Autor_Libro(id_autor = 2, ISBN= '9796078828327')
    log.debug(autor_libro1)
    
    # Simular un DELETE
    autor_libro1 = Autor_Libro(id_autor=1)
    log.debug(autor_libro1)