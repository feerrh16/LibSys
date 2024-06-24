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
    const id_venta = document.getElementById('id_venta').value;
    const ISBN = document.getElementById('ISBN').value;
    const cantidad = document.getElementById('cantidad').value;

    const msg = {
        action: action,
        id_venta: id_venta,
        ISBN: ISBN,
        cantidad: cantidad
    };

    socket.send(JSON.stringify(msg));
}
