from asyncio import log
from logger_base import *
from pedido import *
from Conexion import *
from cursor_del_pool import *

class pedidoDAO:
    _SELECCIONAR = 'SELECT * FROM pedido ORDER BY id_Proveedor'
    _INSERTAR = 'INSERT INTO pedido(id_Proveedor, ISBN, Fecha_Pedido, Fecha_Entrega, Cantidad_Pedida, Precio_Total) VALUES(%s, %s, %s, %s, %s, %s )'
    _ACTUALIZAR = 'UPDATE pedido SET id_Proveedor = %s, ISBN = %s, Fecha_Pedido = %s, Fecha_Entrega = %s, Cantidad_Pedida = %s, Precio_Total = %s WHERE id_pedido = %s'
    _BORRAR = 'DELETE FROM pedido WHERE id_Proveedor = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            pedidos = []
            for registro in registros:
                pedido = pedido(registro[0], registro[1], registro[2], registro[3])
                pedidos.append(pedido)
            return pedidos
        
    @classmethod
    def insertar(cls, pedido):
        with CursorDelPool() as cursor:
            valores = (pedido.id_Proveedor, pedido.ISBN, pedido.Fecha_Pedido, pedido.Fecha_Entrega, pedido.Cantidad_Pedida, pedido.Precio_Total)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {pedido}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, pedido):
        with CursorDelPool() as cursor:
            valores = (pedido.id_Proveedor, pedido.ISBN, pedido.Fecha_Pedido, pedido.Fecha_Entrega, pedido.Cantidad_Pedida, pedido.Precio_Total)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {pedido}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, pedido):
        with CursorDelPool() as cursor:
            valores = (pedido.id_Proveedor, pedido.ISBN, pedido.Fecha_Pedido, pedido.Fecha_Entrega, pedido.Cantidad_Pedida, pedido.Precio_Total)
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {pedido}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    pedido1 = pedido1(id_Proveedor = '1', ISBN = '0987', Fecha_Pedido = '03/03/2002', Fecha_Entrega = '03/03/2002', Cantidad_Pedida = '3', Precio_Total = '$290')
    pedidos_insertados = pedidoDAO.insertar(pedido1)
    log.debug(f'Registro insertado en la base de datos: {pedidos_insertados}')

    # Actualizar un registro
    pedido1 = pedido1(1, 'tukyol', 'Javier', 'Juárez', 'Morales')
    pedidos_actualizados = pedidoDAO.actualizar(pedido1)
    log.debug(f'Registros actualizados: {pedidos_actualizados}')
    

    # Eliminar un registro
    pedido1 = pedido1(id_Proveedor = 1)
    pedidos_eliminados = pedidoDAO.borrar(pedido1)
    log.debug(f'Registros eliminados: {pedidos_eliminados}')
    
    # Seleccionar objetos
    empleados = pedidoDAO.seleccionar()
    for pedido in pedidos:
        log.debug(pedido)
