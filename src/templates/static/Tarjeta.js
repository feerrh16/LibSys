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
    const num_tarjeta = document.getElementById('num_tarjeta').value;
    const id_cliente = document.getElementById('id_cliente').value;
    const cvv = document.getElementById('cvv').value;
    const fecha_vencimiento = document.getElementById('fecha_vencimiento').value;
    const banco = document.getElementById('banco').value;
    
    const msg = {
        action: action,
        num_tarjeta: num_tarjeta,
        id_cliente: id_cliente,
        cvv: cvv,
        fecha_vencimiento: fecha_vencimiento,
        banco: banco
    };

    socket.send(JSON.stringify(msg));
}
