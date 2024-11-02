// function sumame (n1, n2){

//     // Conjunto de instrucciones que ejecuta la función.
//     var suma= n1 + n2;
//     console.log(suma);
//     return
// }

// function multiplicame (n1, n2){

//     // Conjunto de instrucciones que ejecuta la función.
//     var multiplicame= n1 *n2;
//     console.log(multiplicame);
//     return
// }

// function calculadora(n1, n2, n3){

//     // Conjunto de instrucciones que ejecuta la función.
//     console.log("La suma de los dos números es", (n1+ n2+ n3));
//     console.log("La resta de los dos números es", (n1- n2));
//     console.log("La multiplicación de los dos números es", (n1* n2));
//     console.log("La división de los dos números es", (n1/ n2));
// }

// // Así llamamos/invocamos una función.
// // sumame(15, 5);
// // multiplicame(50, 8);
// calculadora (7, 7, 7);




// EJERCICIO
function PorConsola(n1, n2){
    console.log("La suma es :", n1+n2 );
    console.log("La resta es :"+ (n1-n2));
    console.log("La multiplicación es :"+ (n1*n2));
    console.log("La división es :"+ (n1/n2));
}

function PorPantalla(n1,n2){
    document.write("La suma es: ", n1 + n2 +"<br>");
    document.write("La resta es: " +(n1-n2)+"<br>");
    document.write("La multiplicación es:"+(n1*n2)+"<br>");
    document.write("La división es:"+(n1/n2)+"<br>");
}

function calculadora(n1, n2, truofalz=false) {
    if(truofalz==true){
        PorPantalla(n1, n2);
    }

else{
        PorConsola(n1, n2);
}
}

calculadora(2, 2, true);
calculadora(2, 5, false);