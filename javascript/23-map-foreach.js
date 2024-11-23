const carrito= [
    { nombre: 'Monitor 20 pulgadas', precio: 500},
    { nombre: 'Television 50 Pulgadas', precio: 700},
    { nombre: 'Tablet', precio: 300},
    { nombre: 'Audifonos', precio: 200},
    { nombre: 'Teclado', precio: 50},
    { nombre: 'Celular', precio: 500}
]

//Método array map.

const nuevoArray = carrito.map( function(producto) {
    return `Articulo: ${ producto.nombre } Precio: ${producto.precio *2} `;
})

const nuevoArray2 = carrito.forEach( function(producto) {
    console.log(`1-- Articulo: ${ producto.nombre } Precio: ${producto.precio}`);
})

// console.log(nuevoArray);
// console.log(nuevoArray2);

for(let i = 0; i < carrito.length; i++){
    console.log(`2-- Articulo: ${ carrito[i].nombre } Precio: ${carrito[i].precio}`);
}