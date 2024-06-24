const socket = io();

socket.on('connect', () => {
    console.log('Connected to server');
});

socket.on('message', (msg) => {
    const data = JSON.parse(msg);
    const li = document.createElement('li');
    li.textContent = JSON.stringify(data);
    document.getElementById('messages').appendChild(li);
});

function sendAction(action) {
    const id_cliente = document.getElementById('id_cliente').value;
    const nombre_usuario = document.getElementById('nombre_usuario').value;
    const nombre = document.getElementById('nombre').value;
    const apellido_paterno = document.getElementById('apellido_paterno');
    const apellido_materno = document.getElementById('apellido_materno');
    const id_direccion = document.getElementById('id_direccion').value;
    const correo = document.getElementById('correo').value;
    const telefono = document.getElementById('telefono').value;
    const num_tarjeta = document.getElementById('num_tarjeta').value;
    const msg = {
        action: action,
        id_cliente: id_cliente,
        nombre_usuario: nombre_usuario,
        nombre: nombre,
        apellido_paterno: apellido_paterno,
        apellido_materno: apellido_materno,
        id_direccion: id_direccion,
        correo: correo,
        telefono: telefono,
        num_tarjeta: num_tarjeta
    };

    socket.send(JSON.stringify(msg));
}
