from logger_base import *
from Empleado import *
from Conexion import *
from cursor_del_pool import *

class EmpleadoDAO:
    _SELECCIONAR = 'SELECT * FROM empleado ORDER BY id_empleado'
    _INSERTAR = 'INSERT INTO empleado(nombre_usuario, nombre, apellido_paterno, apellido_materno) VALUES(%s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE empleado SET nombre_usuario = %s, nombre = %s, apellido_paterno = %s, apellido_materno = %s WHERE id_empleado = %s'
    _BORRAR = 'DELETE FROM empleado WHERE id_empleado = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            empleados = []
            for registro in registros:
                empleado = Empleado(registro[0], registro[1], registro[2], registro[3])
                empleados.append(empleado)
            return empleados
        
    @classmethod
    def insertar(cls, empleado):
        with CursorDelPool() as cursor:
            valores = (empleado.nombre_usuario, empleado.nombre, empleado.apellido_paterno, empleado.apellido_materno)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {empleado}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, empleado):
        with CursorDelPool() as cursor:
            valores = (empleado.nombre_usuario, empleado.nombre, empleado.apellido_paterno, empleado.apellido_materno)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {empleado}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, empleado):
        with CursorDelPool() as cursor:
            valores = (empleado.id_empleado, )
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {empleado}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    empleado1 = Empleado(nombre_usuario = 'JK_2405', nombre = 'Jessica', apellido_paterno = 'Rodríguez', apellido_materno = 'Pérez')
    empleados_insertados = EmpleadoDAO.insertar(empleado1)
    log.debug(f'Registro insertado en la base de datos: {empleados_insertados}')

    # Actualizar un registro
    empleado1 = Empleado(1, 'tukyol', 'Javier', 'Juárez', 'Morales')
    empleados_actualizados = EmpleadoDAO.actualizar(empleado1)
    log.debug(f'Registros actualizados: {empleados_actualizados}')
    

    # Eliminar un registro
    empleado1 = Empleado(id_empleado = 1)
    empleados_eliminados = EmpleadoDAO.borrar(empleado1)
    log.debug(f'Registros eliminados: {empleados_eliminados}')
    
    # Seleccionar objetos
    empleados = EmpleadoDAO.seleccionar()
    for empleado in empleados:
        log.debug(empleado)
