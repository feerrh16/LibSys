from logger_base import *
from Cliente import *
from Conexion import *
from cursor_del_pool import *

class ClienteDAO:
    _SELECCIONAR = '''
        SELECT c.id_cliente, c.nombre_usuario, c.nombre, c.apellido_paterno, c.apellido_materno, 
               c.id_direccion, d.direccion, c.correo, c.telefono, c.num_tarjeta, t.banco
        FROM cliente c
        LEFT JOIN direccion d ON c.id_direccion = d.id_direccion
        LEFT JOIN tarjeta t ON c.num_tarjeta = t.num_tarjeta
        ORDER BY c.id_cliente
    '''
    _INSERTAR = '''
        INSERT INTO cliente(nombre_usuario, nombre, apellido_paterno, apellido_materno, id_direccion, correo, telefono, num_tarjeta) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
    '''
    _ACTUALIZAR = '''
        UPDATE cliente 
        SET nombre_usuario = %s, nombre = %s, apellido_paterno = %s, apellido_materno = %s, id_direccion = %s, correo = %s, telefono = %s, num_tarjeta = %s 
        WHERE id_cliente = %s
    '''
    _BORRAR = 'DELETE FROM cliente WHERE id_cliente = %s'
    _BORRAR_FAVORITOS = 'DELETE FROM favoritos WHERE id_cliente = %s'
    _BORRAR_TARJETA = 'DELETE FROM tarjeta WHERE id_cliente = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7], registro[8], registro[9], registro[10])
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
            # Verificar existencia de id_direccion y num_tarjeta
            cursor.execute('SELECT 1 FROM direccion WHERE id_direccion = %s', (cliente.id_direccion,))
            if cursor.fetchone() is None:
                log.error(f'No existe la dirección con id {cliente.id_direccion}')
                return 0
            cursor.execute('SELECT 1 FROM tarjeta WHERE num_tarjeta = %s', (cliente.num_tarjeta,))
            if cursor.fetchone() is None:
                log.error(f'No existe la tarjeta con número {cliente.num_tarjeta}')
                return 0

            valores = (cliente.nombre_usuario, cliente.nombre, cliente.apellido_paterno, cliente.apellido_materno, cliente.id_direccion, cliente.correo, cliente.telefono, cliente.num_tarjeta, cliente.id_cliente)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {cliente}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, cliente):
        with CursorDelPool() as cursor:
            # Primero eliminar las referencias en la tabla favoritos
            cursor.execute(cls._BORRAR_FAVORITOS, (cliente.id_cliente,))
            log.debug(f'Referencias eliminadas en favoritos para el cliente: {cliente.id_cliente}')
            
            # Luego eliminar las referencias en la tabla tarjeta
            cursor.execute(cls._BORRAR_TARJETA, (cliente.id_cliente,))
            log.debug(f'Referencias eliminadas en tarjeta para el cliente: {cliente.id_cliente}')
            
            # Finalmente eliminar el cliente
            valores = (cliente.id_cliente,)
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {cliente}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    cliente1 = Cliente(nombre_usuario='JK_2405', nombre='Jessica', apellido_paterno='Rodríguez', apellido_materno='Pérez', id_direccion=11, correo='jk2405@mail.com', telefono='555 555 555', num_tarjeta='1234123412341234')
    clientes_insertados = ClienteDAO.insertar(cliente1)
    log.debug(f'Registro insertado en la base de datos: {clientes_insertados}')

    # Actualizar un registro
    cliente1 = Cliente(1, 'tukyol', 'Javier', 'Juárez', 'Morales', 3, 'tukyol@mail.com', '555 555 555', '2345234523452345')
    clientes_actualizados = ClienteDAO.actualizar(cliente1)
    log.debug(f'Registros actualizados: {clientes_actualizados}')

    # Eliminar un registro
    cliente1 = Cliente(id_cliente=1)
    clientes_eliminados = ClienteDAO.borrar(cliente1)
    log.debug(f'Registros eliminados: {clientes_eliminados}')

    # Seleccionar objetos
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        log.debug(cliente)
