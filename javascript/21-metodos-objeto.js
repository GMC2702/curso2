'use strict';

const curso ={

    nombre: 'programación',
    precio: 40,
    disponible: true,
    informacion:{ //Objeto dentro de un objeto.
        fechaInicio: "5 de noviembre",
        fechaFinalizacion: '20 de Diciembre',
        horas:{
            duracion: "5 horas"
        }
    }

}
console.log(curso);
const carro ={

    nombre: 'Toyota Yaris',
    modelo: 'no sé, Yaris',
    año: 2008,
    colores:{
        uno: "azul",
        dos: "verde",
    },
    precio: 800,
    disponible: false
}
console.log(carro);

// Object.freeze(curso); //Congela un objeto.
// curso.nombre = 'marketing';
// console.log(curso);
// delete curso.nombre;

// console.log(Object.isFrozen(curso)); //Valida si un objeto está congelado.

//SEAL
// Object.seal(curso); //No se puede eliminar ni agregar,pero si se pueden editar los contenidos.
// curso.nombre = 'marketing2';
// console.log(curso);


//UNIR DOS OBJETOS

const planificacion = Object.assign(curso, carro);
console.log(planificacion);

//spread operator

const planificacion2 = {...curso,...carro};