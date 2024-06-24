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
    const id_empleado = document.getElementById('id_empleado').value;
    const nombre_usuario = document.getElementById('nombre_usuario').value;
    const nombre = document.getElementById('nombre').value;
    const apellido_paterno = document.getElementById('apellido_paterno');
    const apellido_materno = document.getElementById('apellido_materno');
    const msg = {
        action: action,
        id_empleado: id_empleado,
        nombre_usuario: nombre_usuario,
        nombre: nombre,
        apellido_paterno: apellido_paterno,
        apellido_materno: apellido_materno,
    };

    socket.send(JSON.stringify(msg));
}
