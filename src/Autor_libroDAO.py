from logger_base import *
from Autor_libro import *
from Conexion import *
from cursor_del_pool import *

class Autor_libroDAO:
    _SELECCIONAR = 'SELECT * FROM autor_libro ORDER BY id_autor'
    _INSERTAR = 'INSERT INTO autor_libro(isbn) VALUES(%s)'
    _ACTUALIZAR = 'UPDATE autor_libro SET isbn = %s WHERE id_autor = %s'
    _BORRAR = 'DELETE FROM autor_libro WHERE id_autor = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            autores_lib = []
            for registro in registros:
                autor_lib = Autor_libro(registro[0],registro[1]);
                autores_lib.append(autor_lib)
    
    @classmethod
    def insertar(cls, autor_lib):
        with CursorDelPool() as cursor:
            valores = (autor_lib.isbn)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {autor_lib}')
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls, autor_lib):
        with CursorDelPool() as cursor:
            valores = (autor_lib.isbn)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {autor_lib}')
            return cursor.rowcount
    
    @classmethod
    def borrar(cls, autor_lib):
        with CursorDelPool() as cursor:
            valores = (autor_lib.id_autor)
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {autor_lib}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    autor_lib1 = Autor_libro(isbn = '9796078828326')
    autores_insertados = Autor_libroDAO.insertar(autor_lib1)
    log.debug(f'Registro insertado en la base de datos: {autores_insertados}')

    # Actualizar un registro
    autor_lib1 = Autor_libro(1, '9796078828326')
    autores_actualizados = Autor_libroDAO.actualizar(autor_lib1)
    log.debug(f'Registros actualizados: {autores_actualizados}')
    

    # Eliminar un registro
    autor_lib1 = Autor_libro(id_autor = 1)
    autores_eliminados = Autor_libroDAO.borrar(autor_lib1)
    log.debug(f'Registros eliminados: {autores_eliminados}')
    
    # Seleccionar objetos
    autores_lib = Autor_libroDAO.seleccionar()
    for autor_lib in autores_lib:
        log.debug(autor_lib)