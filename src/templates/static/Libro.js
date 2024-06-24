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
    const id_autor = document.getElementById('id_autor').value;
    const titulo = document.getElementById('titulo').value;
    const genero = document.getElementById('nombre').value;
    const anio = document.getElementById('anio');
    const editorial = document.getElementById('editorial');
    const precio = document.getElementById('precio').value;
    const cantidad = document.getElementById('cantidad').value;
    const disponibilidad = document.getElementById('disponibilidad').value;

    const msg = {
        action: action,
        id_autor: id_autor,
        titulo: titulo,
        genero: genero,
        anio: anio,
        editorial: editorial,
        precio: precio,
        cantidad: cantidad,
        disponibilidad: disponibilidad
    };

    socket.send(JSON.stringify(msg));
}
