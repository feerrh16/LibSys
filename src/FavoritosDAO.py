from logger_base import *
from Favoritos import *
from Conexion import *
from cursor_del_pool import *

class FavoritosDAO:
    _SELECCIONAR = 'SELECT * FROM favoritos ORDER BY id_cliente'
    _INSERTAR = 'INSERT INTO favoritos(isbn) VALUES(%s)'
    _ACTUALIZAR = 'UPDATE favoritos SET isbn = %s WHERE id_cliente = %s'
    _BORRAR = 'DELETE FROM favoritos WHERE id_cliente = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            favoritos = []
            for registro in registros:
                favoritos = Favoritos(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7], registro[8])
                favoritos.append(favoritos)
            return favoritos
        
    @classmethod
    def insertar(cls, favoritos):
        with CursorDelPool() as cursor:
            valores = (favoritos.isbn)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {favoritos}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, favoritos):
        with CursorDelPool() as cursor:
            valores = (favoritos.isbn, favoritos.id_cliente)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {favoritos}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, favorito):
        with CursorDelPool() as cursor:
            valores = (favorito.id_cliente, )
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {favorito}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    favorito1 = Favoritos(isbn= '9780062310637')
    favoritos_insertados = FavoritosDAO.insertar(favorito1)
    log.debug(f'Registro insertado e    n la base de datos: {favoritos_insertados}')

    # Actualizar un registro
    favorito1 = Favoritos(1, '9780062310637')
    favoritos_actualizados = FavoritosDAO.actualizar(favorito1)
    log.debug(f'Registros actualizados: {favoritos_actualizados}')
    

    # Eliminar un registro
    favorito1 = Favoritos(id_cliente = 1)
    favoritos_eliminados = FavoritosDAO.borrar(favorito1)
    log.debug(f'Registros eliminados: {favoritos_eliminados}')
    
    # Seleccionar objetos
    favoritos = FavoritosDAO.seleccionar()
    for favoritos in favoritos:
        log.debug(favoritos)