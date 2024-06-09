from logger_base import *

class Libro:
    def __init__(self, ISBN = None, id_autor = None, titulo = None, genero = None, anio = None,
                editorial = None, precio = None, cantidad = None, disponibilidad = None):
        self._ISBN = ISBN
        self._id_autor = id_autor
        self._titulo = titulo
        self._genero = genero
        self._anio = anio
        self._editorial = editorial
        self._precio = precio
        self._cantidad = cantidad
        self._disponibilidad = disponibilidad

    def __str__(self):
        return  f'''
                ISBN: {self._ISBN}
                ID Autor: {self._id_autor}
                Título: {self._titulo}
                Género: {self._genero}
                Año: {self._anio}
                Editorial: {self._editorial}
                Precio: ${self._precio}
                Cantidad: {self._cantidad}
                Disponibilidad: {self._disponibilidad}
                '''
    
    @property
    def ISBN(self):
        return self._ISBN
    
    @ISBN.setter
    def ISBN(self, ISBN):
        self._ISBN = ISBN

    @property
    def id_autor(self):
        return self._id_autor
    
    @id_autor.setter
    def id_autor(self, id_autor):
        self._id_autor = id_autor
    
    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def genero(self):
        return self._genero
    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def anio(self):
        return self._anio
    @anio.setter
    def anio(self, anio):
        self._anio = anio

    @property
    def editorial(self):
        return self._editorial
    @editorial.setter
    def editorial(self, editorial):
        self._editorial = editorial

    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, precio):
        self._precio = precio

    @property
    def cantidad(self):
        return self._cantidad
    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    @property
    def disponibilidad(self):
        return self._disponibilidad
    @disponibilidad.setter
    def disponibilidad(self, disponibilidad):
        self._disponibilidad = disponibilidad

if __name__ == '__main__':
    libro1 = Libro('978-0-306-40615-7', '10', 'PHP 5', 'Programación', 2023, 'Planeta', 399.00, 1, 10)
    log.debug(libro1)

    # Simular un INSERT INTO
    libro1 = Libro(ISBN = '978-0-306-40615-8', id_autor = '12', titulo = 'Análisis Vectorial', 
                   genero = 'Matemáticas', anio = '1999', editorial = 'Cambridge', precio = 599.00, 
                   cantidad = 2, disponibilidad = 13)
    log.debug(libro1)

    #Simular un DELETE
    libro1 = Libro(ISBN = '978-0-306-40615-7')
    log.debug(libro1)
    