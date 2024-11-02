var nombre = "GERALDO";
var profesores = ['juan', 'pedro', 'maria', 'pedro', 'rosita'];
var materias = ['matematicas', 'lenguaje', 'ingles'];

// console.log(profesores[2]);//Ubica la posición 2, María.
// console.log(profesores.length);//Cuenta cuantas posiciones tiene el arreglo.

// // metodos para trabajar con texto
// console.log(nombre.toUpperCase());//Mayúsculas.
// console.log(nombre.toLowerCase());//Minúsculas.


document.write("<h1> Ejercicios de Arrays</h1>");
document.write("<ul>");

materias.forEach((element, indice, arr) =>{  //Esto es una función simplificada con una flecha.
    document.write("<li>" +indice+ " " +element + '</li>');
});

profesores.forEach((element, indice, arr) =>{
    document.write("<li>" +indice+ " " +element + '</li>');
});

document.write('</ul>');
