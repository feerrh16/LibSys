from logger_base import *
from proveedor import *
from Conexion import *
from cursor_del_pool import *


class ProveedorDAO:
    _SELECCIONAR = 'SELECT * FROM proveedor ORDER BY id_proveedor'
    _INSERTAR = 'INSERT INTO proveedor(id_proveedor, nombre, tel_contacto) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE proveedor SET nombre = %s, tel_contacto %s WHERE id_proveedor = %s'
    _BORRAR = 'DELETE FROM proveedor WHERE id_proveedor = %s'

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

    def insertar(cls, proveedor):
        with CursorDelPool() as cursor:
            cursor.execute('SELECT * FROM proveedor WHERE id_proveedor = %s', (proveedor.id_proveedor,))
            registro_existente = cursor.fetchone()
    
            if registro_existente:
                # Handle existing record case
                log.error(f'Ya existe un registro con id_proveedor: {proveedor.id_proveedor}')
                return None
    
            valores = (proveedor.id_proveedor, proveedor.nombre, proveedor.tel_contacto)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {proveedor}')
            return cursor.rowcount


    @classmethod
    def actualizar(cls, proveedor):
        with CursorDelPool() as cursor:
            valores = (proveedor.nombre, proveedor.tel_contacto, proveedor.id_proveedor)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {proveedor}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, proveedor):
        with CursorDelPool() as cursor:
            valores = (proveedor.id_proveedor, proveedor.nombre, proveedor.tel_contacto)
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {proveedor}')
            return cursor.rowcount


if __name__ == '__main__':
    # Insertar un registro
    proveedor1 = Proveedor(id_proveedor=10, nombre='Proveedor10', tel_contacto=5259016435)
    proveedor_insertada = ProveedorDAO.insertar(proveedor1)
    log.debug(f'Registro insertado en la base de datos: {proveedor_insertada}')

    # Actualizar un registro
    proveedor1 = Proveedor(1, 'Juan Sánchez', 5544663344)
    proveedor_actualizado = ProveedorDAO.actualizar(proveedor1)
    log.debug(f'Registros actualizados: {proveedor_actualizado}')

    # Eliminar un registro
    proveedor1 = Proveedor(id_proveedor = 5)
    proveedor_eliminado = ProveedorDAO.borrar(proveedor1)
    log.debug(f'Registros eliminados: {proveedor_eliminado}')

    # Seleccionar objetos
    proveedores = ProveedorDAO.seleccionar()
    for Proveedor in proveedores:
        log.debug(Proveedor)
