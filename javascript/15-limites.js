var n1= parseInt(prompt("Introduce un número.", 0));
var n2= parseInt(prompt("Introduce un segundo número mayor que el anterior.", 0));

for(var limite= n1+1; limite < n2; limite=limite+1) {
            document.write("ED-" +limite+", ");
};