function sumar(a, b) {
    return a + b;
}

const resultado = sumar(1,2);
console.log(resultado);


//complicao
let total = 0;

function agregarCarrito(precio) {
    return total += precio;
}

function calcularImpuesto(total){
    return 1.15 * total;
}

total = agregarCarrito(200);
total = agregarCarrito(300);
total = agregarCarrito(400);
console.log(total);

const totalPagar = calcularImpuesto(total);
console.log(`El total a pagar es ${totalPagar}`);

