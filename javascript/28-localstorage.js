'use strict'
// COMPROBAR DISPONIBILIDAD

if (typeof(Storage) !=='underfined') {
    console.log('Local storage está disponible.');
}
else{
    console.log('Local storage no está disponible.');
}


// Guardar datos
localStorage.setItem("titulo", "Curso de Php");

// Guardar un elemento local storage
localStorage.getItem("titulo");

//Imprimir en consola lo que obtuve del local storage.
console.log(localStorage.getItem("titulo"));

//Imprimir en html lo que almacene del local storage

document.querySelector("#curso").innerHTML = localStorage.getItem("titulo");

// guardar objetos json

var usuario ={

    nombre: "Gerardo Montero",
    email: "taltal@gmail.com",
    web: "elpepe.com"

};

localStorage.setItem("usuario", JSON.stringify(usuario));

//LA FORMA CORRECTA DE ALMACENAR DATOS EN LOCAL STORAGE
//ES CONVIRTIENDO LOS OBJETOS EN JSONSTRING PORQUE NO PROCESA EL OBJETO CON JAVA SCRIPT PURO
//LA FORMA CORRECTA DE ENVIAR INFORMACION A UN API SE DEBE HACER IGUAL CON JSON STRING

//Recuperar objetos de local storage

var userjs= JSON.parse(localStorage.getItem("usuario"));
console.log(userjs);

//PARA IMPRIMIR EN HTML

document.querySelector("#alumno").append(" "+userjs.nombre+" "+userjs.email);

//vaciar el local storage
localStorage.removeItem("usuario");

localStorage.clearItem("usuario");