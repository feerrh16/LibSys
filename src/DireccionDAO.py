from logger_base import *
from Direccion import *
from Conexion import *
from cursor_del_pool import *


class DireccionDAO:
    _SELECCIONAR = 'SELECT * FROM direccion ORDER BY id_direccion'
    _INSERTAR = 'INSERT INTO direccion(id_cliente, direccion, ciudad, municipio, cp)' \
                ' VALUES(%s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE direccion SET direccion = %s, ciudad = %s, municipio %s, cp = %s,' \
                  ' WHERE id_direccion = %s'
    _BORRAR = 'DELETE FROM direccion WHERE id_direccion = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            direcciones = []
            for registro in registros:
                direccion = Direccion(registro[0], registro[1], registro[2], registro[3], registro[4])
                direcciones.append(direccion)
            return direcciones

    @classmethod
    def insertar(cls, direccion):
        with CursorDelPool() as cursor:
            valores = (direccion.id_cliente, direccion.direccion, direccion.ciudad, direccion.municipio, direccion.cp)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {direccion}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, direccion):
        with CursorDelPool() as cursor:
            valores = (direccion.direccion, direccion.ciudad, direccion.municipio, direccion.cp, direccion.id_direccion)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {direccion}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, direccion):
        with CursorDelPool() as cursor:
            valores = direccion.id_direccion
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {direccion}')
            return cursor.rowcount


if __name__ == '__main__':
    # Insertar un registro

    direccion1 = Direccion(id_cliente=123212,direccion='Sanchez colin 18',ciudad='CDMX',municipio='Gustavo A Madero',
                           cp=56490)
    direccion_insertada = DireccionDAO.insertar(direccion1)
    log.debug(f'Registro insertado en la base de datos: {direccion_insertada}')

    # Actualizar un registro
    direccion1 = Direccion('Gomez Farias', 'Ciudad de Mexico', 'Venustiano Carranza', 39495, 234554444)
    direccion_actualizada = DireccionDAO.actualizar(direccion1)
    log.debug(f'Registros actualizados: {direccion_actualizada}')

    # Eliminar un registro
    direccion1 = Direccion(id_direccion=11232)
    direccion_eliminada = DireccionDAO.borrar(direccion1)
    log.debug(f'Registros eliminados: {direccion_eliminada}')

    # Seleccionar objetos
    direcciones = DireccionDAO.seleccionar()
    for direccion in direcciones:
        log.debug(direccion)
