from logger_base import *
from Usuario import *
from Conexion import *
from cursor_del_pool import *

class UsuarioDAO:
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY nombre_usuario'
    _INSERTAR = 'INSERT INTO usuario(nombre_usuario, contrasena, rol) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET contrasena = %s, rol = %s WHERE nombre_usuario = %s'
    _BORRAR = 'DELETE FROM usuario WHERE nombre_usuario = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
        
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.nombre_usuario, usuario.contrasena, usuario.rol)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {usuario}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.contrasena, usuario.rol, usuario.nombre_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {usuario}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.nombre_usuario, )
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {usuario}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    usuario1 = Usuario(nombre_usuario = 'jperez', contrasena = 'password', rol = 'Ayudante General')
    usuarios_insertados = UsuarioDAO.insertar(usuario1)
    log.debug(f'Registro insertado en la base de datos: {usuarios_insertados}')

    # Actualizar un registro
    usuario1 = Usuario('jperez', 'drowssap', 'Gerente')
    usuarios_actualizados = UsuarioDAO.actualizar(usuario1)
    log.debug(f'Registros actualizados: {usuarios_actualizados}')
    

    # Eliminar un registro
    usuario1 = Usuario(id_persona = 1)
    usuarios_eliminados = UsuarioDAO.borrar(usuario1)
    log.debug(f'Registros eliminados: {usuarios_eliminados}')
    
    # Seleccionar objetos
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
