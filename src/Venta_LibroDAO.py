from logger_base import *
from Venta_Libro import *
from Conexion import *
from cursor_del_pool import *

class Venta_LibroDAO:
    _SELECCIONAR = 'SELECT * FROM empleado ORDER BY id_empleado'
    _INSERTAR = 'INSERT INTO empleado(nombre_usuario, nombre, apellido_paterno, apellido_materno) VALUES(%s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE empleado SET nombre_usuario = %s, nombre = %s, apellido_paterno = %s, apellido_materno = %s WHERE id_empleado = %s'
    _BORRAR = 'DELETE FROM empleado WHERE id_empleado = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            venta_libros = []
            for registro in registros:
                venta_libro = Venta_Libro(registro[0], registro[1], registro[2])
                venta_libros.append(venta_libro)
            return venta_libros
        
    @classmethod
    def insertar(cls, venta_libro):
        with CursorDelPool() as cursor:
            valores = (venta_libro.id_venta, venta_libro.ISBN, venta_libro.cantidad)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {venta_libro}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, venta_libro):
        with CursorDelPool() as cursor:
            valores = (venta_libro.id_venta, venta_libro.ISBN, venta_libro.cantidad)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {venta_libro}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, venta_libro):
        with CursorDelPool() as cursor:
            valores = (venta_libro.id_venta, venta_libro.ISBN, venta_libro.cantidad)
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {venta_libro}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    venta_libro1 = Venta_Libro(id_venta = 2, ISBN = 3, cantidad = 4)
    venta_libros_insertados = Venta_LibroDAO.insertar(venta_libro1)
    log.debug(f'Registro insertado en la base de datos: {venta_libros_insertados}')

    # Actualizar un registro
    venta_libro1 = Venta_Libro(2, 3, 4)
    venta_libros_actualizados = Venta_LibroDAO.actualizar(venta_libro1)
    log.debug(f'Registros actualizados: {venta_libros_actualizados}')
    

    # Eliminar un registro
    venta_libro1 = Venta_Libro(id_venta = 2)
    venta_libros_eliminados = Venta_LibroDAO.borrar(venta_libro1)
    log.debug(f'Registros eliminados: {venta_libros_eliminados}')
    
    # Seleccionar objetos
    venta_libros = Venta_LibroDAO.seleccionar()
    for venta_libro in venta_libros:
        log.debug(venta_libro)
