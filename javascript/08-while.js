// let text= " ";
// let x = 5;
// while( x<10){
//     text+= "el numero a imprimir es " + x +"<br>" ;
//     x++;
// }
// document.getElementById("text").innerHTML= text;

// let text= " ";
// let x = 1;
// while( x<=100){
//     text+= "el numero a imprimir es " + x +"<br>" ;
//     x++;
// }
// document.getElementById("text").innerHTML= text;

let text="";
let texto = "";
let x= 5;
let y= 5;
var suma= x+y;
texto += "El resultado es: "+ suma;

while(suma <=20){
    text+= "el numero a imprimir es " + suma + "<br>";
    suma++
}

document.getElementById("text").innerHTML = text;
document.getElementById("suma").innerHTML = texto;