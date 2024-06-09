from logger_base import *
from Tarjeta import *
from Conexion import *
from cursor_del_pool import *


class TarjetaDAO:
    _SELECCIONAR = 'SELECT * FROM tarjeta ORDER BY num_tarjeta'
    _INSERTAR = 'INSERT INTO tarjeta(num_tarjeta, id_cliente, cvv, fecha_vencimiento, banco)' \
                ' VALUES(%s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE tarjeta SET id_cliente = %s, cvv = %s, fecha_vencimiento = %s, banco = %s' \
                  ' WHERE num_tarjeta = %s'
    _BORRAR = 'DELETE FROM tarjeta WHERE num_tarjeta = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            tarjetas = []
            for registro in registros:
                tarjeta = Tarjeta(registro[0], registro[1], registro[2], registro[3], registro[4])
                tarjetas.append(tarjeta)
            return tarjetas

    @classmethod
    def insertar(cls, tarjeta):
        with CursorDelPool() as cursor:
            valores = (tarjeta.num_tarjeta, tarjeta.id_cliente, tarjeta.cvv, tarjeta.fecha_vencimiento, tarjeta.banco)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {tarjeta}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, tarjeta):
        with CursorDelPool() as cursor:
            valores = (tarjeta.num_tarjeta, tarjeta.id_cliente, tarjeta.cvv, tarjeta.fecha_vencimiento, tarjeta.banco)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {tarjeta}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, tarjeta):
        with CursorDelPool() as cursor:
            valores = tarjeta.num_tarjeta
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {tarjeta}')
            return cursor.rowcount


if __name__ == '__main__':
    # Insertar un registro
    tarjeta1 = Tarjeta(num_tarjeta=5647637483748162, id_cliente=2323213, cvv=344,
                       fecha_vencimiento='23/12/25', banco='Banamex')

    tarjeta_insertada = TarjetaDAO.insertar(tarjeta1)
    log.debug(f'Registro insertado en la base de datos: {tarjeta_insertada}')

    # Actualizar un registro
    tarjeta_actualizada = TarjetaDAO.actualizar(tarjeta1)
    log.debug(f'Registros actualizados: {tarjeta_actualizada}')

    # Eliminar un registro
    tarjeta1 = Tarjeta(num_tarjeta=5647637483748162)
    tarjeta_eliminada = TarjetaDAO.borrar(tarjeta1)
    log.debug(f'Registros eliminados: {tarjeta_eliminada}')

    # Seleccionar objetos
    tarjetas = TarjetaDAO.seleccionar()
    for tarjeta in tarjetas:
        log.debug(tarjeta)
