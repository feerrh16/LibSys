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
    const id_direccion = document.getElementById('id_direccion').value;
    const id_cliente = document.getElementById('id_cliente').value;
    const direccion = document.getElementById('direccion').value;
    const ciudad = document.getElementById('ciudad').value;
    const municipio = document.getElementById('municipio').value;
    const cp = document.getElementById('cp').value;
    const msg = {
        action: action,
        id_direccion: id_direccion,
        id_cliente: id_cliente,
        direccion: direccion,
        ciudad: ciudad,
        municipio: municipio,
        cp: cp
    };

    socket.send(JSON.stringify(msg));
}
