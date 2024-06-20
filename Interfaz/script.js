let loadMoreBtn = document.querySelector('#cargar-mas');
let currentItems = 5;

let boxes = [...document.querySelectorAll('.conten-lib .libro')];

// Mostrar los primeros 5 libros inicialmente
for(let i = 0; i < currentItems; i++){
    boxes[i].style.display = 'inline-block';
}

loadMoreBtn.onclick = () => {
    // Calcular cuántos libros más mostrar
    let itemsToShow = (currentItems + 4 <= boxes.length) ? 4 : boxes.length - currentItems;

    // Mostrar los próximos libros
    for(let i = currentItems; i < currentItems + itemsToShow; i++){
        boxes[i].style.display = 'inline-block';
    }
    
    currentItems += itemsToShow;

    // Ocultar el botón si se han mostrado todos los libros
    if(currentItems >= boxes.length){
        loadMoreBtn.style.display = 'none';
    }
}

//carrito
const carrito = document.getElementById('carrito');
/*const elementos0 = document.getElementById('slider');*/
const elementos1 = document.getElementById('lista-lib');
const lista = document.querySelector('#lista-carrito tbody');
const vaciarCarritoBtn = document.getElementById('vaciar-carrito');

cargarEventListeners();

function cargarEventListeners(){
    /*elementos0.addEventListener('click', comprarElemento);*/
    elementos1.addEventListener('click', comprarElemento);
    carrito.addEventListener('click', eliminarElemento);
    vaciarCarritoBtn.addEventListener('click', vaciarCarrito);
}

function comprarElemento(e){
    e.preventDefault();
    if(e.target.classList.contains('agreg-carr')){
        const elemento = e.target.parentElement.parentElement;
        leerDatosElemento(elemento);
    }
}

function leerDatosElemento(elemento){
    const infoElemento ={
        imagen: elemento.querySelector('img').src,
        titulo: elemento.querySelector('h3').textContent,
        precio: elemento.querySelector('.precio').textContent,
        id: elemento.querySelector('a').getAttribute('data-id')
    }
    insertarCarrito(infoElemento);
}

function insertarCarrito(elemento){
    const row = document.createElement('tr');
    row.innerHTML = `
    <td>
        <img src="${elemento.imagen}" width=100 height=150px>
    </td>
    <td>
        ${elemento.titulo}
    </td>
    <td>
        ${elemento.precio}
    </td>
    <td>
        <a href="#" class="borrar" data-id="${elemento.id}">X</a>
    </td>
    `;
    lista.appendChild(row);
}

function eliminarElemento(e){
    e.preventDefault();
    let elemento,
        elementoID;
    if(e.target.classList.contains('borrar')){
        e.target.parentElement.parentElement.remove();
        elemento = e.target.parentElement.parentElement;
        elementoID = elemento.querySelector('a').getAttribute('data-id')
    }
}

function vaciarCarrito(){
    while(lista.firstChild){
        lista.removeChild(lista.firstChild)
    }
}