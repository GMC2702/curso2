var n1= parseInt(prompt("Introduce un número.", 0));
var n2= parseInt(prompt("Introduce un segundo número mayor que el anterior.", 0));

for(var impar = n1; impar <= n2; impar=impar+1) {
        if (impar % 2 == 1) {
                document.write(impar+", ");
        }
}