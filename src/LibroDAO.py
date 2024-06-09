from logger_base import *
from Libro import *
from Conexion import *
from cursor_del_pool import *

class LibroDAO:
    _SELECCIONAR = 'SELECT * FROM libro ORDER BY ISBN'
    _INSERTAR = 'INSERT INTO libro(ISBN, id_autor, titulo, genero, anio, editorial, precio, cantidad, disponibilidad) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE libro SET id_autor = %s, titulo = %s, genero = %s, anio = %s, editorial = %s, precio = %s, cantidad = %s, disponibilidad = %s  WHERE ISBN = %s'
    _BORRAR = 'DELETE FROM libro WHERE ISBN = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            libros = []
            for registro in registros:
                libro = Libro(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7], registro[8])
                libros.append(libro)
            return libros
        
    @classmethod
    def insertar(cls, libro):
        with CursorDelPool() as cursor:
            valores = (libro.ISBN, libro.id_autor, libro.titulo, libro.genero, libro.anio, libro.editorial, libro.precio, libro.cantidad, libro.disponibilidad)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {libro}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, libro):
        with CursorDelPool() as cursor:
            valores = (libro.id_autor, libro.titulo, libro.genero, libro.anio, libro.editorial, libro.precio, libro.cantidad, libro.disponibilidad)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {libro}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, libro):
        with CursorDelPool() as cursor:
            valores = (libro.ISBN, )
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {libro}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    libro1 = Libro(ISBN = '978-0-306-40615-7', id_autor = 2, titulo = 'El gran diseño', genero = 'Ciencia', anio = 2013, editorial = 'Cambridge', precio = 699.00, cantidad = 1, disponibilidad = 23)
    libros_insertados = LibroDAO.insertar(libro1)
    log.debug(f'Registro insertado en la base de datos: {libros_insertados}')

    # Actualizar un registro
    libro1 = Libro('978-0-306-40615-8', 2, 'El Gran Diseño', 'Académico', 2013, 'Oxford', 799.00, 1, 20)
    libros_actualizados = LibroDAO.actualizar(libro1)
    log.debug(f'Registros actualizados: {libros_actualizados}')
    

    # Eliminar un registro
    libro1 = Libro(ISBN = '978-0-306-40615-7')
    libros_eliminados = LibroDAO.borrar(libro1)
    log.debug(f'Registros eliminados: {libros_eliminados}')
    
    # Seleccionar objetos
    libros = LibroDAO.seleccionar()
    for libro in libros:
        log.debug(libro)
