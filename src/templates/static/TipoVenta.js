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
    const id_tipo = document.getElementById('id_tipo').value;
    const nombre = document.getElementById('nombre').value;

    const msg = {
        action: action,
        id_tipo: id_tipo,
        nombre: nombre
    };

    socket.send(JSON.stringify(msg));
}
