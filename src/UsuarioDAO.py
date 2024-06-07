from logger_base import *
from Persona import *
from Conexion import *
from cursor_del_pool import *

class PersonaDAO:
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, mail) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre = %s, apellido = %s, mail = %s WHERE id_persona = %s'
    _BORRAR = 'DELETE FROM persona WHERE id_persona = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas
        
    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.mail)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {persona}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.mail, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {persona}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona, )
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {persona}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    persona1 = Persona(nombre = 'Alejandra', apellido = 'Téllez', mail = 'atellez@mail.com')
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f'Registro insertado en la base de datos: {personas_insertadas}')

    # Actualizar un registro
    persona1 = Persona(1, 'Juan', 'Pérez', 'jperez@mail.com')
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f'Registros actualizados: {personas_actualizadas}')
    

    # Eliminar un registro
    persona1 = Persona(id_persona = 16)
    personas_eliminadas = PersonaDAO.borrar(persona1)
    log.debug(f'Registros eliminados: {personas_eliminadas}')
    
    # Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
