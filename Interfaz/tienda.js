let data = [
    "hola",
    "como",
    "estas",
    "pinche",
    "perro",
];

function buscar() {
    let query = document.getElementById("buscar").value;

    console.log(query);

    if (query.trim() === "") {
        return;
    }

    let resultado = [];

    for (let i = 0; i < data.length; i++) {
        if (data[i].toLowerCase().includes(query.toLowerCase())) {
            resultado.push(data[i]);
        }
    }

    document.getElementById("resultado").innerHTML = "";

    if (resultado.length > 0) {
        for (let i = 0; i < resultado.length; i++) {
            let li = document.createElement("li");
            li.textContent = resultado[i];
            document.getElementById("resultado").appendChild(li);
        }
    } else {
        let li = document.createElement("li");
        li.textContent = "No se encontraron elementos para: " + query;
        document.getElementById("resultado").appendChild(li);
    }
}