// exo 6.15
// Trouvez la chaîne de caractères la plus longue dans une liste.
// Affichez son index, sa valeur et sa longueur.
//
// ATTENTION : ne pas utiliser la fonction list.index()
// ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

let my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

// réponse 6.15
let index = null;
let valeur = "";
let longeur = 0;

//my_list.length      longeur liste chaine de caractére
//my_list[0].length   longeur premiére chaine de caractére

console.log(my_list[1]); // affiche 'ipsum' dans la chaine de caractére

for (let i = 0; i < my_list.length; i++) {
    //console.log(i);
   // console.log(my_list[i]);
    //console.log(my_list[i].length);
    if(my_list[i].length > longeur){
        //mise à jour, c'est à dire stockage de la plus grande valeur rencontrée jusque maintenant
        longeur = my_list[i].length;
        //stockage des autres informations demandées
        index = i;
        valeur = my_list[i];
    }
    }

    console.log(index);
    console.log(valeur);
    console.log(longeur);

    // boucle foreach qui permet de recuperer les valeurs mais pas l'index
    //initialisation de l'index
    let i = 0;
    //reset des données(necéssaire parce qu'on a déja le meme algo)
    index = null;
    valeur = "";
    longueur = 0;

    for (let word of my_list){
        console.log(i);
        console.log(word);
        console.log(word.length);
        if(my_list[i].length > longeur){
            longeur = my_list[i].length;
            index = i;
            valeur = my_list[i];
            i++;
        }
        
    }
