// nombre = 'programacion';
// precio = 40;
// disponible = true;

//Un objeto literal en vez  de crear tres variables distintas:

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

curso.modalidad= 'presencial'; //Esta línea adiciona una nueva propiedad.
delete curso.modalidad; //Y delete, la elimina.


console.log(curso);


//El mío :DDD

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


//Destructuración de objetos:

// const nombreCurso= curso.nombre;
// console.log(nombreCurso); //Forma antigua.

// EcmaScrip6 lo simplifica:
//Los campos en las llaves son los únicos que se mostraran.
const {nombre, precio, disponible, informacion, informacion:{fechaFinalizacion}, informacion:{horas:{duracion}}} = curso;
console.log(duracion);