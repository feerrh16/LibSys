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
    const id_proveedor = document.getElementById('id_proveedor').value;
    const nombre = document.getElementById('nombre').value;
    const tel_contacto = document.getElementById('tel_contacto').value;


    const msg = {
        action: action,
        id_proveedor: id_proveedor,
        nombre: nombre,
        tel_contacto: tel_contacto
    };

    socket.send(JSON.stringify(msg));
}
