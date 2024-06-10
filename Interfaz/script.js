let loadMoreBtn = document.querySelector('#cargar-mas');
let currentItems = 8;

loadMoreBtn.onclick = () =>{
    let boxes = [...document.querySelectorAll('.conten-lib .libro')];
    for(var i=currentItems; i<currentItems+4;i++){
        boxes[i].style.display = 'inline-block';
    }
    currentItems +=4;
    if(currentItems <= boxes.length){
        loadMoreBtn.style.display = 'none';
    }
}

//carrito
const carrito = document.getElementById('')