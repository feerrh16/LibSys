from logger_base import *
from Cliente import *
from Conexion import *
from cursor_del_pool import *

class ClienteDAO:
    _SELECCIONAR = 'SELECT * FROM cliente ORDER BY id_cliente'
    _INSERTAR = 'INSERT INTO cliente(nombre_usuario, nombre, apellido_paterno, apellido_materno, id_direccion, correo, telefono, num_tarjeta) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE cliente SET nombre_usuario = %s, nombre = %s, apellido_paterno = %s, apellido_materno = %s, id_direccion = %s, correo = %s, telefono = %s, num_tarjeta = %s WHERE id_cliente = %s'
    _BORRAR = 'DELETE FROM cliente WHERE id_cliente = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7], registro[8])
                clientes.append(cliente)
            return clientes
        
    @classmethod
    def insertar(cls, cliente):
        with CursorDelPool() as cursor:
            valores = (cliente.nombre_usuario, cliente.nombre, cliente.apellido_paterno, cliente.apellido_materno, cliente.id_direccion, cliente.correo, cliente.telefono, cliente.num_tarjeta)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {cliente}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, cliente):
        with CursorDelPool() as cursor:
            valores = (cliente.nombre_usuario, cliente.nombre, cliente.apellido_paterno, cliente.apellido_materno, cliente.id_direccion, cliente.correo, cliente.telefono, cliente.num_tarjeta, cliente.id_cliente)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {cliente}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, cliente):
        with CursorDelPool() as cursor:
            valores = (cliente.id_cliente, )
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {cliente}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    cliente1 = Cliente(nombre_usuario = 'JK_2405', nombre = 'Jessica', apellido_paterno = 'Rodríguez', apellido_materno = 'Pérez', id_direccion = 11, correo = 'jk2405@mail.com', telefono = '555 555 555', num_tarjeta = '1010 1010 1010 1010')
    clientes_insertados = ClienteDAO.insertar(cliente1)
    log.debug(f'Registro insertado en la base de datos: {clientes_insertados}')

    # Actualizar un registro
    cliente1 = Cliente(1, 'tukyol', 'Javier', 'Juárez', 'Morales', 3, 'tukyol@mail.com', '555 555 555', '0101 0101 0101 0101')
    clientes_actualizados = ClienteDAO.actualizar(cliente1)
    log.debug(f'Registros actualizados: {clientes_actualizados}')
    

    # Eliminar un registro
    cliente1 = Cliente(id_cliente = 1)
    clientes_eliminados = ClienteDAO.borrar(cliente1)
    log.debug(f'Registros eliminados: {clientes_eliminados}')
    
    # Seleccionar objetos
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        log.debug(cliente)
