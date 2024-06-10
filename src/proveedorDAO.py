from logger_base import *
from Direccion import *
from Conexion import *
from cursor_del_pool import *


class DireccionDAO:
    _SELECCIONAR = 'SELECT * FROM proveedor ORDER BY id_Proveedor'
    _INSERTAR = 'INSERT INTO proveedor(id_Proveedor, Nombre, Tel_Contacto)' \
                ' VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE proveedor SET id_proveedor = %s, Nombre = %s, Tel_Contacto %s' \
                  ' WHERE id_Proveedor = %s'
    _BORRAR = 'DELETE FROM proveedor WHERE id_Proveedor = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            proveedores = []
            for registro in registros:
                proveedor = Proveedor(registro[0], registro[1], registro[2], registro[3], registro[4])
                proveedores.append(proveedor)
            return proveedores

    @classmethod
    def insertar(cls, proveedor):
        with CursorDelPool() as cursor:
            valores = (proveedor.id_Proveedor, proveedor.Nombre, proveedor.Tel_Contacto)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {proveedor}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, proveedor):
        with CursorDelPool() as cursor:
            valores = (proveedor.id_Proveedor, proveedor.Nombre, proveedor.Tel_Contacto)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {proveedor}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, proveedor):
        with CursorDelPool() as cursor:
            valores = (proveedor.id_Proveedor, proveedor.Nombre, proveedor.Tel_Contacto)
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {proveedor}')
            return cursor.rowcount


if __name__ == '__main__':
    # Insertar un registro

    proveedor1 = proveedor(id_Proveedor=123212,Nombre='Sanchez',Tel_Contacto=234566)
    proveedor_insertada = proveedorDAO.insertar(proveedor1)
    log.debug(f'Registro insertado en la base de datos: {proveedor_insertada}')

    # Actualizar un registro
    proveedor1 = proveedor(id_Proveedor=123212,Nombre='Sanchez',Tel_Contacto=234566)
    proveedor_actualizada = proveedorDAO.actualizar(proveedor1)
    log.debug(f'Registros actualizados: {proveedor_actualizada}')

    # Eliminar un registro
    proveedor1 = proveedor(id_Proveedor=123212,Nombre='Sanchez',Tel_Contacto=234566)
    proveedor_eliminada = proveedorDAO.borrar(proveedor1)
    log.debug(f'Registros eliminados: {proveedor_eliminada}')

    # Seleccionar objetos
    proveedores = proveedorDAO.seleccionar()
    for proveedor in proveedores:
        log.debug(proveedor)
