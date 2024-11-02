var n1= parseInt(prompt("Introduce un número.", 0));
var n2= parseInt(prompt("Introduce un segundo número.", 0));

if(n1 > n2){
    console.log(n1+ " Es mayor que " +n2);
}
else if(n1 == n2){
    console.log(n1+ " Es igual que " +n2);
}
else{
    console.log(n1+ " Es menor que " +n2);
    //return true;
}

console.log(n1, n2);


// Necesito que diga por consola que número es mayor, si son iguales e imprima resultado.