from logger_base import *
from Autor_Libro import *
from Conexion import *
from cursor_del_pool import *

class Autor_LibroDAO:
    _SELECCIONAR = 'SELECT * FROM autor_libro ORDER BY id_autor'
    _INSERTAR = 'INSERT INTO autor_libro(id_autor, ISBN) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE autor_libro SET ISBN = %s WHERE id_autor = %s'
    _BORRAR = 'DELETE FROM autor_libro WHERE id_autor = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            autores_libros = []
            for registro in registros:
                autor_libro = Autor_Libro(registro[0], registro[1])
                autores_libros.append(autor_libro)
            return autores_libros

    @classmethod
    def insertar(cls, autor_libro):
        with CursorDelPool() as cursor:
            # Verificar si el autor existe
            cursor.execute('SELECT id_autor FROM autor WHERE id_autor = %s', (autor_libro.id_autor,))
            autor_existente = cursor.fetchone()
            if not autor_existente:
                raise ValueError(f"El autor con id_autor {autor_libro.id_autor} no existe en la tabla autor.")
            # Verificar si el libro existe
            cursor.execute('SELECT ISBN FROM libro WHERE ISBN = %s', (autor_libro.ISBN,))
            libro_existente = cursor.fetchone()
            if not libro_existente:
                raise ValueError(f"El libro con ISBN {autor_libro.ISBN} no existe en la tabla libro.")
            valores = (autor_libro.id_autor, autor_libro.ISBN)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {autor_libro}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, autor_libro):
        with CursorDelPool() as cursor:
            # Verificar si el libro existe
            cursor.execute('SELECT ISBN FROM libro WHERE ISBN = %s', (autor_libro.ISBN,))
            libro_existente = cursor.fetchone()
            if not libro_existente:
                raise ValueError(f"El libro con ISBN {autor_libro.ISBN} no existe en la tabla libro.")
            valores = (autor_libro.ISBN, autor_libro.id_autor)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {autor_libro}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, autor_libro):
        with CursorDelPool() as cursor:
            valores = (autor_libro.id_autor,)
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {autor_libro}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    try:
        autor_libro1 = Autor_Libro(id_autor=7, ISBN=9780747532700)
        autores_insertados = Autor_LibroDAO.insertar(autor_libro1)
        log.debug(f'Registro insertado en la base de datos: {autores_insertados}')
    except ValueError as e:
        log.error(e)

    # Actualizar un registro
    try:
        autor_libro1 = Autor_Libro(1, 9796078828326)
        autores_actualizados = Autor_LibroDAO.actualizar(autor_libro1)
        log.debug(f'Registros actualizados: {autores_actualizados}')
    except ValueError as e:
        log.error(e)

    # Eliminar un registro
    autor_libro1 = Autor_Libro(id_autor=1)
    autores_eliminados = Autor_LibroDAO.borrar(autor_libro1)
    log.debug(f'Registros eliminados: {autores_eliminados}')

    # Seleccionar objetos
    autores_libros = Autor_LibroDAO.seleccionar()
    for autor_libro in autores_libros:
        log.debug(autor_libro)
