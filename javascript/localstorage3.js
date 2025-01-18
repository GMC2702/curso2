'use strict';

var formulario = document.querySelector('#formulario');
var ul = document.querySelector('#listarJuegos');

//Función para construir la lista
function construirLista() {
    ul.innerHTML = ''; //Limpiamos el contenido antes de reconstruir
    for (var i in localStorage) {
        if (typeof localStorage[i] === 'string') {
            var li = document.createElement('li');
            li.textContent = localStorage[i];
            ul.appendChild(li);
        }
    }
}

//Construimos la lista al cargar la página.

construirLista();

formulario.addEventListener('submit', function(event) {
    event.preventDefault(); //Evita el envio del formulario por defecto

    var juego = document.querySelector('#addJuego').value;
    if(juego.length >= 1) {
        localStorage.setItem(juego, juego);
        //Llamamos a la función para agregar el nuevo elemento a la lista
        construirLista();
    }
});