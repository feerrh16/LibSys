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
    const ISBN = document.getElementById('ISBN').value;
    const fecha_pedido = document.getElementById('fecha_pedido').value;
    const fecha_entrega = document.getElementById('fecha_entrega');
    const cantidad_pedido = document.getElementById('cantidad_pedido');
    const precio_total = document.getElementById('precio_total').value;
 
    const msg = {
        action: action,
        id_proveedor: id_proveedor,
        ISBN: ISBN,
        fecha_pedido: fecha_pedido,
        fecha_entrega: fecha_entrega,
        cantidad_pedido: cantidad_pedido,
        precio_total: precio_total
    };

    socket.send(JSON.stringify(msg));
}
