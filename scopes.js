for(let i = 0; i < 10; i++){
    console.log(i);
}

// si la variable i n'est pas définie dans le scope global,elle n'est pas utilisable
// si la variable i à été definie avec le mot clé let,elle n'est accessible que si elle à été
//définie dans le meme scope ou un scope extérieur
console.log(i);

for(var i = 0; i < 10; i++){
    console.log(i);
}

// si la variable i à été definie avec le mot clé var, elle est accessible meme
//si elle a été définie dans un scope intérieur
console.log(i);

function my_func1() {
    var myVar1 = 123;
}

my_func1();

// meme si la variable myvar1 est déclarée avec le mot clé var,comme elle est 
// déclarée à l'interieur d'une fonction ,elle n'est pas accesible depuis un scope extérieur
// ReferenceError: myvar1 is not defined
//console.log(myVar1);

//closure

function multNFactory(n){
    return function multN(x){
        return x * n;
    }
}

mult3 = multNFactory(3);

for(let i = 0; i < 3; i++){
    console.log(mult3(i));
}

mult54 = multNFactory(54);

for(let i = 0; i < 3; i++){
    console.log(mult54(i));
}
