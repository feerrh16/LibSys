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
    const ISBN = document.getElementById('ISBN').value;

    const msg = {
        action: action,
        id_cliente: id_cliente,
        ISBN: ISBN
    };

    socket.send(JSON.stringify(msg));
}
