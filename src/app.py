from flask import Flask, render_template
from flask_socketio import SocketIO, send
from Autor_LibroDAO import Autor_LibroDAO
from Autor_Libro import Autor_Libro
from Autor import Autor
from ClienteDAO import ClienteDAO
from Cliente import Cliente
from Direccion import Direccion
from DireccionDAO import DireccionDAO
from Empleado import Empleado
from EmpleadoDAO import EmpleadoDAO
from Favoritos import Favoritos
from FavoritosDAO import FavoritosDAO
from Libro import Libro
from LibroDAO import LibroDAO
from pedido import Pedido
from pedidoDAO import PedidoDAO
from Proveedor import Proveedor
from proveedorDAO import ProveedorDAO
from Tarjeta import Tarjeta
from TarjetaDAO import TarjetaDAO
from TipoVenta import TipoVenta
from TipoVentaDAO import TipoVentaDAO
from Usuario import Usuario
from UsuarioDAO import UsuarioDAO
from Venta_Libro import Venta_Libro
from Venta_LibroDAO import Venta_LibroDAO
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('message')
def handle_message(msg):
    data = json.loads(msg)
    action = data.get('action')
    response = {'status': 'error', 'message': 'Invalid action'}

    try:
        # Acciones para Autor_Libro
        if action == 'get_autor_libros':
            autores_libros = Autor_LibroDAO.seleccionar()
            response = {'status': 'success', 'data': [str(autor_libro) for autor_libro in autores_libros]}
        elif action == 'add_autor_libro':
            autor_libro = Autor_Libro(id_autor=data['id_autor'], ISBN=data['ISBN'])
            Autor_LibroDAO.insertar(autor_libro)
            response = {'status': 'success', 'message': 'Autor_Libro added successfully'}
        elif action == 'update_autor_libro':
            autor_libro = Autor_Libro(id_autor=data['id_autor'], ISBN=data['ISBN'])
            Autor_LibroDAO.actualizar(autor_libro)
            response = {'status': 'success', 'message': 'Autor_Libro updated successfully'}
        elif action == 'delete_autor_libro':
            autor_libro = Autor_Libro(id_autor=data['id_autor'])
            Autor_LibroDAO.borrar(autor_libro)
            response = {'status': 'success', 'message': 'Autor_Libro deleted successfully'}

        # Acciones para Cliente
        if action == 'get_clientes':
            clientes = ClienteDAO.seleccionar()
            response = {'status': 'success', 'data': [str(cliente) for cliente in clientes]}
        elif action == 'add_clientes':
            cliente = Cliente(nombre_usuario=data['nombre_usuario'], nombre=data['nombre'],
                              apellido_paterno=data['apellido_paterno'], apellido_materno=data['apellido_materno'],
                              id_direccion=data['id_direccion'], correo=data['correo'], telefono=data['telefono'],
                              num_tarjeta=data['num_tarjeta'])
            ClienteDAO.insertar(cliente)
            response = {'status': 'success', 'message': 'Cliente added successfully'}
        elif action == 'update_clientes':
            cliente = Cliente(nombre_usuario=data['nombre_usuario'], nombre=data['nombre'],
                              apellido_paterno=data['apellido_paterno'], apellido_materno=data['apellido_materno'],
                              id_direccion=data['id_direccion'], correo=data['correo'], telefono=data['telefono'],
                              num_tarjeta=data['num_tarjeta'])
            ClienteDAO.actualizar(cliente)
            response = {'status': 'success', 'message': 'Cliente updated successfully'}
        elif action == 'delete_autor_libro':
            cliente = Cliente(id_cliente=data['id_cliente'])
            ClienteDAO.borrar(autor_libro)
            response = {'status': 'success', 'message': 'Cliente deleted successfully'}

        # Acciones para Direccion
        if action == 'get_direcciones':
            direcciones = DireccionDAO.seleccionar()
            response = {'status': 'success', 'data': [str(direccion) for direccion in direcciones]}
        elif action == 'add_direccion':
            direccion = Direccion(id_cliente=data['id_cliente'], direccion=data['direccion'], ciudad=data['ciudad'],
                                  municipio=data['municipio'], cp=data['cp'])
            DireccionDAO.insertar(direccion)
            response = {'status': 'success', 'message': 'Direccion added successfully'}
        elif action == 'update_direccion':
            direccion = Direccion(id_cliente=data['id_cliente'], direccion=data['direccion'], ciudad=data['ciudad'],
                                  municipio=data['municipio'], cp=data['cp'])
            DireccionDAO.actualizar(direccion)
            response = {'status': 'success', 'message': 'Direccion updated successfully'}
        elif action == 'delete_direccion':
            direccion = Direccion(id_direccion=data['id_direccion'])
            DireccionDAO.borrar(direccion)
            response = {'status': 'success', 'message': 'Direccion deleted successfully'}

        # Acciones para Empleado
        if action == 'get_empleado':
            empleados = EmpleadoDAO.seleccionar()
            response = {'status': 'success', 'data': [str(empleado) for empleado in empleados]}
        elif action == 'add_empleado':
            empleado = Empleado(nombre_usuario=data['nombre_usuario'], nombre=data['nombre'],
                                apellido_paterno=data['apellido_paterno'], apellido_materno=data['apellido_materno'])
            EmpleadoDAO.insertar(empleado)
            response = {'status': 'success', 'message': 'Empleado added successfully'}
        elif action == 'update_empleado':
            empleado = Empleado(nombre_usuario=data['nombre_usuario'], nombre=data['nombre'],
                                apellido_paterno=data['apellido_paterno'],
                                apellido_materno=data['apellido_materno'])
            EmpleadoDAO.actualizar(empleado)
            response = {'status': 'success', 'message': 'Empleado updated successfully'}
        elif action == 'delete_direccion':
            empleado = Empleado(id_empleado=data['id_empleado'])
            EmpleadoDAO.borrar(empleado)
            response = {'status': 'success', 'message': 'Empleado deleted successfully'}

        # Acciones para Favoritos
        if action == 'get_favoritos':
            favoritos = FavoritosDAO.seleccionar()
            response = {'status': 'success', 'data': [str(favorito) for favorito in favoritos]}
        elif action == 'add_favoritos':
            favorito = Favoritos(isbn=data['isbn'])
            FavoritosDAO.insertar(favorito)
            response = {'status': 'success', 'message': 'Favorito added successfully'}
        elif action == 'update_favoritos':
            favorito = Favoritos(isbn=data['isbn'])
            FavoritosDAO.actualizar(favorito)
            response = {'status': 'success', 'message': 'Favoritos updated successfully'}
        elif action == 'delete_favoritos':
            favorito = Favoritos(isbn=data['isbn'])
            EmpleadoDAO.borrar(favorito)
            response = {'status': 'success', 'message': 'Favorito deleted successfully'}

        # Acciones para Libros
        if action == 'get_libro':
            libros = LibroDAO.seleccionar()
            response = {'status': 'success', 'data': [str(libro) for libro in libros]}
        elif action == 'add_libro':
            libro = Libro(ISBN=data['ISBN'], id_autor=data['id_autor'], titulo=data['titulo'], genero=data['genero'],
                          anio=data['anio'], editorial=data['editorial'], precio=data['precio'],
                          cantidad=data['cantidad'],
                          disponibilidad=data['disponibilidad'])
            LibroDAO.insertar(libro)
            response = {'status': 'success', 'message': 'Libro added successfully'}
        elif action == 'update_libro':
            libro = Libro(id_autor=data['id_autor'], titulo=data['titulo'], genero=data['genero'], anio=data['anio'],
                          editorial=data['editorial'], precio=data['precio'], cantidad=data['cantidad'],
                          disponibilidad=data['disponibilidad'])
            LibroDAO.actualizar(libro)
            response = {'status': 'success', 'message': 'Libro updated successfully'}
        elif action == 'delete_libro':
            libro = Libro(ISBN=data['ISBN'])
            LibroDAO.borrar(libro)
            response = {'status': 'success', 'message': 'Libro deleted successfully'}

        # Acciones para Pedidos
        if action == 'get_pedido':
            pedidos = PedidoDAO.seleccionar()
            response = {'status': 'success', 'data': [str(pedido) for pedido in pedidos]}
        elif action == 'add_pedido':
            pedido = Pedido(id_Proveedor=data['id_Proveedor'], ISBN=data['ISBN'], Fecha_Pedido=data['Fecha_Pedido'],
                            Fecha_Entrega=data['Fecha_Entrega'], Cantidad_Pedida=data['Cantidad Pedida'],
                            Precio_Total=data['Precio_Total'])
            PedidoDAO.insertar(pedido)
            response = {'status': 'success', 'message': 'Pedido added successfully'}
        elif action == 'update_pedido':
            pedido = Pedido(id_Proveedor=data['id_Proveedor'], ISBN=data['ISBN'], Fecha_Pedido=data['Fecha_Pedido'],
                            Fecha_Entrega=data['Fecha_Entrega'], Cantidad_Pedida=data['Cantidad Pedida'],
                            Precio_Total=data['Precio_Total'])
            PedidoDAO.actualizar(pedido)
            response = {'status': 'success', 'message': 'Pedido updated successfully'}
        elif action == 'delete_pedido':
            pedido = Pedido(id_Proveedor=data['id_Proveedor'], ISBN=data['ISBN'], Fecha_Pedido=data['Fecha_Pedido'],
                            Fecha_Entrega=data['Fecha_Entrega'], Cantidad_Pedida=data['Cantidad Pedida'],
                            Precio_Total=data['Precio_Total'])
            PedidoDAO.borrar(pedido)
            response = {'status': 'success', 'message': 'Pedido deleted successfully'}

        # Acciones para Proveedor
        if action == 'get_proveedor':
            proveedores = ProveedorDAO.seleccionar()
            response = {'status': 'success', 'data': [str(proveedor) for proveedor in proveedores]}
        elif action == 'add_proveedor':
            proveedor = Proveedor(id_proveedor=data['id_proveedor'], nombre=data['nombre'],
                                  tel_contacto=data['tel_contacto'])
            ProveedorDAO.insertar(proveedor)
            response = {'status': 'success', 'message': 'Proveedor added successfully'}
        elif action == 'update_proveedor':
            proveedor = Proveedor(nombre=data['nombre'], tel_contacto=data['tel_contacto'],
                                  id_proveedor=data['id_proveedor'])
            ProveedorDAO.actualizar(proveedor)
            response = {'status': 'success', 'message': 'Proveedor updated successfully'}
        elif action == 'delete_proveedor':
            proveedor = Proveedor(id_proveedor=data['id_proveedor'], nombre=data['nombre'],
                                  tel_contacto=data['tel_contacto'])
            ProveedorDAO.borrar(proveedor)
            response = {'status': 'success', 'message': 'Proveedor deleted successfully'}

        # Acciones para Tarjeta
        if action == 'get_tarjeta':
            tarjetas = TarjetaDAO.seleccionar()
            response = {'status': 'success', 'data': [str(tarjeta) for tarjeta in tarjetas]}
        elif action == 'add_tarjeta':
            tarjeta = Tarjeta(num_tarjeta=data['num_tarjeta'], id_cliente=data['id_cliente'], cvv=data['cvv'],
                              fecha_vencimiento=data['fecha_vencimiento'], banco=data['banco'])
            TarjetaDAO.insertar(tarjeta)
            response = {'status': 'success', 'message': 'Tarjeta added successfully'}
        elif action == 'update_tarjeta':
            tarjeta = Tarjeta(num_tarjeta=data['num_tarjeta'], id_cliente=data['id_cliente'], cvv=data['cvv'],
                              fecha_vencimiento=data['fecha_vencimiento'], banco=data['banco'])
            TarjetaDAO.actualizar(tarjeta)
            response = {'status': 'success', 'message': 'Tarjeta updated successfully'}
        elif action == 'delete_tarjeta':
            tarjeta = Tarjeta(num_tarjeta=data['tarjeta'])
            TarjetaDAO.borrar(tarjeta)
            response = {'status': 'success', 'message': 'Tarjeta deleted successfully'}

        # Acciones para Tipo Venta
        if action == 'get_tipoventa':
            tipo_ventas = TipoVentaDAO.seleccionar()
            response = {'status': 'success', 'data': [str(tipo_venta) for tipo_venta in tipo_ventas]}
        elif action == 'add_tipoventa':
            tipo_venta = TipoVenta(id_tipo=data['id_tipo'], nombre=data['nombre'])
            TipoVentaDAO.insertar(tipo_venta)
            response = {'status': 'success', 'message': 'TipoVenta added successfully'}
        elif action == 'update_tipoventa':
            tipo_venta = TipoVenta(id_tipo=data['id_tipo'], nombre=data['nombre'])
            TipoVentaDAO.actualizar(tipo_venta)
            response = {'status': 'success', 'message': 'Tipoventa updated successfully'}
        elif action == 'delete_tipoventa':
            tipo_venta = TipoVenta(id_tipo=data['id_tipo'], nombre=data['nombre'])
            TipoVentaDAO.borrar(tipo_venta)
            response = {'status': 'success', 'message': 'TipoVenta deleted successfully'}

        # Acciones para Usuario
        if action == 'get_usuario':
            usuarios = UsuarioDAO.seleccionar()
            response = {'status': 'success', 'data': [str(usuario) for usuario in usuarios]}
        elif action == 'add_usuario':
            usuario = Usuario(nombre_usuario=data['nombre_usuario'], contrasena=data['contrasena'], rol=data['rol'])
            UsuarioDAO.insertar(usuario)
            response = {'status': 'success', 'message': 'Usuario added successfully'}
        elif action == 'update_usuario':
            usuario = Usuario(contrasena=data['contrasena'], rol=data['rol'], nombre_usuario=data['nombre_usuario'])
            UsuarioDAO.actualizar(usuario)
            response = {'status': 'success', 'message': 'Usuario updated successfully'}
        elif action == 'delete_usuario':
            usuario = Usuario(nombre_usuario=data['nombre_usuario'])
            UsuarioDAO.borrar(usuario)
            response = {'status': 'success', 'message': 'Usuario deleted successfully'}

        # Acciones para VentaLibro
        if action == 'get_ventalibro':
            venta_libros = Venta_LibroDAO.seleccionar()
            response = {'status': 'success', 'data': [str(venta_libro) for venta_libro in venta_libros]}
        elif action == 'add_ventalibro':
            venta_libro = Venta_Libro(id_venta=data['id_venta'], ISBN=data['ISBN'], cantidad=data['cantidad'])
            Venta_LibroDAO.insertar(venta_libro)
            response = {'status': 'success', 'message': 'VentaLibro added successfully'}
        elif action == 'update_ventalibro':
            venta_libro = Venta_Libro(id_venta=data['id_venta'], ISBN=data['ISBN'], cantidad=data['cantidad'])
            Venta_LibroDAO.actualizar(venta_libro)
            response = {'status': 'success', 'message': 'VentaLibro updated successfully'}
        elif action == 'delete_ventalibro':
            venta_libro = Venta_Libro(id_venta=data['id_venta'], ISBN=data['ISBN'], cantidad=data['cantidad'])
            Venta_LibroDAO.borrar(venta_libro)
            response = {'status': 'success', 'message': 'VentaLibro deleted successfully'}

    except Exception as e:
        response = {'status': 'error', 'message': str(e)}

    send(json.dumps(response), broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)