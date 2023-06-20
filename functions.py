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


