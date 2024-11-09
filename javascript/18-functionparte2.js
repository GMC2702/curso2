// funciones de declaracion y de expresión

'use strict';

suma1(15, 20);
function suma1(a,b){
    // cuerpo de la function o conjunto de instrucciones que va a ejecutar la función.
    console.log(a+b);
};



// función de expresión

// suma2(25, 45); De declararla no va a funcionar.
const suma2= function(a,b) {
    console.log(a+b);
};

suma2(25, 45);


// Ejemplo de plantillas de texto

function ingresaSistema(nombre='Nombre no indicado', apellidos='Apellido no indicado') {
    document.write(`Bienvenido ${nombre} ${apellidos} puedes ingresar al sistema.`);

}

ingresaSistema('Gerardo','Montero');

