from logger_base import *
from TipoVenta import *
from Conexion import *
from cursor_del_pool import *

class TipoVentaDAO:
    _SELECCIONAR = 'SELECT * FROM empleado ORDER BY id_empleado'
    _INSERTAR = 'INSERT INTO empleado(nombre_usuario, nombre, apellido_paterno, apellido_materno) VALUES(%s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE empleado SET nombre_usuario = %s, nombre = %s, apellido_paterno = %s, apellido_materno = %s WHERE id_empleado = %s'
    _BORRAR = 'DELETE FROM empleado WHERE id_empleado = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            tipo_ventas = []
            for registro in registros:
                tipo_venta = TipoVenta(registro[0], registro[1])
                tipo_ventas.append(tipo_venta)
            return tipo_ventas
        
    @classmethod
    def insertar(cls, tipo_venta):
        with CursorDelPool() as cursor:
            valores = (tipo_venta.id_tipo, tipo_venta.nombre)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {tipo_venta}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, tipo_venta):
        with CursorDelPool() as cursor:
            valores = (tipo_venta.id_tipo, tipo_venta.nombre)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {tipo_venta}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, tipo_venta):
        with CursorDelPool() as cursor:
            valores = (tipo_venta.id_tipo, tipo_venta.nombre)
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {tipo_venta}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    tipo_venta1 = TipoVenta(id_tipo = 2, nombre = 'Linea')
    tipo_venta_insertados = TipoVentaDAO.insertar(tipo_venta1)
    log.debug(f'Registro insertado en la base de datos: {tipo_venta_insertados}')

    # Actualizar un registro
    tipo_venta1 = TipoVenta(2, 'Linea')
    tipo_ventas_actualizados = TipoVentaDAO.actualizar(tipo_venta1)
    log.debug(f'Registros actualizados: {tipo_ventas_actualizados}')
    

    # Eliminar un registro
    tipo_venta1 = TipoVenta(id_tipo = 2)
    tipo_ventas_eliminados = TipoVentaDAO.borrar(tipo_venta1)
    log.debug(f'Registros eliminados: {tipo_ventas_eliminados}')
    
    # Seleccionar objetos
    tipo_ventas = TipoVentaDAO.seleccionar()
    for tipo_venta in tipo_ventas:
        log.debug(tipo_venta)
