import sys
from psycopg2 import pool
from logger_base import *

class Conexion:
    _DATABASE = 'LibSys'
    _USERNAME = 'postgres'
    _PASSWORD = 'Password'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CONEXIONES = 1
    _MAX_CONEXIONES = 5
    _pool = None

    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CONEXIONES,
                    cls._MAX_CONEXIONES,
                    host = cls._HOST,
                    user = cls._USERNAME,
                    password = cls._PASSWORD,
                    port = cls._DB_PORT,
                    database = cls._DATABASE
                    )
                
                log.debug(f'Creación exitosa del pool de conexiones: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error al obtener el pool de conexiones: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pool().getconn()
        log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion
    
    @classmethod
    def liberar_conexion(cls, conexion):
        cls.obtener_pool().putconn(conexion)
        log.debug(f'Conexión regresada al pool de conexiones: {conexion}')

    @classmethod
    def cerrar_conexiones(cls):
        cls.obtener_pool().closeall()

    

if __name__ == '__main__':
    conexion1 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion1)
