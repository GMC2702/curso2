//Arrow functions en métodos.


// const reproductor = {
//     cancion: '', 
//     reproducir: id => console.log(`Reproduciendo canción id ${id}`),
//     pausar: id => console.log(`pausando... canción id ${id}`),
//     borrar: id => console.log(`Borrando canción con id: ${id}`),
//     crearPlaylist: nombre => console.log(`Creando la playlist ${nombre}`),
//     reproducirPlaylist: nombre => console.log(`Reproduciendo la playlist ${nombre}`),


// //SET Y GET

// set nuevaCancion(cancion) {
//     this.cancion = cancion;
//     console.log(`Añadiendo ${cancion}`)
// },
// get obtenerCancion() {
//     console.log(`${this.cancion}`)
// }
// }


// reproductor.reproducir(30);
// reproductor.pausar(30);
// reproductor.crearPlaylist("Hola");
// reproductor.reproducirPlaylist("Hola");


const carro = {
    modelo: '',
    acelerar: modelo => console.log(`Acelerando el carro, ${modelo}`),
    retroceder: modelo => console.log(`Retrocediendo el carro, ${modelo}`),
    chocar: modelo => console.log(`Chocando el carro aaa, ${modelo}`),

set modeloCarro(modelo) {
    this.modelo = modelo;
    console.log(`Añadiendo ${this.modelo}`)
},
get obtenerModelo() {
    console.log(`${this.modelo}`) 
}
}

carro.modeloCarro = 'Yaris tal';
carro.obtenerModelo;
carro.acelerar(carro.modelo);
carro.retroceder(carro.modelo);
carro.chocar(carro.modelo);

console.log(Object.keys(carro)); // nos devolverá un arreglo con los keys del objeto.
console.log(Object.values(carro)); // nos devolverá un arreglo con los valores del objeto.
console.log(Object.entries(carro)); // nos devolverá una matriz de llaves y valores.

