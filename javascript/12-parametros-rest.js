function listadoFrutas(fruta1, fruta2,...todasFrutas){
    console.log("La fruta 1 es: " +fruta1);
    console.log("La fruta 2 es: " +fruta2);
    console.log(todasFrutas);
}

listadoFrutas('Cambur', 'lechoza', 'patilla', 'melon', 'guayaba');
var frutas2= ['fresas', 'limon', 'parchita'];

listadoFrutas('pera', 'hey apple', ...frutas2, 'Cambur', 'lechoza', 'patilla');
