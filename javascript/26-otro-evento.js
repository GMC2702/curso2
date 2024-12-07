const nav = document.querySelector('.navbar');

nav.addEventListener('click', () => {
    console.log('entrando a navegacion')

    nav.style.backgroundColor = 'green'
});

nav.addEventListener('dblclick', () => {
    console.log('saliendo de la navegacion')

    nav.style.backgroundColor = 'yellow'
})

const calculadora = {
    sumar: function(n1,n2){
        suma= n1+n2;
        document.querySelector("#result").innerHTML = `La suma de a: ${n1} mas b: ${n2}=${suma}`;
    },
    multiplicar: function(n1,n2){
        multiplica= n1*n2;
        document.querySelector("#result").innerHTML = `La multiplicación de a: ${n1} más b: ${n2}=${multiplica}`;
    },
    resta: function(n1,n2){
        resta= n1-n2;
        document.querySelector("#result").innerHTML = `La resta de a: ${n1} más b: ${n2}=${resta}`;
    },
    division: function(n1,n2){
        divide= n1/n2;
        document.querySelector("#result").innerHTML = `La división de a: ${n1} más b: ${n2}=${divide}`;
    },
}


const nombres = {
    nombrar: function(){
    let array = ['elpepe', 'etesech', 'tilin', 'hawk tuah', 'adin ross'];
    let arrayrandom = Math.floor(Math.random() * array.length);
    document.querySelector("#nombre").innerHTML= `${arrayrandom}`;
    }
}
