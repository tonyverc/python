// boucle for classique
for (let i = 0; i < 10; i++) {
    console.log("i = " + i);
}

// boucle à rebours
for (let i = 10; i > 0; i--) {
    console.log("i = " + i);
}

//boucle for each
let users = ['foo' , 'bar' , 'baz'];

//le mot clé "of" permet de récuperer l'element
for (let user of users){
    console.log(user);
}

//le mot clé "in" permet de récuperer l'index de l'element
for (let i in users){
    let user = users[i];
    console.log(`i = ${i}, user = ${user}`);
}

//méthode forEach (asyncrone)
users.forEach(
    function(user , i , list) {
        console.log(`i = ${i}, user = ${user}`);
    }
);

//syntaxe alternative
users.forEach(
    (user, i, list) => {
        console.log(`i=${i}, user=${user}`)
    }
);
