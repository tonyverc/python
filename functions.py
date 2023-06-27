import library

#definition
def hello():
    print('hello Python!')

# appel
hello()

#paramétre
def hello2(name):
    print(f"hello {name}!")

hello2('Foo')

#paramétres + retour de valeurs
def addition(a, b):
    return a + b

resultat = addition(42, 123)
print(resultat)

#appel d'une fonction stockée dans un autre module
resultat = library.oui_non(False)
print(resultat)
print(library.oui_non(True))

# reverse lookup
my_list = [42, 123, 3.14]

   # reverse_lookup(my_list, value):

   ## """cette fonction prend en paramétre une liste et une valeur à rechercher.
   # Elle renvoie l index de la valeur si elle est trouvée
    #ou none si la valeur n'est pas trouvée

   # my_list list dans laquelle il faut chercher
    #value any la valeur à rechercher
   # return int si la valeur est trouvée ou None si la valeur n'est pas trouvée
   # """

for i in range(len(my_list)):
        if my_list[i] == value:
            #@dev
            # print(f'{i = }') 
         #  return i

 return None
    
resultat = reverse_lookup(my_list, 3.14)
print(result)

#type hinting
def mult(a: int,b: int) -> int:
    """Cette fonction...

    a...
    b...
    return...
    """
    return a * b
result = mult(2, 5)
print(result)

#le nom de la fonction + ses paramétres + sont type de retour = signature de la fonction
# def mult(a: int, b: int)-> int:

#copie d'une fonction comme si c'etait une variable
mult_copy = mult
mult_copy(2, 5)

# stockage de fonctions dans une liste
operation = []
operations.append(addition)
operations.append(mult)

a = 2
b = 5
resultat = None

for operation in operations:
    resultat = operation(a, b)

#fonction d'ordre supérieur
#c'est une fonction qui accepte une fonction paramétre ou qui renvoie une fonction
def operateur_binaire(a, b, fonction):
    return fonction(a, b)

#appel de la fonction d'ordre superieur
resultat = operateur_binaire(2, 5, mult)

my_list = ['foo', 'ipsum']
text = 'toto'

print(len(my_list))
print(len(text))

def my_len(value):
    return 42

#sauvegarde de la fonction len() originale
len_backup = len
#surcharge de la fonction len() originale
#c'est à dire remplacement par une autre fonction
len = my_len

print(len(my_list))
print(len(text))

#restauration de la fonction len() originale
len = len_backup

#pass permet d'ecrire du code python syntaxiquement valide 
#meme quand on n'a pas encore le corps du la condition if ou de la boucle for
if True :
    pass







