'use strict';

function sumando(n1, n2, sumaMuestra, sumaPordos){

    var suma= n1+n2;
    sumaMuestra(suma);
    sumaPordos(suma);

    return suma; 
    // ^^^^^Este dato se devuelve, y convierte en dato.
}

sumando(5, 2, function (dato){
    console.log("La suma es:"+ dato);

}, function(dato){
    console.log("La suma de por dos es:" + (dato*2));

});
