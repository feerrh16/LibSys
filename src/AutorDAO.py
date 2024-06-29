from logger_base import *
from Autor import *
from Conexion import *
from cursor_del_pool import *

class AutorDAO:
    _SELECCIONAR = 'SELECT * FROM autor ORDER BY id_autor'
    _INSERTAR = 'INSERT INTO autor(nombre) VALUES(%s)'
    _ACTUALIZAR = 'UPDATE autor SET nombre = %s WHERE id_autor = %s'
    _BORRAR = 'DELETE FROM autor WHERE id_autor = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            autores = []
            for registro in registros:
                autor = Autor(registro[0], registro[1])
                autores.append(autor)
            return autores

    @classmethod
    def insertar(cls, autor):
        with CursorDelPool() as cursor:
            # Verificamos si existe el autor en la tabla autor_libro
            cursor.execute('SELECT id_autor FROM autor_libro WHERE id_autor = %s', (autor.id_autor, ))
            valores = (autor.nombre,)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {autor}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, autor):
        with CursorDelPool() as cursor:
            valores = (autor.nombre, autor.id_autor)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {autor}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, autor):
        with CursorDelPool() as cursor:
            valores = (autor.id_autor,)
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {autor}')
            return cursor.rowcount
        
if __name__ == '__main__':
    # Insertar un registro
    autor1 = Autor(id_autor = 8, nombre='Fabian Gasca')
    autores_insertados = AutorDAO.insertar(autor1)
    log.debug(f'Registro insertado en la base de datos: {autores_insertados}')

    # Actualizar un registro
    autor1 = Autor(id_autor=1, nombre='Alice Oseman')
    autores_actualizados = AutorDAO.actualizar(autor1)
    log.debug(f'Registros actualizados: {autores_actualizados}')
    
    # Eliminar un registro
    autor1 = Autor(id_autor=1)
    autores_eliminados = AutorDAO.borrar(autor1)
    log.debug(f'Registros eliminados: {autores_eliminados}')
    
    # Seleccionar objetos
    autores = AutorDAO.seleccionar()
    for autor in autores:
        log.debug(autor)
