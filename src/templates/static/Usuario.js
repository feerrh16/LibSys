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
    const nombre_usuario = document.getElementById('nombre_usuario').value;
    const contraseña = document.getElementById('contraseña').value;
    const rol = document.getElementById('rol').value;


    const msg = {
        action: action,
        nombre_usuario: nombre_usuario,
        contraseña: contraseña,
        rol: rol
    };

    socket.send(JSON.stringify(msg));
}
